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


def get_display_name(self, looker, **kwargs):
    """
    Adds color to the display name.
    """
    name = super().get_display_name(looker, **kwargs)
    if looker == self:
        # special color for our own name
        return f"|c{name}|n"
    return f"|g{name}|n"


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
        hpmax += 50
    elif xp > 500 and xp < 1001:
        damage += 6
        hpmax += 50
    elif xp >= 800:
        damage += 7
        hpmax += 50

    if level < 30 and level > 24:
        damage = damage * 0.5
        exp_reward = exp_reward * 1.3
    elif level < 25 and level > 19:
        damage = damage * 0.65
        exp_reward = exp_reward * 1.15
    elif level < 20 and level > 14:
        damage = damage * 0.75
        exp_reward = exp_reward
    elif level < 15 and level > 9:
        damage = damage * 0.85
        exp_reward = exp_reward * 0.8
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
