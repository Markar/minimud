import math
from random import randint

from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Fox(ChangelingAttack):
    """
    Foxes are small to medium-sized mammals with a bushy tail,
    pointed ears, and a narrow snout. They are known for their
    cunning and agility.
    """

    damage = 10
    energy_cost = 5
    skill = "edged"
    name = "bite"
    speed = 2
    power = 12
    toughness = 9
    dodge = 17
    
    def at_attack(self, wielder, target, **kwargs):
        """
        The fox's pounce attack
        """
        
        bonus = math.ceil(5 + wielder.db.strength / 3)
        base_dmg = bonus + wielder.db.guild_level * self.power / 2
        damage = randint(math.ceil(base_dmg/2), base_dmg)
        
        self.energy_cost = 5
        self.speed = 2
        self.emote = "You pounce at " + str(target) + ", but miss entirely."
        self.emote_hit = "You pounce onto " + str(target) + ", causing some scratches."
            
        # subtract the energy required to use this
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, damage, self.skill)
        super().at_attack(wielder, target, **kwargs)
        wielder.msg("[ Cooldown: " + str(self.speed) + " seconds ]")
        wielder.cooldowns.add("attack", self.speed)
