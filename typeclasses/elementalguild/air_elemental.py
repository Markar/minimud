class AirAttack:
    """
    The default attack for air elementals
    """

    damage = 1
    energy_cost = 3
    skill = "unarmed"
    name = "gust"
    speed = 1
    emit = 1
    damage_type = "blunt"
    
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
        The auto attack for air elementals
        """
        if wielder.db.emit == 1:
            self.name = "gust"
            damage = 20 + wielder.db.wisdom
            self.energy_cost = 1
            self.speed = 1
            self.emote = f"You try to hit $you(target) with a {self.name} of wind, but $conj(misses)."
            self.emote_hit = f"$conj(send) $pron(your) {self.name} at $you(target)!.",
        if wielder.db.emit == 2:
            self.name = "hail"
            damage = 30 + wielder.db.wisdom
            self.energy_cost = 2
            self.speed = 1
            self.emote = f"You try to pour {self.name} on $you(target), but $conj(misses)."
            self.emote_hit = f"$conj(pour) $pron(your) {self.name} on $you(target)!",
        if wielder.db.emit == 3:
            self.name = "hurricane"
            damage = 40 + (wielder.db.wisdom*2)
            self.energy_cost = 3
            self.speed = 1
            self.emote = f"Your {self.name} flings debris at $you(target), but $conj(misses)."
            self.emote_hit = f"$pron(your) {self.name} flinks debris at $you(target)!",
        if wielder.db.emit == 4:
            self.name = "boulders"
            damage = 50 + (wielder.db.wisdom*2)
            self.energy_cost = 4
            self.speed = 1
            self.emote = f"You throw {self.name} at $you(target), but $conj(misses)."
            self.emote_hit = f"$conj(swings) $pron(your) {self.name} at $you(target)!",
        if wielder.db.emit == 5:
            self.name = "lightning"
            damage = 65 + (wielder.db.wisdom*3)
            self.energy_cost = 5
            self.speed = 1
            self.emote = f"You call {self.name} from the sky $you(target), but $conj(misses)."
            self.emote_hit = f"You call {self.name} to strike $you(target)!",
            self.damagetype = "lightning"
        if wielder.db.emit == 6:
            self.name = "energy bolts"
            damage = 70 + (wielder.db.wisdom*4)
            self.energy_cost = 6
            self.speed = 1
            self.emote = f"Your {self.name} $conj(misses) $pron(your) $you(target)."
            self.emote_hit = f"Your {self.name} blasts into $you(target)!",
            self.damage_type = "energy"
        if wielder.db.emit == 7:
            self.name = "air elementals"
            damage = 80 + (wielder.db.wisdom*5)
            self.energy_cost = 7
            self.speed = 1
            self.emote = f"Your {self.name} $conj(misses)."
            self.emote_hit = f"You summon an army of {self.name} to destroy $you(target)!",
            
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
            target.at_damage(wielder, damage, self.damage_type)
            
        wielder.db.gxp += 1 + wielder.db.emit
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)