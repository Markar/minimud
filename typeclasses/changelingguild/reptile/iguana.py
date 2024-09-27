import math
from random import randint, uniform

from typeclasses.changelingguild.changeling_attack import ChangelingAttack


class Iguana(ChangelingAttack):
    """
    Unlike several of the other types of lizard, iguanas and
    other iguanid lizards display fairly complex courtship and
    terretorial behavioral rites.
    """

    damage = 1
    energy_cost = 3
    skill = "blunt"
    name = "tail"
    speed = 3
    power = 8
    toughness = 10
    dodge = 9

    def _calculate_damage(self, wielder):
        """
        Calculate the damage of the attack
        """
        dex = wielder.traits.dex.value
        wis = wielder.traits.wis.value
        stat_bonus = (dex + wis) / 5
        base_dmg = 30 + wielder.db.guild_level / 3
        dmg = base_dmg + stat_bonus

        damage = int(uniform(dmg / 2, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_damage(wielder), "edged", "bite")
        target.at_damage(wielder, self._calculate_damage(wielder), "edged", "tail")

        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)
