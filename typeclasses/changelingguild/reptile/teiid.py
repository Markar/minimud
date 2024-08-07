import math
from random import randint

from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Teiid(ChangelingAttack):
    """
    Teiid lizards are a family of lizards native to the Americas. They are
    found from the southwestern United States through Mexico, Central America,
    and into South America. The common name for members of this family is the
    whiptail lizards. They are long and slender lizards, with laterally flattened
    bodies and long tails. They are diurnal, and are often seen basking in the sun
    on rocks or walls. They are insectivorous, and are known for their speed and
    agility. They are also known for their ability to break off their tails to
    escape predators, and then regrow them. They are also known for their ability
    to reproduce asexually.
    """

    damage = 1
    energy_cost = 3
    speed = 3
    power = 10
    toughness = 8
    dodge = 8
    
    def _calculate_damage(self, wielder):
        """
        Calculate the damage of the attack
        """
        dex = wielder.db.dexterity
        wis = wielder.db.wisdom
        stat_bonus = (dex+wis) / 5
        base_dmg = 15 + wielder.db.guild_level / 2
        dmg = base_dmg + stat_bonus
        
        damage = randint(int(dmg/2), int(dmg))
        return damage
    
    def at_attack(self, wielder, target, **kwargs):
        """
        The auto attack of Teiid
        """
        super().at_attack(wielder, target, **kwargs)
        
        self.energy_cost = 1
        self.speed = 3
        
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, self._calculate_damage(wielder), "edged", "bite")
        target.at_damage(wielder, self._calculate_damage(wielder), "edged", "tail")
        
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)