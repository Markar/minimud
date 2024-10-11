import math
from random import randint, uniform
from evennia import CmdSet
from evennia.utils.evtable import EvTable
from commands.command import Command
from typeclasses.elementalguild.constants_and_helpers import SKILLS_COST
from evennia.utils import delay
from evennia.contrib.rpg.buffs import BaseBuff
from typeclasses.utils import PowerCommand


class PowerCommand(Command):
    def func(self):
        caller = self.caller
        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False
        caller.cooldowns.add("global_cooldown", 2)


# region Burnout
class CmdBurnout(PowerCommand):
    """
    This powerful ability allows the earth elemental to channel energy from all elemental forces, enhancing their physical abilities and combat prowess. While active, the elemental's attacks become more potent, and their movements more fluid and precise. The elemental's power is greatly increased while burnout is active, but the strain of maintaining this heightened state of power can be overwhelming, and the elemental must be cautious not to overextend themselves.

    The duration is boosted by the elemental harmony skill, and the elemental must have a sufficient amount of Primordial Essence to activate Burnout.

    Usage:
        burnout
    """

    key = "burnout"
    help_category = "earth elemental"
    cost = 7
    guild_level = 7

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        if not caller.db.primordial_essence["count"] > 0:
            caller.msg(f"|CYou are too tired to use this power.")
            return
        if caller.db.elemental_fury["active"]:
            caller.msg(f"|CYou can't use Burnout while Elemental Fury is active.")
            return
        if caller.db.burnout["active"]:
            caller.msg(f"|CYour power is already surging.")
            return
        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False
        if not caller.cooldowns.ready("burnout"):
            caller.msg(f"|CNot so fast!")
            return False
        if caller.db.primordial_essence["count"] < self.cost:
            caller.msg(
                f"|rYou need at least {self.cost} primordial essence to use this power."
            )
            return
        if glvl < self.guild_level:
            caller.msg(
                f"|CYou need to be guild level {self.guild_level} to use burnout."
            )
            return

        caller.cooldowns.add("burnout", 60)
        caller.cooldowns.add("global_cooldown", 2)
        skill_rank = caller.db.skills.get("elemental harmony", 1)

        self.msg(
            f"|cA radiant aura of elemental energy envelops you, your power surging to new heights!|n"
        )

        caller.db.burnout["active"] = True
        caller.db.primordial_essence["count"] -= self.cost
        caller.db.burnout["duration"] = 3 + skill_rank * 2


# region Elemental Fury
class CmdElementalFury(PowerCommand):
    """
    This ultimate ability allows the earth elemental to harness the power of the elemental plane, amplifying their physical abilities and combat prowess to a superhuman level. While active, the elemental's attacks become devastatingly powerful, their movements almost instantaneous, and their resilience unmatched. The elemental's power is exponentially increased while Elemental Fury is active, but the strain of maintaining this extreme state of power is immense, requiring careful management to avoid collapse.

    An ancient and rare substance, Primordial Essence is collected from the core of elemental rifts. Consuming Primordial Essence allows the elemental to activate Elemental Fury, but the essence is depleted with each use, requiring careful resource management.

    The duration is significantly extended by the elemental harmony skill, and elemental fury consumes a large amount of Primordial Essence with each use.

    Usage:
        elemental fury, ef, fury
    """

    key = "elemental fury"
    aliases = ["ef", "fury"]
    help_category = "earth elemental"
    cost = 12
    guild_level = 18

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        if not caller.db.primordial_essence["count"] > 1:
            caller.msg(f"|CYou lack the Primordial Essence to use this power.")
            return
        if not caller.cooldowns.ready("elemental_fury"):
            caller.msg(f"|CElemental fury isn't ready yet.")
            return False
        if caller.db.burnout["active"]:
            caller.msg(f"|CYou can't use Elemental Fury while Burnout is active.")
            return
        if glvl < self.guild_level:
            caller.msg(
                f"|CYou need to be guild level {self.guild_level} to use Elemental Fury."
            )
            return
        if caller.db.elemental_fury["active"]:
            caller.msg(f"|CYour power is already surging.")
            return

        caller.db.primordial_essence["count"] -= self.cost
        caller.cooldowns.add("elemental_fury", 90)
        caller.cooldowns.add("global_cooldown", 2)
        skill_rank = caller.db.skills.get("elemental harmony", 1)

        self.msg(
            f"|cA radiant aura of elemental energy envelops you, your power surging to new heights!|n"
        )

        caller.db.elemental_fury["active"] = True
        caller.db.elemental_fury["duration"] = 5 + skill_rank * 3


