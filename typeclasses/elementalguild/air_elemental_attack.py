from random import uniform
from typeclasses.elementalguild.elemental_attack import ElementalAttack


class AirAttack(ElementalAttack):
    """
    Air elementals are known for their speed and agility. They are often
    found in open areas such as deserts and grasslands, where they can
    move quickly and easily. Air elementals have the ability to control
    the air around them, using it to attack their enemies. They are also
    known for their ability to create powerful winds and storms, which
    can cause massive damage to their foes.
    """

    speed = 2
    energy_cost = 3

    def _calculate_melee_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.db.strength
        dex = wielder.db.dexterity

        stat_bonus = str / 5 + dex
        dmg = stat_bonus

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

        dmg += glvl * 2

        damage = int(uniform(dmg / 2, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        if wielder.db.strategy == "melee":
            self.speed = 2
            self._calculate_melee_damage(wielder)

        # Subtract energy and apply damage to target before their defenses
        wielder.db.ep -= self.energy_cost
        dmg = self._calculate_melee_damage(wielder)
        target.at_damage(wielder, dmg, "blunt", "air_elemental_melee")

        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)


# Guild Level: 1, Strength: 20, Dexterity: 10, Damage: 15
# Guild Level: 1, Strength: 20, Dexterity: 20, Damage: 25
# Guild Level: 1, Strength: 20, Dexterity: 30, Damage: 35
# Guild Level: 1, Strength: 20, Dexterity: 40, Damage: 45
# Guild Level: 1, Strength: 20, Dexterity: 50, Damage: 55
# Guild Level: 1, Strength: 20, Dexterity: 60, Damage: 65
# Guild Level: 1, Strength: 30, Dexterity: 10, Damage: 17
# Guild Level: 1, Strength: 30, Dexterity: 20, Damage: 27
# Guild Level: 1, Strength: 30, Dexterity: 30, Damage: 37
# Guild Level: 1, Strength: 30, Dexterity: 40, Damage: 47
# Guild Level: 1, Strength: 30, Dexterity: 50, Damage: 57
# Guild Level: 1, Strength: 30, Dexterity: 60, Damage: 67
# Guild Level: 1, Strength: 40, Dexterity: 10, Damage: 19
# Guild Level: 1, Strength: 40, Dexterity: 20, Damage: 29
# Guild Level: 1, Strength: 40, Dexterity: 30, Damage: 39
# Guild Level: 1, Strength: 40, Dexterity: 40, Damage: 49
# Guild Level: 1, Strength: 40, Dexterity: 50, Damage: 59
# Guild Level: 1, Strength: 40, Dexterity: 60, Damage: 69
# Guild Level: 1, Strength: 50, Dexterity: 10, Damage: 21
# Guild Level: 1, Strength: 50, Dexterity: 20, Damage: 31
# Guild Level: 1, Strength: 50, Dexterity: 30, Damage: 41
# Guild Level: 1, Strength: 50, Dexterity: 40, Damage: 51
# Guild Level: 1, Strength: 50, Dexterity: 50, Damage: 61
# Guild Level: 1, Strength: 50, Dexterity: 60, Damage: 71
# Guild Level: 1, Strength: 60, Dexterity: 10, Damage: 23
# Guild Level: 1, Strength: 60, Dexterity: 20, Damage: 33
# Guild Level: 1, Strength: 60, Dexterity: 30, Damage: 43
# Guild Level: 1, Strength: 60, Dexterity: 40, Damage: 53
# Guild Level: 1, Strength: 60, Dexterity: 50, Damage: 63
# Guild Level: 1, Strength: 60, Dexterity: 60, Damage: 73
# ...
# Guild Level: 30, Strength: 20, Dexterity: 10, Damage: 127
# Guild Level: 30, Strength: 20, Dexterity: 20, Damage: 137
# Guild Level: 30, Strength: 20, Dexterity: 30, Damage: 147
# Guild Level: 30, Strength: 20, Dexterity: 40, Damage: 157
# Guild Level: 30, Strength: 20, Dexterity: 50, Damage: 167
# Guild Level: 30, Strength: 20, Dexterity: 60, Damage: 177
# Guild Level: 30, Strength: 30, Dexterity: 10, Damage: 129
# Guild Level: 30, Strength: 30, Dexterity: 20, Damage: 139
# Guild Level: 30, Strength: 30, Dexterity: 30, Damage: 149
# Guild Level: 30, Strength: 30, Dexterity: 40, Damage: 159
# Guild Level: 30, Strength: 30, Dexterity: 50, Damage: 169
# Guild Level: 30, Strength: 30, Dexterity: 60, Damage: 179
# Guild Level: 30, Strength: 40, Dexterity: 10, Damage: 131
# Guild Level: 30, Strength: 40, Dexterity: 20, Damage: 141
# Guild Level: 30, Strength: 40, Dexterity: 30, Damage: 151
# Guild Level: 30, Strength: 40, Dexterity: 40, Damage: 161
# Guild Level: 30, Strength: 40, Dexterity: 50, Damage: 171
# Guild Level: 30, Strength: 40, Dexterity: 60, Damage: 181
# Guild Level: 30, Strength: 50, Dexterity: 10, Damage: 133
# Guild Level: 30, Strength: 50, Dexterity: 20, Damage: 143
# Guild Level: 30, Strength: 50, Dexterity: 30, Damage: 153
# Guild Level: 30, Strength: 50, Dexterity: 40, Damage: 163
# Guild Level: 30, Strength: 50, Dexterity: 50, Damage: 173
# Guild Level: 30, Strength: 50, Dexterity: 60, Damage: 183
# Guild Level: 30, Strength: 60, Dexterity: 10, Damage: 135
# Guild Level: 30, Strength: 60, Dexterity: 20, Damage: 145
# Guild Level: 30, Strength: 60, Dexterity: 30, Damage: 155
# Guild Level: 30, Strength: 60, Dexterity: 40, Damage: 165
# Guild Level: 30, Strength: 60, Dexterity: 50, Damage: 175
# Guild Level: 30, Strength: 60, Dexterity: 60, Damage: 185
