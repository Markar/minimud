from random import randint
from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Condor(ChangelingAttack):
    """
    Condors are birds of prey known for their speed and agility. They are
    often found in open habitats such as grasslands and deserts, where they hunt
    small mammals and birds. Condors have sharp talons and beaks, which they
    use to catch and kill their prey. They are also known for their distinctive
    diving flight, which allows them to catch prey in mid-air. Condors are
    solitary birds and are highly territorial, defending their hunting
    grounds from other birds of prey.
    """

    speed = 2
    power = 15
    toughness = 15
    dodge = 15

    def _calculate_tackle_damage(self, wielder):
        dex = wielder.db.dexterity
        stat_bonus = dex/3
        dmg = 38 + stat_bonus + wielder.db.guild_level * 3/2
        
        damage = randint(int(dmg/2), int(dmg))
        return damage
     
    def _calculate_bite_damage(self, wielder):
        dex = wielder.db.dexterity
        str = wielder.db.strength
        stat_bonus = (str+dex)/5
        dmg = 30 + stat_bonus + wielder.db.guild_level / 2
        
        damage = randint(int(dmg/2), int(dmg))
        return damage
    
    
    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)
        
        self.energy_cost = 1
        self.speed = 3
        
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_bite_damage(wielder), "edged", "bite")
        target.at_damage(wielder, self._calculate_tackle_damage(wielder), "blunt", "tackle")

        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)