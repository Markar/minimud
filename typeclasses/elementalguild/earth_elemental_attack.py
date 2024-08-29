from random import uniform
from typeclasses.elementalguild.elemental_attack import ElementalAttack


class EarthAttack(ElementalAttack):
    """
    Earth elementals are known for their strength and durability. They are
    often found in rocky areas such as mountains and caves, where they can
    blend in with their surroundings. Earth elementals have the ability to
    control the earth and rocks around them, using them to attack their
    enemies. They are also known for their ability to create earthquakes
    and landslides, which can cause massive damage to their foes.
    """

    speed = 3
    energy_cost = 3

    def _calculate_melee_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        stat_bonus = str / 2 + dex / 4
        dmg = 5 + stat_bonus + glvl * 3 / 2

        if glvl < 10:
            dmg += 7
        elif glvl < 20:
            dmg += 14
        elif glvl < 30:
            dmg += 28
        elif glvl < 40:
            dmg += 42
        else:
            dmg += 65

        damage = int(uniform(dmg / 2, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        # Subtract energy and apply damage to target before their defenses
        if wielder.db.strategy == "melee":
            speed = 3
            wielder.db.ep -= self.energy_cost

            dmg = self._calculate_melee_damage(wielder)
            target.at_damage(wielder, dmg, "blunt", "earth_elemental_melee")
            wielder.msg(f"[ Cooldown: {speed} seconds ]")
            wielder.cooldowns.add("attack", speed)


# Guild Level: 1, Strength: 20, Dexterity: 10, Damage: 32.5
# Guild Level: 1, Strength: 20, Dexterity: 20, Damage: 35.0
# Guild Level: 1, Strength: 20, Dexterity: 30, Damage: 37.5
# Guild Level: 1, Strength: 20, Dexterity: 40, Damage: 40.0
# Guild Level: 1, Strength: 20, Dexterity: 50, Damage: 42.5
# Guild Level: 1, Strength: 20, Dexterity: 60, Damage: 45.0
# Guild Level: 1, Strength: 30, Dexterity: 10, Damage: 37.5
# Guild Level: 1, Strength: 30, Dexterity: 20, Damage: 40.0
# Guild Level: 1, Strength: 30, Dexterity: 30, Damage: 42.5
# Guild Level: 1, Strength: 30, Dexterity: 40, Damage: 45.0
# Guild Level: 1, Strength: 30, Dexterity: 50, Damage: 47.5
# Guild Level: 1, Strength: 30, Dexterity: 60, Damage: 50.0
# Guild Level: 1, Strength: 40, Dexterity: 10, Damage: 42.5
# Guild Level: 1, Strength: 40, Dexterity: 20, Damage: 45.0
# Guild Level: 1, Strength: 40, Dexterity: 30, Damage: 47.5
# Guild Level: 1, Strength: 40, Dexterity: 40, Damage: 50.0
# Guild Level: 1, Strength: 40, Dexterity: 50, Damage: 52.5
# Guild Level: 1, Strength: 40, Dexterity: 60, Damage: 55.0
# Guild Level: 1, Strength: 50, Dexterity: 10, Damage: 47.5
# Guild Level: 1, Strength: 50, Dexterity: 20, Damage: 50.0
# Guild Level: 1, Strength: 50, Dexterity: 30, Damage: 52.5
# Guild Level: 1, Strength: 50, Dexterity: 40, Damage: 55.0
# Guild Level: 1, Strength: 50, Dexterity: 50, Damage: 57.5
# Guild Level: 1, Strength: 50, Dexterity: 60, Damage: 60.0
# Guild Level: 1, Strength: 60, Dexterity: 10, Damage: 52.5
# Guild Level: 1, Strength: 60, Dexterity: 20, Damage: 55.0
# Guild Level: 1, Strength: 60, Dexterity: 30, Damage: 57.5
# Guild Level: 1, Strength: 60, Dexterity: 40, Damage: 60.0
# Guild Level: 1, Strength: 60, Dexterity: 50, Damage: 62.5
# Guild Level: 1, Strength: 60, Dexterity: 60, Damage: 65.0
# ...
# Guild Level: 30, Strength: 20, Dexterity: 10, Damage: 101.0
# Guild Level: 30, Strength: 20, Dexterity: 20, Damage: 103.5
# Guild Level: 30, Strength: 20, Dexterity: 30, Damage: 106.0
# Guild Level: 30, Strength: 20, Dexterity: 40, Damage: 108.5
# Guild Level: 30, Strength: 20, Dexterity: 50, Damage: 111.0
# Guild Level: 30, Strength: 20, Dexterity: 60, Damage: 113.5
# Guild Level: 30, Strength: 30, Dexterity: 10, Damage: 106.0
# Guild Level: 30, Strength: 30, Dexterity: 20, Damage: 108.5
# Guild Level: 30, Strength: 30, Dexterity: 30, Damage: 111.0
# Guild Level: 30, Strength: 30, Dexterity: 40, Damage: 113.5
# Guild Level: 30, Strength: 30, Dexterity: 50, Damage: 116.0
# Guild Level: 30, Strength: 30, Dexterity: 60, Damage: 118.5
# Guild Level: 30, Strength: 40, Dexterity: 10, Damage: 111.0
# Guild Level: 30, Strength: 40, Dexterity: 20, Damage: 113.5
# Guild Level: 30, Strength: 40, Dexterity: 30, Damage: 116.0
# Guild Level: 30, Strength: 40, Dexterity: 40, Damage: 118.5
# Guild Level: 30, Strength: 40, Dexterity: 50, Damage: 121.0
# Guild Level: 30, Strength: 40, Dexterity: 60, Damage: 123.5
# Guild Level: 30, Strength: 50, Dexterity: 10, Damage: 116.0
# Guild Level: 30, Strength: 50, Dexterity: 20, Damage: 118.5
# Guild Level: 30, Strength: 50, Dexterity: 30, Damage: 121.0
# Guild Level: 30, Strength: 50, Dexterity: 40, Damage: 123.5
# Guild Level: 30, Strength: 50, Dexterity: 50, Damage: 126.0
# Guild Level: 30, Strength: 50, Dexterity: 60, Damage: 128.5
# Guild Level: 30, Strength: 60, Dexterity: 10, Damage: 121.0
# Guild Level: 30, Strength: 60, Dexterity: 20, Damage: 123.5
# Guild Level: 30, Strength: 60, Dexterity: 30, Damage: 126.0
# Guild Level: 30, Strength: 60, Dexterity: 40, Damage: 128.5
# Guild Level: 30, Strength: 60, Dexterity: 50, Damage: 131.0
# Guild Level: 30, Strength: 60, Dexterity: 60, Damage: 133.5
