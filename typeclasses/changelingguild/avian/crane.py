from random import randint
from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Crane(ChangelingAttack):
    """
    Cranes are elegant birds known for their grace and beauty. They are
    often found near bodies of water and are known for their long necks
    and distinctive calls.
    """

    speed = 2
    power = 10
    toughness = 10
    dodge = 17
    
    def _calculate_bite_damage(self, wielder):
        dex = wielder.db.dexterity
        str = wielder.db.strength
        stat_bonus = str+dex/5
        dmg = 4 + stat_bonus + wielder.db.guild_level
        
        damage = randint(int(dmg/2), int(dmg))
        return damage
     
    def _calculate_wing_damage(self, wielder):
        dex = wielder.db.dexterity
        str = wielder.db.strength
        stat_bonus = str/4 + dex/5
        dmg = stat_bonus + wielder.db.guild_level / 2
        
        damage = randint(int(dmg/2), int(dmg))
        return damage
    
    
    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)
        
        self.energy_cost = 1
        self.speed = 3
        
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_bite_damage(wielder), "edged", "bite")
        target.at_damage(wielder, self._calculate_wing_damage(wielder), "edged", "wing")
        target.at_damage(wielder, self._calculate_wing_damage(wielder), "edged", "wing")

        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)