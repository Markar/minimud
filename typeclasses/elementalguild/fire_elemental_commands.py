import math
from random import randint
from evennia import CmdSet
from evennia.utils.evtable import EvTable
from commands.command import Command
from typeclasses.elementalguild.constants_and_helpers import SKILLS_COST


class CmdFlameRenewal(Command):
    """
    The fire elemental can rebuild their body to restore health,
    at the cost of focus. The amount of health restored is based on
    the elemental's wisdom and guild level.

    Usage:
        flame renewal
    """

    key = "flame renewal"
    aliases = ["fr"]
    help_category = "fire elemental"
    guild_level = 4

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level

        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return

        if not caller.cooldowns.ready("flame renewal"):
            caller.msg(f"|BNot so fast!")
            return False
        caller.cooldowns.add("flame renewal", 6)

        glvl = caller.db.guild_level
        wis = caller.db.wisdom
        intel = caller.db.intelligence
        hp = caller.db.hp
        hpmax = caller.db.hpmax
        fp = caller.db.fp
        hp_amount = 0

        to_heal = math.floor(10 + glvl + intel / 2 + wis / 2)
        to_heal = randint(int(to_heal / 2), to_heal)
        cost = to_heal * 0.75

        if fp < cost:
            self.msg(f"|rYou can't seem to focus on renewing your form.")
            return

        if hp + to_heal > hpmax:
            hp_amount = hpmax - hp
            caller.db.hp = hpmax
            caller.db.fp -= cost
        else:
            hp_amount = hpmax - hp
            caller.db.hp += max(to_heal, 0)
            caller.db.fp -= cost

        heal_msg = f"|M$pron(Your) wounds start to close as the flames burn away impurities and regenerate $pron(your) form."
        caller.location.msg_contents(heal_msg, from_obj=caller)
        self.msg(f"")
        self.msg(f"You restore {hp_amount or 0} health for {cost or 0} focus")


class CmdAbsorb(Command):
    """
    Absorb the corpse of an enemy to restore energy
    """

    key = "absorb"
    aliases = ["ab"]
    help_category = "fire elemental"

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
                drain_msg = f"|M$pron(You) engulf a fallen corpse in flames, reducing it to ashes. As the body burns, $pron(you) absorb the released energy, $pron(your) flames growing brighter and more intense, restoring $pron(your) vitality and power."
                caller.location.msg_contents(drain_msg, from_obj=caller)
            else:
                caller.msg("Absorb what?")


class CmdReaction(Command):
    """
    Set the elemental's reaction to dropping below a certain health threshold.

    Usage:
        reaction <percentage>
    """

    key = "reaction"
    help_category = "fire elemental"

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
        gtrain flame mastery
    """

    key = "gtrain"
    help_category = "fire elemental"

    def func(self):
        caller = self.caller
        skill = self.args.strip().lower()
        list = [
            "flame mastery",
            "inferno resilience",
            "blazing speed",
            "pyroclastic surge",
            "molten armor",
            "ember infusion",
            "firestorm control",
            "elemental synergy",
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
    Display the help file for the fire elemental guild.

    Usage:
        ghelp
    """

    key = "ghelp"
    help_category = "fire elemental"

    def func(self):
        caller = self.caller
        skill = self.args.strip().lower()
        if skill == "":
            caller.msg(
                "|cFire Elemental Guild|n\n\n"
                "The Fire Elemental Guild is a group of beings that have learned to harness the power of fire to enhance their physical abilities and combat prowess.\n\n"
                "Usage:\n"
                "    ghelp <skill>\n"
            )
            return
        if skill == "flame mastery":
            caller.msg(
                "|cFlame Mastery|n\n\n"
                "Enhances the elemental's control over fire, increasing the damage dealt by fire-based attacks.\n\n"
                "Usage:\n"
                "    flame mastery\n"
                "    fm\n"
            )
            return
        if skill == "inferno resilience":
            caller.msg(
                "|cInferno Resilience|n\n\n"
                "Increases the elemental's resistance to fire-based attacks.\n\n"
                "Usage:\n"
                "    inferno resilience\n"
                "    ir\n"
            )
            return
        if skill == "blazing speed":
            caller.msg(
                "|cBlazing Speed|n\n\n"
                "Enhances the elemental's speed, allowing for faster movement and attacks.\n\n"
                "Usage:\n"
                "    blazing speed\n"
                "    bs\n"
            )
            return
        if skill == "pyroclastic surge":
            caller.msg(
                "|cPyroclastic Surge|n\n\n"
                "Increases the elemental's energy regeneration rate.\n\n"
                "Usage:\n"
                "    pyroclastic surge\n"
                "    ps\n"
            )
            return
        if skill == "molten armor":
            caller.msg(
                "|cMolten Armor|n\n\n"
                "Increases the elemental's physical defense, reducing the damage taken from physical attacks.\n\n"
                "Usage:\n"
                "    molten armor\n"
                "    ma\n"
            )
            return
        if skill == "ember infusion":
            caller.msg(
                "|cEmber Infusion|n\n\n"
                "Enhances the elemental's passive regeneration.\n\n"
                "Usage:\n"
                "    ember infusion\n"
                "    ei\n"
            )
            return
        if skill == "firestorm control":
            caller.msg(
                "|cFirestorm Control|n\n\n"
                "Allows the elemental to control firestorms, dealing damage to all enemies in the area.\n\n"
                "Usage:\n"
                "    firestorm control\n"
                "    fc\n"
            )
            return
        if skill == "elemental synergy":
            caller.msg(
                "|cElemental Synergy|n\n\n"
                "Increases the elemental's overall power, enhancing the effects of other skills.\n\n"
                "Usage:\n"
                "    elemental synergy\n"
                "    es\n"
            )
            return


class CmdPowers(Command):
    """
    List of powers available to the Elemental, their rank, and their cost.

    Usage:
        powers

    """

    key = "powers"
    help_category = "fire elemental"

    def func(self):
        caller = self.caller

        table = EvTable(f"|cPower", f"|cRank", f"|cCost", border="table")
        table.add_row(f"|GAbsorb", 1, 0)
        table.add_row(f"|GReaction", 1, 0)
        table.add_row(f"|GFlame Renewal", 3, 25)

        caller.msg(str(table))


class FireElementalCmdSet(CmdSet):
    key = "Fire Elemental CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        self.add(CmdAbsorb)
        self.add(CmdFlameRenewal)
        self.add(CmdReaction)
        self.add(CmdPowers)
        self.add(CmdGhelp)
        self.add(CmdGTrain)
