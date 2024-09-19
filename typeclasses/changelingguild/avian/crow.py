from random import randint, uniform
from typeclasses.changelingguild.changeling_attack import ChangelingAttack


class Crow(ChangelingAttack):
    """
    Crows are intelligent birds known for their problem-solving
    abilities and adaptability. They are often found in urban
    and suburban environments and are known for their loud cawing
    and scavenging behavior.
    """

    speed = 2
    power = 12
    toughness = 8
    dodge = 13

    def _calculate_bite_damage(self, wielder):
        dex = wielder.traits.dex.value
        str = wielder.traits.str.value
        stat_bonus = str + dex / 10
        dmg = 20 + stat_bonus + wielder.db.guild_level

        damage = int(uniform(dmg / 2, dmg))
        return damage

    def _calculate_wing_damage(self, wielder):
        dex = wielder.traits.dex.value
        str = wielder.traits.str.value
        stat_bonus = str + dex / 10
        dmg = stat_bonus + wielder.db.guild_level / 2

        damage = int(uniform(dmg / 2, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        self.energy_cost = 1
        self.speed = 3

        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_bite_damage(wielder), "edged", "bite")
        target.at_damage(wielder, self._calculate_wing_damage(wielder), "edged", "wing")
        target.at_damage(wielder, self._calculate_wing_damage(wielder), "edged", "wing")

        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)
