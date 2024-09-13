import math
from random import randint, uniform
from evennia import CmdSet
from evennia.utils.evtable import EvTable
from evennia.utils import delay
from commands.command import Command
from typeclasses.cybercorpsguild.cybercorps_wares import (
    HandRazors,
    NanoBlade,
    TacticalShotgun,
    StealthBlade,
    ShockHand,
    SmartGun,
    EnergySword,
)

from typeclasses.cybercorpsguild.cyber_constants_and_helpers import (
    SKILLS_COST,
    SKILL_RANKS,
    GUILD_LEVEL_COST_DICT,
    TITLES,
)

WaresObjects = {
    "hand razors": HandRazors,
    "nanoblade": NanoBlade,
    "tactical shotgun": TacticalShotgun,
    "stealth blade": StealthBlade,
    "shock hand": ShockHand,
    "smart gun": SmartGun,
    "energy sword": EnergySword,
}


class PowerCommand(Command):
    def func(self):
        caller = self.caller
        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False
        caller.cooldowns.add("global_cooldown", 2)


class CmdLoadout(Command):
    """
    Equip a weapon from your inventory.

    Usage:
        loadout <weapon>
    """

    key = "loadout"
    help_category = "cybercorps"

    def func(self):
        caller = self.caller
        args = self.args.strip().lower()
        melee = caller.db.melee_weapon or HandRazors
        ranged = caller.db.ranged_weapon or HandRazors

        if not args:
            caller.msg("Usage: loadout <weapon>")
            return

        if not args in WaresObjects.keys():
            caller.msg(f"|rYou can't equip the {args}.")
            return

        if args == "nanoblade":
            if melee.name == "nanoblade":
                caller.msg(f"|rYou already have the nanoblade equipped.")
                return

            caller.db.melee_weapon = NanoBlade()
            caller.msg(
                f"|gYou equip the nanoblade, a weapon that can cut through almost anything."
            )

        if args == "stealth blade":
            if melee.name == "stealth blade":
                caller.msg(f"|rYou already have the stealth blade equipped.")
                return

            caller.db.melee_weapon = StealthBlade()
            caller.msg(
                f"|gYou equip the stealth blade, a weapon that can cut through almost anything."
            )

        if args == "tactical shotgun":
            if ranged.name == "tactical shotgun":
                caller.msg(f"|rYou already have the tactical shotgun equipped.")
                return

            caller.db.ranged_weapon = TacticalShotgun()
            caller.msg(f"|gYou equip the tactical shotgun, a versatile weapon.")

        if args == "smart gun":
            if ranged.name == "smart gun":
                caller.msg(f"|rYou already have the smart gun equipped.")
                return

            caller.db.ranged_weapon = SmartGun()
            caller.msg(f"|gYou equip the smart gun, a versatile weapon.")

        if args == "shock hand":
            if melee.name == "shock hand":
                caller.msg(f"|rYou already have the shock hand equipped.")
                return
            caller.db.melee_weapon = ShockHand()
            caller.msg(
                f"|gYou equip the shock hand, a weapon that can deliver a powerful shock."
            )
        if args == "energy sword":
            if melee.name == "energy sword":
                caller.msg(f"|rYou already have the energy sword equipped.")
                return
            caller.db.melee_weapon = EnergySword()
            caller.msg(
                f"|gYou equip the energy sword, a weapon that can cut through almost anything."
            )

        if args == "adaptive armor":
            if caller.db.adaptive_armor:
                caller.msg(f"|rYou already have adaptive armor equipped.")
                return

            caller.db.adaptive_armor = True
            caller.msg(f"|gYou equip the adaptive armor.")

        return


