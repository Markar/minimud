import math
from random import randint, uniform
from evennia import CmdSet
from evennia.utils.evtable import EvTable
from commands.command import Command
from typeclasses.elementalguild.constants_and_helpers import SKILLS_COST


class PowerCommand(Command):
    def func(self):
        caller = self.caller
        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False
        caller.cooldowns.add("global_cooldown", 2)


class CmdBurnout(PowerCommand):
    """
    This powerful ability allows the earth elemental to channel energy from all elemental forces, enhancing their physical abilities and combat prowess. While active, the elemental's attacks become more potent, and their movements more fluid and precise. The elemental's power is greatly increased while burnout is active, but the strain of maintaining this heightened state of power can be overwhelming, and the elemental must be cautious not to overextend themselves.

    Usage:
        burnout
    """

    key = "burnout"
    help_category = "earth elemental"
    cost = 10

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        if not caller.db.burnout["count"] > 0:
            caller.msg(f"|CYou are too tired to use this power.")
            return
        if not caller.cooldowns.ready("burnout"):
            caller.msg(f"|CNot so fast!")
            return False
        if caller.db.ep < self.cost:
            caller.msg(f"|rYou need at least {self.cost} energy to use this power.")
            return
        if glvl < 10:
            caller.msg(f"|CYou need to be guild level 10 to use burnout.")
            return
        if caller.db.burnout["active"]:
            caller.msg(f"|CYour power is already surging.")
            return
        caller.db.ep -= self.cost
        caller.cooldowns.add("burnout", 60)
        caller.cooldowns.add("global_cooldown", 2)
        skill_rank = caller.db.skills.get("elemental harmony", 1)

        self.msg(
            f"|cA radiant aura of elemental energy envelops you, your power surging to new heights!|n"
        )

        caller.db.burnout["active"] = True
        caller.db.burnout["count"] -= 1
        caller.db.burnout["duration"] = 3 + skill_rank * 2


# Defensive powers
class CmdStoneSkin(PowerCommand):
    """
    Stone skin increases the earth elemental's defense by
    increasing their resistance to physical damage. The amount of damage
    reduced is based on the elemental's skill rank.

    Usage:
        stone skin
        ss
    """

    key = "stone skin"
    aliases = ["ss"]
    help_category = "earth elemental"
    cost = 25

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        if glvl < 5:
            caller.msg(f"|CYou need to be guild level 5 to use stone skin.")
            return
        if caller.db.ep < self.cost:
            caller.msg(f"|rYou need at least {self.cost} energy to use this power.")
            return
        if not caller.db.stone_skin:
            caller.db.stone_skin = True
            caller.db.ep -= self.cost
            caller.cooldowns.add("global_cooldown", 2)
            activateMsg = f"|C$Your() body hardens, rocky plates forming a protective barrier that absorbs and deflects incoming attacks."
            caller.location.msg_contents(activateMsg, from_obj=caller)
        else:
            caller.db.stone_skin = False
            deactivateMsg = f"|C$Your() body softens, the rocky plates that once protected $pron(you) now dissipating."
            caller.location.msg_contents(deactivateMsg, from_obj=caller)


class CmdEarthForm(PowerCommand):
    """
    The earth elemental can transform their body into a denser form of rock,
    increasing their defense and resistance to damage. The amount of damage
    reduced is based on the elemental's skill rank.

    Usage:
        earth form
    """

    key = "earth form"
    aliases = ["ef"]
    help_category = "earth elemental"
    cost = 50

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        if glvl < 24:
            caller.msg(f"|CYou need to be guild level 24 to use earth form.")
            return
        if caller.db.ep < self.cost:
            caller.msg(f"|rYou need at least {self.cost} energy to use this power.")
            return
        if not caller.db.earth_form:
            caller.db.earth_form = True
            caller.db.ep -= self.cost
            caller.cooldowns.add("global_cooldown", 2)
            activateMsg = f"|C$Your() form shifts and hardens, transforming into a denser, more resilient form of rock."
            caller.location.msg_contents(activateMsg, from_obj=caller)
        else:
            caller.db.earth_form = False
            deactivateMsg = f"|C$Your() form softens and returns to its normal state."
            caller.location.msg_contents(deactivateMsg, from_obj=caller)


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

    def func(self):
        super().func()
        caller = self.caller
        glvl = caller.db.guild_level
        if glvl < 14:
            caller.msg(f"|CYou need to be guild level 14 to use earth shield.")
            return
        if not caller.cooldowns.ready("earth_shield"):
            caller.msg(f"|CNot so fast!")
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
    guild_level = 4

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level

        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return

        if not caller.cooldowns.ready("rebuild"):
            caller.msg(f"|CNot so fast!")
            return False
        caller.cooldowns.add("rebuild", 4)

        wis = caller.traits.wis.value
        strength = caller.traits.str.value
        hp = caller.db.hp
        hpmax = caller.db.hpmax
        fp = caller.db.fp
        hp_amount = 0

        to_heal = math.floor(10 + glvl + strength / 2 + wis / 2)
        to_heal = randint(int(to_heal / 2), to_heal)
        cost = to_heal

        if fp < cost:
            self.msg(f"|rYou can't seem to focus on restoring your form.")
            return

        if hp + to_heal > hpmax:
            hp_amount = hpmax - hp
            caller.db.hp = hpmax
            caller.db.fp -= cost
        else:
            hp_amount = hpmax - hp
            caller.db.hp += max(to_heal, 0)
            caller.db.fp -= cost

        caller.cooldowns.add("global_cooldown", 2)
        self.msg(f"You restore {hp_amount or 0} health for {cost or 0} focus")
        msg = f"|M$pron(Your) rocky exterior begins to shift and mend. Cracks seal themselves as stones and minerals realign, drawn from the surrounding ground."
        caller.location.msg_contents(msg, from_obj=caller)


