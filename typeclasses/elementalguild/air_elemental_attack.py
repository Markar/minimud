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
                
        stat_bonus = str/5 + dex
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
            
        dmg += glvl*2 
        
        damage = int(uniform(dmg/2, dmg))
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