class CmdLoadoutRemove(Command):
    """
    Unequip a ware from your inventory.

    Usage:
        loadout remove <ware>
    """

    key = "loadout remove"
    help_category = "cybercorps"

    def func(self):
        caller = self.caller
        args = self.args.strip().lower()
        melee = caller.db.melee_weapon or HandRazors
        ranged = caller.db.ranged_weapon or None

        if not args:
            caller.msg("Usage: loadout remove <ware>")
            return

        if not args in caller.db.wares:
            caller.msg(f"|rYou can't unequip {args}.")
            return

        if args == "handrazors":
            caller.msg(f"|gYou don't want to be caught without your hand razors.")

        if args == "nanoblade":
            if not melee.name == args:
                caller.msg(f"|rYou don't have the nanoblade equipped.")
                return
            caller.db.melee_weapon = None
            caller.msg(f"|gYou gracefully put the nanoblade back into its sheath.")

        if args == "tactical shotgun":
            if not ranged.name == args:
                caller.msg(f"|rYou don't have the tactical shotgun equipped.")
                return
            caller.db.ranged_weapon = False
            caller.msg(f"|gYou put the tactical shotgun on your back.")

        if args == "adaptive armor":
            if not caller.db.adaptive_armor:
                caller.msg(f"|rYou don't have adaptive armor equipped.")
                return
            caller.db.adaptive_armor = False
            caller.msg(f"|gYou remove the adaptive armor.")

        return


class CmdPulseGrenade(PowerCommand):
    """
    A grenade that emits a burst of energy, stunning and damaging targets within its radius.

    Usage:
        pulse grenade
    """

    key = "pulse grenade"
    help_category = "cybercorps"
    cost = 10
    guild_level = 5

    def func(self):
        caller = self.caller
        if not caller.db.guild_level >= self.guild_level:
            caller.msg(f"|CYou don't have access to pulse grenades yet.")
            return
        if not caller.cooldowns.ready("pulse_grenade"):
            caller.msg(f"|CNot so fast!")
            return False
        if caller.db.ep < self.cost:
            caller.msg(f"|rYou need more energy to do that.")
            return
        caller.db.ep -= self.cost
        caller.cooldowns.add("pulse_grenade", 60)
        caller.cooldowns.add("global_cooldown", 2)
        skill_rank = caller.db.skills.get("energy solutions", 1)

        self.msg(f"|cYou throw a pulse grenade, stunning and damaging your enemies.")
        caller.location.msg_contents(
            f"|c{caller} throws a pulse grenade, stunning and damaging their enemies."
        )

        for obj in caller.location.contents:
            if obj.db.hp:
                obj.db.hp -= 10 + skill_rank * 2
                # obj.db.stunned = True
                # obj.db.stunned_duration = 3 + skill_rank
                # delay(, persistent=True)

        return


class CmdAdaptiveArmor(PowerCommand):
    """
    Adaptive armor is a type of cybernetic enhancement that can change its properties based on the situation. The armor is made of advanced materials that can shift and adapt to different threats, providing protection against physical, energy, and environmental hazards. Adaptive armor is often used by soldiers and security personnel who need versatile protection in combat situations.

    Usage:
        adaptive armor
    """

    key = "adaptive armor"
    help_category = "cybercorps"
    cost = 25
    guild_level = 10

    def func(self):
        caller = self.caller
        if not caller.db.guild_level >= self.guild_level:
            caller.msg(f"|CYou don't have access to adapative armor yet.")
            return
        if not caller.cooldowns.ready("adaptive_armor"):
            caller.msg(f"|CYou can't change wares that quickly!")
            return False
        if caller.db.ep < self.cost:
            caller.msg(f"|rYou need more energy to do that.")
            return
        if caller.db.adaptive_armor:
            caller.msg(f"|rThe adaptive armor retracts, leaving you unprotected.")
            caller.db.adaptive_armor = False
            return

        caller.db.adaptive_armor = True
        caller.msg(f"|The adaptive armor expands to cover your body.")


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
        if caller.db.docwagon["active"]:
            caller.msg(f"|CYour response team is already here.")
            return
        caller.db.ep -= self.cost
        caller.cooldowns.add("docwagon", 60)
        caller.cooldowns.add("global_cooldown", 2)
        skill_rank = caller.db.skills.get("Security Services", 1)

        self.msg(f"|cA DocWagon response team is on their way!|n")
        caller.adjust_hp(caller.traits.hpmax.value)
        caller.adjust_fp(caller.traits.fpmax.value)
        caller.adjust_ep(caller.traits.epmax.value)

        caller.db.docwagon["active"] = True
        caller.db.docwagon["count"] -= 1
        caller.db.docwagon["duration"] = 3 + skill_rank * 2


