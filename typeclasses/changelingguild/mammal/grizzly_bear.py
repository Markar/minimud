from random import randint, uniform

from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class GrizzlyBear(ChangelingAttack):
    """
    The grizzly bear is a large mammal that is native to North America. It is known for its
    strength and agility, as well as its ability to climb trees and swim. Grizzly bears are
    omnivorous and will eat a variety of foods, including berries, nuts, fish, and small
    mammals. They are solitary animals and are highly territorial, defending their hunting
    grounds from other bears. Grizzly bears are also known for their distinctive hump on their
    shoulders, which is made of muscle and helps them dig and climb.
    """

    energy_cost = 3
    speed = 3
    power = 16
    toughness = 22
    dodge = 3

    def _calculate_bite_damage(self, wielder):
        str = wielder.db.strength
        stat_bonus = str / 4
        dmg = 23 + stat_bonus + wielder.db.guild_level / 2
        
        damage = int(uniform(dmg/2, dmg))
        return damage
    
    def _calculate_claw_damage(self, wielder):
        str = wielder.db.strength
        stat_bonus = str / 4
        dmg = 7 + stat_bonus + wielder.db.guild_level / 3
        
        damage = int(uniform(dmg/2, dmg))
        return damage
    
    def _calculate_hug_damage(self, wielder):
        str = wielder.db.strength
        stat_bonus = str / 4
        dmg = 28 + stat_bonus + wielder.db.guild_level * 2
        
        damage = int(uniform(dmg/2, dmg))
        return damage
    
    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)
        
        self.energy_cost = 1
        self.speed = 3
        
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_bite_damage(wielder), "edged", "bite")
        target.at_damage(wielder, self._calculate_claw_damage(wielder), "edged", "claw")
        target.at_damage(wielder, self._calculate_claw_damage(wielder), "edged", "claw")
        target.at_damage(wielder, self._calculate_hug_damage(wielder), "blunt", "hug")
        
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)