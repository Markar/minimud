from random import randint, uniform
from evennia import CmdSet, search_tag
from evennia.utils import iter_to_str
from evennia.utils.evtable import EvTable
from evennia import TICKER_HANDLER as tickerhandler
from typeclasses.utils import get_article
from typeclasses.changelingguild.changeling_constants_and_helpers import (
    AVIAN_FORMS,
    GUILD_LEVEL_COST_DICT,
    MAMMAL_FORMS,
    REPTILE_FORMS,
    SKILLS_COST,
    SKILL_RANKS,
    TITLES,
)
import math
from .command import Command
from evennia.prototypes import spawner, prototypes


# region Morph
class CmdMorph(Command):
    """
    Morph into various things

    Usage:
    morph anole
    """

    key = "morph"
    help_category = "Changeling"

    def func(self):
        caller = self.caller
        form = self.args.strip().lower()
        try:
            my_glvl = caller.db.guild_level
            caller.db.ep -= my_glvl
            caller.adjust_hp(my_glvl)

            form_title = form.title()
            if form == "human":
                print(f"form = human and {caller.db.guild_level}")
                self.msg(f"|rYou morph into your human form!")
                caller.db.form = "Human"
                return
            if form == "slime":
                self.msg(f"|rYou morph into your slime form!")
                caller.db.form = "Slime"
                return

            reptile = next(
                (key for key, value in REPTILE_FORMS.items() if value == form), -1
            )
            if not reptile == -1 and my_glvl >= reptile:
                self.msg(f"|rYou morph into {get_article(form)} {form_title}!")
                caller.db.form = form_title
                return

            mammal = next(
                (key for key, value in MAMMAL_FORMS.items() if value == form), -1
            )
            if not mammal == -1 and my_glvl >= mammal:
                self.msg(f"|rYou morph into {get_article(form)} {form_title}!")
                caller.db.form = form_title
                return

            avian = next(
                (key for key, value in AVIAN_FORMS.items() if value == form), -1
            )
            if not avian == -1 and my_glvl >= avian:
                self.msg(f"|rYou morph into {get_article(form)} {form_title}!")
                caller.db.form = form_title
                return

            self.msg(f"|rYou can't morph into that.")
        except ValueError:
            print(f"You don't know how to use that form.")


# region EC
class CmdEnergyControl(Command):
    """
    Energy control is the Changeling's ability to manipulate the energy
    within their body.  This power allows the Changeling to bolster their
    defenses against physical attacks. This power costs 25 energy points
    to use and lasts until it is turned off or the Changeling runs out of
    energy. This power cannot be used while Energy Dissipation is active until
    both skills are at rank 5.

    Usage:
        energy control
    """

    key = "energy control"
    aliases = "ec"
    help_category = "Changeling"
    fp_cost = 25
    ep_cost = 25
    guild_level = 8

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        ed = caller.db.energy_dissipation
        ed_skill = caller.db.skills["energy_dissipation"]
        ec_skill = caller.db.skills["energy_control"]
        active = getattr(caller.db, "ec", {}).get("active", False)

        if glvl < self.guild_level:
            caller.msg(f"|rYou must be at least guild level 8 to use this power.")
            return

        if caller.db.fp < self.fp_cost:
            caller.msg(f"|rYou can't focus well enough to use this power.")
            return

        if caller.db.ep < self.ep_cost:
            caller.msg(f"|rYou don't have enough energy to use this power.")
            return

        if ed and ed_skill < 5 and ec_skill < 5:
            caller.msg(
                f"|rYou can't use this power while Energy Dissipation is active."
            )
            return

        if active:
            caller.msg(
                f"|MYou feel the energy receding, flowing back into your core. The crackling sounds of the barrier fade away, and the protective shield dissolves into the air."
            )
            self.msg(f"active2: {active}")
            setattr(caller.db, "ec", {"active": False, "duration": 0})
            return
        else:
            caller.msg(
                f"|MAs you focus your mind, a surge of energy begins to flow through your body. You raise your hands, and a shimmering barrier of pure energy forms around you, crackling with power."
            )
            dur = (glvl * 3) + 80 + randint(0, 90) + (ec_skill * 2)
            dur = dur / 3  # 6s rounds, 3k had 2s, so divide by 3
            setattr(caller.db, "ec", {"active": True, "duration": dur})
            caller.adjust_fp(-self.fp_cost)
            caller.adjust_ep(-self.ep_cost)
            return