class CmdEarthenRenewal(PowerCommand):
    """
    Earthen Renewal is a powerful regenerative ability harnessed by earth elementals. This skill taps into the primal energies of the earth, allowing the elemental to restore its vitality and fortitude over time. When activated, the elemental draws strength from the ground beneath it, channeling the life-giving essence of the earth to heal wounds and replenish its energy reserves. The process is gradual but potent, providing a steady flow of rejuvenation that scales with the elemental's mastery of the skill and its connection to the earth.
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
class CmdTremor(PowerCommand):
    """
    The earth elemental can cause the ground to shake, dealing damage to all
    enemies in the room. The amount of damage dealt is based on the elemental's
    skill rank.

    Usage:
        tremor
    """

    key = "tremor"
    help_category = "earth elemental"
    guild_level = 12
    cost = 20

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
        if not caller.cooldowns.ready("tremor"):
            caller.msg(f"|CNot so fast!")
            return False
        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return
        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.adjust_fp(-self.cost)
        caller.cooldowns.add("tremor", 4)
        caller.cooldowns.add("global_cooldown", 2)

        skill_rank = caller.db.skills.get("geological insight", 1) * 10
        damage = self._calculate_damage(skill_rank, caller.traits.str.value, glvl)
        self.msg(f"|gDamage: {damage}")
        target.at_damage(caller, damage, "blunt", "tremor")


class CmdQuickSand(PowerCommand):
    """
    The earth elemental can create a pool of quicksand beneath their enemies,
    slowing their movement and dealing damage over time. The amount of damage
    dealt is based on the elemental's skill rank.

    Usage:
        quicksand
    """

    key = "quicksand"
    help_category = "earth elemental"
    guild_level = 6
    cost = 10

    def _calculate_damage(self, earth_resonance, strength, guild_level):
        base_value = 50
        earth_resonance_weight = 0.6
        strength_weight = 0.3
        guild_level_weight = 0.1

        damage = (
            base_value
            + (earth_resonance * earth_resonance_weight)
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
        if not caller.cooldowns.ready("quicksand"):
            caller.msg(f"|CNot so fast!")
            return False
        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return
        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.adjust_fp(-self.cost)
        caller.cooldowns.add("quicksand", 4)
        caller.cooldowns.add("global_cooldown", 2)
        skill_rank = caller.db.skills.get("earth resonance", 1) * 10

        damage = self._calculate_damage(skill_rank, caller.traits.str.value, glvl)
        self.msg(f"|gDamage: {damage}")
        target.at_damage(caller, damage, "blunt", "quicksand")


class CmdRockThrow(PowerCommand):
    """
    The earth elemental can throw rocks at enemies in the room, dealing
    damage based on the elemental's skill rank.

    Usage:
        rock throw
    """

    key = "rock throw"
    help_category = "earth elemental"
    guild_level = 2
    cost = 5

    def _calculate_damage(self, stone_mastery, strength, guild_level):
        base_value = 5
        stone_mastery_weight = 0.6
        strength_weight = 0.5
        guild_level_weight = 1

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
        if not caller.cooldowns.ready("rock throw"):
            caller.msg(f"|CNot so fast!")
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
        skill_rank = caller.db.skills.get("stone mastery", 1) * 10
        damage = self._calculate_damage(skill_rank, caller.traits.str.value, glvl)

        target.at_damage(caller, damage, "blunt", "rock_throw")


class CmdEarthquake(PowerCommand):
    """
    The earth elemental can cause the ground to shake, causing damage to all
    enemies in the room. The amount of damage dealt is based on the elemental's
    skill rank.

    Usage:
        earthquake
    """

    key = "earthquake"
    help_category = "earth elemental"
    guild_level = 20
    cost = 50

    def _calculate_damage(self, seismic_awareness, strength, guild_level):
        base_value = 50
        seismic_awareness_weight = 0.6
        strength_weight = 0.3
        guild_level_weight = 0.1

        damage = (
            base_value
            + (seismic_awareness * seismic_awareness_weight)
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
        if not caller.cooldowns.ready("earthquake"):
            caller.msg(f"|CNot so fast!")
            return False
        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return
        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.adjust_fp(-self.cost)
        caller.cooldowns.add("earthquake", 4)
        caller.cooldowns.add("global_cooldown", 2)
        skill_rank = caller.db.skills.get("seismic awareness", 1) * 10

        damage = self._calculate_damage(skill_rank, caller.traits.str.value, glvl)
        self.msg(f"|gDamage: {damage}")
        target.at_damage(caller, damage, "blunt", "earthquake")


class CmdAssimilate(Command):
    """
    Assimilate the corpse of an enemy to restore energy
    """

    key = "assimilate"
    aliases = ["asm"]
    help_category = "earth elemental"

    def func(self):
        if not self.args:
            caller = self.caller
            if corpse := caller.location.search("corpse-1"):
                base_power = corpse.db.power
                skill_rank = caller.db.skills.get("assimilate", 0)

                # Calculate the power with the skill rank multiplier
                power = base_power * (1 + (skill_rank * 0.1))

                caller.adjust_ep(power)
                corpse.delete()
                assimilate_msg = f"|M$pron(Your) form glows faintly as it assimilates the energy from the consumed corpse, strengthening $pron(your) rocky exterior."
                caller.location.msg_contents(assimilate_msg, from_obj=caller)
            else:
                caller.msg("Assimilate what?")


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

        table = EvTable(f"|cPower", f"|cRank", f"|cCost", border="table")
        table.add_row(f"|GAssimilate", 1, 0)
        table.add_row(f"|GReaction", 1, 0)
        table.add_row(f"|GRock Throw", 2, "5 Focus")
        table.add_row(f"|GTerran Restoration", 4, "varies")
        table.add_row(f"|GQuicksand", 6, "10 Focus")
        table.add_row(f"|GStone Skin", 7, "25 Energy")
        table.add_row(f"|GEarthen Renewal", 9, "50 Energy")
        table.add_row(f"|GBurnout", 7, "10 Energy")
        table.add_row(f"|GTremor", 12, "20 Focus")
        table.add_row(f"|GEarth Shield", 14, "50 Energy")
        table.add_row(f"|GEarthquake", 20, "50 Focus")
        table.add_row(f"|GEarth Form", 24, "50 Energy")
        table.add_row(f"|GMountain Stance", 28, "75 Energy")
        table.add_row(f"|GEarthshaker Stance", 30, "75 Energy")

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
            self.msg(f"|wYou need {cost-skill_gxp} more experience to train {skill}.")
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
        caller.db.skills[skill] += 1
        caller.msg(f"|yYou grow more experienced in {skill}")


class CmdGhelp(Command):
    """
    Help files for the Elemental Guild.

    mineral fortification
    assimilation
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
                "Increases the elemental's control over stone, enhancing the effectiveness of all earth-based abilities.\n\n"
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
                "Strengthens the elemental's defensive capabilities, making it harder for enemies to penetrate their defenses.\n\n"
                "Usage:\n"
                "    rock solid defense\n"
                "    rsd\n"
            )
            return
        if skill == "elemental harmony":
            caller.msg(
                "|cElemental Harmony|n\n\n"
                "Enhances the elemental's connection to the earth, allowing for greater control over the environment.\n\n"
            )
            return
        if skill == "earthen regeneration":
            caller.msg(
                "|cTerran Restoration|n\n\n"
                "Improves the elemental's natural healing abilities, allowing for faster recovery from injuries.\n\n"
                "Usage:\n"
                "    terran restoration\n"
                "    tr\n"
                "    restore\n"
            )
            return
        if skill == "assimilation":
            caller.msg(
                "|cAssimilation|n\n\n"
                "Improves the elemental's ability to regain energy from corpses.\n\n"
                "Usage:\n"
                "    assimilate\n"
                "    asm\n"
            )
            return

        caller.msg(f"|rNo help found for {skill}.")


class Test(Command):
    key = "test2"

    def func(self):
        self.msg("Test command")
        cost = self.caller.db.skills["mineral fortification"] + 1
        self.msg(f"|gCost: {cost}")
        cost = SKILLS_COST[cost]
        self.msg(f"|gCost2: {cost}")


class EarthElementalCmdSet(CmdSet):
    key = "Earth Elemental CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        self.add(CmdAssimilate)
        self.add(CmdTerranRestoration)
        self.add(CmdEarthShield)
        self.add(CmdStoneSkin)
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
        self.add(Test)
