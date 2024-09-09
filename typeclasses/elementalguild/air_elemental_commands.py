import math
from random import randint, uniform
from evennia import CmdSet
from evennia.utils.evtable import EvTable
from commands.command import Command
from typeclasses.elementalguild.constants_and_helpers import SKILLS_COST
from typeclasses.utils import PowerCommand


class CmdZephyr(PowerCommand):
    """
    The air elemental can unleash a powerful zephyr, dealing damage to their target. The strength of the zephyr is based on the elemental's wisdom and guild level.
    """

    key = "zephyr"
    help_category = "air elemental"
    guild_level = 1
    cost = 5

    def _calculate_damage(self, wind_mastery, wisdom, guild_level):
        base_value = 5
        wind_mastery_weight = 0.6
        wisdom_weight = 0.5
        guild_level_weight = 1

        damage = (
            base_value
            + ((wind_mastery * 10) * wind_mastery_weight)
            + (wisdom * wisdom_weight)
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
        if not caller.cooldowns.ready("zephyr"):
            caller.msg(f"|CNot so fast!")
            return False
        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return
        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.adjust_fp(-self.cost)
        caller.cooldowns.add("zephyr", 4)
        caller.cooldowns.add("global_cooldown", 2)
        skill_rank = caller.db.skills.get("wind mastery", 1) * 10
        damage = self._calculate_damage(skill_rank, caller.traits.wis.value, glvl)

        target.at_damage(caller, damage, "blunt", "zephyr")


class CmdAirForm(PowerCommand):
    """
    The air elemental can transform into an air form, gaining the ability to move more quickly and evade attacks more easily. While in air form, the elemental's attacks become more potent, and their movements more fluid and precise. The elemental's power is greatly increased while in air form, but the strain of maintaining this heightened state of power can be overwhelming, and the elemental must be cautious not to overextend themselves.
    """

    key = "air form"
    aliases = ["af"]
    help_category = "air elemental"
    cost = 50

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        if glvl < 12:
            caller.msg(f"|CYou need to be guild level 5 to use air form.")
            return
        if caller.db.ep < self.cost:
            caller.msg(f"|rYou need at least {self.cost} energy to use this power.")
            return
        if not caller.db.air_form:
            caller.db.air_form = True
            caller.db.ep -= self.cost
            caller.cooldowns.add("global_cooldown", 2)
            activateMsg = f"|C$Your() form shifts, transforming into a swirling vortex of air and energy."
            caller.location.msg_contents(activateMsg, from_obj=caller)
        else:
            caller.db.air_form = False
            deactivateMsg = f"|CThe vortex surrounding $you() dissipates, revealing $pron(your) true form."
            caller.location.msg_contents(deactivateMsg, from_obj=caller)


class CmdTornado(PowerCommand):
    """
    The air elemental can unleash a powerful tornado, dealing damage to their target. The strength of the tornado is based on the elemental's wisdom and guild level.
    """

    key = "tornado"
    help_category = "air elemental"
    guild_level = 15
    cost = 15

    def _calculate_damage(self, tempest_control, wisdom, guild_level):
        base_value = 15
        tempest_control_weight = 10
        wisdom_weight = 0.3
        guild_level_weight = 1

        damage = (
            base_value
            + (tempest_control * tempest_control_weight)
            + (wisdom * wisdom_weight)
            + (guild_level * guild_level_weight)
        )

        # Ensure damage is within the range of 100 to 300
        damage = max(15, min(damage, 300))

        # Adding some randomness to the damage
        damage = int(uniform(damage * 0.6, damage * 1.4))

        return damage

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        target = caller.db.combat_target

        if not target:
            caller.msg("You must be in combat to use this power.")
            return
        if not caller.cooldowns.ready("tornado"):
            caller.msg(f"|CNot so fast!")
            return False
        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return
        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.adjust_fp(-self.cost)
        caller.cooldowns.add("tornado", 4)
        caller.cooldowns.add("global_cooldown", 2)
        skill_rank = caller.db.skills.get("tempest control", 1)

        damage = self._calculate_damage(skill_rank, caller.traits.wis.value, glvl)
        self.msg(f"|gDamage: {damage}")
        target.at_damage(caller, damage, "blunt", "tornado")


class CmdWhirlwind(PowerCommand):
    """
    The air elemental can unleash a powerful whirlwind, dealing damage to their target. The strength of the whirlwind is based on the elemental's wisdom and guild level.
    """

    key = "whirlwind"
    help_category = "air elemental"
    guild_level = 7
    cost = 5

    def _calculate_damage(self, gale_force, wisdom, guild_level):
        base_value = 7
        gale_force_weight = 7
        wisdom_weight = 0.5
        guild_level_weight = 1

        damage = (
            base_value
            + (gale_force * gale_force_weight)
            + (wisdom * wisdom_weight)
            + (guild_level * guild_level_weight)
        )

        # Ensure damage is within the range of 100 to 300
        damage = max(7, min(damage, 300))

        # Adding some randomness to the damage
        damage = int(uniform(damage * 0.6, damage * 1.4))

        return damage

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        target = caller.db.combat_target

        if not target:
            caller.msg("You must be in combat to use this power.")
            return
        if not caller.cooldowns.ready("whirlwind"):
            caller.msg(f"|CNot so fast!")
            return False
        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return
        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.adjust_fp(-self.cost)
        caller.cooldowns.add("whirlwind", 4)
        caller.cooldowns.add("global_cooldown", 2)
        skill_rank = caller.db.skills.get("gale force", 1)
        damage = self._calculate_damage(skill_rank, caller.traits.wis.value, glvl)

        target.at_damage(caller, damage, "blunt", "whirlwind")


class CmdLightningStrike(PowerCommand):
    """
    The air elemental can unleash a powerful lightning strike, dealing damage to their target. The strength of the lightning strike is based on the elemental's wisdom and guild level.
    """

    key = "lightning strike"
    help_category = "air elemental"
    guild_level = 20
    cost = 20

    def _calculate_damage(self, tempest_control, wisdom, guild_level):
        base_value = 50
        tempest_control_weight = 15
        wisdom_weight = 0.6
        guild_level_weight = 0.1

        damage = (
            base_value
            + (tempest_control * tempest_control_weight)
            + (wisdom * wisdom_weight)
            + (guild_level * guild_level_weight)
        )

        # Ensure damage is within the range of 100 to 300
        damage = max(100, min(damage, 200))

        # Adding some randomness to the damage
        damage = int(uniform(damage * 0.6, damage * 1.5))

        return damage

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        target = caller.db.combat_target

        if not target:
            caller.msg("You must be in combat to use this power.")
            return
        if not caller.cooldowns.ready("lightning_strike"):
            caller.msg(f"|CNot so fast!")
            return False
        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return
        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.adjust_fp(-self.cost)
        caller.cooldowns.add("lightning_strike", 4)
        caller.cooldowns.add("global_cooldown", 2)
        skill_rank = caller.db.skills.get("tempest control", 1) * 10

        damage = self._calculate_damage(skill_rank, caller.traits.wis.value, glvl)
        self.msg(f"|gDamage: {damage}")
        target.at_damage(caller, damage, "lightning", "lightning_strike")
        damage = self._calculate_damage(skill_rank, caller.traits.wis.value, glvl)
        self.msg(f"|gDamage: {damage}")
        target.at_damage(caller, damage, "lightning", "lightning_strike")


class CmdStormForm(PowerCommand):
    """
    The air elemental can transform into a storm form, gaining the ability to control the weather and unleash powerful storms. While in storm form, the elemental's attacks become more potent, and their movements more fluid and precise. The elemental's power is greatly increased while in storm form, but the strain of maintaining this heightened state of power can be overwhelming, and the elemental must be cautious not to overextend themselves.
    """

    key = "storm form"
    aliases = ["sf"]
    help_category = "air elemental"
    cost = 50
    guild_level = 24

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        if glvl < self.guild_level:
            caller.msg(f"|CYou need to be guild level 24 to use storm form.")
            return
        if caller.db.ep < self.cost:
            caller.msg(f"|rYou need at least {self.cost} energy to use this power.")
            return
        if not caller.db.storm_form:
            caller.db.storm_form = True
            caller.db.ep -= self.cost
            caller.cooldowns.add("global_cooldown", 2)
            activateMsg = f"|C$Your() form shifts, transforming into a swirling storm of wind and lightning."
            caller.location.msg_contents(activateMsg, from_obj=caller)
        else:
            caller.db.storm_form = False
            deactivateMsg = f"|CThe storm surrounding $you() dissipates, revealing $pron(your) true form."
            caller.location.msg_contents(deactivateMsg, from_obj=caller)


class CmdWindSlash(PowerCommand):
    """
    The air elemental can unleash a powerful wind slash, cutting through the air with incredible speed and force. The strength of the wind slash is based on the elemental's wisdom and guild level.

    Usage:
        wind slash
    """

    key = "wind slash"
    help_category = "air elemental"
    guild_level = 3
    cost = 3

    def _calculate_damage(self, gale_force, wisdom, guild_level):
        base_value = 3
        gale_force_weight = 5
        wisdom_weight = 0.5
        guild_level_weight = 1

        damage = (
            base_value
            + (gale_force * gale_force_weight)
            + (wisdom * wisdom_weight)
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
        if not caller.cooldowns.ready("wind slash"):
            caller.msg(f"|CNot so fast!")
            return False
        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return
        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.adjust_fp(-self.cost)
        caller.cooldowns.add("wind slash", 4)
        caller.cooldowns.add("global_cooldown", 2)
        skill_rank = caller.db.skills.get("gale force", 1)
        damage = self._calculate_damage(skill_rank, caller.traits.wis.value, glvl)

        target.at_damage(caller, damage, "edged", "wind_slash")


class CmdCycloneArmor(PowerCommand):
    """
    Cyclone armor creates a barrier of swirling winds around the air elemental, providing additional protection against incoming attacks. The shield absorbs a portion of the damage dealt to the elemental, reducing the impact of physical and magical attacks. The strength of the shield is based on the elemental's wisdom and guild level.
    """

    key = "cyclone armor"
    aliases = ["ca"]
    help_category = "air elemental"
    cost = 50
    guild_level = 5

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        if glvl < self.guild_level:
            caller.msg(f"|CYou need to be guild level 5 to use air shield.")
            return
        if caller.db.ep < self.cost:
            caller.msg(f"|rYou need at least {self.cost} energy to use this power.")
            return
        if not caller.db.earth_shield["hits"] > 0:
            caller.cooldowns.add("cyclone_armor", 60)
            caller.cooldowns.add("global_cooldown", 2)
            caller.db.cyclone_armor["hits"] = (
                3
                + caller.db.skills.get("storm resilience", 1)
                + int(caller.traits.con.value / 10)
            )
            caller.adjust_ep(-self.cost)
        self.msg(
            f"|cYou raise your arms and a swirling vortex of wind surrounds you, forming a protective barrier."
        )
        caller.location.msg_contents(
            f"|c$You raise $pron(your) arms and a swirling vortex of wind surrounds $you(), forming a protective barrier.",
            from_obj=caller,
        )


class CmdAerialRestoration(PowerCommand):
    """
    The air elemental can restore their body to restore health,
    at the cost of focus. The amount of health restored is based on
    the elemental's wisdom and guild level.

    Usage:
        aerial restoration
    """

    key = "aerial restoration"
    help_category = "air elemental"
    aliases = ["ar"]
    guild_level = 3

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level

        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return

        if not caller.cooldowns.ready("aerial restoration"):
            caller.msg(f"|CNot so fast!")
            return False
        caller.cooldowns.add("aerial restoration", 4)

        wis = caller.traits.wis.value
        hp = caller.db.hp
        hpmax = caller.db.hpmax
        fp = caller.db.fp

        to_heal = math.floor(10 + glvl * 1.5 + wis / 2)
        to_heal = randint(to_heal / 2, to_heal)
        cost = to_heal * 1.5

        if fp < cost:
            self.msg(f"|rYou can't seem to focus on restoring your form.")
            return

        if hp + to_heal > hpmax:
            caller.db.hp = hpmax
            caller.db.fp -= cost
        else:
            caller.db.hp += max(to_heal, 0)
            caller.db.fp -= cost

        msg = f"|M$Your() form shimmers as it draws in surrounding winds. Gentle breezes swirl around it, mending its ethereal body."
        msg2 = f"|M$Your() form becomes more defined and vibrant, as the healing winds restore its strength and vitality."

        caller.location.msg_contents(msg, from_obj=caller)


class CmdBurnout(PowerCommand):
    """
    This powerful ability allows the air elemental to channel energy from all elemental forces, enhancing their physical abilities and combat prowess. While active, the elemental's attacks become more potent, and their movements more fluid and precise. The elemental's power is greatly increased while burnout is active, but the strain of maintaining this heightened state of power can be overwhelming, and the elemental must be cautious not to overextend themselves.

    Usage:
        burnout
    """

    key = "burnout"
    help_category = "air elemental"
    cost = 10
    guild_level = 10

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


class CmdEnvelop(Command):
    """
    Envelop the corpse of an enemy to restore energy
    """

    key = "envelop"
    aliases = ["en", "ev"]
    help_category = "air elemental"

    def func(self):
        if not self.args:
            caller = self.caller
            if corpse := caller.location.search("corpse-1"):
                ep = caller.db.ep
                epmax = caller.db.epmax
                power = corpse.db.power

                if ep + power > epmax:
                    caller.db.ep = epmax
                else:
                    caller.db.ep += max(power, 0)
                corpse.delete()

                drain_msg = f"|M|M$pron(You) envelop the corpse with swirling currents of air, disintegrating it into a fine mist. As the essence of the remains merges with $pron(you), $pron(your) form shimmers with renewed vitality, $pron(your) presence becoming more ethereal and invigorated."

                caller.location.msg_contents(drain_msg, from_obj=caller)

            else:
                caller.msg("Envelop what?")


class CmdReaction(Command):
    """
    Set the elemental's reaction to a dropping below a certain health threshold.

    Usage:
        reaction <percentage>
    """

    key = "reaction"
    help_category = "water elemental"

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


class CmdPowers(Command):
    """
    List of powers available to the Elemental, their rank, and their cost.

    Usage:
        powers

    """

    key = "powers"
    help_category = "air elemental"

    def func(self):
        caller = self.caller

        table = EvTable(f"|cPower", f"|cRank", f"|cCost", border="table")
        table.add_row(f"|GEnvelop", 1, 0)
        table.add_row(f"|GReaction", 1, 0)
        # table.add_row(f"|GZephyr", , 5)
        table.add_row(f"|GAerial Restoration", 3, 25)
        table.add_row(f"|GWind Slash", 3, 5)
        table.add_row(f"|GCyclone Armor", 5, 50)
        table.add_row(f"|GWhirlwind", 7, 8)
        table.add_row(f"|GBurnout", 10, 10)
        table.add_row(f"|GAir Form", 12, 50)
        table.add_row(f"|GTornado", 15, 10)
        table.add_row(f"|GLightning Strike", 20, 10)
        table.add_row(f"|GStorm Form", 24, 50)

        caller.msg(str(table))


class CmdGTrain(Command):
    """
    Train your guild skills by spending skill experience points. Each rank
    increases your effectiveness in that skill.

    Usage:
        gtrain <skill>

    Example:
        gtrain wind mastery
    """

    key = "gtrain"
    help_category = "air elemental"

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

    wind mastery
    aerial agility
    storm resilience
    gale force
    cyclone armor
    zephyr infusion
    tempest control
    elemental harmony

    Usage:
        ghelp
        ghelp <skill>
    """

    key = "ghelp"
    help_category = "air elemental"

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
        if skill == "wind mastery":
            caller.msg(
                "|cWind Mastery|n\n\n"
                "Increases the elemental's control over wind, enhancing the effectiveness of all wind-based abilities.\n\n"
            )
            return
        if skill == "aerial agility":
            caller.msg(
                "|cAerial Agility|n\n\n"
                "Enhances the elemental's speed and maneuverability, making it more elusive in combat.\n\n"
            )
            return
        if skill == "storm resilience":
            caller.msg(
                "|cStorm Resilience|n\n\n"
                "Improves the elemental's resistance to electrical and wind damage, allowing for greater endurance in battle.\n\n"
            )
            return
        if skill == "gale force":
            caller.msg(
                "|cGale Force|n\n\n"
                "Grants the elemental the ability to channel powerful gusts of wind, improving the impact of its attacks.\n\n"
            )
            return
        if skill == "zephyr infusion":
            caller.msg(
                "|cZephyr Infusion|n\n\n"
                "Infuses the elemental's core with the essence of the wind, enhancing its regenerative abilities.\n\n"
            )
            return
        if skill == "tempest control":
            caller.msg(
                "|cTempest Control|n\n\n"
                "Improves the elemental's ability to manipulate large-scale storms, increasing the effectiveness of area-of-effect attacks.\n\n"
            )
            return
        if skill == "elemental harmony":
            caller.msg(
                "|cElemental Harmony|n\n\n"
                "Enhances the elemental's ability to work in harmony with other elements, boosting the effectiveness of combined elemental attacks.\n\n"
            )
            return
        caller.msg(f"|rNo help found for {skill}.")


class AirElementalCmdSet(CmdSet):
    key = "Air Elemental CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        self.add(CmdEnvelop)
        self.add(CmdAerialRestoration)
        self.add(CmdBurnout)
        self.add(CmdCycloneArmor)
        self.add(CmdWindSlash)
        self.add(CmdStormForm)
        self.add(CmdTornado)
        self.add(CmdWhirlwind)
        self.add(CmdLightningStrike)
        self.add(CmdZephyr)
        self.add(CmdPowers)
        self.add(CmdReaction)
        self.add(CmdGTrain)
        self.add(CmdGhelp)
