from random import randint, uniform

from typeclasses.changelingguild.changeling_attack import ChangelingAttack


class Crocodile(ChangelingAttack):
    """
    Crocodiles are large, aquatic reptiles that are known for their powerful jaws
    and sharp teeth. They are found in tropical and subtropical regions of the
    world, where they inhabit rivers, lakes, and swamps. Crocodiles are opportunistic
    hunters and will eat a variety of foods, including fish, birds, and mammals.
    They are also known for their distinctive armored scales, which protect them
    from other predators and help them blend in with their surroundings. Crocodiles
    are solitary animals and are highly territorial, defending their hunting grounds
    from other predators. They are capable of running at speeds of up to 20 miles
    per hour and can leap up to 6 feet in the air. Crocodiles are also known for
    their ability to swim long distances and hold their breath underwater for up
    to an hour.
    """

    energy_cost = 3
    speed = 3
    power = 20
    toughness = 23
    dodge = 2

    def _calculate_tail_damage(self, wielder):
        dex = wielder.traits.dex.value
        str = wielder.traits.str.value
        stat_bonus = (dex + str) / 3
        base_dmg = 17 + wielder.db.guild_level / 2
        dmg = base_dmg + stat_bonus

        damage = int(uniform(dmg / 2, dmg))
        return damage

    def _calculate_bite_damage(self, wielder):
        dex = wielder.traits.dex.value
        str = wielder.traits.str.value
        stat_bonus = (dex + str) / 3
        base_dmg = 32 + wielder.db.guild_level
        dmg = base_dmg + stat_bonus

        damage = int(uniform(dmg / 2, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):

        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_damage(wielder), "edged", "bite")
        target.at_damage(wielder, self._calculate_damage(wielder), "blunt", "tail")

        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)