# region ED
class CmdEnergyDissipation(Command):
    """
    Energy Dissipation is the Changeling's ability to manipulate the energy
    within their body.  This power allows the Changeling to bolster their
    defenses against non-physical attacks. This power costs 25 energy points
    to use and lasts until it is turned off or the Changeling runs out of
    energy. This power cannot be used while Energy Control is active until
    both skills are at rank 5.

    Usage:
        energy dissipation
    """

    key = "energy dissipation"
    aliases = "ed"
    help_category = "Changeling"
    fp_cost = 180
    ep_cost = 45
    guild_level = 18

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        ed_skill = caller.db.skills["energy_dissipation"]
        ec_skill = caller.db.skills["energy_control"]
        duration = (glvl * 3) + 90 + randint(0, 90)
        duration = duration / 3  # 6s rounds, 3k had 2s, so divide by 3
        ec_active = getattr(caller.db, "ec", {}).get("active", False)
        ed_active = getattr(caller.db, "ed", {}).get("active", False)

        if glvl < self.guild_level:
            caller.msg(
                f"|rYou must be at least guild level {self.guild_level} to use this power."
            )
            return

        if caller.db.fp < self.fp_cost:
            caller.msg(f"|rYou can't focus well enough to use this power.")
            return

        if caller.db.ep < self.ep_cost:
            caller.msg(f"|rYou don't have enough energy to use this power.")
            return

        if ec_active and ec_skill < 5 and ed_skill < 5:
            caller.msg(
                f"|rYou can't use this power while Energy Control is active yet."
            )
            return

        if ed_active:
            caller.msg(
                f"|MYou feel the energy receding, flowing back into your core. The crackling sounds of the barrier fade away, and the protective shield dissolves into the air."
            )
            setattr(caller.db, "ed", {"active": False, "duration": 0})
            return
        else:
            caller.msg(
                f"|MAs you focus your mind, a surge of energy begins to flow through your body. You raise your hands, and a shimmering barrier of pure energy forms around you, crackling with power."
            )
            setattr(caller.db, "ed", {"active": True, "duration": duration})
            caller.adjust_fp(-self.fp_cost)
            caller.adjust_ep(-self.ep_cost)
            return


# region Engulf
class CmdEngulf(Command):
    """
    Engulf is the Changeling's Super Power.  You only get a limited
    number of them per time, rather than having them cost stamina.

    Engulf causes you to enclose the targets entire body within
    your plasmic form, once enclosed you drain their life energy
    away from them, this does severe damage to them and heals
    you greatly.  After engulfing, you are unable to move (or quit) for
    up to 5 rounds, so be careful.

    You may not engulf a creature if you are above full health or focus.

    Usage:
        engulf
    """

    key = "engulf"
    aliases = "eg"
    help_category = "changeling"
    guild_level = 7
    cost = 10

    def func(self):
        print(self.caller)
        caller = self.caller
        target = caller.search(caller.db.combat_target)
        glvl = caller.db.guild_level
        hp = caller.db.hp
        hpmax = caller.db.hpmax
        fp = caller.db.fp
        fpmax = caller.db.fpmax

        if caller.db.engulfs < 1:
            caller.msg(f"|rYou do not have the strength to engulf at this time.\n")
            return
        if hp > hpmax or fp > fpmax:
            caller.msg(f"|rYou may not engulf a creature at this time.\n")
            return

        if not caller.cooldowns.ready("engulf"):
            caller.msg(f"|rYou can't use this power yet.")
            return

        if glvl < self.guild_level:
            caller.msg(f"|rYou must be at least guild level 7 to use this power.")
            return

        if not target:
            target = caller.search(self.args)
            if not target:
                caller.msg("|rEngulf who?")
                return
            target.enter_combat(caller)
            caller.enter_combat(target)

        if caller.db.ep < self.cost:
            self.msg(f"|rYou don't have enough energy to use this power.")
            return

        power = math.ceil(caller.db.hpmax * (9 + caller.db.guild_level / 7) / 10)
        fpower = math.ceil(caller.db.fpmax * (9 + caller.db.guild_level / 7) / 10)
        caller.db.hp += power
        caller.db.fp += fpower
        caller.adjust_ep(-self.cost)
        caller.db.engulfs -= 1
        caller.cooldowns.add("engulf", 5)
        caller.cooldowns.add("global_cooldown", 2)

        caller.location.msg_contents(
            f"|M{caller} flows around {target} completely enclosing them in plasma!",
            exclude=[caller, target],
        )
        caller.msg(f"|rYou flow around {target} completely enclosing them in plasma!")
        target.msg(f"|r{caller} flows around you completely enclosing you in plasma!")

        target.at_damage(caller, power, "acid", "engulf")


