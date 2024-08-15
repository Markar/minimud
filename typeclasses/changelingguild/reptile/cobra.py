from random import randint, uniform
from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Cobra(ChangelingAttack):
    """
    Cobras are venomous snakes known for their distinctive hoods, which they
    use to intimidate predators. They are found in a variety of habitats,
    including forests, grasslands, and deserts. Cobras are carnivores and
    will eat a variety of prey, including rodents, birds, and other snakes.
    They are highly territorial and will defend their hunting grounds from
    other predators. Cobras are known for their potent venom, which they
    use to immobilize and kill their prey. They are also known for their
    distinctive hissing sound, which they use to warn predators to stay away.
    """

    power = 14
    toughness = 14
    dodge = 10
    
    def _calculate_damage(self, wielder):
        dex = wielder.db.dexterity
        str = wielder.db.strength
        stat_bonus = (str+dex) / 3
        base_dmg = 47 + wielder.db.guild_level * 2
        dmg = base_dmg + stat_bonus
        
        damage = int(uniform(dmg/2, dmg))
        return damage
    
    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)
        
        self.energy_cost = 1
        self.speed = 3
        
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_damage(wielder), "poison", "bite")
        
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)