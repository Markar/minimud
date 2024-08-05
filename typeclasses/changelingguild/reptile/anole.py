import math
from random import randint
from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Anole(ChangelingAttack):
    """
    The green anole is often mistaken, and erroneously called,
    the chameleon--although it changes color from green to
    brown, its ability is poor compared to the true chameleon.
    This 'false chameleon' is often sold as the true thing in
    pet shops.
    """

    damage = 1
    energy_cost = 3
    skill = "edged"
    name = "bite"
    speed = 3
    power = 5
    toughness = 5
    dodge = 5

    def at_attack(self, wielder, target, **kwargs):
        """
        The auto attack Cat
        """
        super().at_attack(wielder, target, **kwargs)
        
        bonus = math.ceil(5 + wielder.db.dexterity / 3)
        base_dmg = bonus + wielder.db.guild_level * self.power / 2
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