# region Forms
class CmdForms(Command):
    """
    List of forms available to the Changeling, their guild level
    requirement, and their description.

    Usage:
    forms
    forms <form>, - forms hummingbird
    """

    key = "forms"
    help_category = "Changeling"

    def func(self):
        caller = self.caller
        form = self.args.strip().lower()

        if (
            form in REPTILE_FORMS.values()
            or form in MAMMAL_FORMS.values()
            or form in AVIAN_FORMS.values()
        ):
            form_desc = caller.get_form_help(form)
            caller.msg(f"|G{form_desc}")
            return

        my_glvl = caller.db.guild_level

        table = EvTable(
            f"|cAvian", f"|cMammal", f"|cReptile", f"|cGlvl", border="table"
        )
        for glvl in REPTILE_FORMS:
            if my_glvl >= glvl:
                table.add_row(
                    f"|Y{AVIAN_FORMS[glvl]}",
                    f"|Y{MAMMAL_FORMS[glvl]}",
                    f"|Y{REPTILE_FORMS[glvl]}",
                    glvl,
                )
            else:
                table.add_row(
                    f"|G{AVIAN_FORMS[glvl]}",
                    f"|G{MAMMAL_FORMS[glvl]}",
                    f"|G{REPTILE_FORMS[glvl]}",
                    glvl,
                )
        table.add_row("", "", "", "")
        table.add_row(f"|Yslime", f"|Yhuman", "", 1)

        caller.msg(str(table))


# region Powers
class CmdPowers(Command):
    """
    List of powers available to the Changeling, their rank, and their cost.

    Usage:
        powers

    """

    key = "powers"
    help_category = "Changeling"

    def func(self):
        caller = self.caller

        table = EvTable(f"|cPower", f"|cRank", f"|cEnergy", f"|cFocus", border="table")
        table.add_row(f"|GAbsorb", 1, 0, 0)
        table.add_row(f"|GCellular Regrowth", 3, 25, 25)
        table.add_row(f"|GDrain", 6, 15, 0)
        table.add_row(f"|GEngulf", 7, 0, 0)
        table.add_row(f"|GEnergy Control", 8, 25, 20)
        table.add_row(f"|GCellular Reconstruction", 9, 25, 50)
        table.add_row(f"|GBody Control", 12, 50, 180)
        table.add_row(f"|GEnergy Dissipation", 15, 45, 180)

        caller.msg(str(table))


# region Gtrain
class CmdGTrain(Command):
    """
    Train your guild skills by spending skill experience points. Each rank
    increases your effectiveness in that skill.

    Usage:
        gtrain <skill>

    Example:
        gtrain body_control
    """

    key = "gtrain"
    help_category = "Changeling"

    def func(self):
        caller = self.caller
        skill = self.args.strip().lower()
        list = ["body_control", "drain", "energy_control", "regeneration"]

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

    help_category = "Changeling"
    key = "gadvance"
    aliases = "gadv"

    def _adv_level(self):
        print(f"adv level {self} and caller: {self.caller}")
        caller = self.caller
        cost = GUILD_LEVEL_COST_DICT.get(caller.db.guild_level + 1, 0)

        if caller.db.gxp < cost:
            self.msg(f"|wYou need {cost - caller.db.gxp} more experience to advance.")
            return
        else:
            caller.db.gxp -= cost
            caller.db.guild_level += 1
            caller.db.epmax += 10

        if caller.db.guild_level >= 7:
            caller.db.max_engulfs = 1
        if caller.db.guild_level >= 14:
            caller.db.max_engulfs = 2
        if caller.db.guild_level >= 21:
            caller.db.max_engulfs = 3
        if caller.db.guild_level >= 30:
            caller.db.max_engulfs = 4

    def func(self):
        caller = self.caller
        caller.msg(f"|G{caller}")
        print(f"in advance function")

        self._adv_level()
        title = TITLES[caller.db.guild_level]
        caller.db.title = title
        self.msg(f"|rYou become {title} {caller.db.guild_level}.")


