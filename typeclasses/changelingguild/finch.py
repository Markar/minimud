import math

class Finch:
    """
    The finch is a small bird, typically weighing around 20 grams and measuring
    about 12 centimeters in length. Finches are known for their vibrant colors
    and melodious songs. They are agile fliers and can navigate through dense
    foliage with ease.
    """

    damage = 2
    energy_cost = 2
    skill = "edged"
    name = "peck"
    speed = 2
    
    def at_pre_attack(self, wielder, **kwargs):
        wielder.msg("|cat_pre_attack in finch")
        # make sure we have enough strength left
        print(f"at_pre_attack on weapon: {wielder} and {wielder.db.ep} and self {self}")
        if wielder.db.ep < self.energy_cost:
            wielder.msg("You are too tired to hit anything.")
            return False
        # can't attack if on cooldown
        if not wielder.cooldowns.ready("attack"):
            wielder.msg("You can't attack again yet.")
            return False

        return True

    def at_attack(self, wielder, target, **kwargs):
        wielder.msg("|cat_attack in finch")
        """
        The auto attack Finch
        """
        self.name = "peck"
        damage = 3 + math.ceil(wielder.db.dexterity / 2)
        self.energy_cost = 2
        self.speed = 2
        self.emote = f"You peck viciously at $you(target), but miss entirely."
        self.emote_hit = f"You peck glancingly into $you(target), and cause some minor scratches"        
            
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
            target.at_damage(wielder, damage, "peck")
        wielder.db.gxp += 1
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)