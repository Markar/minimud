import math

class Slime:
    """
    The slime is a gelatinous creature that can change its shape
    and size at will. It is often found in dark, damp places and
    can engulf its prey with its sticky, acidic body.
    """

    damage = 2
    energy_cost = 2
    skill = "acid"
    name = "engulf"
    speed = 2
    emit = 1
    
    def at_pre_attack(self, wielder, **kwargs):
        wielder.msg("|cat_pre_attack in slime")
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
        wielder.msg("|cat_attack in slime")
        """
        The auto attack Slime
        """
        self.name = "engulf"
        damage = 4 + math.ceil(wielder.db.dexterity / 2)
        self.energy_cost = 2
        self.speed = 2
        self.emote = f"You try to engulf $you(target), but miss entirely."
        self.emote_hit = f"You engulf $you(target), causing acidic burns and damage."        
            
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
            target.at_damage(wielder, damage, "acidic touch")
        wielder.db.gxp += 1
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)
