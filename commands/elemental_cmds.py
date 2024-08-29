from random import choice
from evennia import CmdSet, search_tag
from evennia.utils import iter_to_str
from evennia.utils.evtable import EvTable
from evennia import TICKER_HANDLER as tickerhandler
from evennia import logger

from .command import Command
from typeclasses.elementalguild.earth_elemental_commands import EarthElementalCmdSet
from typeclasses.elementalguild.air_elemental_commands import AirElementalCmdSet
from typeclasses.elementalguild.fire_elemental_commands import FireElementalCmdSet
from typeclasses.elementalguild.water_elemental_commands import WaterElementalCmdSet
from typeclasses.elementalguild.constants_and_helpers import (
    SKILLS_COST,
    SKILL_RANKS,
    GUILD_LEVEL_COST_DICT,
)


class CmdGAdvance(Command):
    """
    Advance a level or attribute by spending experience points.

    Enter "advance" to see what you can learn.

    Usage:
        gadvance

    Example:
        gadvance
    """

    key = "gadvance"
    aliases = "gadv"
    help_category = "elemental"

    def _adv_level(self):
        caller = self.caller
        cost = GUILD_LEVEL_COST_DICT[caller.db.guild_level + 1]
        if caller.db.gxp < cost:
            self.msg(f"|wYou need {cost - caller.db.gxp} more experience to advance.")
            return
        else:
            caller.db.gxp -= cost
            caller.db.guild_level += 1
            caller.db.epmax += 10
            self.msg(f"|rYou grow more powerful.")

        if caller.db.guild_level >= 30:
            caller.db.burnout["max"] = 4
        elif caller.db.guild_level >= 21:
            caller.db.burnout["max"] = 3
        elif caller.db.guild_level >= 14:
            caller.db.burnout["max"] = 2
        elif caller.db.guild_level >= 7:
            caller.db.burnout["max"] = 1

    def func(self):
        caller = self.caller
        caller.msg(f"|G{caller}")
        print(f"in advance function")

        self._adv_level()
        print(f"after _adv_level {caller.db.gxp}")


class CmdGuildStatSheet(Command):
    """
    Display your guild stats
    """

    key = "gscore"
    aliases = "gs"
    help_category = "elemental"

    def func(self):
        caller = self.caller
        title = caller.db.title or "the novice"
        alignment = caller.db.alignment or "neutral"
        my_glvl = caller.db.guild_level or 1
        gxp = caller.db.gxp or 0
        skill_gxp = caller.db.skill_gxp or 0
        form = caller.db.subguild or "adventurer"
        gxp_needed = GUILD_LEVEL_COST_DICT[my_glvl + 1]
        reaction = caller.db.reaction_percentage or 50
        burnout_count = caller.db.burnout["count"]
        burnout_max = caller.db.burnout["max"]

        table = EvTable(f"|c{caller}", f"|c{title}", border="table")
        table.add_row(f"|GGuild Level", my_glvl)
        table.add_row(f"|GGXP", f"{gxp} / {gxp_needed}")
        table.add_row(f"|GSkill GXP", skill_gxp)
        table.add_row(f"|GForm", form.title())
        table.add_row(f"|GReaction", f"{reaction}%")
        table.add_row(f"|GBurnouts", f"{burnout_count} / {burnout_max}")

        caller.msg(str(table))

        skill_table = EvTable(f"|cSkills", f"|cCost", f"|cRank", border="table")
        skills = (
            caller.db.skills.items()
        )  # Get the items (key-value pairs) of the skills dictionary

        # Assuming SKILLS_COST is a dictionary that maps ranks to costs
        for skill, rank in skills:
            skill_table.add_row(
                f"|G{skill.title()}", f"{SKILLS_COST[rank]}", f"{SKILL_RANKS[rank]}"
            )

        caller.msg(str(skill_table))


class CmdSkills(Command):
    """
    List of skills available to the Elemental, their rank, and their cost.

    Usage:
        skills

    """

    key = "skills"
    help_category = "elemental"

    def func(self):
        caller = self.caller

        table = EvTable(f"|cSkill", f"|cRank", f"|cCost", border="table")
        for skill, rank in caller.db.skills.items():
            table.add_row(f"|G{skill.title()}", f"{rank}", f"{SKILLS_COST[rank]}")

        caller.msg(str(table))


class CmdJoinElementals(Command):
    """
    Join the Elementals guild
    """

    key = "join elementals"

    def func(self):
        caller = self.caller
        if caller.db.guild == "adventurer":
            caller.msg(f"|rYou join the Elementals guild")
            # caller.swap_typeclass("typeclasses.elementals.Elemental")
            caller.swap_typeclass(
                "typeclasses.elementalguild.earth_elemental.EarthElemental",
                clean_attributes=False,
            )
        else:
            caller.msg(f"|rYou are already in a guild")


class CmdLeaveElementals(Command):
    """
    Leave the Elementals guild
    """

    key = "leave elementals"

    def func(self):
        caller = self.caller
        if caller.db.guild == "elemental":
            caller.swap_typeclass("typeclasses.characters.PlayerCharacter")
            caller.cmdset.delete(ElementalCmdSet)
            caller.msg(f"|rYou leave the Elementals guild")
        else:
            caller.msg(f"|rYou are already an adventurer")


