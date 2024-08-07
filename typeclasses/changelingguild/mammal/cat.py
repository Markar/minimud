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

    energy_cost = 3
    speed = 3
    power = 5
    toughness = 20
    dodge = 15
    
    def _calculate_bite_damage(self, wielder):
        dex = wielder.db.dexterity
        str = wielder.db.strength
        stat_bonus = (dex+str) / 8
        dmg = 10 + stat_bonus + wielder.db.guild_level / 3
        
        damage = randint(int(dmg/2), int(dmg))
        return damage
    
    def _calculate_claw_damage(self, wielder):
        dex = wielder.db.dexterity
        str = wielder.db.strength
        stat_bonus = (dex+str) / 10
        dmg = 7 + stat_bonus + wielder.db.guild_level / 3
        
        damage = randint(int(dmg/2), int(dmg))
        return damage
    
    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)
        
        self.energy_cost = 1
        self.speed = 3
        
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_bite_damage(wielder), "edged", "bite")
        target.at_damage(wielder, self._calculate_claw_damage(wielder), "edged", "claw")
        target.at_damage(wielder, self._calculate_claw_damage(wielder), "edged", "claw")
        
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)