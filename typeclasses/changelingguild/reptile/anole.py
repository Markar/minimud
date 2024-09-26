import math
from random import randint, uniform
from typeclasses.changelingguild.changeling_attack import ChangelingAttack


class Anole(ChangelingAttack):
    """
    The green anole is often mistaken, and erroneously called,
    the chameleon--although it changes color from green to
    brown, its ability is poor compared to the true chameleon.
    This 'false chameleon' is often sold as the true thing in
    pet shops.
    """

    energy_cost = 1
    speed = 3
    power = 5
    toughness = 8
    dodge = 5

    def _calculate_damage(self, wielder):
        """
        Calculate the damage of the attack
        """
        dex = wielder.traits.dex.value
        str = wielder.traits.str.value
        stat_bonus = (dex + str) / 5
        base_dmg = 10 + wielder.db.guild_level / 2
        dmg = base_dmg + stat_bonus

        damage = int(uniform(dmg / 2, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        """
        The auto attack of Anole
        """
        super().at_attack(wielder, target, **kwargs)

        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_damage(wielder), "edged", "bite")
        target.at_damage(wielder, self._calculate_damage(wielder), "edged", "tail")

        wielder.msg("[ Cooldown: " + str(self.speed) + " seconds ]")
        wielder.cooldowns.add("attack", self.speed)
