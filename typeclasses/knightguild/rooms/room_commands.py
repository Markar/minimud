from evennia import CmdSet
from evennia.utils.evtable import EvTable
from commands.command import Command
from typeclasses.knightguild.knight_commands import KnightCmdSet
from evennia import TICKER_HANDLER as tickerhandler


class CmdJoinKnights(Command):
    """
    Join the Knights Guild
    """

    key = "join knights"

    def func(self):
        caller = self.caller
        if caller.db.guild == "adventurer":
            caller.msg(
                f"|gWith a flourish and a bow, you pledge your allegiance to the Knights Guild!|n"
            )
            caller.swap_typeclass(
                "typeclasses.knights.Knight",
                clean_attributes=False,
                no_default=True,
                clean_cmdsets=False,
            )
            creator_id = caller.db.creator_id
            self.caller.locks.add(
                f"call:false(); control:perm(Developer); delete:id({creator_id}) or perm(Admin);drop:holds(); edit:pid({creator_id}) or perm(Admin); examine:perm(Builder); get:false(); puppet:id(4270) or pid({creator_id}) or perm(Developer) or pperm(Developer); teleport:perm(Admin); teleport_here:perm(Admin); tell:perm(Admin); view:all()"
            )
            caller.cmdset.add(KnightCmdSet, persistent=True)
        else:
            caller.msg(f"|rYou are already in a guild")


# region Leave Cybercorps
class CmdLeaveKnights(Command):
    """
    Leave the Knights guild
    """

    key = "leave knights"

    def strip(self):
        caller = self.caller
        caller.cmdset.delete(KnightCmdSet)
        caller.cmdset.delete(PaladinCmdSet)
        caller.cmdset.delete(ShadowKnightCmdSet)
        del caller.db.skills
        del caller.db.guild_level

        return

    def func(self):
        caller = self.caller
        if caller.db.guild == "knight":
            caller.swap_typeclass("typeclasses.characters.PlayerCharacter")
            self.strip()
            caller.msg(
                f"|rWith a heavy heart, you renounce your vows and leave the Knights Guild."
            )
        else:
            caller.msg(f"|rYou are not a knight.")


class KnightsRoomCmdSet(CmdSet):
    key = "Knights CmdSet"
    priority = 1

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        self.add(CmdJoinKnights)
        self.add(CmdLeaveKnights)


from typeclasses.knightguild.paladin_commands import PaladinCmdSet


class CmdJoinPaladins(Command):
    """
    Become a Paladin
    """

    key = "join paladins"

    def func(self):
        caller = self.caller
        if caller.db.guild == "knight" and caller.db.subguild == None:
            caller.msg(
                f"|gWith a flourish and a bow, you pledge your allegiance to the Mithaniel Marr!|n"
            )
            caller.cmdset.add(PaladinCmdSet, persistent=True)
            caller.db.subguild = "paladin"
        else:
            caller.msg(f"|rYou can't do that.")


class PaladinRoomCmdSet(CmdSet):
    key = "Paladin CmdSet"
    priority = 1

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        self.add(CmdJoinPaladins)


from typeclasses.knightguild.shadow_knight_commands import ShadowKnightCmdSet


class CmdJoinShadowKnights(Command):
    """
    Become a Shadow Knight
    """

    key = "join shadow knights"

    def func(self):
        caller = self.caller
        if caller.db.guild == "knight" and caller.db.subguild == None:
            caller.msg(
                f"|gWith a flourish and a bow, you pledge your allegiance to Innoruuk!|n"
            )
            caller.cmdset.add(ShadowKnightCmdSet, persistent=True)
            caller.db.subguild = "shadow knight"
        else:
            caller.msg(f"|rYou can't do that.")


class ShadowKnightRoomCmdSet(CmdSet):
    key = "Shadow Knight CmdSet"
    priority = 1

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        self.add(CmdJoinShadowKnights)
