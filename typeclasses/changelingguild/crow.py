import math

from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Crow(ChangelingAttack):
    """
    Crows are intelligent birds known for their problem-solving
    abilities and adaptability. They are often found in urban
    and suburban environments and are known for their loud cawing
    and scavenging behavior.
    """

    damage = 2
    energy_cost = 2
    skill = "edged"
    name = "claw"
    speed = 2
    
    def at_attack(self, wielder, target, **kwargs):
        self.name = "claw"
        damage = 10 + self.db.guild_level + math.ceil(wielder.db.dexterity / 2)
        self.energy_cost = 2
        self.speed = 2
        self.emote = f"You peck viciously at $you(target), but miss entirely."
        self.emote_hit = f"You peck glancingly into $you(target), and cause some minor scratches"        
            
        # subtract the energy required to use this
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, damage, "claw")
        super().at_attack(wielder, target, **kwargs)
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)