# region Ghelp
class CmdGHelp(Command):
    """
    Display help for the Changeling guild.

    Usage:
        ghelp
    """

    key = "ghelp"
    help_category = "Changeling"

    def func(self):
        caller = self.caller
        file = self.args.strip().lower()

        if file == "":
            caller.msg(
                "|wYou can get help on the following topics: "
                "|rbody control skill, drain skill, energy control skill, regeneration skill"
            )
            return
        if file == "body control skill":
            caller.msg(
                "|wBody Control allows you to control your body in ways that are not normally possible. This skill is improves your ability to boost your physical attributes."
            )
            return
        if file == "drain skill":
            caller.msg(
                "|wDrain allows you to drain the life energy from your enemies, creating a capsule.  This skill improves the effectiveness of your drain ability."
            )
        if file == "energy control skill":
            caller.msg(
                "|wEnergy Control allows you to manipulate the energy within your body. This skill improves your energy control and energy dissipation abilities."
            )
        if file == "regeneration skill":
            caller.msg(
                "|wRegeneration allows you to regenerate lost cells, but it takes time and energy to do so.  This skill improves cellular regrowth and cellular reconstruction abilities."
            )


# region BC
class CmdBodyControl(Command):
    """
    Body Control allows you to control your body in ways that are not normally possible. This power allows you to boost one physical attribute at the cost of another. The first argument is the attribute you want to boost, the second is the attribute you want to lower.  The amount of the boost is determined by your skill level in Body Control. Attributes include strength, dexterity, and constitution.

    Usage:
        body control str dex
    """

    key = "body control"
    help_category = "Changeling"
    aliases = "bc"
    ep_cost = 50
    fp_cost = 180
    guild_level = 12  # 35

    def func(self):
        caller = self.caller
        skill = caller.db.skills.get("body_control", 1)
        args = self.args.split()
        active = caller.db.body_control.get("active", False)
        boosted = caller.db.body_control.get("boosted", "str")
        nerfed = caller.db.body_control.get("nerfed", "dex")
        amount = caller.db.body_control.get("amount", 0)
        caller.traits.str.mod = 0
        caller.traits.dex.mod = 0

        if args == ["off"] and active:
            caller.db.body_control = {
                "active": False,
                "boosted": "none",
                "nerfed": "none",
                "amount": 0,
            }

            caller.traits[boosted].mod -= amount
            caller.traits[nerfed].mod += amount

            deactivateMsg = f"|yYou deactivate Body Control, lowering your {caller.db.arg1} and boosting your {caller.db.arg2}."
            caller.location.msg_contents(deactivateMsg, from_obj=caller)
            return

        if len(args) != 2:
            caller.msg(
                "You need to provide exactly two arguments. body control str dex"
            )
            return

        arg1, arg2 = args

        if caller.db.ep < self.ep_cost:
            caller.msg("You don't have enough energy to use this power.")
            return

        if caller.db.fp < self.fp_cost:
            caller.msg("You can't focus well enough to use this power.")
            return

        if caller.db.guild_level < self.guild_level:
            caller.msg("You must be at least guild level 12 to use this power.")
            return

        if arg1 == arg2:
            caller.msg("You must provide two different arguments.")
            return

        if active and args:
            caller.msg("You already have Body Control active.")
            return

        if not active and not args:
            caller.msg("You need to provide two arguments.")
            return

        # this one has to go after the active and not args block or it will fail early
        if arg1 not in ["str", "dex", "con"] or arg2 not in ["str", "dex", "con"]:
            caller.msg("You must provide valid arguments.")
            return

        caller.traits[arg1].mod += skill
        caller.traits[arg2].mod -= skill
        caller.db.body_control = {
            "active": True,
            "boosted": arg1,
            "nerfed": arg2,
            "amount": skill,
        }
        caller.db.ep -= self.ep_cost
        caller.db.fp -= self.fp_cost

        activateMsg = f"|yYou activate Body Control, boosting your {arg1} and lowering your {arg2}."
        caller.location.msg_contents(activateMsg, from_obj=caller)


