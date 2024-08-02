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
    desc = """
    The green anole is often mistaken, and erroneously called,
    the chameleon--although it changes color from green to
    brown, its ability is poor compared to the true chameleon.
    This 'false chameleon' is often sold as the true thing in
    pet shops.
    """
    
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
        damage = 1 + wielder.db.guild_level + math.ceil(wielder.db.dexterity / 3)
        self.energy_cost = 1
        self.speed = 3
        self.emote = f"You bite viciously at $you(target), but miss entirely."
        self.emote_hit = f"You bite glancingly into $you(target), and cause some minor scratches"        
            
        # subtract the energy required to use this
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, damage, "edged")
        super().at_attack(wielder, target, **kwargs)
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)
