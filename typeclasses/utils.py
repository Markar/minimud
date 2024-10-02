from evennia.prototypes import spawner
from random import randint, uniform
from commands.command import Command


def get_display_name(self, looker, **kwargs):
    """
    Adds color to the display name.
    """
    name = super().get_display_name(looker, **kwargs)
    if looker == self:
        # special color for our own name
        return f"|c{name}|n"
    return f"|g{name}|n"


def get_article(word):
    vowels = "aeiou"
    return "an" if word[0].lower() in vowels else "a"


def geHealthStatus(self, hpPercent):
    if hpPercent >= 0.9:
        return "is in perfect health."
    elif hpPercent >= 0.7:
        return "is slightly bruised."
    elif hpPercent >= 0.5:
        return "is moderately wounded."
    elif hpPercent >= 0.3:
        return "is heavily injured."
    elif hpPercent >= 0.1:
        return "is severely wounded."
    else:
        return "is near death."


def SetNPCStats(self, level, xp, hits):
    level = randint(level, level + 2)
    xp = int(uniform(xp, xp * 1.2))
    exp_reward = xp
    hpmax = 100 + int(xp / 5)
    hpmax = int(uniform(hpmax * 0.9, hpmax * 1.1))
    damage = 5 + int(xp / 150)
    hits = hits
    armor = int(level / 2.5)

    if xp > 80 and xp < 201:
        damage += 2
        hpmax += 50
    elif xp > 200 and xp < 501:
        damage += 5
    elif xp > 500 and xp < 1001:
        damage += 6
    elif xp >= 800:
        damage += 7

    if level < 30 and level > 24:
        damage = damage * 0.5
        exp_reward = exp_reward * 1.35
    elif level < 25 and level > 19:
        damage = damage * 0.65
        exp_reward = exp_reward * 1.25
    elif level < 20 and level > 14:
        damage = damage * 0.75
        exp_reward = exp_reward * 1.15
    elif level < 15 and level > 9:
        damage = damage * 0.85
        exp_reward = exp_reward
    elif level < 10 and level > 4:
        damage = damage * 0.9
        exp_reward = exp_reward * 0.6

    if hits > 1:
        damage = damage * (1 + hits * 0.2)  # 20% increase per hit
        damage = int(
            damage / hits
        )  # divide by number of hits, higher total damage but lower per hit

    self.db.hp = hpmax
    self.db.hpmax = hpmax
    self.db.exp_reward = xp
    self.db.level = level
    self.db.armor = armor
    self.db.natural_weapon["damage"] = damage
    self.db.natural_weapon["hits"] = hits
    self.db.natural_weapon["energy_cost"] = 0

    return {
        "level": level,
        "xp": xp,
        "exp_reward": exp_reward,
        "hpmax": hpmax,
        "damage": damage,
        "hits": hits,
        "armor": armor,
    }


def SpawnMob(self, xp, level, hits, name, tag):
    mobs = spawner.spawn(name)
    self.tags.add("room", category=tag)

    for mob in mobs:
        mob.tags.add("mob", category=tag)
        mob.location = self
        mob.home = self

        SetNPCStats(mob, level, xp, hits)

    return mob


class PowerCommand(Command):
    def func(self):
        caller = self.caller
        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False
        caller.cooldowns.add("global_cooldown", 2)


def get_glvl_cost(glvl):
    if glvl > 40:
        return "Max level reached."
    else:
        return GUILD_LEVEL_COST_DICT[glvl]


GUILD_LEVEL_COST_DICT = {
    2: 297,  # Total: 297
    3: 413,  # Total: 710
    4: 645,  # Total: 1,355
    5: 949,  # Total: 2,304
    6: 1531,  # Total: 3,835
    7: 2412,  # Total: 6,247
    8: 3327,  # Total: 9,574
    9: 4642,  # Total: 14,216 = 4.7 hours
    10: 4998,  # Total: 19,214 = 6.4 hours
    11: 9003,  # Total: 28,217 = 9.4 hours
    12: 10007,  # Total: 38,224 = 12.7 hours
    13: 11998,  # Total: 50,222 = 16.7 hours
    14: 15003,  # Total: 65,225 = 21.7 hours
    15: 19997,  # Total: 85,222 = 28.4 hours
    16: 22498,  # Total: 110,220 = 36.7 hours
    17: 25002,  # Total: 135,222 = 45.1 hours
    18: 29999,  # Total: 165,221 = 55.1 hours
    19: 34998,  # Total: 200,219 = 66.7 hours
    20: 39997,  # Total: 240,216 = 80.1 hours = 3.3 days
    21: 59999,  # Total: 300,215 = 100.1 hours = 4.2 days
    22: 69998,  # Total: 370,213 = 123.4 hours = 5.1 days
    23: 79997,  # Total: 450,210 = 150.1 hours = 6.3 days
    24: 89996,  # Total: 540,206 = 180.1 hours = 7.5 days
    25: 99995,  # Total: 640,201 = 213.4 hours = 8.9 days
    26: 109994,  # Total: 750,195 = 250.1 hours = 10.4 days
    27: 119993,  # Total: 870,188 = 290.1 hours = 12.1 days
    28: 129992,  # Total: 1,000,180 = 333.4 hours = 13.9 days
    29: 139991,  # Total: 1,140,171 = 380.1 hours = 15.8 days
    30: 149990,  # Total: 1,290,161 = 430.1 hours = 17.9 days
    31: 151232,  # Total: 1,441,393 = 480.5 hours = 20.0 days
    32: 152474,  # Total: 1,593,867 = 531.3 hours = 22.1 days
    33: 153716,  # Total: 1,747,583 = 582.5 hours = 24.3 days
    34: 154958,  # Total: 1,902,541 = 635.1 hours = 26.5 days
    35: 156200,  # Total: 2,058,741 = 688.2 hours = 28.7 days
    36: 157442,  # Total: 2,216,183 = 741.9 hours = 30.9 days
    37: 158684,  # Total: 2,374,867 = 796.1 hours = 33.2 days
    38: 159926,  # Total: 2,534,793 = 850.9 hours = 35.5 days
    39: 161168,  # Total: 2,695,961 = 906.1 hours = 37.8 days
    40: 162410,  # Total: 2,858,371 = 961.0 hours = 40.0 days
}

SKILL_RANKS = {
    0: "Very poor",
    1: "Poor",
    2: "Below average",
    3: "Average",
    4: "Above average",
    5: "Moderate",
    6: "Good",
    7: "Very good",
    8: "High",
    9: "Very high",
    10: "Excellent",
    12: "Exceptional",
    14: "Masterful",
    16: "Supreme",
    17: "God-like",
}
