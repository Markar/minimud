from random import randint, uniform

from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Lion(ChangelingAttack):
    """
    The lion is a large, powerful cat known for its strength and ferocity. 
    Lions are social animals and live in groups called prides, which are 
    led by a dominant male. This male lion is responsible for protecting 
    the pride and its territory, while the lionesses do most of the hunting.
    The pride's social structure is complex, with strong bonds formed 
    between members, ensuring the survival and success of the group.
    """

    energy_cost = 3
    speed = 3
    power = 16
    toughness = 14
    dodge = 15
    
    def _calculate_claw_damage(self, wielder):
        str = wielder.db.strength
        dex = wielder.db.dexterity
        stat_bonus = str / 4 + dex / 4
        dmg = stat_bonus + wielder.db.guild_level
        
        damage = randint(int(dmg*2/3), int(dmg))
        return damage
    
    def _calculate_bite_damage(self, wielder):
        str = wielder.db.strength
        dex = wielder.db.dexterity
        stat_bonus = str / 4 + dex / 4
        dmg = 33 + stat_bonus + wielder.db.guild_level / 2
        
        damage = randint(int(dmg*2/3), int(dmg))
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