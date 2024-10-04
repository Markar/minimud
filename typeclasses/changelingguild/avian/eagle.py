from random import randint, uniform
from typeclasses.changelingguild.changeling_attack import ChangelingAttack


class Eagle(ChangelingAttack):
    """
    Eagles are birds of prey known for their speed and agility. They are
    often found in open habitats such as grasslands and deserts, where they hunt
    small mammals and birds. Eagles have sharp talons and beaks, which they
    use to catch and kill their prey. They are also known for their distinctive
    diving flight, which allows them to catch prey in mid-air. Eagles are
    solitary birds and are highly territorial, defending their hunting
    grounds from other birds of prey.
    """

    speed = 3
    energy_cost = 3
    power = 25
    toughness = 10
    dodge = 2

    def _calculate_beak_damage(self, wielder):
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value
        stat_bonus = str / 3 + dex / 5
        dmg = 14 + stat_bonus + wielder.db.guild_level * 2

        damage = randint(int(dmg * 2 / 3), int(dmg))
        return damage

    def _calculate_claw_damage(self, wielder):
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value
        stat_bonus = str / 7 + dex / 6
        dmg = stat_bonus + wielder.db.guild_level / 3

        damage = randint(int(dmg * 2 / 3), int(dmg))
        return damage

    def _calculate_wing_damage(self, wielder):
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value
        stat_bonus = (str + dex) / 10
        dmg = stat_bonus + wielder.db.guild_level / 6

        damage = randint(int(dmg * 2 / 3), int(dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_beak_damage(wielder), "edged", "bite")
        target.at_damage(wielder, self._calculate_claw_damage(wielder), "blunt", "claw")
        target.at_damage(wielder, self._calculate_claw_damage(wielder), "blunt", "claw")
        target.at_damage(wielder, self._calculate_wing_damage(wielder), "blunt", "wing")
        target.at_damage(wielder, self._calculate_wing_damage(wielder), "blunt", "wing")

        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)
