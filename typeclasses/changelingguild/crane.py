import math
from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Crane(ChangelingAttack):
    """
    Cranes are elegant birds known for their grace and beauty. They are
    often found near bodies of water and are known for their long necks
    and distinctive calls.
    """

    damage = 2
    energy_cost = 2
    skill = "blunt"
    name = "bite2"
    speed = 2
    
    def at_attack(self, wielder, target, **kwargs):
        self.name = "bite2"
        damage = 13 + self.db.guild_level + math.ceil(wielder.db.dexterity / 2)
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
