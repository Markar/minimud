import math
from random import randint

from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Finch(ChangelingAttack):
    """
    The finch is a small bird, typically weighing around 20 grams and measuring
    about 12 centimeters in length. Finches are known for their vibrant colors
    and melodious songs. They are agile fliers and can navigate through dense
    foliage with ease.
    """

    damage = 2
    energy_cost = 2
    skill = "edged"
    name = "peck"
    speed = 2
    power = 4
    toughness = 4
    dodge = 6
    
    def at_attack(self, wielder, target, **kwargs):
        bonus = math.ceil(5 + wielder.db.dexterity / 3)
        base_dmg = bonus + wielder.db.guild_level * self.power / 2
        damage = randint(math.ceil(base_dmg/2), base_dmg)
        
        self.energy_cost = 2
        self.speed = 2
        self.emote = f"You peck viciously at $you(target), but miss entirely."
        self.emote_hit = f"You peck glancingly into $you(target), and cause some minor scratches"        
            
        # subtract the energy required to use this
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, damage, "peck")
        super().at_attack(wielder, target, **kwargs)
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)