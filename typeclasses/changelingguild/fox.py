import math

from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Fox(ChangelingAttack):
    """
    Foxes are small to medium-sized mammals with a bushy tail,
    pointed ears, and a narrow snout. They are known for their
    cunning and agility.
    """

    damage = 10
    energy_cost = 5
    skill = "edged"
    name = "bite"
    speed = 2
    
    def at_pre_attack(self, wielder, **kwargs):
        # make sure we have enough energy left
        if wielder.db.ep < self.energy_cost:
            wielder.msg("You are too tired to attack.")
            return False
        # can't attack if on cooldown
        if not wielder.cooldowns.ready("attack"):
            wielder.msg("You can't attack again yet.")
            return False

        return True

    def at_attack(self, wielder, target, **kwargs):
        """
        The fox's pounce attack
        """
        damage = 15 + math.ceil(wielder.db.strength / 3)
        self.energy_cost = 5
        self.speed = 2
        self.emote = "You pounce at " + str(target) + ", but miss entirely."
        self.emote_hit = "You pounce onto " + str(target) + ", causing some scratches."
            
        # subtract the energy required to use this
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, damage, self.skill)
        super().at_attack(wielder, target, **kwargs)
        wielder.msg("[ Cooldown: " + str(self.speed) + " seconds ]")
        wielder.cooldowns.add("attack", self.speed)
