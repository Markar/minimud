import math
from random import randint
from evennia import CmdSet
from evennia.utils.evtable import EvTable
from commands.command import Command
from typeclasses.elementalguild.constants_and_helpers import SKILLS_COST


class CmdAerialRestoration(Command):
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
    guild_level = 4

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level

        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return

        if not caller.cooldowns.ready("aerial restoration"):
            caller.msg(f"|BNot so fast!")
            return False
        caller.cooldowns.add("aerial restoration", 4)

        wis = caller.db.wisdom
        hp = caller.db.hp
        hpmax = caller.db.hpmax
        fp = caller.db.fp

        to_heal = math.floor(10 + glvl * 1.5 + wis / 2)
        to_heal = randint(to_heal / 2, to_heal)
        cost = to_heal * 0.5

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

                drain_msg = f"|M|M$pron(You) envelop the corpse with tendrils of water, dissolving it into liquid. As the remains merge with $pron(you), $pron(your) body glows with renewed energy, $pron(your) form becoming more vibrant and fluid."
                caller.location.msg_contents(drain_msg, from_obj=caller)

            else:
                caller.msg("Drain what?")


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
        table.add_row(f"|GAerial Restoration", 3, 25)

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
        list = [
            "wind mastery",
            "aerial agility",
            "storm resilience",
            "gale force",
            "cyclone armor",
            "zephyr infusion",
            "tempest control",
            "elemental harmony",
        ]

        if skill == "":
            self.msg(f"|gWhat would you like to raise?")
            return

        if skill not in list:
            caller.msg(f"|gYou can't raise that.")
            return

        skill_gxp = getattr(caller.db, "skill_gxp", 0)
        cost = caller.db.skills[f"{skill}"] + 1
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
        if skill == "cyclone armor":
            caller.msg(
                "|cCyclone Armor|n\n\n"
                "Surrounds the elemental with a protective vortex of wind, providing additional defense and offensive capabilities.\n\n"
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
        self.add(CmdPowers)
        self.add(CmdReaction)
        self.add(CmdGTrain)
        self.add(CmdGhelp)
