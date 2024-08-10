from random import randint, uniform
from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Toaster(ChangelingAttack):
    """
    // Toaster
//  3 attacks : burn, burn, pop up
//  stat bonus is (wis/2)
//  base burn damage is guild_level/2 + 25
//  base pop up damage is guild_level/2
//  Tot: 2*(25 + 15 + 25) + (25 + 15)  = 170
// Bmax: 2*(12 + 16 + 25) + (12 + 16)  = 134
//  Avg: 2*(25) + (13)                 = 63

    """

    speed = 2
    power = 2
    toughness = 3
    dodge = 5
    
    def _calculate_burn_damage(self, wielder):
        wis = wielder.db.wisdom
        stat_bonus = wis/2
        dmg = 25 + stat_bonus + wielder.db.guild_level / 2
        
        damage = int(uniform(dmg/2, dmg))
        return damage
    
    def _calculate_popup_damage(self, wielder):
        wis = wielder.db.wisdom
        stat_bonus = wis/2
        dmg = stat_bonus + wielder.db.guild_level / 2
        
        damage = int(uniform(dmg/2, dmg))
        return damage
    
    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)
        
        self.energy_cost = 1
        self.speed = 3
        
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_damage(wielder), "fire", "burn")
        target.at_damage(wielder, self._calculate_popup_damage(wielder), "fire", "toast_attack")
        target.at_damage(wielder, self._calculate_popup_damage(wielder), "fire", "toast_attack")
        
        

        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)