# region StatSheet
class CmdGuildStatSheet(Command):
    """
    View your character's current stats.
    """

    key = "gscore"
    aliases = "gs"
    help_category = "Changeling"

    def func(self):
        caller = self.caller
        title = caller.db.title
        alignment = caller.db.alignment
        my_glvl = caller.db.guild_level or 1
        gxp = caller.db.gxp or 0
        skill_gxp = caller.db.skill_gxp or 0
        form = caller.db.form or "none"
        gxp_needed = GUILD_LEVEL_COST_DICT[my_glvl + 1]
        ec = getattr(caller.db, "ec", {}).get("active", False)
        ed = caller.db.energy_dissipation or "none"
        engulfs = caller.db.engulfs or 0
        engulfMax = caller.db.max_engulfs or 0
        bc = caller.db.body_control or "none"

        if ec == True:
            ecActive = "Active"
        else:
            ecActive = "Inactive"
        cg = caller.db.regrowth or "none"

        if cg == True:
            cgActive = "Active"
        else:
            cgActive = "Inactive"

        if bc == True:
            bcActive = "Active"
        else:
            bcActive = "Inactive"

        if ed == True:
            edActive = "Active"
        else:
            edActive = "Inactive"

        table = EvTable(f"|c{caller} {title} ({alignment})", border="table")
        table.add_row(f"|GGuild Level: {my_glvl}")
        table.add_row(f"|GGXP: {gxp} / {gxp_needed}")
        table.add_row(f"|GSkill GXP: {skill_gxp}")
        table.add_row(f"|GEngulfs: {engulfs} / {engulfMax}")
        table.add_row(f"|GForm: {form}")
        table.add_row(f"|GEnergy Control: {ecActive}")
        table.add_row(f"|GEnergy Dissipation: {edActive}")
        table.add_row(f"|GCellular Regrowth: {cgActive}")
        table.add_row(f"|GBody Control: {bcActive}")

        skill_table = EvTable(f"|cSkills", f"|cCost", f"|cRank", border="table")
        body_control = caller.db.skills["body_control"]
        drain = caller.db.skills["drain"]
        energy_control = caller.db.skills["energy_control"]
        regeneration = caller.db.skills["regeneration"]
        ed = caller.db.skills["energy_dissipation"]

        body_control_cost = SKILLS_COST[body_control]
        drain_cost = SKILLS_COST[drain]
        energy_control_cost = SKILLS_COST[energy_control]
        ed_cost = SKILLS_COST[ed]
        regeneration_cost = SKILLS_COST[regeneration]

        skill_table.add_row(
            f"|GBody Control",
            f"|M{body_control_cost}",
            f"|Y{SKILL_RANKS[body_control]}",
        )
        skill_table.add_row(f"|GDrain", f"|M{drain_cost}", f"|Y{SKILL_RANKS[drain]}")
        skill_table.add_row(
            f"|GEnergy Control",
            f"|M{energy_control_cost}",
            f"|Y{SKILL_RANKS[energy_control]}",
        )
        skill_table.add_row(
            f"|GEnergy Dissipation",
            f"|M{ed_cost}",
            f"|Y{SKILL_RANKS[ed]}",
        )
        skill_table.add_row(
            f"|GRegeneration",
            f"|M{regeneration_cost}",
            f"|Y{SKILL_RANKS[regeneration]}",
        )

        caller.msg(str(table))
        caller.msg(str(skill_table))


# region Join
class CmdJoinChangelings(Command):
    """
    Join the Changeling guild
    """

    key = "join changelings"

    def func(self):
        caller = self.caller
        if caller.db.guild == "adventurer":
            caller.msg(f"|rYou join the Changeling guild")
            caller.swap_typeclass("typeclasses.changelings.Changelings")
        else:
            caller.msg(f"|rYou are already in a guild")


