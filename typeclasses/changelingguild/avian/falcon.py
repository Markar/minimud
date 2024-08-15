from random import randint, uniform
from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Falcon(ChangelingAttack):
    """
    Falcons are birds of prey known for their speed and agility. They are
    often found in open habitats such as grasslands and deserts, where they hunt
    small mammals and birds. Falcons have sharp talons and beaks, which they
    use to catch and kill their prey. They are also known for their distinctive
    diving flight, which allows them to catch prey in mid-air. Falcons are
    solitary birds and are highly territorial, defending their hunting
    grounds from other birds of prey.
    """

    speed = 2
    power = 14
    toughness = 8
    dodge = 10

    def _calculate_bite_damage(self, wielder):
        dex = wielder.db.dexterity
        str = wielder.db.strength
        stat_bonus = (str+dex)/5
        dmg = 8 + stat_bonus + wielder.db.guild_level
        
        damage = randint(int(dmg*2/3), int(dmg))
        return damage
     
    def _calculate_claw_damage(self, wielder):
        dex = wielder.db.dexterity
        str = wielder.db.strength
        stat_bonus = (str+dex)/5
        dmg = stat_bonus + wielder.db.guild_level / 3
        
        damage = randint(int(dmg*2/3), int(dmg))
        return damage
    
    
    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)
        
        self.energy_cost = 1
        self.speed = 3
        
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_bite_damage(wielder), "edged", "peck")
        target.at_damage(wielder, self._calculate_bite_damage(wielder), "edged", "peck")
        target.at_damage(wielder, self._calculate_claw_damage(wielder), "edged", "claw")
        target.at_damage(wielder, self._calculate_claw_damage(wielder), "edged", "claw")

        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)