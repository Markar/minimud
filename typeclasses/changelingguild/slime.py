import math

from typeclasses.changelingguild.changeling_attack import ChangelingAttack

class Slime(ChangelingAttack):
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
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, damage, "engulf")
        super().at_attack(wielder, target, **kwargs)
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)
