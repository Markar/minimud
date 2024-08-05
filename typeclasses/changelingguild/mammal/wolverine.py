import math
from random import randint

from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Wolverine(ChangelingAttack):
    """
    The wolverine is a stocky and muscular carnivorous mammal that resembles a small bear.
    It is known for its strength, aggression, and tenacity. Wolverines are solitary animals
    that inhabit remote forests and tundra regions. They have sharp claws and powerful jaws,
    which they use to hunt and scavenge for food. Wolverines are also excellent climbers and
    swimmers, allowing them to navigate various terrains. Despite their small size, they are
    feared by many animals due to their ferocity and ability to take down prey much larger than
    themselves.
    """

    damage = 1
    energy_cost = 3
    skill = "edged"
    name = "claw"
    speed = 3
    power = 22
    toughness = 10
    dodge = 6
    
    def at_attack(self, wielder, target, **kwargs):
        """
        The auto attack Boa
        """
        bonus = math.ceil(5 + wielder.db.strength / 3)
        base_dmg = bonus + wielder.db.guild_level * self.power / 2
        damage = randint(math.ceil(base_dmg/2), base_dmg)
        
        self.energy_cost = 3
        self.speed = 3
        self.emote = "You bite viciously at " + str(target) + ", but miss entirely."
        self.emote_hit = "You bite glancingly into " + str(target) + ", and cause some minor scratches"        
        
        # subtract the energy required to use this
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, damage, self.skill)
        super().at_attack(wielder, target, **kwargs)
        wielder.msg("[ Cooldown: " + str(self.speed) + " seconds ]")
        wielder.cooldowns.add("attack", self.speed)
