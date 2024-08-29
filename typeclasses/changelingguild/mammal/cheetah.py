from random import randint, uniform

from typeclasses.changelingguild.changeling_attack import ChangelingAttack


class Cheetah(ChangelingAttack):
    """
    The cheetah is a large mammal that is native to Africa and Asia. It is known for its
    speed and agility, as well as its distinctive spots and long tail. Cheetahs are carnivores
    and are the fastest land animals on Earth, capable of reaching speeds of up to 70 miles
    per hour. They are solitary animals and are highly territorial, defending their hunting
    grounds from other predators. Cheetahs are also known for their distinctive hunting
    techniques, which involve stalking and chasing down their prey over long distances.
    """

    energy_cost = 3
    speed = 3
    power = 19
    toughness = 12
    dodge = 14

    def _calculate_claw_damage(self, wielder):
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value
        stat_bonus = str / 5 + dex / 3
        dmg = 1 + stat_bonus + wielder.db.guild_level / 2

        damage = randint(int(dmg * 2 / 3), int(dmg))
        return damage

    def _calculate_bite_damage(self, wielder):
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value
        stat_bonus = str / 5 + dex / 3
        dmg = 30 + stat_bonus + wielder.db.guild_level / 4

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
