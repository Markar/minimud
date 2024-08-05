import math

from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Iguana(ChangelingAttack):
    """
    Unlike several of the other types of lizard, iguanas and
    other iguanid lizards display fairly complex courtship and
    terretorial behavioral rites.
    """

    damage = 1
    energy_cost = 3
    skill = "blunt"
    name = "tail"
    speed = 3
    power = 8,
    toughness = 10,
    dodge = 9,
    
    def at_attack(self, wielder, target, **kwargs):
        """
        The auto attack Iguana
        """
        damage = 20 + self.db.guild_level + math.ceil(wielder.db.strength / 3)
        self.energy_cost = 3
        self.speed = 3
        self.emote = f"Your tail catches nothing but air."
        self.emote_hit = f"$pron(your) tail nicks {target}."
            
        # subtract the energy required to use this
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, damage, self.skill)
        super().at_attack(wielder, target, **kwargs)
        wielder.msg("[ Cooldown: " + str(self.speed) + " seconds ]")
        wielder.cooldowns.add("attack", self.speed)

