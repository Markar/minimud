from random import randint, uniform
from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Boa(ChangelingAttack):
    """
    Most species are secretive ground dwellers or burrowers,
    and may show such adaptations as a clear ("window") scale
    on the lower eyelid, reduction or loss of limbs, and
    sunken eardrumms.  Some are arboreal or somewhat aquatic.
    """

    damage = 1
    energy_cost = 3
    speed = 3
    power = 16
    toughness = 13
    dodge = 6
    
    def _calculate_bite_damage(self, wielder):
        str = wielder.db.strength
        stat_bonus = str / 3
        base_dmg = 10 + wielder.db.guild_level / 3
        dmg = base_dmg + stat_bonus
        
        damage = int(uniform(dmg/2, dmg))
        return damage
    
    def _calculate_constrict_damage(self, wielder):
        str = wielder.db.strength

        stat_bonus = str/3
        base_dmg = 28 + wielder.db.guild_level*3/2
        dmg = base_dmg + stat_bonus
        
        damage = int(uniform(dmg/2, dmg))
        return damage
    
    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)
        
        self.energy_cost = 1
        self.speed = 3
        
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_bite_damage(wielder), "edged", "bite")
        target.at_damage(wielder, self._calculate_constrict_damage(wielder), "blunt", "constrict")
        
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)
        