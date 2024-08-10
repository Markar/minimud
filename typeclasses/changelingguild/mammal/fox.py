from random import randint, uniform

from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Fox(ChangelingAttack):
    """
    Foxes are small to medium-sized mammals with a bushy tail,
    pointed ears, and a narrow snout. They are known for their
    cunning and agility.
    """

    energy_cost = 5
    speed = 2
    power = 12
    toughness = 9
    dodge = 17
    
    def _calculate_bite_damage(self, wielder):
        dex = wielder.db.dexterity
        str = wielder.db.strength
        stat_bonus = (dex+str) / 5
        dmg = 20 + stat_bonus + wielder.db.guild_level / 2
        
        damage = int(uniform(dmg/2, dmg))
        return damage
    
    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)
        
        self.energy_cost = 1
        self.speed = 3
        
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_bite_damage(wielder), "edged", "bite")
        target.at_damage(wielder, self._calculate_bite_damage(wielder), "edged", "bite")
        
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)