# Defensive powers
# region Stone Skin
class CmdStoneSkin(PowerCommand):
    """
    Stone skin increases the earth elemental's defense by
    increasing their resistance to physical damage. The amount of damage
    reduced is based on the elemental's skill rank. This spell uses mineral
    fortification and constitution to determine the amount of damage reduced.


    Usage:
        stone skin
        ss
    """

    key = "stone skin"
    aliases = ["ss"]
    help_category = "earth elemental"
    cost = 25
    guild_level = 8

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        if glvl < self.guild_level:
            caller.msg(
                f"|CYou need to be guild level {self.guild_level} to use stone skin."
            )
            return
        if not caller.cooldowns.ready("stoneskin"):
            caller.msg(f"|YStone Skin isn't ready yet.")
            return False
        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return
        if caller.db.ep < self.cost:
            caller.msg(f"|rYou need at least {self.cost} energy to use this power.")
            return
        if not caller.db.stone_skin:
            caller.db.stone_skin = True
            caller.db.ep -= self.cost
            activateMsg = f"|CYour body hardens, rocky plates forming a protective barrier that absorbs and deflects incoming attacks."
            caller.location.msg_contents(activateMsg, from_obj=caller)
        else:
            caller.db.stone_skin = False
            deactivateMsg = f"|CYour body softens, the rocky plates that once protected $pron(you) now dissipating."
            caller.location.msg_contents(deactivateMsg, from_obj=caller)

        caller.cooldowns.add("global_cooldown", 2)
        caller.cooldowns.add("stoneskin", 60)


# region Earth Form
class CmdEarthForm(PowerCommand):
    """
    The earth elemental can transform their body into a denser form of rock,
    increasing their defense and resistance to damage. The amount of damage
    reduced is based on the elemental's skill rank. Uses: stone mastery, guild
    level, constitution, rock solid defense, and stone mastery.

    Usage:
        earthform
        earth
    """

    key = "earthform"
    aliases = ["earth"]
    help_category = "earth elemental"
    cost = 50
    guild_level = 15

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return
        if not caller.cooldowns.ready("earth_form"):
            caller.msg(f"|YEarth Form isn't ready yet.")
            return False
        if glvl < self.guild_level:
            caller.msg(
                f"|CYou need to be guild level {self.guild_level} to use earth form."
            )
            return
        if caller.db.ep < self.cost:
            caller.msg(f"|rYou need at least {self.cost} energy to use this power.")
            return
        if caller.db.active_form == None:
            caller.db.active_form = "earth"
            caller.db.ep -= self.cost
            caller.cooldowns.add("global_cooldown", 2)
            caller.cooldowns.add("earth_form", 60)
            activateMsg = f"|C$Your() form shifts and hardens, transforming into a denser, more resilient form of rock."
            caller.location.msg_contents(activateMsg, from_obj=caller)
        else:
            caller.db.active_form = None
            deactivateMsg = f"|C$Your() form softens and returns to its normal state."
            caller.location.msg_contents(deactivateMsg, from_obj=caller)


# region Mountain Stance
class CmdMountainStance(PowerCommand):
    """
    The earth elemental can take a defensive stance, increasing their
    resistance to damage and reducing the amount of damage taken. The amount
    of damage reduced is based on the elemental's skill rank.

    Usage:
        mountain stance
    """

    key = "mountain stance"
    aliases = ["ms"]
    help_category = "earth elemental"
    cost = 75

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        if glvl < 28:
            caller.msg(f"|CYou need to be guild level 28 to use mountain stance.")
            return
        if caller.db.ep < self.cost:
            caller.msg(f"|rYou need at least {self.cost} energy to use this power.")
            return
        if caller.db.earthshaker_stance:
            caller.msg(f"|CYou can't use Mountain Stance while in Earthshaker Stance.")
            return
        if not caller.db.mountain_stance:
            caller.db.mountain_stance = True
            caller.traits.con.mod += 10
            caller.db.ep -= self.cost
            caller.cooldowns.add("global_cooldown", 2)
            activateMsg = f"|C$Your() form grows larger and more imposing, taking on the appearance of a mountain."
            caller.location.msg_contents(activateMsg, from_obj=caller)
        else:
            caller.db.mountain_stance = False
            caller.traits.con.mod -= 10
            deactivateMsg = f"|C$Your() form shrinks and returns to its normal state."
            caller.location.msg_contents(deactivateMsg, from_obj=caller)

        caller.db.hpmax = 50 + caller.traits.con.value * caller.db.con_increase_amount


# region Earthshaker Stance
class CmdEarthshakerStance(PowerCommand):
    """
    The Earthshaker Stance is an aggressive combat stance that allows the elemental to channel the raw power of the earth into devastating attacks. While in this stance, the elemental's movements become more forceful and deliberate, each strike carrying the weight of the earth itself. This stance enhances the elemental's offensive capabilities, increasing the damage dealt to enemies but at the cost of reduced defense.

    Usage:
        earthshaker stance
    """

    key = "earthshaker stance"
    aliases = ["ess"]
    help_category = "earth elemental"
    cost = 75

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        if glvl < 30:
            caller.msg(f"|CYou need to be guild level 30 to use earthshaker stance.")
            return
        if caller.db.ep < self.cost:
            caller.msg(f"|rYou need at least {self.cost} energy to use this power.")
            return
        if caller.db.mountain_stance:
            caller.msg(f"|CYou can't use Earthshaker Stance while in Mountain Stance.")
            return
        if not caller.db.earthshaker_stance:
            caller.db.earthshaker_stance = True
            caller.traits.str.mod += 10
            caller.db.ep -= self.cost
            caller.cooldowns.add("global_cooldown", 2)
            activateMsg = f"|cYou adopt the Earthshaker Stance, your movements becoming more forceful as the ground trembles beneath you.|n"
            caller.location.msg_contents(activateMsg, from_obj=caller)
        else:
            caller.db.earthshaker_stance = False
            caller.traits.str.mod -= 10

            activateMsg = f"|cYou relax your stance, the ground settling as you exit the Earthshaker stance.|n"
            caller.location.msg_contents(activateMsg, from_obj=caller)


