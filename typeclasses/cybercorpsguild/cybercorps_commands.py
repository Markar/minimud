import math
from random import randint, uniform
from evennia import CmdSet
from commands.command import Command
from evennia.utils.evtable import EvTable
from evennia.utils import delay
from evennia.contrib.rpg.buffs import BaseBuff
from typeclasses.utils import PowerCommand

from typeclasses.cybercorpsguild.cyber_constants_and_helpers import (
    SKILLS_COST,
    TITLES,
)
from typeclasses.utils import get_glvl_cost, SKILL_RANKS


# region Pulse Grenade
class CmdPulseGrenade(PowerCommand):
    """
    A grenade that emits a burst of energy, stunning and damaging targets within its radius.

    Usage:
        pulse grenade
    """

    key = "pulse grenade"
    help_category = "cybercorps"
    cost = 10
    guild_level = 12

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


# region First Aid
class CmdFirstAid(PowerCommand):
    """
    Perform first aid on yourself or another character.

    Usage:
        first aid
    """

    key = "first aid"
    aliases = ["fa", "aid"]
    help_category = "cybercorps"
    cost = 5
    ep_cost = 20
    guild_level = 5

    def func(self):
        caller = self.caller
        hp = caller.db.hp
        hpmax = caller.db.hpmax
        percent = hp / hpmax * 100
        if caller.db.combat_target:
            caller.msg(f"|CYou can't do that while in combat.")
            return
        if percent >= 50:
            caller.msg(f"|CYou don't need first aid.")
            return
        if not caller.db.guild_level >= self.guild_level:
            caller.msg(f"|CYou don't have access to first aid yet.")
            return
        if not caller.cooldowns.ready("first_aid"):
            caller.msg(f"|CNot so fast!")
            return False
        if caller.db.ep < self.cost:
            caller.msg(f"|rYou need more energy to do that.")
            return

        caller.cooldowns.add("first_aid", 4)
        caller.cooldowns.add("global_cooldown", 2)
        skill_rank = caller.db.skills.get("Security Services", 1)

        # self.msg(f"|cYou perform first aid on yourself or another character.")
        caller.location.msg_contents(f"|c{caller} performs first aid on themselves.")

        amount = 10 + skill_rank * 2
        caller.adjust_hp(amount)
        caller.adjust_fp(-self.cost)
        caller.adjust_ep(-self.ep_cost)
        caller.msg(caller.get_display_status(caller))
        # for obj in caller.location.contents:
        #     if obj.db.hp:
        #         obj.db.hp += 10 + skill_rank * 2
        #         if obj.db.hp > obj.db.hpmax:
        #             obj.db.hp = obj.db.hpmax

        return


def _calculate_resupply_restoration(self):
    """
    Calculate the amount of focus and energy restored during resupplying.
    """
    caller = self
    intel = caller.traits.int.value
    dex = caller.traits.dex.value
    skill_rank = caller.db.skills.get("energy solutions", 1)
    stat_bonus = int((intel + dex) * 0.5)
    epmax = caller.db.epmax

    fp_restored = 5 + randint(1, skill_rank)
    ep_restored = 5 + int(uniform(3, stat_bonus)) + (skill_rank * 3) + (epmax * 0.05)
    caller.msg(f"|GYou load up some ammunition, grenades, and energy cells.")

    caller.adjust_fp(fp_restored)
    caller.adjust_ep(ep_restored)
    caller.msg(caller.get_display_status(caller))


