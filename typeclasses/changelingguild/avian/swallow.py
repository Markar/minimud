from random import randint, uniform
from typeclasses.changelingguild.changeling_attack import ChangelingAttack


class Swallow(ChangelingAttack):
    """
    Swallows are small, fast birds that are known for their
    agility and quick reflexes. They are often found in
    rural and suburban environments and are known for their
    graceful flight and aerial acrobatics.
    """

    speed = 2
    power = 2
    toughness = 3
    dodge = 5

    def _calculate_bite_damage(self, wielder):
        dex = wielder.traits.dex.value
        str = wielder.traits.str.value
        stat_bonus = str + dex / 3
        dmg = 10 + stat_bonus + wielder.db.guild_level / 2

        damage = int(uniform(dmg / 2, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        self.energy_cost = 1
        self.speed = 3

        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_bite_damage(wielder), "edged", "bite")

        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)