# region Leave
class CmdLeaveChangelings(Command):
    """
    Leave the Elementals guild
    """

    key = "leave changelings"

    def func(self):
        caller = self.caller
        if caller.db.guild == "changeling":
            caller.db.guild = "adventurer"
            caller.db.guild_level = 1
            caller.db.gxp = 0
            caller.db.subguild = "none"
            del caller.db.skills
            del caller.db.form
            del caller.db.ec
            del caller.db.ed
            del caller.db.body_control
            del caller.db.regrowth_rate
            del caller.db.regrowth_cost
            del caller.db.engulfs
            del caller.db.max_engulfs

            try:
                tickerhandler.remove(
                    interval=6,
                    callback=caller.at_tick,
                    idstring=f"{caller}-regen",
                    persistent=True,
                )
                tickerhandler.remove(
                    interval=60 * 5,
                    callback=caller.at_engulf_tick,
                    idstring=f"{caller}-superpower",
                    persistent=True,
                )
            except ValueError:
                print(f"tickerhandler.remove failed")

            caller.cmdset.delete(ChangelingCmdSet)
            caller.swap_typeclass("typeclasses.characters.PlayerCharacter")
            caller.msg(f"|rYou leave the Changeling guild")
        else:
            caller.msg(f"|rYou are already an adventurer")


# region Kickstart
class CmdKickstart(Command):
    key = "kickstart"

    def func(self):
        caller = self.caller
        caller.kickstart()


# region Absorb
class CmdAbsorb(Command):
    """
    The corpse of a freshly slain enemy is a rich source of cellular
    material, which can easily be absorbed and converted into protoplasm
    and stamina, serving to replenish some, or all that you may have lost.

    If you so choose, you may also 'fully' absorb the corpse, leaving
    nothing left to decay.

    Usage:
        absorb
        ab
    """

    key = "absorb"
    aliases = "ab"
    help_category = "Changeling"

    def func(self):
        if not self.args:
            target = self.caller
            if corpse := target.location.search("corpse-1"):
                ep = target.db.ep
                epmax = target.db.epmax
                power = corpse.db.power or 0

                if ep + power > epmax:
                    target.db.ep = epmax
                else:
                    target.db.ep += max(power, 0)
                corpse.delete()
                self.msg(
                    f"|yYou absorb the corpse and feel its inner power flow through you."
                )


# region Drain
class CmdDrain(Command):
    """
    Just as it is able to 'feed' upon a corpse to revitalize its stamina,
    the morph is able to 'drain' a corpse of its soul and vital energies
    that are unaccessable to any other creature.  By concentrating on
    draining the corpse, the morph can create a small pellet which may be
    consumed, transferring the vital energies from the corpse to the morph,
    increasing the morph's health.

    Usage:
        drain
        dr
    """

    key = "drain"
    aliases = "dr"
    help_category = "Changeling"
    ep_cost = 15

    def func(self):
        caller = self.caller
        args = self.args.strip().lower()
        drain = caller.db.skills["drain"]
        glvl = caller.db.guild_level

        if not args:
            target = self.caller
            if caller.db.ep < self.ep_cost:
                self.msg(f"|rYou don't have enough energy to use this power.")
                return
            if corpse := target.location.search("corpse-1"):
                mob_level = corpse.db.power / 8

                if drain < 5:
                    power = uniform(0, (drain * 1.5) + randint(0, drain * 2) + glvl / 2)
                    power = int(power + mob_level * 2)
                    if mob_level > 9:
                        power += 5
                    if mob_level > 19:
                        power += 5
                    if mob_level > 29:
                        power += 5
                else:
                    power = (
                        (glvl * drain / 3)
                        + randint(0, drain * 2)
                        + randint(0, drain * 2)
                        + glvl / 2
                    )

                capsule = {
                    "key": f"|Ya glowing capsule {power}",
                    "tags": ["edible"],
                    "typeclass": "typeclasses.corpse.Capsule",
                    "desc": f"|YA glowing capsule. It looks heavy, and full of nutrients.|n",
                    "location": caller.location,
                    "power": power,
                }

                capsule = spawner.spawn(capsule)
                corpse.delete()
                caller.location.msg_contents(
                    f"|M{caller} drains the corpse and creates a glowing capsule."
                )
            else:
                self.msg(f"|rThere is no corpse here to drain.")
                return