class CmdSyntheticConversion(Command):
    """
    A soldier of the Cybercorps can use synthetic conversion to turn the body into synthetic materials that can be repurposed for industrial use.
    """

    key = "synthetic conversion"
    aliases = ["convert", "synth", "syn"]
    help_category = "cybercorps"

    def func(self):
        if not self.args:
            caller = self.caller
            if corpse := caller.location.search("corpse-1"):
                base_power = corpse.db.power
                skill_rank = caller.db.skills.get("energy solutions", 0)

                # Calculate the power with the skill rank multiplier
                power = base_power * (1 + (skill_rank * 0.1))

                caller.adjust_ep(power)
                corpse.delete()
                self.msg(
                    f"|CYour command initiates the synthetic conversion process. The body is swiftly broken down and repurposed into valuable materials, leaving no trace behind."
                )

            else:
                caller.msg("Convert what synthetically?")


# Other powers
class CmdPowers(Command):
    """
    List of powers available to the Elemental, their rank, and their cost.

    Usage:
        powers

    """

    key = "powers"
    help_category = "cybercorps"

    def func(self):
        caller = self.caller

        table = EvTable(f"|cPower", f"|cRank", f"|cCost", border="table")
        table.add_row(f"|GSynthetic Conversion", 1, 0)
        table.add_row(f"|GLoadout", 1, 0)
        table.add_row(f"|GLoadout Remove", 1, 0)
        table.add_row(f"|GAdaptive Armor", 10, "25 Energy")
        table.add_row(f"|GDocWagon Revive", 7, "10 Energy")

        caller.msg(str(table))