# region Earth Shield
class CmdEarthShield(PowerCommand):
    """
    The earth elemental can create a shield of stone to protect themselves
    from incoming attacks. The shield absorbs a portion of the damage based
    on the elemental's skill rank.

    Usage:
        earth shield
        es
    """

    key = "earth shield"
    aliases = ["es"]
    help_category = "earth elemental"
    cost = 50
    guild_level = 13

    def func(self):
        super().func()
        caller = self.caller
        glvl = caller.db.guild_level

        if glvl < self.guild_level:
            caller.msg(f"|CYou need to be guild level 14 to use earth shield.")
            return
        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False
        if not caller.cooldowns.ready("earth_shield"):
            caller.msg(f"|YEarth Shield isn't ready yet.")
            return False
        if caller.db.ep < self.cost:
            caller.msg(f"|rYou need at least {self.cost} energy to use this power.")
            return
        if not caller.db.earth_shield["hits"] > 0:
            caller.cooldowns.add("earth_shield", 60)
            caller.cooldowns.add("global_cooldown", 2)
            caller.db.earth_shield["hits"] = (
                3
                + caller.db.skills.get("stone mastery", 1)
                + int(caller.traits.con.value / 10)
            )
            caller.adjust_ep(-self.cost)
            self.msg(f"|gYou create a shield of stone to protect yourself.")
            activateMsg = f"|C$Your() form shimmers as a protective shield of stone forms around $pron(you)."
            caller.location.msg_contents(activateMsg, from_obj=caller)


# region Mud Patch
class CmdMudPatch(PowerCommand):
    """
    The earth elemental can apply a mud patch to heal minor injuries. The amount of health restored is based on the elemental's skill rank in elemental harmony.

    Usage:
        mud patch, patch
    """

    key = "mud patch"
    aliases = ["patch"]
    help_category = "earth elemental"
    cost = 10
    guild_level = 2

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level

        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return

        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False
        if not caller.cooldowns.ready("mud_patch"):
            caller.msg(f"|YMud Patch isn't ready yet.")
            return False
        if caller.db.hp == caller.db.hpmax:
            self.msg(f"|rYou are already at full health.")
            return
        if caller.db.ep < self.cost:
            self.msg(f"|rYou need at least {self.cost} energy to use this power.")
            return

        caller.adjust_hp(20 + caller.db.skills.get("elemental harmony", 1) * 2)
        caller.adjust_ep(-self.cost)
        caller.cooldowns.add("global_cooldown", 2)
        caller.cooldowns.add("mud_patch", 10)
        self.msg(f"|gYou apply a mud patch to your wounds, healing minor injuries.")
        activateMsg = f"|C$Your() form shimmers as a protective patch of mud forms around $pron(your) wounds."
        caller.location.msg_contents(activateMsg, from_obj=caller)


# region Terran Restoration
class CmdTerranRestoration(PowerCommand):
    """
    The earth elemental can rebuild their body to restore health,
    at the cost of focus. The amount of health restored is based on
    the elemental's wisdom and guild level.

    Usage:
        terran restoration
    """

    key = "terran restoration"
    aliases = ["tr", "restore"]
    help_category = "earth elemental"
    guild_level = 11
    cost = 20

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level

        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return

        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False
        if not caller.cooldowns.ready("restoration"):
            caller.msg(f"|CNot so fast!")
            return False

        wis = caller.traits.wis.value
        strength = caller.traits.str.value
        stat_bonus = strength * 0.25 + wis * 0.5
        hp = caller.db.hp
        hpmax = caller.db.hpmax
        fp = caller.db.fp

        to_heal = math.floor(30 + glvl + stat_bonus)
        to_heal = randint(int(to_heal * 0.75), to_heal)

        if fp < self.cost:
            self.msg(f"|rYou can't seem to focus on restoring your form.")
            return

        if hp + to_heal > hpmax:
            caller.db.hp = hpmax
            caller.db.fp -= self.cost
        else:
            caller.db.hp += max(to_heal, 0)
            caller.db.fp -= self.cost

        caller.cooldowns.add("global_cooldown", 2)
        caller.cooldowns.add("restoration", 10)

        msg = f"|M$pron(Your) rocky exterior begins to shift and mend. Cracks seal themselves as stones and minerals realign, drawn from the surrounding ground."
        caller.location.msg_contents(msg, from_obj=caller)


