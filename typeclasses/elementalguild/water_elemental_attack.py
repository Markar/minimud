from random import uniform
from typeclasses.elementalguild.elemental_attack import ElementalAttack


class WaterAttack(ElementalAttack):
    """
    Water elementals are known for their fluidity and adaptability. They are
    often found in rivers and lakes, where they can move quickly and easily
    through the water. Water elementals have the ability to control water
    and ice, using them to attack their enemies. They are also known for
    their ability to create whirlpools and tidal waves, which can cause
    massive damage to their foes.
    """

    speed = 3
    energy_cost = 3

    def _calculate_melee_damage(self, wielder):
        glvl = wielder.db.guild_level
        wis = wielder.db.wisdom
        intel = wielder.db.intelligence

        stat_bonus = intel / 4 + wis / 2
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

        dmg += 5 + glvl * 2 + stat_bonus

        damage = int(uniform(dmg / 2, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        if wielder.db.strategy == "melee":
            self.speed = 3
            self._calculate_melee_damage(wielder)

        # Subtract energy and apply damage to target before their defenses
        wielder.db.ep -= self.energy_cost
        dmg = self._calculate_melee_damage(wielder)
        target.at_damage(wielder, dmg, "ice", "water_elemental_melee")

        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)
