import math
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

    def at_attack(self, wielder, target, **kwargs):
        """
        The auto attack Hummingbird
        """
        self.name = "bite"
        damage = self.db.guild_level + math.ceil(wielder.db.dexterity / 3)
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