class CmdReaction(Command):
    """
    Set the elemental's reaction to a dropping below a certain health threshold.

    Usage:
        reaction <percentage>
    """

    key = "reaction"
    help_category = "earth elemental"

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
        gtrain cybernetic enhancements
    """

    key = "gtrain"
    help_category = "cybercorps"

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
    Help files for the Cybercorps Guild.

    Cybernetic Enhancements
    Artificial Intelligence
    Security Services
    Biotech Research
    Corporate Espionage
    Energy Solutions

    Usage:
        ghelp
        ghelp <skill>
    """

    key = "ghelp"
    help_category = "cybercorps"

    def func(self):
        caller = self.caller
        skill = self.args.strip().lower()
        if skill == "":
            caller.msg(
                "|The Cybercorps Mega Corporation|n\n\n"
                "The CyberCorps Mega Corporation is a powerful conglomerate specializing in advanced cybernetic technologies and artificial intelligence. CyberCorps is known for its influence and control over multiple markets, often operating with the power and autonomy of a sovereign entity. Their presence in the city is a testament to their dominance in the field of cybernetics and technology. \n\n"
                "Usage:\n"
                "    ghelp <skill>\n"
            )
        if skill == "adaptive armor":
            caller.msg(
                "|cAdaptive Armor|n\n\n"
                "Adaptive armor is a type of cybernetic enhancement that can change its properties based on the situation. The armor is made of advanced materials that can shift and adapt to different threats, providing protection against physical, energy, and environmental hazards. Adaptive armor is often used by soldiers and security personnel who need versatile protection in combat situations."
            )
        if skill == "cybernetic enhancements":
            caller.msg(
                "|cCybernetic Enhancements|n\n\n"
                "Cybernetic enhancements are advanced technologies that can be integrated into the human body to enhance physical capabilities. These enhancements can include cybernetic limbs, neural interfaces, and other technologies that can improve strength, speed, and endurance. Cybernetic enhancements are often used by soldiers, security personnel, and other professionals who need to perform at the highest levels."
            )
        if skill == "artificial intelligence":
            caller.msg(
                "|cArtificial Intelligence|n\n\n"
                "Artificial intelligence is a field of computer science that focuses on the development of intelligent machines that can perform tasks that typically require human intelligence. These tasks can include speech recognition, problem-solving, and decision-making. Artificial intelligence is used in a wide range of applications, from self-driving cars to virtual assistants."
            )
        if skill == "security services":
            caller.msg(
                "|cSecurity Services|n\n\n"
                "Security services are a critical component of the Cybercorps Mega Corporation's operations. Security personnel are responsible for protecting the corporation's assets, employees, and facilities from threats such as theft, vandalism, and espionage. Security services can include physical security, cybersecurity, and emergency response services."
            )
        if skill == "biotech research":
            caller.msg(
                "|cBiotech Research|n\n\n"
                "Biotech research is a field of science that focuses on the development of technologies that use biological systems to create new products and processes. Biotech research can include the development of new drugs, medical devices, and agricultural products. Biotech research is a rapidly growing field with the potential to revolutionize healthcare, agriculture, and other industries."
            )
        if skill == "corporate espionage":
            caller.msg(
                "|cCorporate Espionage|n\n\n"
                "Corporate espionage is the practice of using covert methods to obtain confidential information from a competitor or rival company. Corporate espionage can include activities such as hacking, surveillance, and bribery. Corporate espionage is a serious threat to businesses, as it can result in the loss of valuable intellectual property and competitive advantage."
            )
        if skill == "energy solutions":
            caller.msg(
                "|cEnergy Solutions|n\n\n"
                "Energy solutions are technologies and strategies that can help reduce energy consumption, increase energy efficiency, and promote the use of renewable energy sources. Energy solutions can include technologies such as solar panels, wind turbines, and energy-efficient appliances. Energy solutions are essential for addressing climate change and reducing the environmental impact of energy production and consumption."
            )

        caller.msg(f"|rNo help found for {skill}.")


class CmdGAdvance(Command):
    """
    Advance your guild level by spending gxp.

    Enter "advance" to see what you can learn.

    Usage:
        gadvance

    Example:
        gadvance
    """

    help_category = "cybercorps"
    key = "gadvance"
    aliases = "gadv"

    def _adv_level(self):
        caller = self.caller
        cost = GUILD_LEVEL_COST_DICT.get(caller.db.guild_level + 1, 0)

        if caller.db.gxp < cost:
            self.msg(f"|wYou need {cost - caller.db.gxp} more experience to advance.")
            return
        else:
            caller.db.gxp -= cost
            caller.db.guild_level += 1
            caller.db.epmax += 10
            caller.db.title = TITLES[caller.db.guild_level]
            self.msg(f"|rYou are now {caller.db.title} ({caller.db.guild_level}).")

        if caller.db.guild_level >= 7:
            caller.db.docwagon["max"] = 1
        elif caller.db.guild_level >= 14:
            caller.db.docwagon["max"] = 2
        elif caller.db.guild_level >= 21:
            caller.db.docwagon["max"] = 3
        elif caller.db.guild_level >= 30:
            caller.db.docwagon["max"] = 4

    def func(self):
        caller = self.caller
        caller.msg(f"|G{caller}")

        self._adv_level()


