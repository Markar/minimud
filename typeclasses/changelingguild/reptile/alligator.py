from random import randint, uniform

from typeclasses.changelingguild.changeling_attack import ChangelingAttack


class Alligator(ChangelingAttack):
    """
    Alligators are large, carnivorous reptiles that are native to the
    southeastern United States and eastern China. They are known for their
    powerful jaws and sharp teeth, which they use to catch and kill their
    prey. Alligators are found in freshwater habitats, such as swamps, rivers,
    and lakes, where they hunt fish, birds, and small mammals. They are
    opportunistic hunters and will eat a variety of foods, including carrion.
    Alligators are also known for their distinctive armored scales, which
    protect them from other predators and help them blend in with their
    surroundings. They are solitary animals and are highly territorial,
    defending their hunting grounds from other predators.
    """

    energy_cost = 3
    speed = 3
    power = 24
    toughness = 20
    dodge = 0

    def _calculate_tail_damage(self, wielder):
        dex = wielder.traits.dex.value
        str = wielder.traits.str.value
        stat_bonus = (dex + str) / 3
        base_dmg = 9 + wielder.db.guild_level / 2
        dmg = base_dmg + stat_bonus

        damage = int(uniform(dmg / 2, dmg))
        return damage

    def _calculate_bite_damage(self, wielder):
        dex = wielder.traits.dex.value
        str = wielder.traits.str.value
        stat_bonus = (dex + str) / 3
        base_dmg = 40 + wielder.db.guild_level
        dmg = base_dmg + stat_bonus

        damage = int(uniform(dmg / 2, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):

        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_damage(wielder), "edged", "bite")
        target.at_damage(wielder, self._calculate_damage(wielder), "blunt", "tail")

        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)
