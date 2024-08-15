from random import randint, uniform

from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class GilaMonster(ChangelingAttack):
    """
    The Gila Monster is a venomous lizard native to the southwestern United States
    and northwestern Mexico. It is known for its bright colors and distinctive
    patterns, as well as its slow movement and powerful bite. Gila Monsters are
    carnivorous and will eat a variety of foods, including small mammals, birds,
    and eggs. They are solitary animals and are highly territorial, defending their
    hunting grounds from other predators. Gila Monsters are also known for their
    distinctive venom, which they use to subdue their prey and defend themselves
    from other predators.
    """

    energy_cost = 3
    speed = 3
    power = 12
    toughness = 12
    dodge = 12
    
    def _calculate_tail_damage(self, wielder):
        dex = wielder.db.dexterity
        str = wielder.db.strength
        stat_bonus = (dex+str) / 3
        base_dmg = 12 + wielder.db.guild_level
        dmg = base_dmg + stat_bonus
        
        damage = int(uniform(dmg/2, dmg))
        return damage
    
    def _calculate_bite_damage(self, wielder):
        dex = wielder.db.dexterity
        str = wielder.db.strength
        stat_bonus = (dex+str) / 3
        base_dmg = 12 + wielder.db.guild_level
        dmg = base_dmg + stat_bonus
        
        damage = int(uniform(dmg/2, dmg))
        return damage
    
    def at_attack(self, wielder, target, **kwargs):

        self.energy_cost = 3
        self.speed = 3   
        
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_damage(wielder), "edged", "bite")
        target.at_damage(wielder, self._calculate_damage(wielder), "blunt", "tail")
        
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)