# region Earthen Renewal
class CmdEarthenRenewal(PowerCommand):
    """
    Earthen Renewal is a powerful regenerative ability harnessed by earth elementals. This skill taps into the primal energies of the earth, allowing the elemental to restore its vitality and fortitude over time. When activated, the elemental draws strength from the ground beneath it, channeling the life-giving essence of the earth to heal wounds and replenish its energy reserves. The process is gradual but potent, providing a steady flow of rejuvenation that scales with the elemental's mastery of the skill and its connection to the earth.

    Uses: earth resonance, earthen regeneration, wisdom, guild level
    """

    key = "earthen renewal"
    aliases = ["renew", "renewal", "er"]
    help_category = "earth elemental"
    guild_level = 9

    def _calculate_regeneration(
        self, earth_resonance, earthen_regeneration, wisdom, guild_level
    ):
        base_value = 10
        earth_resonance_weight = 0.4
        earthen_regeneration_weight = 0.4
        wisdom_weight = 0.1
        guild_level_weight = 0.1

        regeneration = (
            base_value
            + (earth_resonance * earth_resonance_weight)
            + (earthen_regeneration * earthen_regeneration_weight)
            + (wisdom * wisdom_weight)
            + (guild_level * guild_level_weight)
        )

        # Ensure regeneration is within the range of 10 to 30
        regeneration = max(10, min(regeneration, 30))

        return regeneration

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        energy_cost = 25 + glvl * 2

        if not caller.cooldowns.ready("earthen_renewal"):
            caller.msg(f"|yEarthen renewal isn't ready yet.")
            return False
        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False
        if not caller.db.earthen_renewal:
            caller.db.earthen_renewal = {"duration": 0, "rate": 0}
        if caller.db.earthen_renewal["duration"] > 0:
            caller.msg("You are already regenerating.")
            return
        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return
        if not caller.db.ep or caller.db.ep <= energy_cost:
            caller.msg("You don't have enough energy to regenerate.")
            return

        earthen_regen = caller.db.skills.get("earthen regeneration", 1)
        earth_resonance = caller.db.skills.get("earth resonance", 1)
        glvl = caller.db.guild_level
        wis = caller.traits.wis.value

        regen = self._calculate_regeneration(earth_resonance, earthen_regen, wis, glvl)
        # Calculate duration
        duration = int(2 + glvl * 0.1 + wis * 0.1 + earth_resonance)
        caller.db.earthen_renewal["duration"] = randint(duration, duration * 2)
        caller.db.earthen_renewal["rate"] = regen

        caller.adjust_ep(-energy_cost)
        caller.cooldowns.add("earthen_renewal", 60)
        caller.cooldowns.add("global_cooldown", 2)
        activateMsg = f"|C$Your() body glows with a soft, greenish light, and the ground around $pron(you) pulses with energy."
        caller.location.msg_contents(activateMsg, from_obj=caller)


# Offensive powers
# region Tremor
class CmdTremor(PowerCommand):
    """
    The earth elemental can cause the ground to shake, dealing damage to all
    enemies in the room. The amount of damage dealt is based on the elemental's
    skill rank.

    Uses: geological insight, strength, guild level

    Usage:
        tremor
    """

    key = "tremor"
    help_category = "earth elemental"
    guild_level = 10
    cost = 25

    def _calculate_damage(self, geological_insight, strength, guild_level):
        base_value = 20
        geological_insight_weight = 0.6
        strength_weight = 0.3
        guild_level_weight = 0.1

        damage = (
            base_value
            + (geological_insight * geological_insight_weight)
            + (strength * strength_weight)
            + (guild_level * guild_level_weight)
        )

        # Ensure damage is within the range of 100 to 300
        damage = max(100, min(damage, 300))

        # Adding some randomness to the damage
        damage = int(uniform(damage * 0.6, damage * 1.1))

        return damage

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        target = caller.db.combat_target

        if not target:
            caller.msg("You must be in combat to use this power.")
            return
        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False
        if not caller.cooldowns.ready("tremor"):
            caller.msg(f"|YTremor isn't ready yet.")
            return False
        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return
        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.adjust_fp(-self.cost)
        caller.cooldowns.add("tremor", 8)
        caller.cooldowns.add("global_cooldown", 2)

        skill_rank = caller.db.skills.get("geological insight", 1) * 10
        damage = self._calculate_damage(skill_rank, caller.traits.str.value, glvl)
        if self.caller.key == "Markar":
            self.msg(f"|gDamage: {damage}")

        for obj in caller.location.contents:
            if obj.db.can_attack == True:
                obj.at_damage(caller, damage, "blunt", "tremor")


# region Quicksand
class CmdQuickSand(PowerCommand):
    """
    The earth elemental can create a pool of quicksand beneath their enemies,
    slowing their movement and dealing damage over time. The amount of damage
    dealt is based on the elemental's skill rank in earth resonance, wisdom,
    and guild level.

    Usage:
        quicksand
        qs
        sand
    """

    key = "quicksand"
    aliases = ["qs", "sand"]
    help_category = "earth elemental"
    guild_level = 6
    cost = 10

    def _calculate_damage(self):
        earth_resonance = self.caller.db.skills.get("earth resonance", 1)
        wisdom = self.caller.traits.wis.value
        glvl = self.caller.db.guild_level

        base_value = 30
        earth_resonance_weight = 10
        wis_weight = 0.75
        guild_level_weight = 1

        damage = (
            base_value
            + (earth_resonance * earth_resonance_weight)
            + (wisdom * wis_weight)
            + (glvl * guild_level_weight)
        )

        # Adding some randomness to the damage
        damage = int(uniform(damage * 0.6, damage * 1))

        return damage

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        target = caller.db.combat_target

        if not target:
            caller.msg("You must be in combat to use this power.")
            return
        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False
        if not caller.cooldowns.ready("quicksand"):
            caller.msg(f"|YQuicksand isn't ready yet.")
            return False
        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return
        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.adjust_fp(-self.cost)
        caller.cooldowns.add("quicksand", 6)
        caller.cooldowns.add("global_cooldown", 2)

        damage = self._calculate_damage()
        target.at_damage(caller, damage, "blunt", "quicksand")


