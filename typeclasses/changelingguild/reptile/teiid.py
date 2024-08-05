import math
from random import randint

from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Teiid(ChangelingAttack):
    """
    Teiids have flat, elongate scaly tongues that end in two 
    long, smooth points, which they use to secure prey.
    """

    damage = 1
    energy_cost = 3
    skill = "blunt"
    name = "bite"
    speed = 3
    power = 10
    toughness = 8
    dodge = 8
    
    def at_attack(self, wielder, target, **kwargs):
        """
        The auto attack Teiid
        """
        bonus = math.ceil(5 + wielder.db.strength / 3)
        base_dmg = bonus + wielder.db.guild_level * self.power / 2
        damage = randint(math.ceil(base_dmg/2), base_dmg)
        
        self.energy_cost = 1
        self.speed = 3
        self.emote = f"You bite viciously at $you(target), but miss entirely."
        self.emote_hit = f"You bite glancingly into $you(target), and cause some minor scratches"
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, damage, "blunt")
        super().at_attack(wielder, target, **kwargs)
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)