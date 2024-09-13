from evennia import CmdSet
from evennia.utils.evtable import EvTable
from .command import Command

# A dict of all skills, with their associated stat as the value
SKILL_DICT = {
    "smithing": "strength",
    "tailoring": "dexterity",
    "evasion": "dexterity",
    "daggers": "dexterity",
    "swords": "strength",
    "cooking": "wisdom",
}

STAT_DICT = {
    "level": "level",
    "str": "strength",
    "dex": "dexterity",
    "int": "intelligence",
    "wis": "wisdom",
    "con": "constitution",
    "cha": "charisma",
}

STAT_COST_DICT = {
    1: 30,
    2: 34,
    3: 42,
    4: 57,
    5: 78,
    6: 106,
    7: 145,
    8: 195,
    9: 271,
    10: 371,
    11: 508,
    12: 695,
    13: 952,
    14: 1304,
    15: 1760,
    16: 2376,
    17: 3208,
    18: 4331,
    19: 5847,
    20: 7893,
    21: 10656,
    22: 14386,
    23: 19421,
    24: 26218,
    25: 35395,
    26: 47784,
    27: 64508,
    28: 87086,
    29: 117566,
    30: 158714,
    31: 214265,
    32: 289000,
    33: 390000,
    34: 526000,
    35: 710000,
    36: 960000,
    37: 1300000,
    38: 1760000,
    39: 2380000,
    40: 3220000,
    41: 4350000,
    42: 5880000,
    43: 7040000,
    44: 7740000,
    45: int(7740000 * 1.1),
    46: int(8514000 * 1.1),
    47: int(9365400 * 1.1),
    48: int(10301940 * 1.1),
    49: int(11332134 * 1.1),
    50: int(12465347 * 1.1),
    51: int(13711881 * 1.1),
    52: int(15083069 * 1.1),
    53: int(16591376 * 1.1),
    54: int(18250513 * 1.1),
    55: int(20075564 * 1.1),
    56: int(22083120 * 1.1),
    57: int(24291432 * 1.1),
    58: int(26720575 * 1.1),
    59: int(29392432 * 1.1),
    60: int(32331775 * 1.1),
    61: int(35565752 * 1.1),
    62: int(39124427 * 1.1),
    63: int(43040970 * 1.1),
    64: int(47352267 * 1.1),
    65: int(52199093 * 1.1),
    66: int(57626402 * 1.1),
    67: int(63683942 * 1.1),
    68: int(70426436 * 1.1),
    69: int(77914280 * 1.1),
    70: int(86214708 * 1.1),
    71: int(95401179 * 1.1),
    72: int(105554297 * 1.1),
    73: int(116109726 * 1.1),
    74: int(127720698 * 1.1),
    75: int(140492768 * 1.1),
    76: int(154541045 * 1.1),
    77: int(170095149 * 1.1),
    78: int(187354663 * 1.1),
    79: int(206576129 * 1.1),
    80: int(228060742 * 1.1),
    81: int(252166816 * 1.1),
}
# self.msg(sum(STAT_COST_DICT.values()))
# 2,936,390,438


LEVEL_COST_DICT = {
    2: 300,
    3: 400,
    4: 648,
    5: 951,
    6: 1529,
    7: 2409,
    8: 3330,
    9: 4645,
    10: 6000,
    11: 7500,
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
    30: 4200000,
    31: 6058451,
    32: 6876946,
    33: 7982402,
    34: 9214443,
    35: 10583019,
    36: 12098644,
    37: 13814400,
    38: 15730400,
    39: 17846600,
    40: 20163000,
    41: 22679600,
    42: 25396400,
    43: 28313400,
    44: 31430600,
    45: 34748000,
    46: 38265600,
    47: 41983400,
    48: 45901400,
    49: 50019600,
    50: 54338000,
    51: 58856600,
}
# 56,579,101
# 565,791,017


class CmdStatSheet(Command):
    """
    View your character's current stats.
    """

    key = "stats"
    aliases = ("sheet", "score", "sc")

    def func(self):
        caller = self.caller
        levelcost = int(LEVEL_COST_DICT[caller.db.level + 1])
        self.msg(f" |g{caller} {caller.db.title} ({caller.db.alignment})")
        self.msg(f" |GLevel {caller.db.level or 0}, {levelcost} xp to next level")
        self.msg(f" |GEXP: {caller.db.exp or 0}")
        self.msg(f" |GStats: ({caller.db.stat_points} stats available)")
        self.msg(f" |GCoins: {caller.db.coins or 0}")
        if caller.db.best_kill:
            best_kill = caller.db.best_kill or "None"
            best_kill_name = best_kill.get("name", "None")
            best_kill_level = best_kill.get("level", 0)
            best_kill_exp = best_kill.get("xp", 0)
            self.msg(
                f" |GBest Kill: {best_kill_name} (lvl {best_kill_level}) for {best_kill_exp} exp\n"
            )

        # display the primary stats
        strcost = int(STAT_COST_DICT[caller.traits.str.base + 1])
        dexcost = int(STAT_COST_DICT[caller.traits.dex.base + 1])
        wiscost = int(STAT_COST_DICT[caller.traits.wis.base + 1])
        concost = int(STAT_COST_DICT[caller.traits.con.base + 1])
        intcost = int(STAT_COST_DICT[caller.traits.int.base + 1])
        chacost = int(STAT_COST_DICT[caller.traits.cha.base + 1])

        table = EvTable(f"|G", "|GBase", "|GMod", "|GCost", border="none")
        table.add_row(
            f"|GStr",
            f"|C{int(caller.traits.str.value or 1)}",
            f"|C{int(caller.traits.str.mod or 0)}",
            f"|C{strcost}",
        ),
        table.add_row(
            f"|GDex",
            f"|C{int(caller.traits.dex.value or 1)}",
            f"|C{int(caller.traits.str.mod or 0)}",
            f"|C{dexcost}",
        ),
        table.add_row(
            f"|GWis",
            f"|C{int(caller.traits.wis.value or 1)}",
            f"|C{int(caller.traits.str.mod or 0)}",
            f"|C{wiscost}",
        ),
        table.add_row(
            f"|GCon",
            f"|C{int(caller.traits.con.value or 1)}",
            f"|C{int(caller.traits.str.mod or 0)}",
            f"|C{concost}",
        ),
        table.add_row(
            f"|GInt",
            f"|C{int(caller.traits.int.value or 1)}",
            f"|C{int(caller.traits.str.mod or 0)}",
            f"|C{intcost}",
        ),
        table.add_row(
            f"|GCha",
            f"|C{int(caller.traits.cha.value or 1)}",
            f"|C{int(caller.traits.str.mod or 0)}",
            f"|C{chacost}\n",
        ),

        table.add_row(f"|GHp", f"|C {int(caller.db.hp) or 0} / {int(caller.db.hpmax)}"),
        table.add_row(f"|GFp", f"|C {int(caller.db.fp) or 0} / {int(caller.db.fpmax)}"),
        table.add_row(f"|GEp", f"|C {int(caller.db.ep) or 0} / {int(caller.db.epmax)}"),
        table.reformat(width=50, align="l")
        self.msg(f"{str(table)}\n\n")


