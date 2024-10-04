import math
from random import randint, uniform
from evennia import CmdSet
from commands.command import Command
from evennia.utils.evtable import EvTable
from evennia.utils import delay

from typeclasses.knightguild.knight_constants_and_helpers import (
    TITLES,
)
from typeclasses.utils import get_glvl_cost, SKILL_RANKS, SKILLS_COST


class PowerCommand(Command):
    def func(self):
        caller = self.caller
        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False
        caller.cooldowns.add("global_cooldown", 2)


# region Bash
class CmdBash(PowerCommand):
    """
    Bash allows the knight to deliver a powerful blow to an enemy, stunning them and knocking them off balance. The knight can use their strength and weapon to deliver a crushing blow, disrupting the enemy's attacks and leaving them vulnerable to further attacks. The effectiveness of the bash is based on the knight's skill and strength.
    """

    key = "bash"
    help_category = "knight"
    guild_level = 9
    cost = 0

    def _calculate_damage(self):
        caller = self.caller
        str = caller.traits.str.value

        return randint(10, str + 10)

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        target = caller.db.combat_target
        super().func()

        if glvl < self.guild_level:
            caller.msg(
                f"|rYou must be at least level {self.guild_level} to use this power."
            )
            return

        if not target:
            caller.msg(f"|rYou must be in combat to use this power.")
            return

        if not caller.cooldowns.ready("bash"):
            caller.msg(f"|CNot so fast!")
            return False

        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.cooldowns.add("global_cooldown", 2)
        caller.cooldowns.add("bash", 18)

        caller.msg(f"|gYou prepare to deliver a powerful blow to your enemy.")
        caller.location.msg_contents(
            f"|C{caller.name} prepares to deliver a powerful blow to $you(target), focusing $pron(your) energy on offense.",
            exclude=caller,
        )

        damage = self._calculate_damage()
        target.at_damage(caller, damage, "blunt", "bash")


# region Riposte
class CmdRiposte(PowerCommand):
    """
    Riposte allows the knight to counterattack an enemy after successfully parrying their strike. The knight can use their agility and reflexes to quickly strike back at the enemy, dealing damage and punishing them for their attack. The effectiveness of the riposte is based on the knight's skill and dexterity.
    """

    key = "riposte"
    help_category = "knight"
    guild_level = 20
    cost = 0

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        super().func()

        if glvl < self.guild_level:
            caller.msg(
                f"|rYou must be at least level {self.guild_level} to use this power."
            )
            return

        if not caller.db.parrying:
            caller.msg(f"|rYou must be parrying to riposte.")
            return

        if not caller.cooldowns.ready("riposte"):
            caller.msg(f"|CNot so fast!")
            return False

        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.cooldowns.add("global_cooldown", 2)
        caller.cooldowns.add("riposte", 2)

        caller.msg(f"|gYou prepare to riposte the next attack.")
        caller.location.msg_contents(
            f"|C{caller.name} prepares to riposte the next attack, focusing $pron(your) energy on defense.",
            exclude=caller,
        )

        caller.db.riposting = True

    def _end_riposte(self, caller):
        caller.tags.remove("riposting", category="status")
        caller.location.msg_contents(
            f"|C$You() finish riposting the next attack, looking ready for action.",
            from_obj=caller,
        )
        caller.db.riposting = False


