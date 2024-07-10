from random import randint, choice
from evennia.prototypes import spawner, prototypes
from string import punctuation
from evennia import AttributeProperty
from evennia.utils import lazy_property, iter_to_str, delay, logger
from evennia.contrib.rpg.traits import TraitHandler
from evennia.contrib.game_systems.cooldowns import CooldownHandler
from evennia.contrib.game_systems.clothing.clothing import (
    ClothedCharacter,
    get_worn_clothes,
)
from commands.elementals import ElementalCmdSet
from typeclasses.characters import PlayerCharacter

class Elemental(PlayerCharacter):
    """
    The base typeclass for non-player characters, implementing behavioral AI.
    """

    def at_object_creation(self):
        self.cmdset.add(ElementalCmdSet, persistent=True)
        super().at_object_creation()
        self.db.guild_level = 1
        self.db.gxp = 0
        self.db.title = "the title less"
        self.db.con_increase_amount = 14
        self.db.hpmax = 50 + 14 * self.db.constitution
        self.db.int_increase_amount = 3
        self.db.epmax = 50 + 3 * self.db.intelligence
        self.db.natural_weapon = {
            "name": "earth_attack",
            "damage_type": "blunt",
            "damage": 12,
            "speed": 3,
            "energy_cost": 10
        }
        self.db.guild = "elemental"
        self.db._wielded = {"left": None, "right": None}
        self.db.emit = 1
        self.db.maxEmit = 2
        self.at_wield(EarthAttack)
        
    def get_display_name(self, looker, **kwargs):
        """
        Adds color to the display name.
        """
        name = super().get_display_name(looker, **kwargs)
        if looker == self:
            # special color for our own name
            return f"|c{name}|n"
        return f"|g{name}|n"    

    # property to mimic weapons
    @property
    def speed(self):
        weapon = self.db.natural_weapon
        return weapon.get("speed", 3)

    def at_wield(self, weapon, **kwargs):
        self.msg(f"You cannot wield weapons.")
        return False
    
    def at_attack(self, wielder, target, **kwargs):
        """
        attack with your natural weapon
        """
        self.msg(f"at_attack in elemental: {self} and {wielder} and {target}")
        weapon = self.db.natural_weapon
        self.msg(f"at_attack in elemental: {weapon}")
        damage = weapon.get("damage", 0)
        speed = weapon.get("speed", 10)
        # attack with your natural attack skill - whatever that is
        result = self.use_skill(weapon.get("skill"), speed=speed)
        # apply the weapon damage as a modifier to skill
        damage = damage * result
        # subtract the energy required to use this
        self.db.ep -= weapon.get("energy_cost", 5)
        if not damage:
            # the attack failed
            self.at_emote(
                f"$conj(swings) $pron(your) {weapon.get('name')} at $you(target), but $conj(misses).",
                mapping={"target": target},
            )
        else:
            verb = weapon.get("damage_type", "hits")
            wielder.at_emote(
                f"$conj({verb}) $you(target) with $pron(your) {weapon.get('name')}.",
                mapping={"target": target},
            )
            # the attack succeeded! apply the damage
            target.at_damage(wielder, damage, weapon.get("damage_type"))
            wielder.db.gxp += 1
        
        wielder.msg(f"[ Cooldown: {speed} seconds ]")
        wielder.cooldowns.add("attack", speed)
        
    def attack(self, target, weapon, **kwargs):
        """
        Execute an attack

        Args:
            target (Object or None): the entity being attacked. if None, attempts to use the combat_target db attribute
            weapon (Object): the object dealing damage
        """
        # can't attack if we're not in combat!
        if not self.in_combat:
            return
        # can't attack if we're fleeing!
        if self.db.fleeing:
            return
        if not weapon.at_pre_attack(self):
            # the method handles its own error messaging
            return

        # if target is not set, use stored target
        if not target:
            # make sure there's a stored target
            if not (target := self.db.combat_target):
                self.msg("You cannot attack nothing.")
                return

        if target.location != self.location:
            self.msg("You don't see your target.")
            return

        print(f"attack with weapon {self} and target {target} and weapon {weapon}")
        # attack with the weapon
        weapon.at_attack(self, target)

        status = self.get_display_status(target)
        self.msg(prompt=status)

        # check if we have auto-attack in settings
        if self.account and (settings := self.account.db.settings):
            if settings.get("auto attack") and (speed := weapon.speed):
                # queue up next attack; use None for target to reference stored target on execution
                delay(speed + 1, self.attack, None, weapon, persistent=True)
                
    def use_rebuild(self):
        """
        Restores health
        """

        hp = self.db.hp
        hpmax = self.db.hpmax
        ep = self.db.ep
        hp_amount = 0
        
        damage = 10 + self.db.guild_level + self.db.wisdom
        cost = damage / 2
        
        if cost > ep:
            return
        
        if hp + damage > hpmax:            
            hp_amount = hpmax-hp
            self.db.hp = hpmax
            self.db.ep -= cost
        else: 
            hp_amount = hpmax-hp
            self.db.hp += max(damage, 0)
            self.db.ep -= cost
            
        self.msg(f"You restore {hp_amount or 0} health for {cost or 0} energy!")
        
    def use_emit(self):
        print(f"args: {self.args.strip()}")
        try:
            power = int(self.args.strip())
            if power == 1 and self.db.guild_level > 0:
                self.db.emit = 1
            if power == 2 and self.db.guild_level > 1:
                self.db.emit = 2
        except ValueError:
            print(f"Not an integer for use_emit")
                
class EarthAttack:
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
        Hit something with your fists!
        """
        if wielder.db.emit == 1:
            self.name = "pebbles"
            damage = 10 + wielder.db.wisdom
            self.energy_cost = 1
            self.speed = 3
            self.emote = f"You rain {self.name} at $you(target), but $conj(misses)."
        if wielder.db.emit == 2:
            self.name = "stones"
            damage = 20 + wielder.db.wisdom
            self.energy_cost = 2
            self.speed = 3
            self.emote = f"You smash {self.name} with $you(target), but $conj(misses)."
            self.emote_hit = f"$conj(swings) $pron(your) {self.name} at $you(target), but $conj(misses).",
            
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
            target.at_damage(wielder, damage, "bludgeon")
        wielder.db.gxp += 1
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)