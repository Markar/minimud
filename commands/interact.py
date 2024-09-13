from .command import Command
from evennia import CmdSet
from evennia.commands.default.general import CmdGet
from evennia.utils import make_iter


class CmdGather(Command):
    """
    Gather resources from the node in this location.
    """

    key = "gather"
    aliases = ("collect", "harvest")
    help_category = "here"

    def func(self):
        if not self.obj:
            return

        try:
            self.obj.at_gather(self.caller)
        except AttributeError:
            self.msg("You cannot gather anything from that.")


class GatherCmdSet(CmdSet):
    key = "Gather CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()
        # add the cmd
        self.add(CmdGather)


class CmdEat(Command):
    """
    Eat something edible

    Usage:
        eat <obj>

    Example:
        eat apple
    """

    key = "eat"
    aliases = ("drink", "consume")

    def func(self):
        obj = self.caller.search(self.args.strip(), stacked=1)
        if not obj:
            return
        # stacked sometimes returns a list, so make sure it is one for consistent handling
        obj = make_iter(obj)[0]

        if not obj.tags.has("edible"):
            self.msg("You cannot eat that.")
            return

        energy = obj.attributes.get("energy", 0)
        self.caller.db.ep += energy
        self.caller.at_emote(
            f"$conj({self.cmdstring}) the {{target}}.", mapping={"target": obj}
        )
        obj.delete()


class CmdGetAll(CmdGet):
    """
    Get an object from the room or from another object.

    Usage:
        get <obj> or get all

    Example:
        get apple, get all
    """

    key = "get"
    aliases = "grab, ga"
    help_category = "general"

    def func(self):
        arg = self.args.strip().lower()
        if arg == "all":
            for obj in self.caller.location.contents_get(content_type="object"):
                if not obj.access(self.caller, "get"):
                    if obj.db.get_err_msg:
                        self.msg(obj.db.get_err_msg)
                        continue
                    else:
                        self.msg("You can't get that.")
                        continue
                else:
                    self.caller.msg(f"Getting {obj}")
                    obj.move_to(self.caller, quiet=True)
            return
        else:
            super().func()


class InteractCmdSet(CmdSet):
    key = "Interact CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()
        self.add(CmdEat)
        self.add(CmdGetAll)