# region CellRecon
class CmdCellularReconstruction(Command):
    """
    The Changeling's ability to regenerate is a powerful one, but it
    is not without its limits.  The Changeling can regenerate lost
    cells, but it takes time and energy to do so.

    Usage:
        cellular reconstruction
        cr
        recon
    """

    help_category = "Changeling"
    key = "cellular reconstruction"
    aliases = ("cr", "recon")
    epcost = 25
    fpcost = 50
    guild_level = 9

    def func(self):
        caller = self.caller
        gl = caller.db.guild_level
        if not caller.cooldowns.ready("reconstruction"):
            self.msg(f"|rYou are already reconstructing your cells!")
            return
        if gl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return
        if caller.db.ep < self.epcost:
            self.msg(f"|rYou don't have enough energy to use this power.")
            return
        if caller.db.fp < self.fpcost:
            self.msg(f"|rYou can't focus well enough to use this power.")
            return
        if not caller.cooldowns.ready("reconstruction"):
            self.msg(f"|rYou can't use this power yet.")
            return
        if caller.db.hp == caller.db.hpmax:
            self.msg(f"|rYou are already at full health.")
            return

        regen = caller.db.skills["regeneration"]
        regen_bonus = randint(0, regen * 5)
        to_heal = math.floor(
            30 + gl / 2 + randint(0, caller.traits.wis.value) + regen_bonus
        )
        caller.cooldowns.add("reconstruction", 6)

        caller.adjust_hp(to_heal)
        caller.adjust_ep(-self.epcost)
        caller.db.fp -= self.fpcost  # not working with overmax?
        caller.msg(
            f"|yYou concentrate on your cells and new ones begin to grow and form."
        )


# region CellRegrow
class CmdCellularRegrowth(Command):
    """
    The Changeling's ability to regenerate is a powerful one, but it
    is not without its limits.  The Changeling can regenerate lost
    cells, but it takes time and energy to do so.  The Changeling
    can regenerate up to 10% of their maximum health every 6 seconds.
    This power costs 25 energy points and focus to use and then additional
    energy to sustain the regeneration.

    Usage:
        cellular regrowth
    """

    help_category = "Changeling"
    key = "cellular regrowth"
    aliases = ("regrowth", "cg")
    cost = 25
    guild_level = 3

    def func(self):
        caller = self.caller
        gl = caller.db.guild_level
        if getattr(caller.db, "regrowth", True):
            setattr(caller.db, "regrowth", False)
            caller.msg(f"|rYou stop regenerating.")
            return
        if gl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return
        if caller.db.ep < self.cost:
            self.msg(f"|rYou don't have enough energy to use this power.")
            return

        # cost to activate
        caller.adjust_ep(-self.cost)
        caller.adjust_fp(-self.cost)
        setattr(caller.db, "regrowth", True)

        caller.msg(f"|yYou begin to reconstruct your lost cells.")


# region Hp
class CmdHp(Command):
    """
    Display the current and maximum health of the caller.

    Usage:
        hp
    """

    key = "hp"
    help_category = "changeling"

    def func(self):
        caller = self.caller

        caller.msg(caller.get_display_status(caller))


# region Test
class CmdTest(Command):
    key = "test"

    def func(self):
        caller = self.caller
        caller.msg("test")

        tagged = search_tag(key="player", category="type")
        for x in tagged:
            x.db.best_kill = {"name": "none", "level": 0, "xp": 0}

        caller.msg("done")


# region CmdSet
class ChangelingCmdSet(CmdSet):
    key = "Changeling CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        self.add(CmdAbsorb)
        self.add(CmdGAdvance)
        self.add(CmdGuildStatSheet)
        self.add(CmdMorph)
        self.add(CmdEnergyControl)
        self.add(CmdEnergyDissipation)
        self.add(CmdEngulf)
        self.add(CmdForms)
        self.add(CmdTest)
        self.add(CmdKickstart)
        self.add(CmdCellularReconstruction)
        self.add(CmdCellularRegrowth)
        self.add(CmdGTrain)
        self.add(CmdPowers)
        self.add(CmdHp)
        self.add(CmdGHelp)
        self.add(CmdBodyControl)
        self.add(CmdDrain)
