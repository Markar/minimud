class FireAttack:
    """
    A dummy "object" class that provides basic combat functionality for unarmed combat
    """

    damage = 1
    energy_cost = 3
    skill = "unarmed"
    name = "landslide"
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
        The auto attack for earth elementals
        """
        if wielder.db.emit == 1:
            self.name = "fire"
            damage = 20 + wielder.db.wisdom
            self.energy_cost = 1
            self.speed = 3
            self.emote = f"You try to rain {self.name} at $you(target), but $conj(misses)."
            self.emote_hit = f"$conj(swings) $pron(your) {self.name} at $you(target), but $conj(misses).",
        if wielder.db.emit == 2:
            self.name = "fire"
            damage = 30 + wielder.db.wisdom
            self.energy_cost = 2
            self.speed = 3
            self.emote = f"You try to throw {self.name} at $you(target), but $conj(misses)."
            self.emote_hit = f"$conj(swings) $pron(your) {self.name} at $you(target), but $conj(misses).",
        if wielder.db.emit == 3:
            self.name = "fire"
            damage = 40 + (wielder.db.wisdom*2)
            self.energy_cost = 3
            self.speed = 3
            self.emote = f"You try to smash {self.name} with $you(target), but $conj(misses)."
            self.emote_hit = f"$conj(swings) $pron(your) {self.name} at $you(target)!",
        if wielder.db.emit == 4:
            self.name = "fire"
            damage = 50 + (wielder.db.wisdom*2)
            self.energy_cost = 4
            self.speed = 3
            self.emote = f"You throw {self.name} at $you(target), but $conj(misses)."
            self.emote_hit = f"$conj(swings) $pron(your) {self.name} at $you(target)!",
        if wielder.db.emit == 5:
            self.name = "spikes of fire"
            damage = 65 + (wielder.db.wisdom*3)
            self.energy_cost = 5
            self.speed = 3
            self.emote = f"You raise {self.name} from the ground $you(target), but $conj(misses)."
            self.emote_hit = f"You raise {self.name} at $you(target)!",
        if wielder.db.emit == 6:
            self.name = "fire"
            damage = 70 + (wielder.db.wisdom*4)
            self.energy_cost = 6
            self.speed = 3
            self.emote = f"Your {self.name} $conj(misses) $pron(your) $you(target)."
            self.emote_hit = f"Your {self.name} flattens $you(target)!",
        if wielder.db.emit == 7:
            self.name = "fire elementals"
            damage = 80 + (wielder.db.wisdom*5)
            self.energy_cost = 7
            self.speed = 3
            self.emote = f"Your {self.name} $conj(misses)."
            self.emote_hit = f"You summon {self.name} to destroy $you(target)!",
            
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
            target.at_damage(wielder, damage, "blunt")
        wielder.db.gxp += 1 + wielder.db.emit
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)