class CmdGuildStatSheet(Command):
    """
    Display your guild stats
    """

    key = "gscore"
    aliases = "gs"
    help_category = "cybercorps"

    def func(self):
        caller = self.caller
        title = caller.db.title or TITLES[0]
        my_glvl = caller.db.guild_level or 1
        gxp = caller.db.gxp or 0
        skill_gxp = caller.db.skill_gxp or 0
        gxp_needed = GUILD_LEVEL_COST_DICT[my_glvl + 1]
        reaction = caller.db.reaction_percentage or 50

        table = EvTable(f"|c{caller}", f"|c{title}", border="table")
        table.add_row(f"|GGuild Level", my_glvl)
        table.add_row(f"|GGXP", f"{gxp} / {gxp_needed}")
        table.add_row(f"|GSkill GXP", skill_gxp)
        table.add_row(f"|GReaction", f"{reaction}%")

        caller.msg(str(table))

        skill_table = EvTable(f"|cSkills", f"|cCost", f"|cRank", border="table")
        skills = (
            caller.db.skills.items()
        )  # Get the items (key-value pairs) of the skills dictionary

        # Assuming SKILLS_COST is a dictionary that maps ranks to costs
        for skill, rank in skills:
            skill_table.add_row(f"|G{skill.title()}", f"{rank}", f"{SKILLS_COST[rank]}")

        caller.msg(str(skill_table))


class CmdSkills(Command):
    """
    List of skills available to the Cyber, their rank, and their cost.

    Usage:
        skills

    """

    key = "skills"
    help_category = "cybercorps"

    def func(self):
        caller = self.caller

        table = EvTable(f"|cSkill", f"|cRank", f"|cCost", border="table")
        for skill, rank in caller.db.skills.items():
            table.add_row(f"|G{skill.title()}", f"{rank}", f"{SKILLS_COST[rank]}")

        caller.msg(str(table))


class CmdWares(Command):
    """
    List of wares available to the Cybercorps Guild.

    Usage:
        wares

    """

    key = "wares"
    help_category = "cybercorps"

    def func(self):
        caller = self.caller
        ware = self.args.strip().lower()

        if ware in WaresObjects.keys():
            obj = WaresObjects[ware]
            caller.msg(
                f"    |g{obj.name.title()}\n    |GCost: {obj.cost}\n|G{obj.__doc__}\n"
            )
            return

        if not ware:
            table = EvTable(f"|gName", f"|gDescription", f"|gCost", border="table")
            table.add_row(
                f"|GAdaptive Armor", "Armor that can adapt to different threats.", 0
            )

            for obj in WaresObjects.values():
                if obj.name in caller.db.wares:
                    table.add_row(
                        f"|Y{obj.name.title()}",
                        f"|Y{obj.short}",
                        f"|Y{obj.cost}",
                    )
                else:
                    table.add_row(
                        f"|G{obj.name.title()}", f"|G{obj.short}", f"|G{obj.cost}"
                    )
            caller.msg(str(table))
        return


class CmdTest(Command):
    key = "test"

    # from typeclasses.elementalguild.earth_elemental_commands import EarthElementalCmdSet
    # from typeclasses.elementalguild.fire_elemental_commands import FireElementalCmdSet

    def func(self):
        caller = self.caller
        caller.msg("test")
        # from commands.shops import ShopCmdSet
        del caller.db.docwagon
        del caller.db.skills
        del caller.db.guild_level
        del caller.db.strategy
        del caller.db.wares

        # caller.cmdset.delete(FireElementalCmdSet)
        # caller.cmdset.delete(EarthElementalCmdSet)
        # caller.cmdset.delete(EarthElementalCmdSet)
        # caller.cmdset.delete(CybercorpsCmdSet)
        # caller.cmdset.delete(CybercorpsCmdSet)
        # caller.cmdset.delete(CybercorpsCmdSet)
        # caller.location.cmdset.delete(ShopCmdSet)

        caller.msg("done")


class CmdTestRestock(Command):
    key = "testrestock"

    # from typeclasses.elementalguild.earth_elemental_commands import EarthElementalCmdSet
    # from typeclasses.elementalguild.fire_elemental_commands import FireElementalCmdSet

    def func(self):
        caller = self.caller
        caller.msg("test")
        from typeclasses.scripts import RestockScript

        caller.location.scripts.delete(RestockScript)
        caller.location.scripts.add(RestockScript, key="restock", autostart=True)

        caller.msg("done")


