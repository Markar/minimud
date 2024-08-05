import math
from random import randint
from typeclasses.changelingguild.changeling_attack import ChangelingAttack
class Hummingbird(ChangelingAttack):
    """
    The bee hummingbird weighs 2 grams and is 5.5 centimeters,
    or 2 1/8 inches long, making it the world's smallest bird,
    and ranking it with the smallest of mammals.  Hummingbirds
    can fly in all directions, including backward, and may hover
    in place.
    """

    damage = 1
    energy_cost = 3
    skill = "edged"
    name = "bite"
    speed = 3
    power = 1
    toughness = 2
    dodge = 27

    def at_attack(self, wielder, target, **kwargs):
        """
        The auto attack Hummingbird
        """
        bonus = math.ceil(5 + wielder.db.dexterity / 3)
        base_dmg = bonus + wielder.db.guild_level * self.power / 2
        damage = randint(math.ceil(base_dmg/2), base_dmg)
        
        self.energy_cost = 1
        self.speed = 3
        self.emote = f"You bite viciously at $you(target), but miss entirely."
        self.emote_hit = f"You bite glancingly into $you(target), and cause some minor scratches"        
            
        # subtract the energy required to use this
        wielder.db.ep -= self.energy_cost
        if not damage:
            # the attack failed
            wielder.at_emote(
                f"$conj(swings) $pron(your) {self.name} at $you(target), but $conj(misses).",
                mapping={"target": target},
            )
        else:
            wielder.at_emote(
                f"$conj(hits) $you(target) with $pron(your) {self.name}.",
                mapping={"target": target},
            )
            # the attack succeeded! apply the damage
            target.at_damage(wielder, damage, "edged")
        super().at_attack(wielder, target, **kwargs)
        wielder.cooldowns.add("attack", self.speed)