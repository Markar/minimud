from random import randint, uniform

from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Lynx(ChangelingAttack):
    """
    Most species are secretive ground dwellers or burrowers,
    and may show such adaptations as a clear ("window") scale
    on the lower eyelid, reduction or loss of limbs, and
    sunken eardrumms.  Some are arboreal or somewhat aquatic.
    """

    energy_cost = 3
    speed = 3
    power = 10
    toughness = 20
    dodge = 15
    
    def _calculate_bite_damage(self, wielder):
        dex = wielder.db.dexterity
        str = wielder.db.strength
        stat_bonus = str / 8 + dex / 6
        dmg = 14 + stat_bonus + wielder.db.guild_level / 3
        
        damage = int(uniform(dmg/2, dmg))
        return damage
    
    def _calculate_claw_damage(self, wielder):
        dex = wielder.db.dexterity
        str = wielder.db.strength
        stat_bonus = str / 8 + dex / 6
        dmg = 7 + stat_bonus + wielder.db.guild_level / 2
        
        damage = int(uniform(dmg/2, dmg))
        return damage
    
    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)
        
        self.energy_cost = 1
        self.speed = 3
        
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_bite_damage(wielder), "edged", "bite")
        target.at_damage(wielder, self._calculate_claw_damage(wielder), "edged", "claw")
        target.at_damage(wielder, self._calculate_claw_damage(wielder), "edged", "claw")
        
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)