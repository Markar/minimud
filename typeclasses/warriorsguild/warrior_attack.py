class WarriorAttack:
    """
    All warrior attacks inherit from this one
    """

    skill = "edged"
    name = "weapon"
    speed = 3
    gxp_rate = 5
    skill_gxp_rate = 5

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
        The auto attack for elementals. Only put things that are shared
        between all forms here.
        """
        wielder.db.gxp += self.gxp_rate
        wielder.db.skill_gxp += self.skill_gxp_rate