class CybercorpsCmdSet(CmdSet):
    key = "Cybercorps CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        self.add(CmdGhelp)
        self.add(CmdGAdvance)
        self.add(CmdGuildStatSheet)
        self.add(CmdSkills)
        self.add(CmdPowers)
        self.add(CmdGTrain)
        self.add(CmdTest)
        self.add(CmdTestRestock)
        self.add(CmdWares)

        self.add(CmdSyntheticConversion)
        self.add(CmdReaction)
        self.add(CmdDocWagon)
        self.add(CmdLoadout)
        self.add(CmdLoadoutRemove)

        self.add(CmdAdaptiveArmor)
        self.add(CmdPulseGrenade)


class CmdJoinCybercorps(Command):
    """
    Join the Cybercorps Mega corporation
    """

    key = "join cybercorps"

    def func(self):
        caller = self.caller
        if caller.db.guild == "adventurer":
            caller.msg(f"|rYou sign up to join the Cybercorps Mega Corporation")
            caller.swap_typeclass(
                "typeclasses.cybercorps.Cybercorps",
                clean_attributes=False,
            )
            caller.cmdset.add(CybercorpsCmdSet, persistent=True)
        else:
            caller.msg(f"|rYou are already in a guild")


class CmdLeaveCybercorps(Command):
    """
    Leave the Cybercorps Mega Corporation
    """

    key = "leave cybercorps"

    def strip(self):
        caller = self.caller
        caller.cmdset.delete(CybercorpsCmdSet)
        del caller.db.docwagon
        del caller.db.skills
        del caller.db.guild_level
        del caller.db.strategy
        del caller.db.wares

        return

    def func(self):
        caller = self.caller
        if caller.db.guild == "cybercorps":
            caller.swap_typeclass("typeclasses.characters.PlayerCharacter")
            self.strip()
            caller.msg(f"|rYou leave the Cybercorps Mega Corporation")
        else:
            caller.msg(f"|rYou are already an adventurer")


class CmdListWares(Command):
    """
    List wares available for purchase from the Cybercorps Mega Corporation
    """

    key = "list"

    def func(self):
        caller = self.caller
        table = EvTable(f"|gWares", f"|gSkill", f"|gRank", f"|gCost", border="table")
        for ware in WaresObjects.values():
            table.add_row(
                f"|G{ware.name}", f"|G{ware.skill}", f"|G{ware.rank}", f"|G{ware.cost}"
            )

        caller.msg(str(table))


class CmdBuyWares(Command):
    """
    Buy wares from the Cybercorps Mega Corporation
    """

    key = "buy"

    def func(self):
        caller = self.caller
        ware = self.args.strip().lower()

        if caller.db.guild != "cybercorps":
            caller.msg(
                f"|rYou need to be part of the Cybercorps Mega Corporation to buy wares."
            )
            return
        if not ware:
            caller.msg(f"|rUsage: wares buy <ware>")
            return

        if ware in caller.db.wares:
            caller.msg(f"|rYou already have the {ware}.")
            return

        for obj in WaresObjects.values():
            if obj.name.lower() == ware:
                ware = obj

                if caller.db.skills[f"{ware.skill}"] < ware.rank:
                    caller.msg(
                        f"|rYou need to be level {ware.rank} in {ware.skill} to buy the {ware.name}."
                    )
                    return

                if caller.db.coins < ware.cost:
                    caller.msg(
                        f"|rYou need {ware.cost - caller.db.coins} more coins to buy the {ware.name}."
                    )
                    return

                caller.db.wares.append(ware.name)
                caller.db.coins -= ware.cost
                caller.msg(
                    f"|gYou buy the {ware.name} from the Cybercorps Mega Corporation."
                )
                return

        caller.msg(f"|rYou can't buy the {ware.name}.")
        return


class CybercorpsWaresCmdSet(CmdSet):
    key = "Cybercorps Wares CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        self.add(CmdBuyWares)
        self.add(CmdListWares)
