from random import uniform
from typeclasses.elementalguild.elemental_attack import ElementalAttack

class FireAttack(ElementalAttack):
    """
    Earth elementals are known for their strength and durability. They are
    often found in rocky areas such as mountains and caves, where they can
    blend in with their surroundings. Earth elementals have the ability to
    control the earth and rocks around them, using them to attack their
    enemies. They are also known for their ability to create earthquakes
    and landslides, which can cause massive damage to their foes.
    """
    speed = 3
    emit = 1
    energy_cost = 1

    def _calculate_melee_damage(self, wielder):
        glvl = wielder.db.guild_level
        wis = wielder.db.wisdom
        intel = wielder.db.intelligence
        
        stat_bonus = intel/2 + wis/2
        dmg = stat_bonus
        
        if glvl < 10:
            dmg += 10
        elif glvl < 20:
            dmg += 30
        elif glvl < 30:
            dmg += 60
        elif glvl < 40:
            dmg += 90
        else: 
            dmg += 120
        
        dmg += glvl*3
        
        damage = int(uniform(dmg/2, dmg))
        return damage
    
    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)
        
        if wielder.db.strategy == "melee":
            self.speed = 3
            self._calculate_melee_damage(wielder)
            
        # Subtract energy and apply damage to target before their defenses
        wielder.db.ep -= self.energy_cost
        dmg = self._calculate_melee_damage(wielder)
        target.at_damage(wielder, dmg, "fire", "fire_elemental_melee")
             
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)