import math
from random import randint

from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Wolf(ChangelingAttack):
    """
    The wolf is a carnivorous mammal that is known for its social behavior and hunting skills.
    Wolves are highly adaptable and can be found in various habitats, including forests, tundra,
    and grasslands. They have sharp teeth and strong jaws, which they use to capture and kill
    their prey. Wolves are also excellent runners and can reach speeds of up to 35 miles per hour.
    They live in packs and have a complex social structure, with an alpha male and female leading
    the group. Wolves are highly intelligent and have a wide range of vocalizations for communication.
    """

    damage = 1
    energy_cost = 3
    skill = "edged"
    name = "bite"
    speed = 3
    power = 17
    toughness = 14
    dodge = 14
    
    def at_attack(self, wielder, target, **kwargs):
        """
        The wolf's attack method
        """
        bonus = math.ceil(5 + wielder.db.strength / 3)
        base_dmg = bonus + (wielder.db.guild_level * self.power)/2
        damage = randint(math.ceil(base_dmg/2), base_dmg)
        
        self.energy_cost = 3
        self.speed = 3
        self.emote = "You lunge at " + str(target) + ", but miss entirely."
        self.emote_hit = "You sink your teeth into " + str(target) + ", causing some minor injuries"        
        
        # subtract the energy required to use this
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, damage, self.skill)
        super().at_attack(wielder, target, **kwargs)
        wielder.msg("[ Cooldown: " + str(self.speed) + " seconds ]")
        wielder.cooldowns.add("attack", self.speed)
