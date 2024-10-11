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


class CmdAdvFireSkills(Command):
    """
    adv fire elemental skills
    """

    key = "advfireskills"

    def func(self):
        self.db.skills = {
            "flame mastery": 10,
            "inferno resilience": 10,
            "blazing speed": 10,
            "pyroclastic surge": 10,
            "molten armor": 10,
            "ember infusion": 10,
            "firestorm control": 10,
            "elemental synergy": 10,
        }
        self.caller.msg("Fire skills set to 50.")


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


# from typeclasses.utils import SpawnMob2


# class TestSpawn(Command):
#     """
#     Display the available guilds
#     """

#     key = "ts"
#     help_category = "General"

#     def func(self):
#         caller = self.caller
#         SpawnMob2(caller, "BLARGE_RAT")
#         caller.msg(f"|gSpawned a rat.")


from typeclasses.rooms import MobRoom
from typeclasses.rooms import SpecialMobRoom


class RegenerateMobs(Command):
    """
    Regenerate all mobs in the room
    """

    key = "regenmobs"

    def func(self):
        caller = self.caller
        if caller.key.lower() != "markar":
            caller.msg(f"|rYou cannot regenerate specials, {caller.key.lower()}.")
            return

        for room in MobRoom.objects.all_family():
            room.regenerate_mobs()

        caller.msg(f"|gRegenerated mobs.")


class RespawnMobs(Command):
    """
    Respawn all mobs in the room
    """

    key = "respawnmobs"

    def func(self):
        caller = self.caller
        if caller.key.lower() != "markar":
            caller.msg(f"|rYou cannot respawn specials, {caller.key.lower()}.")
            return

        for room in MobRoom.objects.all_family():
            room.respawn_mobs()

        caller.msg(f"|gRespawned mobs.")


class RespawnSpecials(Command):
    """
    Respawn all mobs in the room
    """

    key = "respawnspecials"

    def func(self):
        caller = self.caller
        if caller.key.lower() != "markar":
            caller.msg(f"|rYou cannot respawn specials, {caller.key.lower()}.")
            return

        for room in SpecialMobRoom.objects.all_family():
            room.respawn_mobs()

        caller.msg(f"|gRespawned specials.")


class RegenerateSpecials(Command):
    """
    Regenerate all special mobs in the room
    """

    key = "regenspecials"

    def func(self):
        caller = self.caller
        if caller.key.lower() != "markar":
            caller.msg(f"|rYou cannot regenerate specials, {caller.key.lower()}.")
            return

        for room in SpecialMobRoom.objects.all_family():
            room.regenerate_mobs()

        caller.msg(f"|gRegenerated specials.")


class StartSpecialMobTicker(Command):
    """
    Start the ticker for special mobs
    """

    key = "startspecialmobticker"

    def func(self):
        caller = self.caller
        if caller.key.lower() != "markar":
            caller.msg(f"|rYou cannot start the ticker, {caller.key.lower()}.")
            return

        tickerhandler.add(
            interval=60 * 10,
            callback=SpecialMobRoom.respawn_mobs,
            idstring=f"{self}",
            persistent=True,
        )

        caller.msg(f"|gStarted special mob ticker.")


class StopSpecialMobTicker(Command):
    """
    Stop the ticker for special mobs
    """

    key = "stopspecialmobticker"

    def func(self):
        caller = self.caller
        if caller.key.lower() != "markar":
            caller.msg(f"|rYou cannot stop the ticker, {caller.key.lower()}.")
            return

        tickerhandler.remove(
            interval=300,
            callback=SpecialMobRoom.respawn_mobs,
            idstring=f"startspecialmobticker-superpower",
            persistent=True,
        )
        caller.msg(f"|gStopped special mob ticker.")


class JoinCharacter(Command):
    key = "joinadv"

    def func(self):

        self.caller.swap_typeclass(
            "typeclasses.characters.Character",
            # clean_attributes=False,
            run_start_hooks=None,
            # no_default=True,
            # clean_cmdsets=False,
        )

        # caller = self.caller
        # creator_id = caller.db.creator_id
        # self.caller.locks.add(
        #     f"call:false(); control:perm(Developer); delete:id({creator_id}) or perm(Admin);drop:holds(); edit:pid({creator_id}) or perm(Admin); examine:perm(Builder); get:false(); puppet:id(4270) or pid({creator_id}) or perm(Developer) or pperm(Developer); teleport:perm(Admin); teleport_here:perm(Admin); tell:perm(Admin); view:all()"
        # )


class JoinPlayer(Command):
    key = "joinplayer"

    def func(self):
        self.caller.swap_typeclass(
            "typeclasses.players.Player",
            clean_attributes=False,
            run_start_hooks="all",
            no_default=True,
            clean_cmdsets=False,
        )


class GeneralCmdSet(CmdSet):
    key = "General"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()
        self.add(CmdHelpGuilds)
        self.add(CmdAdv50)
        self.add(CmdAdvGuild)
        self.add(CmdAdvCyberSkills)
        # self.add(TestSpawn)
        self.add(RespawnMobs)
        self.add(RespawnSpecials)
        self.add(RegenerateSpecials)
        self.add(RegenerateMobs)
        self.add(StartSpecialMobTicker)
        self.add(StopSpecialMobTicker)
        self.add(JoinCharacter)
        self.add(JoinPlayer)
