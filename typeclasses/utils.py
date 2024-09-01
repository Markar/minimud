from evennia.prototypes import spawner
from random import randint, uniform


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


def SpawnMob(self, xp, level, hits, name, tag):
    mobs = spawner.spawn(name)
    self.tags.add("room", category=tag)
    level = randint(level, level + 2)
    xp = int(uniform(xp, xp * 1.2))
    damage = 5 + int(xp / 100)
    hpmax = int(xp / 5)
    if xp < 500:
        hpmax += int(xp / 2)
    if xp > 500:
        hpmax += 50
    if xp > 1000:
        hpmax += 50
    if xp > 2000:
        hpmax += 50
    hits = hits

    if hits > 1:
        damage = damage * (1 + hits * 0.2)  # 20% increase per hit
        damage = int(
            damage / hits
        )  # divide by number of hits, higher total damage but lower per hit

    for mob in mobs:
        mob.tags.add("mob", category=tag)
        mob.location = self
        mob.home = self
        mob.db.hp = hpmax
        mob.db.hpmax = hpmax
        mob.db.exp_reward = xp
        mob.db.level = level
        mob.db.natural_weapon["damage"] = damage
        mob.db.natural_weapon["hits"] = hits
