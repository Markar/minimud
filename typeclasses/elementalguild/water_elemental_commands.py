import math
from random import uniform, randint
from evennia import CmdSet
from evennia.utils.evtable import EvTable
from commands.command import Command
from typeclasses.elementalguild.constants_and_helpers import SKILLS_COST


class CmdRejuvenate(Command):
    """
    Water droplets coalesce from the surrounding moisture, swirling around the elemental in a graceful dance. The droplets merge into streams, flowing over the elemental's body, mending cracks and filling gaps with a soothing, liquid touch. The elemental's form becomes more defined and robust, the water infusing it with renewed strength and vitality. As the healing process completes, the elemental stands rejuvenated, its surface glistening with a fresh, revitalized sheen.

     Usage:
         rejuvenate
    """

    key = "rejuvenate"
    aliases = ["rejuv", "rej"]
    help_category = "water elemental"
    guild_level = 4

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level

        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return

        if not caller.cooldowns.ready("rejuvenate"):
            caller.msg(f"|BNot so fast!")
            return False
        caller.cooldowns.add("rejuvenate", 4)

        wis = caller.db.wisdom
        strength = caller.db.strength
        hp = caller.db.hp
        hpmax = caller.db.hpmax
        fp = caller.db.fp
        hp_amount = 0

        to_heal = math.floor(10 + glvl + strength / 2 + wis / 2)
        to_heal = randint(int(to_heal / 2), to_heal)
        to_heal = max(to_heal, 0)
        cost = to_heal * 0.5

        if caller.db.fp < cost:
            self.msg(f"|rYou can't seem to focus on restoring your form.")
            return

        if hp + to_heal > hpmax:
            hp_amount = hpmax - hp
            caller.adjust_hp(hpmax)
            caller.adjust_fp(-cost)
            # caller.db.hp = hpmax
            # caller.db.fp -= cost
        else:
            hp_amount = hpmax - hp
            caller.adjust_hp(to_heal)
            caller.adjust_fp(-cost)
            # caller.db.hp += to_heal
            # adjust_hp(caller, hpmax)
            # caller.db.fp -= cost

        msg = f"|MAs $pron(you) concentrate, $pron(your) body glows with a soft, blue light, and water swirls around you, knitting wounds and restoring vitality. {hp_amount or 0} health restored for {cost or 0} focus."

        caller.location.msg_contents(msg, from_obj=caller)


class CmdEnvelop(Command):
    """
    Drain the corpse of an enemy to restore energy
    """

    key = "envelop"
    aliases = ["en", "env"]
    help_category = "water elemental"

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
                caller.msg("Envelop what?")


class CmdPowers(Command):
    """
    List of powers available to the Elemental, their rank, and their cost.

    Usage:
        powers

    """

    key = "powers"
    help_category = "elemental"

    def func(self):
        caller = self.caller

        table = EvTable(f"|cPower", f"|cRank", f"|cCost", border="table")
        table.add_row(f"|GEnvelop", 1, 0)
        table.add_row(f"|GReaction", 1, 0)
        table.add_row(f"|GRejuvenate", 3, 25)

        caller.msg(str(table))


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


class CmdGTrain(Command):
    """
    Train your guild skills by spending skill experience points. Each rank
    increases your effectiveness in that skill.

    Usage:
        gtrain <skill>

    Example:
        gtrain water mastery
    """

    key = "gtrain"
    help_category = "Water Elemental"

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
    Display the help file for the fire elemental guild.

    Usage:
        ghelp
    """

    key = "ghelp"
    help_category = "water elemental"

    def func(self):
        caller = self.caller
        skill = self.args.strip().lower()
        if skill == "":
            caller.msg(
                "|Water Elemental Guild|n\n\n"
                "The Water Elemental Guild is a group of beings that have learned to harness the power of water to enhance their physical abilities and combat prowess.\n\n"
                "Usage:\n"
                "    ghelp <skill>\n"
            )
            return
        if skill == "water mastery":
            caller.msg(
                "|Water Mastery|n\n\n"
                "Water Mastery is the foundation of the Water Elemental's power. It allows the elemental to manipulate water in a variety of ways, from creating weapons to healing wounds.\n\n"
                "Usage:\n"
                "    gtrain water mastery\n"
            )
            return
        if skill == "fluid agility":
            caller.msg(
                "|Fluid Agility|n\n\n"
                "Fluid Agility allows the Water Elemental to move with grace and speed, dodging attacks and striking with precision.\n\n"
                "Usage:\n"
                "    gtrain fluid agility\n"
            )
            return
        if skill == "aqua resilience":
            caller.msg(
                "|Aqua Resilience|n\n\n"
                "Aqua Resilience enhances the Water Elemental's ability to absorb damage, reducing the impact of physical attacks.\n\n"
                "Usage:\n"
                "    gtrain aqua resilience\n"
            )
            return
        if skill == "tidal force":
            caller.msg(
                "|Tidal Force|n\n\n"
                "Tidal Force increases the Water Elemental's strength, allowing it to deal more damage with its attacks.\n\n"
                "Usage:\n"
                "    gtrain tidal force\n"
            )
            return
        if skill == "hydro armor":
            caller.msg(
                "|Hydro Armor|n\n\n"
                "Hydro Armor surrounds the Water Elemental with a protective layer of water, reducing the impact of physical attacks.\n\n"
                "Usage:\n"
                "    gtrain hydro armor\n"
            )
            return
        if skill == "aqua infusion":
            caller.msg(
                "|Aqua Infusion|n\n\n"
                "Aqua Infusion enhances the Water Elemental's ability to heal itself, restoring health and energy more quickly.\n\n"
                "Usage:\n"
                "    gtrain aqua infusion\n"
            )
            return
        if skill == "wave control":
            caller.msg(
                "|Wave Control|n\n\n"
                "Wave Control allows the Water Elemental to manipulate water in large quantities, creating powerful area-of-effect attacks.\n\n"
                "Usage:\n"
                "    gtrain wave control\n"
            )
            return
        if skill == "elemental synergy":
            caller.msg(
                "|Elemental Synergy|n\n\n"
                "Elemental Synergy enhances the Water Elemental's ability to work in harmony with other elements, increasing the effectiveness of combined elemental attacks.\n\n"
                "Usage:\n"
                "    gtrain elemental synergy\n"
            )
            return


class WaterElementalCmdSet(CmdSet):
    key = "Water Elemental CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        self.add(CmdEnvelop)
        self.add(CmdRejuvenate)
        self.add(CmdPowers)
        self.add(CmdReaction)
        self.add(CmdGTrain)
        self.add(CmdGhelp)
