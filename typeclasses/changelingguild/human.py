from typeclasses.changelingguild.changeling_attack import ChangelingAttack
from random import randint
import math

class Human(ChangelingAttack):
    """
    You know what humans are. 
    """

    damage = 1
    energy_cost = 3
    skill = "blunt"
    name = "punch"
    speed = 3
    power = 3,
    toughness = 3,
    dodge = 3,

    def at_attack(self, wielder, target, **kwargs):
        """
        The auto attack for humans.
        """
        bonus = math.ceil(5 + wielder.db.strength / 3)
        base_dmg = bonus + wielder.db.guild_level * self.power / 2
        damage = randint(int(base_dmg/2), int(base_dmg))
        
        self.energy_cost = 1
        self.speed = 3
        self.emote = f"You punch viciously at $you(target), but miss entirely."
        self.emote_hit = f"You punch glancingly into $you(target), and cause some minor scratches"        
            
        # subtract the energy required to use this
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, damage, "blunt")
        super().at_attack(wielder, target, **kwargs)
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)
