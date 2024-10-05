from random import randint
from evennia import CmdSet, search_tag
from evennia.utils import iter_to_str
from evennia.utils.evtable import EvTable
from evennia import TICKER_HANDLER as tickerhandler
from typeclasses.utils import get_article

import math
from .command import Command


class CmdHelpGuilds(Command):
    """
    Display the available guilds
    """

    key = "guilds"
    help_category = "General"

    def func(self):
        args = self.args.strip().lower()
        if args == "cybercorps":
            self.caller.msg(
                f"|114 The Cybercorps Mega Corporation is the ruling entity in the technological world. Members of the Cybercorps have access to advanced technology and cybernetic enhancements."
            )
            return
        if args == "elementals":
            self.caller.msg(
                f"|114 The Elementals are the masters of the elements; fire, air, earth, and water. Members of the Elementals can manipulate the elements to their will."
            )
            return
        if args == "changelings":
            self.caller.msg(
                f"|114 The Changelings are shapeshifting beings that can take on any form. Members of the Changelings can change their appearance and abilities at will."
            )
            return
        if args == "adventurer":
            self.caller.msg(
                f"|114 The Adventurer is the default guild for all players. Members of the Adventurer guild have no special abilities or restrictions.|/|/To join a guild, go to the guild entrance and use the command |wjoin <guild>|/|/From Millennium Square:|/The elementals guild is s, w, 2s, w from |/The cybercorps guild is s, 2e, n, 2e, 2s|/The changeling guild is n, w, 2n, e, n, w"
            )
            return

        table = EvTable(border="header")
        table.add_row(
            f"|wThe Adventurer is the default guild for all players. Members of the Adventurer guild have no special abilities or restrictions.|/|/To join a guild, go to the guild entrance and use the command |wjoin <guild>|/|/|wFrom Millennium Square:|/|014The elementals guild is s, w, 2s, w from |/The cybercorps guild is s, 2e, n, 2e, 2s|/The changeling guild is n, w, 2n, e, n, w|/|/"
        )
        table.add_row(f"|014Adventurer", "|114 The default guild for all players.")
        table.add_row(
            f"|014Cybercorps", "|114 The Mega Corporation that rules the world."
        )
        table.add_row(
            f"|014Elementals",
            "|114 Masters of the elements; fire, air, earth, and water.",
        )
        table.add_row(
            f"|014Changelings",
            "|114 Shapeshifting beings that can take on any form.|/|/",
        )
        self.caller.msg(table)


class CmdAdv50(Command):
    """
    Display the available guilds
    """

    key = "adv50"
    help_category = "General"

    def func(self):
        self.caller.db.exp = 500000000000000
        self.caller.db.gxp = 500000000000000
        self.caller.db.skill_gxp = 500000000000000
        self.caller.level = 50
        self.caller.traits.con.base = 50
        self.caller.traits.int.base = 50
        self.caller.traits.str.base = 50
        self.caller.traits.dex.base = 50
        self.caller.traits.wis.base = 50
        self.caller.traits.cha.base = 50
        self.caller.db.coins = 500000000000000
        self.caller.db.hp = 1000
        self.caller.db.fp = 1000
        self.caller.db.ep = 1000
        self.caller.db.hpmax = 1000
        self.caller.db.fpmax = 1000
        self.caller.db.epmax = 1000
        self.caller.msg("Level set to 50.")


class CmdAdvCyberSkills(Command):
    """
    Display the available guilds
    """

    key = "advcyberskills"
    help_category = "General"

    def func(self):
        self.caller.db.skills = {
            "standard weapons": 10,
            "energy weapons": 10,
            "heavy weapons": 10,
            "cybernetic enhancements": 10,
            "security services": 10,
            "biotech research": 10,
            "energy solutions": 10,
        }
        self.caller.msg("Cyber skills set to 50.")


class CmdAdvGuild(Command):
    """
    Display the available guilds
    """

    key = "advguild"
    help_category = "General"

    def func(self):
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")

        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")

        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")

        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")
        self.execute_cmd("gadvance")

        self.caller.msg("Guild level set to 50.")


class GeneralCmdSet(CmdSet):
    key = "General"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()
        self.add(CmdHelpGuilds)
        self.add(CmdAdv50)
        self.add(CmdAdvGuild)
        self.add(CmdAdvCyberSkills)