# region Rock Throw
class CmdRockThrow(PowerCommand):
    """
    The earth elemental can throw rocks at enemies in the room, dealing
    damage based on the elemental's skill rank.

    Usage:
        rock throw
    """

    key = "rock throw"
    aliases = ["rt"]
    help_category = "earth elemental"
    guild_level = 4
    cost = 5

    def _calculate_damage(self):
        base_value = 5
        stone_mastery_weight = 0.6
        strength_weight = 0.5
        guild_level_weight = 1
        stone_mastery = self.caller.db.skills.get("stone mastery", 1)
        strength = self.caller.traits.str.value
        guild_level = self.caller.db.guild_level

        damage = (
            base_value
            + ((stone_mastery * 10) * stone_mastery_weight)
            + (strength * strength_weight)
            + (guild_level * guild_level_weight)
        )

        # Ensure damage is within the range of 100 to 300
        damage = max(10, min(damage, 150))

        # Adding some randomness to the damage
        damage = int(uniform(damage * 0.6, damage * 1.1))

        return damage

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        target = caller.db.combat_target

        if not target:
            caller.msg("You must be in combat to use this power.")
            return
        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False
        if not caller.cooldowns.ready("rock throw"):
            caller.msg(f"|YRock Throw isn't ready yet.")
            return False
        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return
        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.adjust_fp(-self.cost)
        caller.cooldowns.add("rock throw", 4)
        caller.cooldowns.add("global_cooldown", 2)
        damage = self._calculate_damage()

        target.at_damage(caller, damage, "blunt", "rock_throw")


# region Landslide
class CmdLandslide(PowerCommand):
    """
    The earth elemental can create a landslide to rush over their target, inflicting massive damage. The amount of damage dealt is based on the elemental's skill in geological insight, seismic awareness, strength, and guild level.

    Usage:
        landslide
        lsl
    """

    key = "landslide"
    aliases = ["lsl"]
    help_category = "earth elemental"
    guild_level = 12
    cost = 20

    def _calculate_damage(self, caller):
        geo = caller.db.skills.get("geological insight", 1)
        seismic = caller.db.skills.get("seismic awareness", 1)
        strength = caller.traits.str.value
        guild_level = caller.db.guild_level

        base_value = 40
        geo_weight = 10
        seismic_weight = 10
        strength_weight = 0.6
        guild_level_weight = 1

        damage = (
            base_value
            + (geo * geo_weight)
            + (seismic * seismic_weight)
            + (strength * strength_weight)
            + (guild_level * guild_level_weight)
        )

        # Ensure damage is within the range of 100 to 300
        damage = max(100, min(damage, 300))

        # Adding some randomness to the damage
        damage = int(uniform(damage * 0.6, damage))

        return damage

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        target = caller.db.combat_target

        if not target:
            caller.msg("You must be in combat to use this power.")
            return
        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False
        if not caller.cooldowns.ready("landslide"):
            caller.msg(f"|YLandslide isn't ready yet.")
            return False
        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return
        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.adjust_fp(-self.cost)
        caller.cooldowns.add("landslide", 6)
        caller.cooldowns.add("global_cooldown", 2)

        damage = self._calculate_damage(caller)
        target.at_damage(caller, damage, "blunt ", "landslide")


class CmdHurlBoulder(PowerCommand):
    """
    The earth elemental can hurl a boulder at their target, dealing massive damage. The amount of damage dealt is based on the elemental's skill in stone mastery, strength, and guild level. Hurling a boulder requires a significant amount of focus, and time must pass before the elemental can use this power again.

    Usage:
        hurl boulder
        hb
    """

    key = "hurl boulder"
    aliases = ["hb"]
    help_category = "earth elemental"
    guild_level = 18
    cost = 30

    def _calculate_damage(self, caller):
        stone_mastery = caller.db.skills.get("stone mastery", 1)
        strength = caller.traits.str.value
        guild_level = caller.db.guild_level

        base_value = 50
        stone_mastery_weight = 10
        strength_weight = 1
        guild_level_weight = 1

        damage = (
            base_value
            + (stone_mastery * stone_mastery_weight)
            + (strength * strength_weight)
            + (guild_level * guild_level_weight)
        )

        # Ensure damage is within the range of 100 to 300
        damage = max(150, min(damage, 300))

        # Adding some randomness to the damage
        damage = int(uniform(damage * 0.85, damage))

        return damage

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        target = caller.db.combat_target

        if not target:
            caller.msg("You must be in combat to use this power.")
            return
        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False
        if not caller.cooldowns.ready("hurl_boulder"):
            caller.msg(f"|YHurl Boulder isn't ready yet.")
            return False
        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return
        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.adjust_fp(-self.cost)
        caller.cooldowns.add("hurl_boulder", 60)
        caller.cooldowns.add("global_cooldown", 2)

        damage = self._calculate_damage(caller)
        target.at_damage(caller, damage, "blunt", "hurl_boulder")


