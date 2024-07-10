from random import choice
from evennia import CmdSet
from evennia.utils import iter_to_str
from evennia.utils.evtable import EvTable

from .command import Command

GUILD_LEVEL_COST_DICT = {
    2: 10,
    3: 20,
    4: 30,
    5: 40,
    6: 50,
    7: 60,
    8: 70,
    9: 80,
    10: 90,
    11: 100,
    12: 10000,
    13: 12900,
    14: 16000,
    15: 22500,
    16: 32000,
    17: 47000,
    18: 67000,
    19: 90000,
    20: 120000,
    21: 160000,
    22: 220000,
    23: 295000,
    24: 445000,
    25: 675000,
    26: 950000,
    27: 1300000,
    28: 1900000,
    29: 2900000,
    30: 4200000 
}

class CmdRebuild(Command):
    """
    Restores health

    Usage:
        rebuild
    """

    key = "rebuild"
    help_category = "combat"

    def func(self):
        print(self.caller)
        caller = self.caller
        caller.use_rebuild()


class CmdEmit(Command):
    """
    Changes your emit level

    Usage:
        emit 1
        emit 2
    """

    key = "emit"
    help_category = "combat"

    def func(self):
        caller = self.caller
        
        try:
            print(f"emit: args {self.args}")
            print(f"emit: {self.caller}")
            power = int(self.args.strip())
            if power == 1 and caller.db.guild_level > 0:
                print(f"power = 1, caller.db.guild_level {power} and {caller.db.guild_level}")
                caller.db.emit = 1
                self.msg(f"|rYou set your emit to power level {power}")
            if power == 2 and caller.db.guild_level > 1:
                print(f"power = 2, caller.db.guild_level {power} and {caller.db.guild_level}")
                caller.db.emit = 2
            self.msg(f"|rYou set your emit to power level {caller.db.emit}")
        except ValueError:
            print(f"Not an integer for use_emit")
        
        
        
    def use_emit(self):
        print(f"args: {self.args.strip()}")
        try:
            power = int(self.args.strip())
            if power == 1 and self.db.guild_level > 0:
                self.db.emit = 1
            if power == 2 and self.db.guild_level > 1:
                self.db.emit = 2
        except ValueError:
            print(f"Not an integer for use_emit")

class CmdGAdvance(Command):
    """
    Advance a level or attribute by spending experience points.

    Enter "advance" to see what you can learn.

    Usage:
        gadvance

    Example:
        gadvance
    """

    key = "gadvance"
    aliases = ("gadv")

    def _adv_level(self):
        print(f"adv level {self} and caller: {self.caller}")
        caller = self.caller
        cost = GUILD_LEVEL_COST_DICT[caller.db.guild_level+1]
        if caller.db.gxp < cost:
            self.msg(f"|wYou need {cost - caller.db.gxp} more experience to advance.")
            return
        else:
            caller.db.gxp -= cost
            caller.db.guild_level += 1
            self.msg(f"|rYou grow more powerful.")
            
            
        
        
    def func(self):
        caller = self.caller
        caller.msg(f"|G{caller}")
        print(f"in advance function")

        self._adv_level()
        print(f"after _adv_level {caller.db.gxp}")

class CmdGuildStatSheet(Command):
    """
    View your character's current stats.
    """

    key = "gscore"
    aliases = ("gs")

    def func(self):
        caller = self.caller
        self.msg(f"|g{caller} {caller.db.title} ({caller.db.alignment})")
        self.msg(f"|GGuild Level: {caller.db.guild_level or 0}")
        self.msg(f"|GGXP: {caller.db.gxp or 0}\n")
        self.msg(f"|GEmit: {caller.db.emit or 0}\n")
        
class ElementalCmdSet(CmdSet):
    key = "Elemental CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        # self.add(CmdFireball)
        self.add(CmdRebuild)
        self.add(CmdGAdvance)
        self.add(CmdEmit)
        self.add(CmdGuildStatSheet)










            

        

  
        
class CmdTrainSkill(Command):
    """
    Improve a skill, based on how much experience you have.

    Enter just "train" by itself to see what you can learn here.

    Usage:
        train <levels>

    Example:
        train 5
    """

    key = "train"

    def _calc_exp(self, start, increase):
        """
        Calculates the experience cost for increasing your skill from the start level.
        """
        return int((start + (start + increase)) * (increase + 1) / 2.0)

    def func(self):
        if not self.obj:
            self.msg("You cannot train skills here.")
            return
        if not (to_train := self.obj.db.skill_training):
            self.msg("You cannot train any skills here.")
            return

        # make sure this is actually a valid skill
        if to_train not in SKILL_DICT:
            self.msg("You cannot train any skills here.")
            return

        if not self.args:
            self.msg(f"You can improve your |w{to_train}|n here.")
            return

        caller = self.caller

        try:
            levels = int(self.args.strip())
        except ValueError:
            self.msg("Usage: train <levels>")
            return

        if not (caller_xp := caller.db.exp):
            self.msg("You do not have any experience.")
            return

        if not (skill := caller.traits.get(to_train)):
            exp_cost = self._calc_exp(0, levels)
            if caller_xp < exp_cost:
                self.msg(
                    f"You do not have enough experience - you need {exp_cost} to learn {levels} levels of {to_train}."
                )
                return

            confirm = yield (
                f"It will cost you {exp_cost} experience to learn {to_train} up to level {levels}. Confirm? Yes/No"
            )
            if confirm.lower() not in (
                "yes",
                "y",
            ):
                self.msg("Cancelled.")
                return
            caller.traits.add(
                to_train,
                trait_type="counter",
                min=0,
                max=100,
                base=0,
                stat=SKILL_DICT.get(to_train),
            )
            skill = caller.traits.get(to_train)
        else:
            exp_cost = self._calc_exp(skill.base, levels)
            if caller_xp < exp_cost:
                self.msg(
                    f"You do not have enough experience - you need {exp_cost} experience to increase your {to_train} by {levels} levels."
                )
                return
            confirm = yield (
                f"It will cost you {exp_cost} experience to improve your {to_train} by {levels} levels. Confirm? Yes/No"
            )
            if confirm.lower() not in (
                "yes",
                "y",
            ):
                self.msg("Cancelled.")
                return

        caller.db.exp -= exp_cost
        skill.base += levels
        self.msg(f"You practice your {to_train} and improve it to level {skill.base}.")


# class TrainCmdSet(CmdSet):
#     key = "Train CmdSet"

#     def at_cmdset_creation(self):
#         super().at_cmdset_creation()
#         self.add(CmdTrainSkill)


# class SkillCmdSet(CmdSet):
#     key = "Skill CmdSet"

#     def at_cmdset_creation(self):
#         super().at_cmdset_creation()
#         self.add(CmdStatSheet)

# class AdvanceCmdSet(CmdSet):
#     key = "Advance CmdSet"

#     def at_cmdset_creation(self):
#         super().at_cmdset_creation()
#         self.add(CmdGAdvance)

# class AdvanceCmdSet(CmdSet):
#     key = "Advance CmdSet"

#     def at_cmdset_creation(self):
#         super().at_cmdset_creation()
#         self.add(CmdEmit)
        