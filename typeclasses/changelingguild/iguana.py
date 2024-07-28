import math

class Iguana:
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
    emit = 1
    
    def at_pre_attack(self, wielder, **kwargs):
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
        """
        The auto attack Iguana
        """
        self.name = "bite"
        damage = 20 + math.ceil(wielder.db.strength / 3)
        self.energy_cost = 3
        self.speed = 3
        self.emote = f"Your tail catches nothing but air."
        self.emote_hit = f"$pron(your) tail nicks {target}."
            
        # subtract the energy required to use this
        wielder.db.ep -= self.energy_cost
        # if not damage:
        #     # the attack failed
        #     wielder.at_emote(
        #     f"$conj(swings) $pron(your) tail at $you(target), but $conj(misses).",
        #     mapping={"target": target},
        # )
        # else:
        #     wielder.at_emote(
        #         f"{wielder}'s tail $conj(nicks) $you(target).",
        #         mapping={"target": target},
        #     )
            # the attack succeeded! apply the damage
        target.at_damage(wielder, damage, "blunt")
        wielder.db.gxp += 1
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)
        
        # "You dash out of the way of the attack!",
        #  "You barely avoid the attack!",
        #  "The anole dashes out of the way of the attack!\n",
        #  "The anole barely manages to dash out of the way of the attack!\n"