# region Lava flow
class CmdLavaFlow(PowerCommand):
    """
    The earth elemental can cause a flow of lava to erupt from the ground, dealing heavy fire damage. The amount of damage dealt is based on the elemental's skill rank.

    Usage:
        lava flow
    """

    key = "lava flow"
    aliases = ["lf"]
    help_category = "earth elemental"
    guild_level = 17
    cost = 40

    def _calculate_damage(self):
        base_value = 50
        geological_insight_weight = 4
        elemental_harmony_weight = 8
        strength_weight = 0.5
        wisdom = self.caller.traits.wis.value
        wisdom_weight = 0.5
        guild_level_weight = 0.1
        geological_insight = self.caller.db.skills.get("geological insight", 1)
        strength = self.caller.traits.str.value
        guild_level = self.caller.db.guild_level
        elemental_harmony = self.caller.db.skills.get("elemental harmony", 1)

        damage = (
            base_value
            + (geological_insight * geological_insight_weight)
            + (elemental_harmony * elemental_harmony_weight)
            + (strength * strength_weight)
            + (wisdom * wisdom_weight)
            + (guild_level * guild_level_weight)
        )

        # Ensure damage is within the range of 100 to 300
        damage = max(100, min(damage, 300))

        # Adding some randomness to the damage
        damage = int(uniform(damage * 0.8, damage * 1.1))

        return damage

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        target = caller.db.combat_target

        if not target:
            caller.msg("You must be in combat to use this power.")
            return
        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False
        if not caller.cooldowns.ready("lava_flow"):
            caller.msg(f"|YLava Flow isn't ready yet.")
            return False
        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return
        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.adjust_fp(-self.cost)
        caller.cooldowns.add("lava_flow", 12)
        caller.cooldowns.add("global_cooldown", 2)

        damage = self._calculate_damage()

        if self.caller.key == "Markar":
            self.msg(f"|gDamage: {damage}")

        for obj in caller.location.contents:
            if obj.db.can_attack == True:
                obj.at_damage(caller, damage, "fire", "lava_flow")


class CmdMagmaForm(PowerCommand):
    """
    The earth elemental can transform their body into molten magma, increasing their offensive capabilities and dealing fire damage to enemies. The amount of damage dealt is based on the elemental's skill rank.

    Usage:
        magma form
    """

    key = "magma form"
    aliases = ["mf"]
    help_category = "earth elemental"
    guild_level = 15
    cost = 50

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        if glvl < self.guild_level:
            caller.msg(
                f"|CYou need to be guild level {self.guild_level} to use magma form."
            )
            return
        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False
        if not caller.cooldowns.ready("magma_form"):
            caller.msg(f"|YMagma Form isn't ready yet.")
            return False
        if caller.db.ep < self.cost:
            caller.msg(f"|rYou need at least {self.cost} energy to use this power.")
            return

        if not caller.db.magma_form:
            caller.db.magma_form = {"active": True, "duration": 10}
            caller.db.active_form = "magma"
            caller.db.ep -= self.cost
            cooldown = 60

            caller.cooldowns.add("global_cooldown", 2)
            caller.cooldowns.add("magma_form", cooldown)

            activateMsg = f"|C$Your() form shifts and hardens, transforming into a molten, fiery form."
            caller.location.msg_contents(activateMsg, from_obj=caller)
        else:
            caller.db.magma_form = {"active": False, "duration": 0}
            deactivateMsg = (
                f"|C$Your() form cools and solidifies, returning to its normal state."
            )
            caller.location.msg_contents(deactivateMsg, from_obj=caller)


# region Earthquake
class CmdEarthquake(PowerCommand):
    """
    The earth elemental can cause the ground to shake, causing damage to all
    enemies in the room. The amount of damage dealt is based on the elemental's
    skill rank.

    Usage:
        earthquake
    """

    key = "earthquake"
    aliases = ["eq", "quake"]
    help_category = "earth elemental"
    guild_level = 20
    cost = 30

    def _calculate_damage(self, seismic_awareness, guild_level):
        base_value = 50
        seismic_awareness_weight = 15
        wisdom_weight = 0.75
        wisdom = self.caller.traits.wis.value
        guild_level_weight = 1.5
        # 50 + 80 + 25 + 30

        damage = (
            base_value
            + (seismic_awareness * seismic_awareness_weight)
            + (wisdom * wisdom_weight)
            + (guild_level * guild_level_weight)
        )

        # Ensure damage is within the range of 100 to 300
        damage = max(100, min(damage, 300))

        # Adding some randomness to the damage
        damage = int(uniform(damage * 0.7, damage))

        return damage

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        target = caller.db.combat_target

        if not target:
            caller.msg("You must be in combat to use this power.")
            return
        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False
        if not caller.cooldowns.ready("earthquake"):
            caller.msg(f"|YEarthquake isn't ready yet.")
            return False
        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return
        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.adjust_fp(-self.cost)
        caller.cooldowns.add("earthquake", 10)
        caller.cooldowns.add("global_cooldown", 2)
        skill_rank = caller.db.skills.get("seismic awareness", 1)

        damage = self._calculate_damage(skill_rank, caller.traits.str.value, glvl)
        for obj in caller.location.contents:
            if obj.db.can_attack == True:
                obj.at_damage(caller, damage, "blunt", "earthquake")