class CmdChooseForm(Command):
    """
    You can choose from earth, fire, water, or air. Earth is more defensive,
    fire is more offensive, water is more balanced, and air is more
    evasive. Once you choose a form, you cannot change it.
    """

    key = "chooseform"
    help_category = "elemental"

    def _remove_cmdsets(self):
        caller = self.caller
        if caller.db.subguild == "earth":
            caller.cmdset.delete(FireElementalCmdSet)
            caller.cmdset.delete(WaterElementalCmdSet)
            caller.cmdset.delete(AirElementalCmdSet)
        if caller.db.subguild == "fire":
            caller.cmdset.delete(EarthElementalCmdSet)
            caller.cmdset.delete(WaterElementalCmdSet)
            caller.cmdset.delete(AirElementalCmdSet)
        if caller.db.subguild == "water":
            caller.cmdset.delete(EarthElementalCmdSet)
            caller.cmdset.delete(FireElementalCmdSet)
            caller.cmdset.delete(AirElementalCmdSet)
        if caller.db.subguild == "air":
            caller.cmdset.delete(EarthElementalCmdSet)
            caller.cmdset.delete(FireElementalCmdSet)
            caller.cmdset.delete(WaterElementalCmdSet)

    def func(self):
        target = self.args.strip()
        caller = self.caller
        if caller.db.guild_level > 5:
            caller.msg(
                f"|rYou have already chosen {caller.db.subguild} as your permanent form."
            )
            return
        if not target:
            self.msg(f"|rYou can choose earth, fire, water, or air.")
            return

        if target == "earth":
            caller.db.subguild = "earth"
            caller.msg(f"|yYou choose {caller.db.subguild} as your permanent form.")
            caller.swap_typeclass(
                "typeclasses.elementalguild.earth_elemental.EarthElemental",
                clean_attributes=False,
                clean_cmdsets=True,
            )
            caller.cmdset.add(EarthElementalCmdSet, persistent=True)
            self._remove_cmdsets()
        if target == "fire":
            caller.db.subguild = "fire"
            caller.msg(f"|rYou choose {caller.db.subguild} as your permanent form.")
            caller.swap_typeclass(
                "typeclasses.elementalguild.fire_elemental.FireElemental",
                clean_attributes=False,
                clean_cmdsets=True,
            )
            caller.cmdset.add(FireElementalCmdSet, persistent=True)
            self._remove_cmdsets()
        if target == "water":
            caller.db.subguild = "water"
            caller.msg(f"|bYou choose {caller.db.subguild} as your permanent form.")
            caller.swap_typeclass(
                "typeclasses.elementalguild.water_elemental.WaterElemental",
                clean_attributes=False,
                clean_cmdsets=True,
            )
            caller.cmdset.add(WaterElementalCmdSet, persistent=True)
            self._remove_cmdsets()
        if target == "air":
            caller.db.subguild = "air"
            caller.msg(f"|wYou choose {caller.db.subguild} as your permanent form.")
            caller.swap_typeclass(
                "typeclasses.elementalguild.air_elemental.AirElemental",
                clean_attributes=False,
                clean_cmdsets=True,
            )
            caller.cmdset.add(AirElementalCmdSet, persistent=True)
            self._remove_cmdsets()


class CmdGHelp(Command):
    """
    Search for guild topics to learn more about the elementals.
    """

    key = "ghelp"
    help_category = "elemental"


class CmdKickstart(Command):
    key = "kickstart"

    def func(self):
        caller = self.caller
        caller.kickstart()


class CmdBurnout(Command):
    """
    Burnout is a powerful ability granted to members of the Elemental Guild. When activated, this superpower channels the raw essence of the elements, significantly amplifying the user's offensive and defensive capabilities. The elemental energies surge through the user's body, enhancing their attacks and fortifying their defenses. However, this immense power comes at a cost, as it rapidly depletes the user's energy reserves, requiring careful management to avoid exhaustion.

    Usage:
        burnout

    """

    key = "burnout"
    help_category = "elemental"

    def func(self):
        caller = self.caller
        caller.use_burnout()


class CmdTest(Command):
    key = "test"

    def func(self):
        caller = self.caller
        caller.msg("test")
        # caller.cmdset.delete(ElementalCmdSet)
        # caller.cmdset.delete(ElementalCmdSet)
        # caller.cmdset.delete(ElementalCmdSet)
        # caller.cmdset.delete(ElementalCmdSet)
        # caller.cmdset.delete(ElementalCmdSet)

        caller.msg("done")


class ElementalCmdSet(CmdSet):
    key = "Elemental CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        # self.add(CmdDrain)
        self.add(CmdGAdvance)
        self.add(CmdGuildStatSheet)
        self.add(CmdChooseForm)
        self.add(CmdSkills)
        self.add(CmdTest)
        self.add(CmdKickstart)
        self.add(CmdBurnout)