# region Resupply
class CmdResupply(PowerCommand):
    """
    Resupply your ammunition, grenades, energy cells, and other consumables.
    """

    key = "resupply"
    aliases = ["resup", "sup"]
    help_category = "cybercorps"
    guild_level = 1
    cost = 10

    def _end_resupply(self, caller):
        caller.tags.remove("resupplying", category="status")

        caller.location.msg_contents(
            f"|C$You() stand up, locked and loaded.",
            from_obj=caller,
        )
        _calculate_resupply_restoration(self)

    def func(self):
        super().func()
        caller = self.caller
        args = self.args.strip()
        glvl = caller.db.guild_level

        if caller.db.ep == caller.db.epmax:
            caller.msg(f"|gYou are already at fully supplied.")
            return

        if caller.db.combat_target:
            caller.msg(f"|rYou can't resupply while in combat.")
            return

        if glvl < self.guild_level:
            self.msg(
                f"|rYou must be at least guild level {self.guild_level} to use this power."
            )
            return

        if not caller.cooldowns.ready("resupply"):
            caller.msg(f"|CYou can't resupply yet.")
            return False

        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.tags.add("resupplying", category="status")
        caller.cooldowns.add("global_cooldown", 6)
        caller.cooldowns.add("resupply", 6)

        caller.location.msg_contents(
            f"|C$You() sits down and start resupplying their ammunition, grenades, and energy cells.",
            from_obj=caller,
        )
        if args == "full":
            caller.buffs.add(ResupplyBuff)
        else:
            delay(5, self._end_resupply, caller)


class ResupplyBuff(BaseBuff):
    """
    A buff that restores supplies to the user.
    """

    duration = 60
    tickrate = 5
    type = "resupply"
    key = "resupply"

    def at_tick(self, initial, **kwargs):
        _calculate_resupply_restoration(self.owner)

        if (
            self.owner.db.ep == self.owner.db.epmax
            and self.owner.db.fp == self.owner.db.fpmax
        ):
            self.duration = 0
            self.owner.msg(f"|gYou stand up, locked and loaded.")
            self.owner.tags.remove("resupplying", category="status")
            return

        if self.ticknum == 12:
            self.owner.msg(f"|gYou stand up, locked and loaded.")
            self.owner.tags.remove("resupplying", category="status")
            return


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
        table.add_row(f"|GLoadout", 1, 0)
        table.add_row(f"|GLoadout Remove", 1, 0)
        table.add_row(f"|GFirst Aid", 5, "5 Energy")
        table.add_row(f"|GDocWagon Revive", 7, "10 Energy")
        table.add_row(f"|GAdaptive Armor", 10, "25 Energy")
        table.add_row(f"|GPulse Grenade", 12, "10 Energy")
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
        cost = get_glvl_cost(caller.db.guild_level + 1)

        if caller.db.gxp < cost:
            self.msg(f"|wYou need {cost - caller.db.gxp} more experience to advance.")
            return
        else:
            caller.db.gxp -= cost
            caller.db.guild_level += 1
            caller.db.title = TITLES[caller.db.guild_level]
            self.msg(f"|rYou are now {caller.db.title} ({caller.db.guild_level}).")

            max = 0
            if caller.db.guild_level >= 7:
                max += 1
            if caller.db.guild_level >= 14:
                max += 1
            if caller.db.guild_level >= 21:
                max += 1
            if caller.db.guild_level >= 28:
                max += 1
            if caller.db.guild_level >= 30:
                max += 1
            caller.db.docwagon["max"] = max
            energy_solutions = caller.db.skills.get("energy solutions", 1)
            ep_max_bonus = energy_solutions * 10
            ep_max_bonus += math.floor(caller.db.guild_level / 5) * 50
            caller.db.epmax = 50 * caller.db.guild_level + ep_max_bonus

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
    help_category = "cybercorps"

    def func(self):
        caller = self.caller
        title = caller.db.title or TITLES[0]
        my_glvl = caller.db.guild_level or 1
        gxp = caller.db.gxp or 0
        skill_gxp = caller.db.skill_gxp or 0
        gxp_needed = get_glvl_cost(my_glvl + 1)
        reaction = caller.db.reaction_percentage or 50
        melee_weapon = "None"
        if caller.db.melee_weapon:
            melee_weapon = caller.db.melee_weapon.name
        ranged_weapon = "None"
        if caller.db.ranged_weapon:
            ranged_weapon = caller.db.ranged_weapon.name

        doc_count = caller.db.docwagon["count"]
        doc_max = caller.db.docwagon["max"]
        platelet_factory = getattr(caller.db, "platelet_factory", False)

        table = EvTable(f"|c{caller}", f"|c{title}", border="table")
        table.add_row(f"|GGuild Level", my_glvl)
        table.add_row(f"|GGXP", f"{gxp} / {gxp_needed}")
        table.add_row(f"|GSkill GXP", skill_gxp)
        table.add_row(f"|GReaction", f"{reaction}%")
        table.add_row(f"|GMelee Weapon", melee_weapon)
        table.add_row(f"|GRanged Weapon", ranged_weapon)
        table.add_row(f"|GDocWagon Revives", f"{doc_count} / {doc_max}")
        table.add_row(
            f"|GNano Reinforced Skeleton",
            getattr(caller.db, "nano_reinforced_skeleton", False),
        )
        table.add_row(f"|GAdaptive Armor", getattr(caller.db, "adaptive_armor", False))
        table.add_row(f"|GPlatelet Factory", platelet_factory)

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