class CmdEnervate(PowerCommand):
    """
    Enervate is a powerful ability that allows the earth elemental to drain the energy from their enemies, weakening them and restoring the elemental's own energy reserves. The elemental can siphon the energy from a single target, reducing their combat effectiveness and replenishing their own strength. The amount of energy drained is based on your elemental harmony rank and the target's level of vitality.
    """

    key = "enervate"
    help_category = "earth elemental"
    guild_level = 16
    aliases = ["en"]
    fp_cost = 25

    def func(self):
        caller = self.caller
        target = caller.db.combat_target
        skill_rank = caller.db.skills.get("energy drain", 1)
        vitality = target.db.level

        if not target:
            caller.msg("You must be in combat to use this power.")
            return
        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False
        if not caller.cooldowns.ready("enervate"):
            caller.msg(f"|YEnervate isn't ready yet.")
            return False
        if caller.db.guild_level < self.guild_level:
            caller.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return
        if caller.db.fp < self.fp_cost:
            caller.msg(f"|rYou need at least {self.fp_cost} focus to use this power.")
            return

        caller.cooldowns.add("enervate", 60)
        caller.cooldowns.add("global_cooldown", 2)

        energy_drained = randint(vitality, vitality * 2) + skill_rank * 10

        caller.adjust_fp(-self.fp_cost)
        caller.adjust_ep(energy_drained)

        target.msg(f"|r$You feel your energy being drained by {caller}.")
        caller.msg(f"|gYou drain energy from {target}, restoring your own strength.")
        caller.location.msg_contents(
            f"|r$You() drains energy from {target}.", from_obj=caller
        )


# Other powers
class CmdPowers(Command):
    """
    List of powers available to the Elemental, their rank, and their cost.

    Usage:
        powers

    """

    key = "powers"
    help_category = "earth elemental"

    def func(self):
        caller = self.caller

        table = EvTable(f"|cPower", f"|cRank", f"|cType", f"|cCost", border="table")
        table.add_row(f"|GReaction", 1, "Utility", 0)
        table.add_row(f"|GMeditate", 1, "Utility", 0)
        table.add_row(f"|GMud Patch", 2, "Healing", "10 Focus")
        table.add_row(f"|GRock Throw", 4, "Direct Damage", "5 Focus")
        table.add_row(f"|GQuicksand", 6, "Direct Damage", "10 Focus")
        table.add_row(f"|GBurnout", 7, "Essence", "7 Essence")
        table.add_row(f"|GStone Skin", 8, "Defensive", "25 Energy")
        table.add_row(f"|GEarthen Renewal", 9, "Healing", "50 Energy")
        table.add_row(f"|GTremor", 10, "Area Damage", "25 Focus")
        table.add_row(f"|GTerran Restoration", 11, "Healing", "20 Focus")
        table.add_row(f"|GLandslide", 12, "Direct Damage", "20 Focus")
        table.add_row(f"|GEarth Shield", 13, "Defensive", "50 Energy")
        table.add_row(f"|GHurl Boulder", 14, "Direct Damage", "35 Focus")
        table.add_row(f"|GEarth Form", 15, "Form", "50 Energy")
        table.add_row(f"|GEnervate", 16, "Healing", "25 Focus")
        table.add_row(f"|GLava Flow", 17, "Area Damage", "30 Energy")
        table.add_row(f"|GElemental Fury", 18, "Essence", "12 Essence")
        table.add_row(f"|GEarthquake", 20, "Area Damage", "50 Focus")
        table.add_row(f"|GMagma Form", 22, "Form", "50 Energy")
        table.add_row(f"|GMountain Stance", 28, "Stance", "75 Energy")
        table.add_row(f"|GEarthshaker Stance", 30, "Stance", "75 Energy")

        caller.msg(str(table))


class CmdReaction(Command):
    """
    Set the elemental's reaction to a dropping below a certain health threshold.

    Usage:
        reaction <percentage>
    """

    key = "reaction"
    help_category = "earth elemental"

    def func(self):
        caller = self.caller
        args = self.args.strip()

        if not self.args:
            caller.msg("Usage: reaction <percentage>")
            return

        if not args.isdigit():
            caller.msg("Invalid percentage")
            return

        caller.db.reaction_percentage = args
        caller.msg(f"Reaction set to {args}.")


class CmdGTrain(Command):
    """
    Train your guild skills by spending skill experience points. Each rank
    increases your effectiveness in that skill.

    Usage:
        gtrain <skill>

    Example:
        gtrain mineral fortification
    """

    key = "gtrain"
    help_category = "Earth Elemental"

    def func(self):
        caller = self.caller
        skill = self.args.strip().lower()
        list = caller.db.skills.keys()

        if skill == "":
            self.msg(f"|gWhat would you like to raise?")
            return

        if skill not in list:
            caller.msg(f"|gYou can't raise that.")
            return

        skill_gxp = getattr(caller.db, "skill_gxp", 0)
        cost = caller.db.skills[f"{skill}"]
        cost = SKILLS_COST[cost]

        if skill_gxp < cost:
            self.msg(f"|wYou need {skill_gxp-cost} more experience to train {skill}.")
            return

        confirm = yield (
            f"It will cost you {cost} experience to advance {skill}. Confirm? Yes/No"
        )
        if confirm.lower() not in (
            "yes",
            "y",
        ):
            self.msg("Cancelled.")
            return

        setattr(caller.db, "skill_gxp", skill_gxp - cost)
        if skill == "elemental harmony":
            caller.db.epmax += 25
        caller.db.skills[skill] += 1
        caller.msg(f"|yYou grow more experienced in {skill}")


