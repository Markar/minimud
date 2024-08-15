import math
from random import randint, uniform

from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Skink(ChangelingAttack):
    """
    Most species are secretive ground dwellers or burrowers,
    and may show such adaptations as a clear ("window") scale
    on the lower eyelid, reduction or loss of limbs, and
    sunken eardrumms.  Some are arboreal or somewhat aquatic.
    """

    energy_cost = 3
    speed = 3
    power = 2
    toughness = 4
    dodge = 5
    
    def _calculate_damage(self, wielder):
        """
        Calculate the damage of the attack
        """
        dex = wielder.db.dexterity
        wis = wielder.db.wisdom
        stat_bonus = (dex+wis) / 5
        base_dmg = 20 + wielder.db.guild_level / 2
        dmg = base_dmg + stat_bonus
        
        damage = int(uniform(dmg/2, dmg))
        return damage
    
    def at_attack(self, wielder, target, **kwargs):
        """
        The auto attack Skink
        """
        
        self.energy_cost = 3
        self.speed = 3   
        
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_damage(wielder), "edged", "bite")
        target.at_damage(wielder, self._calculate_damage(wielder), "edged", "tail")
        
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)
