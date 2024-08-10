from random import uniform
from typeclasses.elementalguild.elemental_attack import ElementalAttack
class EarthAttack(ElementalAttack):
    """
    Earth elementals are known for their strength and durability. They are
    often found in rocky areas such as mountains and caves, where they can
    blend in with their surroundings. Earth elementals have the ability to
    control the earth and rocks around them, using them to attack their
    enemies. They are also known for their ability to create earthquakes
    and landslides, which can cause massive damage to their foes.
    """
    speed = 3
    emit = 1

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)
        
        if wielder.db.emit == 1:
            self.name = "pebbles"
            damage = 20 + wielder.db.wisdom
            self.energy_cost = 1
            self.speed = 3
        if wielder.db.emit == 2:
            self.name = "stones"
            damage = 30 + wielder.db.wisdom
            self.energy_cost = 2
            self.speed = 3
            self.emote = f"You try to throw {self.name} at $you(target), but $conj(misses)."
            self.emote_hit = f"$conj(swings) $pron(your) {self.name} at $you(target), but $conj(misses).",
        if wielder.db.emit == 3:
            self.name = "rocks"
            damage = 40 + (wielder.db.wisdom*2)
            self.energy_cost = 3
            self.speed = 3
            self.emote = f"You try to smash {self.name} with $you(target), but $conj(misses)."
            self.emote_hit = f"$conj(swings) $pron(your) {self.name} at $you(target)!",
        if wielder.db.emit == 4:
            self.name = "boulders"
            damage = 50 + (wielder.db.wisdom*2)
            self.energy_cost = 4
            self.speed = 3
            self.emote = f"You throw {self.name} at $you(target), but $conj(misses)."
            self.emote_hit = f"$conj(swings) $pron(your) {self.name} at $you(target)!",
        if wielder.db.emit == 5:
            self.name = "spikes of earth"
            damage = 65 + (wielder.db.wisdom*3)
            self.energy_cost = 5
            self.speed = 3
            self.emote = f"You raise {self.name} from the ground $you(target), but $conj(misses)."
            self.emote_hit = f"You raise {self.name} at $you(target)!",
        if wielder.db.emit == 6:
            self.name = "landslide"
            damage = 70 + (wielder.db.wisdom*4)
            self.energy_cost = 6
            self.speed = 3
            self.emote = f"Your {self.name} $conj(misses) $pron(your) $you(target)."
            self.emote_hit = f"Your {self.name} flattens $you(target)!",
        if wielder.db.emit == 7:
            self.name = "earth elementals"
            damage = 80 + (wielder.db.wisdom*5)
            self.energy_cost = 7
            self.speed = 3
            self.emote = f"Your {self.name} $conj(misses)."
            self.emote_hit = f"You summon {self.name} to destroy $you(target)!",
            
        # Subtract energy and apply damage to target before their defenses
        wielder.db.ep -= self.energy_cost
        target.at_damage(wielder, damage, "blunt", "earth_elemental_melee")
             
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)