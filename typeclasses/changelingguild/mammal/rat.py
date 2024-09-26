import math
from random import randint, uniform

from typeclasses.changelingguild.changeling_attack import ChangelingAttack


class Rat(ChangelingAttack):
    """
    Rats are small, agile creatures known for their ability to
    scurry through tight spaces and spread disease.
    """

    damage = 1
    energy_cost = 1
    speed = 3
    power = 4
    toughness = 5
    dodge = 17

    def _calculate_bite_damage(self, wielder):
        dex = wielder.traits.dex.value
        str = wielder.traits.str.value
        stat_bonus = (dex + str) / 10
        dmg = 5 + stat_bonus + wielder.db.guild_level / 2

        damage = int(uniform(dmg / 2, dmg))
        return damage

    def _calculate_claw_damage(self, wielder):
        dex = wielder.traits.dex.value
        str = wielder.traits.str.value
        stat_bonus = (dex + str) / 10
        dmg = 10 + stat_bonus + wielder.db.guild_level / 2

        damage = int(uniform(dmg / 2, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_bite_damage(wielder), "edged", "bite")
        target.at_damage(wielder, self._calculate_claw_damage(wielder), "edged", "claw")
        target.at_damage(wielder, self._calculate_claw_damage(wielder), "edged", "claw")

        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)
