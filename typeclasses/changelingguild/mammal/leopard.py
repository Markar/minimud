from random import randint, uniform

from typeclasses.changelingguild.changeling_attack import ChangelingAttack


class Leopard(ChangelingAttack):
    """
    The leopard is a large, carnivorous feline known for its speed and agility.
    Leopards are solitary animals and are highly territorial, defending their
    hunting grounds from other predators. They are known for their distinctive
    spots and long tail, which help them blend in with their surroundings and
    stalk their prey. Leopards are also known for their powerful jaws and sharp
    claws, which they use to catch and kill their prey. They are capable of
    running at speeds of up to 60 miles per hour and can leap up to 20 feet
    in the air. Leopards are opportunistic hunters and will eat a variety of
    foods, including antelope, deer, and small mammals.
    """

    energy_cost = 3
    speed = 3
    power = 17
    toughness = 14
    dodge = 14

    def _calculate_claw_damage(self, wielder):
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value
        stat_bonus = str / 5 + dex / 5
        dmg = 9 + stat_bonus + wielder.db.guild_level / 2

        damage = randint(int(dmg * 2 / 3), int(dmg))
        return damage

    def _calculate_bite_damage(self, wielder):
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value
        stat_bonus = str / 5 + dex / 5
        dmg = 37 + stat_bonus + wielder.db.guild_level / 2

        damage = randint(int(dmg * 2 / 3), int(dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_bite_damage(wielder), "edged", "bite")
        target.at_damage(wielder, self._calculate_claw_damage(wielder), "edged", "claw")
        target.at_damage(wielder, self._calculate_claw_damage(wielder), "edged", "claw")

        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)
