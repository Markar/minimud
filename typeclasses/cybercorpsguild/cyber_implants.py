from commands.command import Command
from typeclasses.cybercorpsguild.cybercorps_commands import PowerCommand
from evennia import CmdSet
from evennia.utils.evtable import EvTable

ImplantObjects = [
    {
        "name": "Adaptive Armor",
        "skill": "cybernetic enhancements",
        "skill_req": 1,
        "cost": 1,
        "rank": 10,
    },
    {
        "name": "Adrenaline Boost",
        "skill": "biotech research",
        "skill_req": 2,
        "cost": 1,
        "rank": 10,
    },
    {
        "name": "Platelet Factory",
        "skill": "biotech research",
        "skill_req": 1,
        "cost": 100,
        "rank": 4,
    },
]


# region Adaptive Armor
class CmdAdaptiveArmor(PowerCommand):
    """
    Adaptive armor is a type of cybernetic enhancement that can change its properties based on the situation. The armor is made of advanced materials that can shift and adapt to different threats, providing protection against physical, energy, and environmental hazards. Adaptive armor is often used by soldiers and security personnel who need versatile protection in combat situations.

    Usage:
        adaptive armor
    """

    key = "adaptive armor"
    help_category = "cybercorps"
    cost = 50
    guild_level = 10

    def func(self):
        caller = self.caller
        if not caller.db.guild_level >= self.guild_level:
            caller.msg(f"|CYou don't have access to adapative armor yet.")
            return
        if not caller.cooldowns.ready("adaptive_armor"):
            caller.msg(f"|CYou can't change wares that quickly!")
            return False
        if caller.db.ep < self.cost and not caller.db.adaptive_armor:
            caller.msg(f"|rYou need more energy to do that.")
            return
        if caller.db.adaptive_armor:
            caller.location.msg_contents(
                f"|c{caller} deactivates their adaptive armor.", from_obj=caller
            )
            caller.db.adaptive_armor = False
            return

        caller.cooldowns.add("adaptive_armor", 50)
        caller.cooldowns.add("global_cooldown", 2)
        caller.db.adaptive_armor = True
        caller.db.ep -= self.cost
        caller.location.msg_contents(
            f"|c{caller} activates their adaptive armor.", from_obj=caller
        )


# region DocWagon
class CmdDocWagon(PowerCommand):
    """
    DocWagon is a premier emergency medical service provider known for its rapid response and high-tech solutions. Founded in 2037, DocWagon has revolutionized the medical services industry with its unique offerings, including:

    Usage:
        docwagon revive

    """

    key = "docwagon revive"
    help_category = "cybercorps"
    cost = 10

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        if not caller.db.docwagon["count"] > 0:
            caller.msg(f"|CYou are too tired to use this power.")
            return
        if not caller.cooldowns.ready("docwagon"):
            caller.msg(f"|CNot so fast!")
            return False
        if caller.db.ep < self.cost:
            caller.msg(f"|rYou need at least {self.cost} energy to use this power.")
            return
        if glvl < 10:
            caller.msg(f"|CYou need to be guild level 10 to use burnout.")
            return
        caller.db.ep -= self.cost
        caller.cooldowns.add("docwagon", 60)
        caller.cooldowns.add("global_cooldown", 2)
        skill_rank = caller.db.skills.get("Security Services", 1)

        self.msg(f"|304A DocWagon medical team arrives to treat you!|n")
        caller.adjust_hp(caller.db.hpmax)
        caller.adjust_fp(caller.db.fpmax)

        caller.db.docwagon["count"] -= 1
        caller.db.docwagon["duration"] = 3 + skill_rank * 2


# region Platelet Factory
class CmdPlateletFactory(Command):
    """
    Activate your platelet factory, increasing your health regeneration rate.

    Usage:
        pulse grenade
    """

    key = "platelet factory "
    help_category = "cybercorps"
    cost = 50
    guild_level = 4
    skill = "biotech research"
    skill_req = 1

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


# region Adrenaline Boost
class CmdAdrenalineBoost(PowerCommand):
    key = "adrenaline boost"
    aliases = ["boost"]
    cost = 50
    guild_level = 10
    skill = "biotech research"
    skill_req = 2
    help_category = "cybercorps"

    def func(self):
        caller = self.caller
        implants = getattr(caller.db, "implants", {})
        adrenaline = getattr(caller.db, "adrenaline_boost", {})
        biotech = caller.db.skills.get("biotech research", 0)
        hasAdrenal = "adrenaline boost" in implants

        if not hasAdrenal:
            caller.msg(f"|CYou don't have an adrenal implant yet.")
            return

        if not caller.db.guild_level >= self.guild_level:
            caller.msg(f"|CYou don't have access to adrenal boost yet.")
            return

        if not caller.cooldowns.ready("adrenaline_boost"):
            caller.msg(f"|CYou're still recovering from the last dose of adrenaline.")
            return False

        if caller.db.ep < self.cost and not adrenaline:
            caller.msg(f"|rYou need more energy to do that.")
            return

        if getattr(adrenaline, "duration", 0) > 0:
            caller.msg(f"|CYou're already under the effects of adrenaline.")
            return
        else:
            caller.cooldowns.add("global_cooldown", 2)
            caller.cooldowns.add("adrenaline_boost", 6)
            caller.db.adrenaline_boost = {"active": True, "duration": 2 + biotech}
            caller.adjust_ep(-self.cost)
            caller.location.msg_contents(
                f"|c{caller} gets a crazed look in his eyes!", from_obj=caller
            )

        return


class CmdCyberneticImplants(PowerCommand):
    key = "cybernetic implants"
    aliases = ["implants"]
    cost = 0
    guild_level = 1
    help_category = "cybercorps"

    def func(self):
        caller = self.caller
        implants = getattr(caller.db, "implants", {})

        table = EvTable(
            f"|wImplant", f"|wSkill", f"|wRank", f"|wCost", f"|wLevel", border="table"
        )
        for implant in ImplantObjects:
            if implant["name"].lower() in implants:
                table.add_row(
                    f"|g{implant['name']}",
                    f"|g{implant['skill']}",
                    f"|g{implant['rank']}",
                    f"|g{implant['cost']}",
                    f"|g{implant['skill_req']}",
                )

        caller.msg(str(table))

        return


class CybercorpsImplantCmdSet(CmdSet):
    key = "Cybercorps Implant CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()
        self.add(CmdDocWagon)
        self.add(CmdAdaptiveArmor)
        self.add(CmdCyberneticImplants)
        self.add(CmdAdrenalineBoost)
        self.add(CmdPlateletFactory)
