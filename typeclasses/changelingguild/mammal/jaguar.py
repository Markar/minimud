from random import randint, uniform

from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Jaguar(ChangelingAttack):
    """
    Jaguars are large cats known for their strength and agility. They are
    often found in tropical rainforests and grasslands, where they hunt
    large mammals and birds. Jaguars have sharp claws and powerful jaws,
    which they use to catch and kill their prey. They are also known for
    their distinctive spots and long tail, which help them blend in with
    their surroundings and stalk their prey. Jaguars are solitary animals
    and are highly territorial, defending their hunting grounds from other
    predators. They are opportunistic hunters and will eat a variety of
    foods, including deer, capybaras, and caimans.
    """

    energy_cost = 3
    speed = 3
    power = 22
    toughness = 17
    dodge = 6

    def _calculate_claw_damage(self, wielder):
        str = wielder.db.strength
        dex = wielder.db.dexterity
        stat_bonus = str / 4 + dex / 4
        dmg = 11 + stat_bonus + wielder.db.guild_level / 2
        
        damage = randint(int(dmg*2/3), int(dmg))
        return damage
    
    def _calculate_bite_damage(self, wielder):
        str = wielder.db.strength
        dex = wielder.db.dexterity
        stat_bonus = str / 4 + dex / 4
        dmg = 21 + stat_bonus + wielder.db.guild_level / 2
        
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