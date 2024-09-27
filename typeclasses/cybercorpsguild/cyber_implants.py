from commands.command import Command
from evennia import CmdSet


class CmdPlateletFactory(Command):
    """
    Activate your platelet factory, increasing your health regeneration rate.

    Usage:
        pulse grenade
    """

    key = "platelet factory "
    help_category = "cybercorps"
    cost = 50
    guild_level = 8
    skill = "biotech research"
    skill_req = 2

    def func(self):
        caller = self.caller
        implants = getattr(caller.db, "implants", {})
        active = getattr(caller.db, "platelet_factory_active", False)

        if not implants.get("platelet factory", False):
            caller.msg(f"|CYou don't have a platelet factory implanted yet.")
            return
        if active:
            setattr(caller.db, "platelet_factory_active", False)
            caller.msg(f"|cYou feel your platelet production slowing down.")
        else:
            setattr(caller.db, "platelet_factory_active", True)
            self.msg(f"|cYour feel your platelet production flooding your system.")
            caller.db.ep -= self.cost

        return


class CybercorpsCmdSet(CmdSet):
    key = "Cybercorps CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        self.add(CmdPlateletFactory)