class CmdGhelp(Command):
    """
    Help files for the Elemental Guild.

    mineral fortification
    earthen regeneration
    rock solid defense

    Usage:
        ghelp
        ghelp <skill>
    """

    key = "ghelp"
    help_category = "earth elemental"

    def func(self):
        caller = self.caller
        skill = self.args.strip().lower()
        if skill == "":
            caller.msg(
                "|cElemental Guild|n\n\n"
                "The Elemental Guild is a group of beings that have learned to harness the power of the elements to enhance their physical abilities and combat prowess.\n\n"
                "Usage:\n"
                "    ghelp <skill>\n"
            )
            return
        if skill == "stone mastery":
            caller.msg(
                "|cStone Mastery|n\n\n"
                "Increases the elemental's control over stone, enhancing the effectiveness of all stone-based abilities.\n\n"
            )
            return
        if skill == "earth resonance":
            caller.msg(
                "|cEarth Resonance|n\n\n"
                "Enhances the elemental's connection to the earth, allowing for greater control over the environment.\n\n"
            )
            return
        if skill == "mineral fortification":
            caller.msg(
                "|cMineral Fortification|n\n\n"
                "Enhances the elemental's body with rare minerals, increasing overall resilience and strength.\n\n"
                "Usage:\n"
                "    mineral fortification\n"
                "    mf\n"
            )
            return
        if skill == "geological insight":
            caller.msg(
                "|cGeological Insight|n\n\n"
                "Geological Insight grants the elemental a heightened awareness of the earth's hidden treasures and weaknesses. This skill allows the elemental to sense valuable minerals, underground water sources, and structural vulnerabilities in the terrain. By tapping into this knowledge, the elemental can gain strategic advantages, such as creating more effective traps, finding hidden resources, and exploiting the terrain to outmaneuver opponents.\n\n"
            )
            return
        if skill == "seismic awareness":
            caller.msg(
                "|cSeismic Awareness|n\n\n"
                "Increases the elemental's ability to sense vibrations in the earth, allowing for greater awareness of their surroundings.\n\n"
            )
            return
        if skill == "rock solid defense":
            caller.msg(
                "|cRock Solid Defense|n\n\n"
                "Strengthens the elemental's defensive capabilities, making it harder for enemies to penetrate their defenses. This skill provides benefits earth form, and provides a passive benefit. \n\n"
                "Usage:\n"
                "    rock solid defense\n"
                "    rsd\n"
            )
            return
        if skill == "elemental harmony":
            caller.msg(
                "Enhances the elemental's connection to the earth, allowing for greater control over the environment. \n\n"
                "Additionally, this skill allows the elemental to restore more Primordial Essence over time, increasing their ability to use powerful abilities.\n\n"
            )
            return
        if skill == "earthen regeneration":
            caller.msg(
                "|cTerran Restoration|n\n\n"
                "Improves the elemental's natural healing abilities, allowing for faster recovery from mental exhaustion. This skill also directly impacts the efficacy of earthen renewal.\n\n"
            )
            return

        caller.msg(f"|rNo help found for {skill}.")


from typeclasses.cybercorpsguild.cybercorps_commands import CybercorpsCmdSet
from typeclasses.cybercorpsguild.cybercorps_wares import CybercorpsWaresCmdSet
from typeclasses.cybercorpsguild.cyber_implants import CybercorpsImplantCmdSet


class Test(Command):
    key = "test2"

    def func(self):
        caller = self.caller
        self.msg("Test command")
        # cost = self.caller.db.skills["mineral fortification"] + 1
        # self.msg(f"|gCost: {cost}")
        # cost = SKILLS_COST[cost]
        # self.msg(f"|gCost2: {cost}")

        caller.cmdset.delete(CybercorpsCmdSet)
        caller.cmdset.delete(CybercorpsWaresCmdSet)
        caller.cmdset.delete(CybercorpsImplantCmdSet)
        self.msg("DONE")


class EarthElementalCmdSet(CmdSet):
    key = "Earth Elemental CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        self.add(CmdTerranRestoration)
        self.add(CmdEarthShield)
        self.add(CmdStoneSkin)
        self.add(CmdEnervate)
        self.add(CmdPowers)
        self.add(CmdReaction)
        self.add(CmdGTrain)
        self.add(CmdGhelp)
        self.add(CmdTremor)
        self.add(CmdQuickSand)
        self.add(CmdRockThrow)
        self.add(CmdEarthquake)
        self.add(CmdEarthForm)
        self.add(CmdMountainStance)
        self.add(CmdEarthenRenewal)
        self.add(CmdEarthshakerStance)
        self.add(CmdBurnout)
        self.add(CmdLandslide)
        self.add(CmdMagmaForm)
        self.add(CmdMudPatch)
        self.add(CmdHurlBoulder)
        self.add(CmdLavaFlow)
        self.add(CmdElementalFury)
        self.add(Test)
