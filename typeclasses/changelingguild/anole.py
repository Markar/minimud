import math

class Anole:
    """
    The green anole is often mistaken, and erroneously called,
    the chameleon--although it changes color from green to
    brown, its ability is poor compared to the true chameleon.
    This 'false chameleon' is often sold as the true thing in
    pet shops.
    """

    damage = 1
    energy_cost = 3
    skill = "edged"
    name = "bite"
    speed = 3
    emit = 1
    
    def at_pre_attack(self, wielder, **kwargs):
        wielder.msg("|cat_pre_attack in anole")
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
        wielder.msg("|cat_attack in anole")
        """
        The auto attack Anole
        """
        self.name = "bite"
        damage = 5 + math.ceil(wielder.db.dexterity / 3)
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
        wielder.db.gxp += 1
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)
        
        # "You dash out of the way of the attack!",
        #  "You barely avoid the attack!",
        #  "The anole dashes out of the way of the attack!\n",
        #  "The anole barely manages to dash out of the way of the attack!\n"