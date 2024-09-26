from random import randint, uniform

from typeclasses.changelingguild.changeling_attack import ChangelingAttack


class Caiman(ChangelingAttack):
    """
    Caimans are large, carnivorous reptiles that are closely related to alligators.
    They are known for their powerful jaws and sharp teeth, which they use to catch
    and kill their prey. Caimans are found in tropical and subtropical regions of
    Central and South America, where they inhabit rivers, lakes, and swamps. They
    are opportunistic hunters and will eat a variety of foods, including fish, birds,
    and small mammals. Caimans are solitary animals and are highly territorial,
    defending their hunting grounds from other predators. They are also known for
    their distinctive armored scales, which protect them from other predators and
    help them blend in with their surroundings.
    """

    energy_cost = 3
    speed = 3
    power = 22
    toughness = 21
    dodge = 2

    def _calculate_tail_damage(self, wielder):
        dex = wielder.traits.dex.value
        wis = wielder.traits.wis.value
        stat_bonus = (dex + wis) / 5
        base_dmg = 15 + wielder.db.guild_level
        dmg = base_dmg + stat_bonus

        damage = int(uniform(dmg / 2, dmg))
        return damage

    def _calculate_bite_damage(self, wielder):
        dex = wielder.traits.dex.value
        wis = wielder.traits.wis.value
        stat_bonus = (dex + wis) / 5
        base_dmg = 10 + wielder.db.guild_level * 3 / 2
        dmg = base_dmg + stat_bonus

        damage = int(uniform(dmg / 2, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_damage(wielder), "edged", "bite")
        target.at_damage(wielder, self._calculate_damage(wielder), "blunt", "tail")

        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)
