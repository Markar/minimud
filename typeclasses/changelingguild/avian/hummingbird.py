from random import randint, uniform
from typeclasses.changelingguild.changeling_attack import ChangelingAttack


class Hummingbird(ChangelingAttack):
    """
    The bee hummingbird weighs 2 grams and is 5.5 centimeters,
    or 2 1/8 inches long, making it the world's smallest bird,
    and ranking it with the smallest of mammals.  Hummingbirds
    can fly in all directions, including backward, and may hover
    in place.
    """

    energy_cost = 3
    speed = 3
    power = 1
    toughness = 4
    dodge = 27

    def _calculate_bite_damage(self, wielder):
        dex = wielder.traits.dex.value
        str = wielder.traits.str.value
        stat_bonus = str + dex / 4
        dmg = 1 + stat_bonus + wielder.db.guild_level / 2

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