class CmdAdvance(Command):
    """
    Advance a level or attribute by spending experience points.

    Enter "advance" to see what you can learn.

    Usage:
        advance

    Example:
        advance
        advance level
        advance str, dex, con, int, wis, cha
    """

    key = "advance"
    aliases = "adv"

    def _calc_stat_exp(self, stat, stat_level):
        """
        Calculates the experience cost for increasing your skill from the start level.
        """
        if not stat == "level":
            print(f"stat cost dict: {STAT_COST_DICT}")
            return int(STAT_COST_DICT[stat_level])
        return int(LEVEL_COST_DICT[stat_level])

    def adv_player_level(self):
        caller = self.caller
        cost = LEVEL_COST_DICT[caller.db.level + 1]
        if caller.db.exp < cost:
            self.msg(
                f"|wYou need {cost-caller.db.exp} more experience to advance your level."
            )
            return

        confirm = yield (
            f"It will cost you {cost} experience to advance your level. Confirm? Yes/No"
        )
        if confirm.lower() not in (
            "yes",
            "y",
        ):
            self.msg("Cancelled.")
            return
        caller.db.exp -= cost
        caller.db.level += 1
        caller.db.stat_points += 5
        self.msg(f"You grow more powerful ({caller.db.level})")

    def set_max_hp(self):
        caller = self.caller
        caller.db.hpmax = (
            50
            + caller.db.level
            + caller.db.con_increase_amount * caller.traits.con.value
        )

    def set_max_fp(self):
        caller = self.caller
        caller.db.fpmax = (
            50
            + caller.db.level
            + caller.db.int_increase_amount * caller.traits.int.value
        )

    def func(self):
        caller = self.caller
        try:
            stat = self.args.strip()
            list = ["level", "str", "con", "dex", "int", "wis", "cha"]

            if stat == "":
                caller.msg(f"|gWhat would you like to raise?")
                return

            if stat not in list:
                caller.msg(f"|gYou can't raise that.")
                return

            if stat == "level":
                cost = LEVEL_COST_DICT[caller.db.level + 1]
                if caller.db.exp < cost:
                    self.msg(
                        f"|wYou need {cost-caller.db.exp} more experience to advance your level."
                    )
                    return

                confirm = yield (
                    f"It will cost you {cost} experience to advance your level. Confirm? Yes/No"
                )
                if confirm.lower() not in (
                    "yes",
                    "y",
                ):
                    self.msg("Cancelled.")
                    return
                caller.db.exp -= cost
                caller.db.level += 1
                caller.db.stat_points += 5
                self.set_max_hp()
                self.set_max_fp()
                caller.msg(f"|rYou grow more powerful ({caller.db.level})")
            else:
                self.msg(f"stat: {stat}")
                caller = self.caller
                if not (caller.db.stat_points > 0):
                    print(f"caller stat points: {caller.db.stat_points}")
                    self.msg("You do not have any stat points available.")
                    return

                current_stat = caller.traits.get(stat).base

                cost = STAT_COST_DICT[current_stat + 1]
                if caller.db.exp < cost:
                    self.msg(
                        f"|wYou need {cost-caller.db.exp} more experience to advance your {stat}."
                    )
                    return
                caller.db.exp -= cost
                caller.db.stat_points -= 1
                caller.traits.get(stat).base = current_stat + 1

                if stat == "con":
                    self.msg(f"con increase amount: {caller.db.con_increase_amount}")
                    self.msg(f"con value: {caller.traits.con.value}")
                    self.set_max_hp()
                if stat == "int":
                    self.msg(f"int increase amount: {caller.db.int_increase_amount}")
                    self.msg(f"int value: {caller.traits.int.value}")
                    self.set_max_fp()

                self.msg(f"|rYou advance your {stat} to {current_stat + 1}.")

        except ValueError:
            self.msg("Usage: Advance, adv <stat or level>")
            return


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


class TrainCmdSet(CmdSet):
    key = "Train CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()
        self.add(CmdTrainSkill)


class SkillCmdSet(CmdSet):
    key = "Skill CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()
        self.add(CmdStatSheet)


class AdvanceCmdSet(CmdSet):
    key = "Advance CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()
        self.add(CmdAdvance)
