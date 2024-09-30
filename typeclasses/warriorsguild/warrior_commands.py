import math
from random import randint, uniform
from evennia import CmdSet
from commands.command import Command
from evennia.utils.evtable import EvTable
from evennia.utils import delay

from typeclasses.cybercorpsguild.cyber_constants_and_helpers import (
    SKILLS_COST,
    TITLES,
)
from typeclasses.utils import get_glvl_cost, SKILL_RANKS


class PowerCommand(Command):
    def func(self):
        caller = self.caller
        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False
        caller.cooldowns.add("global_cooldown", 2)


# region Powers
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
        table.add_row(f"|GPulse Grenade", 5, "10 Energy")
        table.add_row(f"|GNano Reinforced Skeleton", 20, "75 Energy")

        caller.msg(str(table))


# region Reaction
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


# region Gtrain
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
            f"It will cost you {int(cost)} experience to advance {skill}. Confirm? Yes/No"
        )
        if confirm.lower() not in (
            "yes",
            "y",
        ):
            self.msg("Cancelled.")
            return

        setattr(caller.db, "skill_gxp", skill_gxp - cost)
        caller.db.skills[skill] += 1
        if skill == "energy solutions":
            caller.db.epmax += 10
        caller.msg(f"|yYou grow more experienced in {skill}")


# region Ghelp
class CmdGhelp(Command):
    """
    Help files for the Cybercorps Guild.

    Cybernetic Enhancements
    Security Services
    Biotech Research
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
        if skill == "energy solutions":
            caller.msg(
                "|cEnergy Solutions|n\n\n"
                "Energy solutions are technologies and strategies that can help reduce energy consumption, increase energy efficiency, and promote the use of renewable energy sources. Energy solutions can include technologies such as solar panels, wind turbines, and energy-efficient appliances. Energy solutions are essential for addressing climate change and reducing the environmental impact of energy production and consumption."
            )
        if skill == "nano reinforced skeleton":
            caller.msg(
                "|cNano Reinforced Skeleton|n\n\n"
                "The Nano-Reinforced Endoskeleton is a cutting-edge cybernetic implant that enhances the user's physical resilience and durability. By integrating advanced nanomaterials into the skeletal structure, this implant significantly boosts constitution, allowing the user to withstand greater physical stress and recover more quickly from injuries."
            )

        caller.msg(f"|rNo help found for {skill}.")


# region GAdvance
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
        cost = get_glvl_cost.get(caller.db.guild_level + 1, 0)

        if caller.db.gxp < cost:
            self.msg(f"|wYou need {cost - caller.db.gxp} more experience to advance.")
            return
        else:
            caller.db.gxp -= cost
            caller.db.guild_level += 1
            caller.db.title = TITLES[caller.db.guild_level]
            self.msg(f"|rYou are now {caller.db.title} ({caller.db.guild_level}).")

    def func(self):
        caller = self.caller
        caller.msg(f"|G{caller}")

        self._adv_level()


# region Gscore
class CmdGuildStatSheet(Command):
    """
    Display your guild stats
    """

    key = "gscore"
    aliases = "gs"
    help_category = "warrior"

    def func(self):
        caller = self.caller
        title = caller.db.title or TITLES[0]
        my_glvl = caller.db.guild_level or 1
        gxp = caller.db.gxp or 0
        skill_gxp = caller.db.skill_gxp or 0
        gxp_needed = get_glvl_cost[my_glvl + 1]
        reaction = caller.db.reaction_percentage or 50
        melee_weapon = "None"
        if caller.db.melee_weapon:
            melee_weapon = caller.db.melee_weapon.name

        table = EvTable(f"|c{caller}", f"|c{title}", border="table")
        table.add_row(f"|GGuild Level", my_glvl)
        table.add_row(f"|GGXP", f"{gxp} / {gxp_needed}")
        table.add_row(f"|GSkill GXP", skill_gxp)
        table.add_row(f"|GReaction", f"{reaction}%")
        table.add_row(f"|GMelee Weapon", melee_weapon)

        caller.msg(str(table))

        skill_table = EvTable(f"|cSkills", f"|cCost", f"|cRank", border="table")
        skills = (
            caller.db.skills.items()
        )  # Get the items (key-value pairs) of the skills dictionary

        # Assuming SKILLS_COST is a dictionary that maps ranks to costs
        for skill, rank in skills:
            skill_table.add_row(f"|G{skill.title()}", f"{rank}", f"{SKILLS_COST[rank]}")

        caller.msg(str(skill_table))


# region Kickstart
class CmdKickstart(Command):
    key = "kickstart"

    def func(self):
        caller = self.caller
        caller.kickstart()


# region Skills
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


# region CmdSet
class WarriorCmdSet(CmdSet):
    key = "Warrior CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        self.add(CmdGhelp)
        self.add(CmdGAdvance)
        self.add(CmdGuildStatSheet)
        self.add(CmdSkills)
        self.add(CmdPowers)
        self.add(CmdGTrain)
        self.add(CmdKickstart)
        self.add(CmdReaction)
