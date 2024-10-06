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
        hp = obj.attributes.get("hp", 0)
        self.caller.db.ep += energy
        self.caller.db.hp += hp

        power = obj.attributes.get("power", 0)
        if power > 0:
            self.caller.adjust_hp(power)
            self.caller.adjust_fp(power)
            self.caller.location.msg_contents(
                f"{self.caller} eats {obj} and looks more powerful."
            )
            obj.delete()
            return

        self.caller.at_emote(
            f"$conj({self.cmdstring}) the {{target}}.", mapping={"target": obj}
        )
        obj.delete()


class CmdDropAll(CmdGet):
    """
    Get an object from the room or from another object.

    Usage:
        drop <obj> or drop all

    Example:
        drop apple, drop all
    """

    key = "drop"
    aliases = "drop"
    help_category = "general"

    def func(self):
        caller = self.caller
        arg = self.args.strip().lower()

        if not arg:
            caller.msg("Drop what?")
            return

        if arg == "all":
            objs = caller.contents

            if not objs:
                return

            for obj in objs:
                if obj.move_to(caller.location, quiet=True, move_type="drop"):
                    caller.msg(f"Dropped {obj}.")
                    obj.at_drop(caller)

        super().func()


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
        caller = self.caller
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
                    caller.msg(f"Getting {obj}")
                    obj.move_to(self.caller, quiet=True)

        super().func()


class InteractCmdSet(CmdSet):
    key = "Interact CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()
        self.add(CmdEat)
        self.add(CmdGetAll)
        self.add(CmdDropAll)
