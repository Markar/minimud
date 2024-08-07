from random import randint

from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Elephant(ChangelingAttack):
    """
    The elephant is the largest land animal on Earth. It is known for its
    strength and intelligence, as well as its distinctive trunk and tusks.
    Elephants are herbivores and will eat a variety of foods, including
    grasses, fruits, and leaves. They are social animals and live in groups
    called herds, which are led by a matriarch. Elephants are highly
    territorial and will defend their herds from predators and other
    elephants. They are also known for their distinctive trumpet calls,
    which they use to communicate with each other over long distances.
    """

    energy_cost = 3
    speed = 3
    power = 13
    toughness = 25
    dodge = 7

    def _calculate_tusk_damage(self, wielder):
        str = wielder.db.strength
        stat_bonus = str / 2
        dmg = 10 + stat_bonus + wielder.db.guild_level / 4
        
        damage = randint(int(dmg*2/3), int(dmg))
        return damage
    
    def _calculate_stomp_damage(self, wielder):
        str = wielder.db.strength
        stat_bonus = str / 2
        dmg = 1 + stat_bonus + wielder.db.guild_level / 4
        
        damage = randint(int(dmg*2/3), int(dmg))
        return damage
    
    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)
        
        self.energy_cost = 1
        self.speed = 3
        
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_tusk_damage(wielder), "edged", "tusk")
        target.at_damage(wielder, self._calculate_tusk_damage(wielder), "edged", "tusk")
        target.at_damage(wielder, self._calculate_stomp_damage(wielder), "blunt", "stomp")
        target.at_damage(wielder, self._calculate_stomp_damage(wielder), "blunt", "stomp")
        
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)