# region Dodge
class CmdDodge(PowerCommand):
    """
    Dodge allows the knight to evade incoming attacks with their agility and reflexes. The knight can use their agility to dodge and avoid enemy strikes, reducing the damage taken. The effectiveness of the dodge is based on the knight's skill and dexterity.
    """

    key = "dodge"
    help_category = "knight"
    guild_level = 7
    cost = 0

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        super().func()

        if glvl < self.guild_level:
            caller.msg(
                f"|rYou must be at least level {self.guild_level} to use this power."
            )
            return

        if caller.db.dodging:
            self._end_dodge(caller)
            return

        if not caller.cooldowns.ready("dodge"):
            caller.msg(f"|CNot so fast!")
            return False

        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.cooldowns.add("global_cooldown", 2)
        caller.cooldowns.add("dodge", 2)

        caller.msg(f"|gYou prepare to dodge incoming attacks.")
        caller.location.msg_contents(
            f"|C{caller.name} prepares to dodge incoming attacks, focusing $pron(your) energy on defense.",
            exclude=caller,
        )

        caller.db.dodging = True

    def _end_dodge(self, caller):
        caller.tags.remove("dodging", category="status")
        caller.location.msg_contents(
            f"|C$You() finish dodging incoming attacks, looking ready for action.",
            from_obj=caller,
        )
        caller.db.dodging = False


# region Parry
class CmdParry(PowerCommand):
    """
    Parry allows the knight to deflect incoming attacks with their weapon. The elemental can use their weapon to block and deflect enemy strikes, reducing the damage taken. The amount of damage reduced is based on the knight's dexterity.
    """

    key = "parry"
    aliases = ["pa"]
    help_category = "knight"
    guild_level = 5
    cost = 0

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        super().func()

        if glvl < self.guild_level:
            caller.msg(
                f"|rYou must be at least level {self.guild_level} to use this power."
            )
            return

        if caller.db.parrying:
            self._end_parry(caller)
            return

        if not caller.cooldowns.ready("parry"):
            caller.msg(f"|CNot so fast!")
            return False

        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.cooldowns.add("global_cooldown", 2)
        caller.cooldowns.add("parry", 2)

        caller.msg(f"|gYou prepare to parry incoming attacks.")
        caller.location.msg_contents(
            f"|C{caller.name} prepares to parry incoming attacks, focusing $pron(your) energy on defense.",
            exclude=caller,
        )

        caller.db.parrying = True

    def _end_parry(self, caller):
        caller.tags.remove("parrying", category="status")
        caller.location.msg_contents(
            f"|C$You() finish parrying incoming attacks, looking ready for action.",
            from_obj=caller,
        )
        caller.db.parrying = False


# region Bind Wounds
class CmdBindWounds(PowerCommand):
    """
    Bind Wounds allows the earth elemental to use their connection to the earth to heal themselves. The elemental can focus their energy to mend their wounds and restore health. The amount of health restored is based on the elemental's skill in earth resonance and wisdom.
    """

    key = "bind wounds"
    aliases = ["bw"]
    help_category = "knight"
    guild_level = 1
    cost = 0

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        super().func()

        if glvl < self.guild_level:
            caller.msg(
                f"|rYou must be at least level {self.guild_level} to use this power."
            )
            return
        if hppercent := caller.db.hp / caller.traits.hp.value * 100:
            if hppercent > 45:
                caller.msg(f"|rYou can't bandage any further.")
                return
        if caller.db.combat_target:
            caller.msg(f"|rYou can't bind your wounds while in combat.")
            return

        if not caller.cooldowns.ready("bind_wounds"):
            caller.msg(f"|CNot so fast!")
            return False

        # if not caller.cooldowns.ready("global_cooldown"):
        #     caller.msg(f"|CNot so fast!")
        #     return False

        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.cooldowns.add("global_cooldown", 6)
        caller.cooldowns.add("bind_wounds", 6)

        caller.msg(f"|gYou focus your energy and begin to bind your wounds.")
        caller.location.msg_contents(
            f"|C{caller.name} begins to bind $pron(your) wounds, focusing $pron(your) energy on healing.",
            exclude=caller,
        )

        caller.tags.add("binding wounds", category="status")
        delay(6, self._end_bind_wounds, caller, persistent=True)

    def _end_bind_wounds(self, caller):
        caller.tags.remove("binding wounds", category="status")
        caller.location.msg_contents(
            f"|C$You() finish binding $pron(your) wounds, looking refreshed and invigorated.",
            from_obj=caller,
        )
        caller.adjust_hp(10 + caller.db.glvl + caller.db.skills["bind wounds"])
        caller.msg(caller.get_display_status(caller))


