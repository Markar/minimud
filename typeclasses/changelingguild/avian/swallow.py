import math
from random import randint
from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Swallow(ChangelingAttack):
    """
    Swallows are small, fast birds that are known for their
    agility and quick reflexes. They are often found in
    rural and suburban environments and are known for their
    graceful flight and aerial acrobatics.
    """

    damage = 2
    energy_cost = 2
    skill = "edged"
    name = "bite2"
    speed = 2
    power = 2,
    toughness = 3,
    dodge = 5,
    
    def at_attack(self, wielder, target, **kwargs):
        bonus = math.ceil(5 + wielder.db.strength / 3)
        base_dmg = bonus + wielder.db.guild_level * self.power / 2
        damage = randint(math.ceil(base_dmg/2), base_dmg)
        
        self.energy_cost = 2
        self.speed = 2
        self.emote = f"You peck viciously at $you(target), but miss entirely."
        self.emote_hit = f"You peck glancingly into $you(target), and cause some minor scratches"        
            
        # subtract the energy required to use this
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, damage, "bite2")
        super().at_attack(wielder, target, **kwargs)
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)