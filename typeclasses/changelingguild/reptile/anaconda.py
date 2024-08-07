from random import randint
from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Anaconda(ChangelingAttack):
    """
    Anacondas are large, non-venomous snakes found in tropical South America.
    They are known for their size and strength, which they use to constrict
    and kill their prey. Anacondas are solitary animals and are highly
    territorial, defending their hunting grounds from other predators. They
    are opportunistic hunters and will eat a variety of foods, including fish,
    birds, and small mammals. Anacondas are also known for their distinctive
    patterned scales, which help them blend in with their surroundings and
    stalk their prey.
    """

    speed = 3
    power = 15
    toughness = 20
    dodge = 2
    
    def _calculate_bite_damage(self, wielder):
        str = wielder.db.strength
        stat_bonus = str / 2
        base_dmg = 5 + wielder.db.guild_level / 2
        dmg = base_dmg + stat_bonus
        
        damage = randint(int(dmg/2), int(dmg))
        return damage
    
    def _calculate_constrict_damage(self, wielder):
        str = wielder.db.strength

        stat_bonus = str/2
        base_dmg = 40 + wielder.db.guild_level*2
        dmg = base_dmg + stat_bonus
        
        damage = randint(int(dmg/2), int(dmg))
        return damage
    
    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)
        
        self.energy_cost = 1
        self.speed = 3
        
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_bite_damage(wielder), "edged", "bite")
        target.at_damage(wielder, self._calculate_constrict_damage(wielder), "blunt", "constrict")
        
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)
        