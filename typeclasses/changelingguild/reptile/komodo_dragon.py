from random import randint

from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class KomodoDragon(ChangelingAttack):
    """
    Komodo dragons are large, carnivorous reptiles that are native to the
    Indonesian islands of Komodo, Rinca, Flores, and Gili Motang. They are
    known for their powerful jaws and sharp teeth, which they use to catch
    and kill their prey. Komodo dragons are found in tropical forests and
    grasslands, where they hunt deer, pigs, and water buffalo. They are
    opportunistic hunters and will eat a variety of foods, including carrion.
    Komodo dragons are also known for their distinctive armored scales, which
    protect them from other predators and help them blend in with their
    surroundings. They are solitary animals and are highly territorial,
    defending their hunting grounds from other predators.
    """

    energy_cost = 3
    speed = 3
    power = 18
    toughness = 15
    dodge = 12
    
    def _calculate_tail_damage(self, wielder):
        dex = wielder.db.dexterity
        str = wielder.db.strength
        stat_bonus = (dex+str) / 2
        base_dmg = 10 + wielder.db.guild_level * 4
        dmg = base_dmg + stat_bonus
        
        damage = randint(int(dmg/2), int(dmg))
        return damage
    
    def _calculate_bite_damage(self, wielder):
        dex = wielder.db.dexterity
        str = wielder.db.strength
        stat_bonus = (dex+str) / 2
        base_dmg = 40 + wielder.db.guild_level * 3
        dmg = base_dmg + stat_bonus
        
        damage = randint(int(dmg/2), int(dmg))
        return damage
    
    def at_attack(self, wielder, target, **kwargs):

        self.energy_cost = 3
        self.speed = 3   
        
        wielder.db.ep -= self.energy_cost
        if randint(0,1) == 0:
            target.at_damage(wielder, self._calculate_damage(wielder), "edged", "bite")
        else: 
            target.at_damage(wielder, self._calculate_damage(wielder), "blunt", "tail")
        
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)

