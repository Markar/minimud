import math
from random import randint, uniform

from typeclasses.changelingguild.changeling_attack import ChangelingAttack


class Finch(ChangelingAttack):
    """
    The finch is a small bird, typically weighing around 20 grams and measuring
    about 12 centimeters in length. Finches are known for their vibrant colors
    and melodious songs. They are agile fliers and can navigate through dense
    foliage with ease.
    """

    damage = 2
    energy_cost = 2
    skill = "edged"
    name = "peck"
    speed = 2
    power = 4
    toughness = 4
    dodge = 22

    def _calculate_bite_damage(self, wielder):
        dex = wielder.traits.dex.value
        str = wielder.traits.str.value
        stat_bonus = str + dex / 3
        dmg = 5 + stat_bonus + wielder.db.guild_level / 2

        damage = int(uniform(dmg / 2, dmg))
        return damage

    def _calculate_claw_damage(self, wielder):
        dex = wielder.traits.dex.value
        str = wielder.traits.str.value
        stat_bonus = str / 5 + dex / 3
        dmg = 1 + stat_bonus + wielder.db.guild_level / 4

        damage = int(uniform(dmg / 2, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        self.energy_cost = 1
        self.speed = 3

        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_bite_damage(wielder), "edged", "bite")
        target.at_damage(wielder, self._calculate_claw_damage(wielder), "edged", "claw")
        target.at_damage(wielder, self._calculate_claw_damage(wielder), "edged", "claw")

        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)
