import math
from random import randint, uniform

from typeclasses.changelingguild.changeling_attack import ChangelingAttack


class Wolf(ChangelingAttack):
    """
    The wolf is a carnivorous mammal that is known for its social behavior and hunting skills.
    Wolves are highly adaptable and can be found in various habitats, including forests, tundra,
    and grasslands. They have sharp teeth and strong jaws, which they use to capture and kill
    their prey. Wolves are also excellent runners and can reach speeds of up to 35 miles per hour.
    They live in packs and have a complex social structure, with an alpha male and female leading
    the group. Wolves are highly intelligent and have a wide range of vocalizations for communication.
    """

    damage = 1
    energy_cost = 3
    skill = "edged"
    name = "bite"
    speed = 3
    power = 17
    toughness = 14
    dodge = 14

    def _calculate_bite_damage(self, wielder):
        str = wielder.traits.str.value
        stat_bonus = str / 4
        dmg = 10 + stat_bonus + wielder.db.guild_level

        damage = int(uniform(dmg / 2, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        self.energy_cost = 1
        self.speed = 3

        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_bite_damage(wielder), "edged", "bite")
        target.at_damage(wielder, self._calculate_bite_damage(wielder), "edged", "bite")

        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)
