import math
from random import randint

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
    power = 2
    toughness = 5
    dodge = 5

    def at_attack(self, wielder, target, **kwargs):
        bonus = math.ceil(5 + wielder.db.strength / 3)
        base_dmg = bonus + wielder.db.guild_level * self.power / 2
        damage = randint(math.ceil(base_dmg/2), base_dmg)
        
        self.energy_cost = 2
        self.speed = 2
        self.emote = f"You try to engulf $you(target), but miss entirely."
        self.emote_hit = f"You engulf $you(target), causing acidic burns and damage."        
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, damage, "engulf")
        super().at_attack(wielder, target, **kwargs)
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)
