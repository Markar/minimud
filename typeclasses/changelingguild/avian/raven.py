from random import randint, uniform

from typeclasses.changelingguild.changeling_attack import ChangelingAttack


class Raven(ChangelingAttack):
    """
    Ravens are intelligent birds known for their problem-solving
    abilities and adaptability. They are often found in urban
    and suburban environments and are known for their loud cawing
    and scavenging behavior.
    """

    speed = 3
    energy_cost = 3
    power = 8
    toughess = 9
    dodge = 9

    def _calculate_bite_damage(self, wielder):
        dex = wielder.traits.dex.value
        str = wielder.traits.str.value
        stat_bonus = str + dex / 5
        dmg = 20 + stat_bonus + wielder.db.guild_level

        damage = int(uniform(dmg / 2, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_bite_damage(wielder), "edged", "bite")
        target.at_damage(wielder, self._calculate_bite_damage(wielder), "edged", "bite")

        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)
