import math

from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Skink(ChangelingAttack):
    """
    Most species are secretive ground dwellers or burrowers,
    and may show such adaptations as a clear ("window") scale
    on the lower eyelid, reduction or loss of limbs, and
    sunken eardrumms.  Some are arboreal or somewhat aquatic.
    """

    damage = 1
    energy_cost = 3
    skill = "blunt"
    name = "bite"
    speed = 3
    power = 2,
    toughness = 4,
    dodge = 5,
    
    def at_attack(self, wielder, target, **kwargs):
        """
        The auto attack Skink
        """
        self.name = "bite"
        damage = 15 + self.db.guild_level + math.ceil(wielder.db.strength / 3)
        self.energy_cost = 3
        self.speed = 3
        self.emote = f"You bite viciously at $you(target), but miss entirely."
        self.emote_hit = f"You bite glancingly into $you(target), and cause some minor scratches"        
            
        # subtract the energy required to use this
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, damage, self.db.skill)
        super().at_attack(wielder, target, **kwargs)
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)
