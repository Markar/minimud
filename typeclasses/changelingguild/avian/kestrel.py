from random import randint, uniform
from typeclasses.changelingguild.changeling_attack import ChangelingAttack


class Kestrel(ChangelingAttack):
    """
    Kestrels are small birds of prey known for their speed and agility. They are
    often found in open habitats such as grasslands and deserts, where they hunt
    small mammals and insects. Kestrels have sharp talons and beaks, which they
    use to catch and kill their prey. They are also known for their distinctive
    hovering flight, which allows them to spot prey from a distance. Kestrels
    are solitary birds and are highly territorial, defending their hunting
    grounds from other birds of prey.

    """

    speed = 2
    power = 13
    toughness = 10
    dodge = 6

    def _calculate_bite_damage(self, wielder):
        dex = wielder.traits.dex.value
        str = wielder.traits.str.value
        stat_bonus = str / 5 + dex / 3
        dmg = 8 + stat_bonus + wielder.db.guild_level

        damage = int(uniform(dmg / 2, dmg))
        return damage

    def _calculate_claw_damage(self, wielder):
        dex = wielder.traits.dex.value
        str = wielder.traits.str.value
        stat_bonus = str / 5 + dex / 3
        dmg = 5 + stat_bonus + wielder.db.guild_level / 4

        damage = int(uniform(dmg / 2, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        self.energy_cost = 1
        self.speed = 3

        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_bite_damage(wielder), "edged", "peck")
        target.at_damage(wielder, self._calculate_claw_damage(wielder), "edged", "claw")
        target.at_damage(wielder, self._calculate_claw_damage(wielder), "edged", "claw")

        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)
