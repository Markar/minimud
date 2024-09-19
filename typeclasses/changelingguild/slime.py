from random import uniform

from typeclasses.changelingguild.changeling_attack import ChangelingAttack


class Slime(ChangelingAttack):
    """
    The slime is a gelatinous creature that can change its shape
    and size at will. It is often found in dark, damp places and
    can engulf its prey with its sticky, acidic body.
    """

    energy_cost = 2
    skill = "acid"
    name = "engulf"
    speed = 2
    power = 5
    toughness = 5
    dodge = 5

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
        The auto attack of Slime
        """
        super().at_attack(wielder, target, **kwargs)

        self.energy_cost = 1
        self.speed = 3

        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_damage(wielder), "acid", "engulf")

        wielder.msg("[ Cooldown: " + str(self.speed) + " seconds ]")
        wielder.cooldowns.add("attack", self.speed)
