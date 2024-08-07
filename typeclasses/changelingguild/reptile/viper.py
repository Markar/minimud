import math
from random import randint
from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Viper(ChangelingAttack):
    """
    Most species are secretive ground dwellers or burrowers,
    and may show such adaptations as a clear ("window") scale
    on the lower eyelid, reduction or loss of limbs, and
    sunken eardrumms.  Some are arboreal or somewhat aquatic.
    """

    damage = 1
    energy_cost = 3
    speed = 3
    power = 20
    toughness = 17
    dodge = 6
    
    def _calculate_damage(self, wielder):
        """
        Calculate the damage of the attack
        """
        dex = wielder.db.dexterity
        str = wielder.db.strength
        stat_bonus = (str+dex) / 4
        base_dmg = 15 + wielder.db.guild_level * 3
        dmg = base_dmg + stat_bonus
        
        damage = randint(int(dmg/2), int(dmg))
        return damage
    
    def at_attack(self, wielder, target, **kwargs):
        """
        The auto attack of Teiid
        """
        super().at_attack(wielder, target, **kwargs)
        
        self.energy_cost = 1
        self.speed = 3
        
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_damage(wielder), "poison", "bite")
        
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)