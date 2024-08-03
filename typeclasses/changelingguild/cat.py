import math
from random import randint
from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Cat(ChangelingAttack):
    """
    Cats are small, carnivorous mammals that are often kept as pets.
    They are known for their agility, sharp claws, and ability to
    land on their feet. Cats are typically solitary animals and
    are known for their independent nature. They are also known
    for their grooming behavior and their ability to purr.
    """

    damage = 1
    energy_cost = 3
    skill = "blunt"
    name = "claw"
    speed = 3
    
    def at_attack(self, wielder, target, **kwargs):
        """
        The auto attack Cat
        """
        super().at_attack(wielder, target, **kwargs)
        base_dmg = 5 + wielder.db.guild_level + math.ceil(wielder.db.dexterity / 3)
        damage = randint(math.ceil(base_dmg/2), base_dmg)
        self.energy_cost = 3
        self.speed = 3
        self.emote = "You scratch at " + str(target) + ", but miss entirely."
        self.emote_hit = "You scratch into " + str(target) + ", and cause some minor scratches"        
            
        # subtract the energy required to use this
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, damage, self.skill)
        wielder.msg("[ Cooldown: " + str(self.speed) + " seconds ]")
        wielder.cooldowns.add("attack", self.speed)