# region Rest
class CmdMeditate(Command):
    """
    Meditate allows the knight to focus their energy and regain focus points. The knight can enter a meditative state, drawing on the power of their deity to replenish their energy reserves. The knight will be unable to move or take any actions while meditating.

    Health returned is based on constitution
    Focus returned is based on wisdom
    Energy returned is based on charisma

    Usage:
        meditate, med
    """

    key = "meditate"
    aliases = ["med"]
    help_category = "knight"
    guild_level = 9
    cost = 0

    def _end_meditation(self, caller):
        caller.tags.remove("meditating", category="status")
        caller.msg(
            f"|gYou feel refreshed and invigorated, the energy of the earth flowing through you."
        )
        caller.location.msg_contents(
            f"|C$You() open $pron(your) eyes and rise from $pron(your) meditative state, looking refreshed and invigorated.",
            from_obj=caller,
        )
        caller.msg(caller.get_display_status(caller))

        wis = caller.traits.wis.value
        con = caller.traits.con.value
        cha = caller.traits.cha.value

        hp_restored = int(uniform(3, con * 0.5)) + 5
        fp_restored = int(uniform(3, wis * 0.5)) + 5
        ep_restored = int(uniform(3, cha * 0.5)) + 5

        caller.adjust_hp(hp_restored)
        caller.adjust_fp(fp_restored)
        caller.adjust_ep(ep_restored)

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level

        if caller.db.combat_target:
            caller.msg(f"|rYou can't meditate while in combat.")
            return

        if not caller.cooldowns.ready("meditate"):
            caller.msg(f"|CNot so fast!")
            return False

        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False

        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.tags.add("meditating", category="status")
        caller.cooldowns.add("global_cooldown", 6)
        caller.cooldowns.add("meditate", 6)

        caller.msg(f"|gYou enter a meditative state, drawing energy from the earth.")
        caller.location.msg_contents(
            f"|C$You() close your eyes and begins to meditate, drawing energy from the earth.",
            from_obj=caller,
        )
        delay(6, self._end_meditation, caller)


# region Powers
class CmdPowers(Command):
    """
    List of powers available to the Knight, their rank, and their cost.

    Usage:
        powers

    """

    key = "powers"
    help_category = "knight"

    def func(self):
        caller = self.caller

        table = EvTable(f"|cPower", f"|cRank", f"|cCost", border="table")
        table.add_row(f"|GBind Wounds", 1, 0)
        table.add_row(f"|GParry", 5, 0)
        table.add_row(f"|GDodge", 7, 0)
        table.add_row(f"|GBash", 9, 0)
        table.add_row(f"|GMeditate", 9, 0)
        table.add_row(f"|GDouble Attack", 16, 0)
        table.add_row(f"|GRiposte", 20, 0)

        caller.msg(str(table))


