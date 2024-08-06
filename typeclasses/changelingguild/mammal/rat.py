import math
from random import randint

from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Rat(ChangelingAttack):
    """
    Rats are small, agile creatures known for their ability to
    scurry through tight spaces and spread disease.
    """

    damage = 1
    energy_cost = 3
    skill = "edged"
    name = "claw"
    speed = 3
    power = 4
    toughness = 6
    dodge = 17

    def at_attack(self, wielder, target, **kwargs):
        """
        The auto attack Rat
        """
        bonus = math.ceil(5 + wielder.db.strength / 3)
        base_dmg = bonus + wielder.db.guild_level * self.power / 2
        damage = randint(math.ceil(base_dmg/2), base_dmg)
        
        self.energy_cost = 3
        self.speed = 3
        self.emote = f"Your tail catches nothing but air."
        self.emote_hit = f"$pron(your) tail nicks {target}."
            
        # subtract the energy required to use this
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, damage, self.skill)
        super().at_attack(wielder, target, **kwargs)
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)
