from random import randint, uniform

from typeclasses.changelingguild.changeling_attack import ChangelingAttack


class Tiger(ChangelingAttack):
    """
    The tiger is the largest cat species, known for its distinctive orange coat
    with black stripes. Tigers are solitary animals and are highly territorial,
    defending their hunting grounds from other tigers. They are carnivores and
    are known for their strength and agility, as well as their ability to swim
    and climb trees. Tigers are also known for their distinctive hunting
    techniques, which involve stalking and ambushing their prey over long
    distances. They are apex predators and are at the top of the food chain in
    their natural habitats. Tigers are also known for their powerful jaws and
    sharp claws, which they use to catch and kill their prey. They are capable
    of running at speeds of up to 40 miles per hour and can leap up to 10 feet
    in the air.
    """

    energy_cost = 3
    speed = 3
    power = 20
    toughness = 15
    dodge = 10

    def _calculate_claw_damage(self, wielder):
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value
        stat_bonus = str / 3 + dex / 5
        dmg = stat_bonus + wielder.db.guild_level

        damage = randint(int(dmg * 2 / 3), int(dmg))
        return damage

    def _calculate_bite_damage(self, wielder):
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value
        stat_bonus = str / 4 + dex / 4
        dmg = 17 + stat_bonus + wielder.db.guild_level / 2

        damage = randint(int(dmg * 2 / 3), int(dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        self.energy_cost = 1
        self.speed = 3

        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_bite_damage(wielder), "edged", "bite")
        target.at_damage(wielder, self._calculate_claw_damage(wielder), "edged", "claw")
        target.at_damage(wielder, self._calculate_claw_damage(wielder), "edged", "claw")

        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)