# region Test
class CmdTest(Command):
    key = "test"

    from evennia import TICKER_HANDLER as tickerhandler

    # from typeclasses.elementalguild.earth_elemental_commands import EarthElementalCmdSet
    # from typeclasses.elementalguild.fire_elemental_commands import FireElementalCmdSet

    def func(self):
        caller = self.caller
        caller.msg("test")
        # from typeclasses.cybercorpsguild.cybercorps_wares import CybercorpsWaresCmdSet
        # from typeclasses.cybercorpsguild.cyber_implants import CybercorpsImplantCmdSet

        self.tickerhandler.clear()
        # from commands.shops import ShopCmdSet
        # del caller.db.docwagon
        # del caller.db.skills
        # del caller.db.guild_level
        # del caller.db.strategy
        # del caller.db.wares

        caller.cmdset.remove(CybercorpsCmdSet)
        # caller.cmdset.remove(CybercorpsWaresCmdSet)
        # caller.cmdset.remove(CybercorpsImplantCmdSet)
        # caller.cmdset.delete(EarthElementalCmdSet)
        # caller.cmdset.delete(EarthElementalCmdSet)
        # caller.cmdset.delete(CybercorpsCmdSet)
        # caller.cmdset.delete(CybercorpsCmdSet)
        # caller.cmdset.delete(CybercorpsCmdSet)
        # caller.location.cmdset.delete(ShopCmdSet)

        caller.msg("done")


# region TestRestock
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


class CmdUpdateChessboard(Command):
    key = "upd chessboard"

    def func(self):
        caller = self.caller
        from typeclasses.chessboardrooms import (
            ChessboardDecayingSkeleton,
            ChessboardGnoll,
            ChessboardGnollPup,
        )

        creatures = (
            list(ChessboardDecayingSkeleton.objects.all())
            + list(ChessboardGnoll.objects.all())
            + list(ChessboardGnollPup.objects.all())
        )

        for room in creatures:
            caller.msg(f"room: {room}")
            for obj in room.contents:
                check = obj.is_typeclass("typeclasses.characters.NPC", exact=False)
                if check:
                    caller.msg(f"check: {check}")
                    obj.delete()
            room.at_object_creation()
        caller.msg("done")


class CmdHp(Command):
    """
    Display the current and maximum health of the caller.

    Usage:
        hp
    """

    key = "hp"
    help_category = "cybercorps"

    def func(self):
        caller = self.caller

        caller.msg(caller.get_display_status(caller))


# region CmdSet
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
        self.add(CmdKickstart)
        self.add(CmdTestRestock)

        self.add(CmdReaction)
        self.add(CmdPulseGrenade)
        self.add(CmdFirstAid)
        self.add(CmdResupply)

        self.add(CmdUpdateChessboard)
        self.add(CmdHp)
