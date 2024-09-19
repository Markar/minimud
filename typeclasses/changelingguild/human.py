from typeclasses.changelingguild.changeling_attack import ChangelingAttack
from random import uniform


class Human(ChangelingAttack):
    """
    You know what humans are.
    """

    speed = 3
    power = 3
    toughness = 3
    dodge = 3

    def _calculate_damage(self, wielder):
        """
        Calculate the damage of the attack
        """
        dex = wielder.traits.dex.value
        wis = wielder.traits.wis.value
        stat_bonus = (dex + wis) / 5
        base_dmg = 3 + wielder.db.guild_level
        dmg = base_dmg + stat_bonus

        damage = int(uniform(dmg / 2, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        """
        The auto attack of Human
        """
        super().at_attack(wielder, target, **kwargs)

        self.energy_cost = 1
        self.speed = 3

        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_damage(wielder), "blunt", "punch")

        wielder.msg("[ Cooldown: " + str(self.speed) + " seconds ]")
        wielder.cooldowns.add("attack", self.speed)