# region Reaction
class CmdReaction(Command):
    """
    Set the elemental's reaction to a dropping below a certain health threshold.

    Usage:
        reaction <percentage>
    """

    key = "reaction"
    help_category = "knight"

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
    help_category = "knight"

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
                "|cKnights|n\n\n"
                "The Knights Guild is a group of elite warriors dedicated to protecting the realm and upholding justice. Knights are skilled in combat, diplomacy, and leadership, and are known for their courage, honor, and loyalty. Knights are trained in the use of weapons, armor, and martial arts, and are often called upon to defend the realm from threats both within and without. Knights are respected and admired for their bravery, skill, and dedication to the cause of justice."
            )
        if skill == "":
            caller.msg(
                "|cBind Wounds|n\n\n"
                "The Bind Wounds skill improves the knight's ability to heal themselves. The effectiveness of the Bind Wounds skill is based on this skill, their rank, and their Wisdom attribute. By binding their wounds, knights can recover health more quickly and efficiently out of combat."
            )
        if skill == "double attack":
            caller.msg(
                "|cDouble Attack|n\n\n"
                "The Double Attack skill allows the knight to make two attacks in a single round of combat. The effectiveness of the Double Attack skill is based on the knight's skill, their rank, and their Dexterity attribute. "
            )
        if skill == "dodge":
            caller.msg(
                "|cDodge|n\n\n"
                "The Dodge skill allows the knight to evade incoming attacks with their dexterity and reflexes. The knight can use their dexterity to dodge and avoid enemy strikes, reducing the damage taken. The effectiveness of the dodge is based on the knight's skill, rank, and dexterity."
            )
        if skill == "defense":
            caller.msg(
                "|cDefense|n\n\n"
                "The Defense skill allows the knight to increase their armor class and reduce the damage taken from incoming attacks. The knight can use their skill in defense to protect themselves from harm and withstand enemy attacks. The effectiveness of the defense skill is based on the knight's skill, rank, and constitution."
            )
        if skill == "offense":
            caller.msg(
                "|cOffense|n\n\n"
                "The Offense skill allows the knight to increase their attack bonus and deal more damage with their attacks. The knight can use their skill in offense to strike more effectively and defeat their enemies more quickly. The effectiveness of the offense skill is based on the knight's skill, rank, and strength."
            )
        if skill == "riposte":
            caller.msg(
                "|cRiposte|n\n\n"
                "The Riposte skill allows the knight to counterattack an enemy after successfully parrying their strike. The knight can use their dexterity and reflexes to quickly strike back at the enemy, dealing damage and punishing them for their attack. The effectiveness of the riposte is based on the knight's skill, rank, and dexterity."
            )
        if skill == "bash":
            caller.msg(
                "|cBash|n\n\n"
                "The Bash skill allows the knight to deliver a powerful blow to an enemy, stunning them and knocking them off balance. The knight can use their strength and weapon to deliver a crushing blow, disrupting the enemy's attacks and leaving them vulnerable to further attacks. The effectiveness of the bash is based on the knight's skill, rank, and strength."
            )
        if skill == "parry":
            caller.msg(
                "|cParry|n\n\n"
                "The Parry skill allows the knight to deflect incoming attacks with their weapon. The knight can use their weapon to block and deflect enemy strikes, reducing the damage taken. The amount of damage reduced is based on the knight's dexterity."
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

    help_category = "knight"
    key = "gadvance"
    aliases = "gadv"

    def _adv_level(self):
        caller = self.caller
        cost = get_glvl_cost(caller.db.guild_level + 1)

        if caller.db.gxp < cost:
            self.msg(f"|wYou need {cost - caller.db.gxp} more experience to advance.")
            return
        else:
            if caller.db.guild_level == 8 and caller.db.subguild is None:
                caller.msg(f"|rYou have to pick a subguild before advancing.")
                return

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
    help_category = "knight"

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
    help_category = "knight"

    def func(self):
        caller = self.caller

        table = EvTable(f"|cSkill", f"|cRank", f"|cCost", border="table")
        for skill, rank in caller.db.skills.items():
            table.add_row(f"|G{skill.title()}", f"{rank}", f"{SKILLS_COST[rank]}")

        caller.msg(str(table))


class CmdHp(Command):
    """
    Display the current and maximum health of the caller.

    Usage:
        hp
    """

    key = "hp"
    help_category = "knight"

    def func(self):
        caller = self.caller

        caller.msg(caller.get_display_status(caller))


# region CmdSet
class KnightCmdSet(CmdSet):
    key = "Knight CmdSet"

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
        self.add(CmdHp)
        self.add(CmdMeditate)
        self.add(CmdBindWounds)
        self.add(CmdParry)
        self.add(CmdDodge)
        self.add(CmdBash)
        self.add(CmdRiposte)
