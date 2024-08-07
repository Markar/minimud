from random import randint, choice
from evennia.prototypes import spawner, prototypes
from string import punctuation
from evennia import AttributeProperty
from evennia.utils import lazy_property, iter_to_str, delay, logger
from evennia.contrib.rpg.traits import TraitHandler
from evennia.contrib.game_systems.cooldowns import CooldownHandler
from evennia import TICKER_HANDLER as tickerhandler
from evennia.contrib.game_systems.clothing.clothing import (
    ClothedCharacter,
    get_worn_clothes,
)
from commands.elemental_cmds import ElementalCmdSet
from typeclasses.characters import PlayerCharacter
from typeclasses.elementalguild.air_elemental import AirAttack
from typeclasses.elementalguild.earth_elemental import EarthAttack
from typeclasses.elementalguild.fire_elemental import FireAttack
from typeclasses.elementalguild.water_elemental import WaterAttack

class Elemental(PlayerCharacter):
    """
    The base typeclass for non-player characters, implementing behavioral AI.
    """

    def at_object_creation(self):
        self.cmdset.add(ElementalCmdSet, persistent=True)
        super().at_object_creation()
        self.db.guild_level = 1
        self.db.gxp = 0
        self.db.title = "the novice Elemental"
        self.db.con_increase_amount = 12
        self.db.hpmax = 50 + (12 * self.db.constitution)
        self.db.int_increase_amount = 5
        self.db.fpmax = 50 + (5 * self.db.intelligence)
        self.db.natural_weapon = {
            "name": "earth_attack",
            "damage_type": "blunt",
            "damage": 12,
            "speed": 3,
            "energy_cost": 10
        }
        self.db.guild = "elemental"
        self.db.subguild = "earth"
        self.db._wielded = {"left": None, "right": None}
        self.db.emit = 1
        self.db.maxEmit = 1
        self.db.hpregen = 1
        self.db.fpregen = 1
        self.db.epregen = 1
        self.at_wield(EarthAttack)
        tickerhandler.add(interval=3, callback=self.at_tick, idstring="ticker1", persistent=True)
    
    def addhp(self, amount):
        hp = self.db.hp
        hpmax = self.db.hpmax
        if hp >= hpmax:
            return
        if hp < hpmax + amount:
            self.db.hp += amount
    
    def addfp(self, amount):
        fp = self.db.fp
        fpmax = self.db.fpmax
        if fp >= fpmax:
            return
        if fp < fpmax + amount:
            self.db.fp += amount
    
    def addep(self, amount):
        ep = self.db.ep
        epmax = self.db.epmax
        if ep >= epmax:
            return
        if ep < epmax + amount:
            self.db.ep += amount
        
    def at_tick(self):
        self.addhp(1)
        self.addfp(1)
        self.addep(1)
            
        
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
    
    def attack(self, target, weapon, **kwargs):
        # can't attack if we're not in combat!
        self.msg(f"|cAttack in elementals {weapon}")
        if self.db.subguild == "earth":
            weapon = EarthAttack()
        if self.db.subguild == "air":
            weapon = AirAttack()
        if self.db.subguild == "water":
            weapon = WaterAttack()
        if self.db.subguild == "fire":
            weapon = FireAttack()
            
        if not self.in_combat:
            return
        # can't attack if we're fleeing!
        if self.db.fleeing:
            return
        # make sure that we can use our chosen weapon
        if not (hasattr(weapon, "at_pre_attack") and hasattr(weapon, "at_attack")):
            self.msg(f"You cannot attack with {weapon.get_numbered_name(1, self)}.")
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

        self.msg(f"|cbefore at_attack in elementals {weapon}")
        weapon.at_attack(self, target)

        status = self.get_display_status(target)
        self.msg(prompt=status)

        # check if we have auto-attack in settings
        if self.account and (settings := self.account.db.settings):
            if settings.get("auto attack") and (speed := weapon.speed):
                # queue up next attack; use None for target to reference stored target on execution
                delay(speed + 1, self.attack, None, weapon, persistent=True)
    
    def at_damage(self, attacker, damage, damage_type=None):
        """
        Apply damage, after taking into account damage resistances.
        """
        # apply armor damage reduction
        damage -= self.defense(damage_type)
        self.db.hp -= max(damage, 0)
        if self.db.reactive_armor:
            self.msg(f"|cYour reactive armor blocks some damage!")
            self.db.ep -= 1
        self.msg(f"You take {damage} damage from {attacker.get_display_name(self)}.")
        attacker.msg(f"You deal {damage} damage to {self.get_display_name(attacker)}.")
        
        status = self.get_display_status(self)
        self.msg(prompt=status)
            
        if self.db.hp <= 0:
            self.tags.add("unconscious", category="status")
            self.tags.add("lying down", category="status")
            self.msg(
                "You fall unconscious. You can |wrespawn|n or wait to be |wrevive|nd."
            )
            if self.in_combat:
                combat = self.location.scripts.get("combat")[0]
                combat.remove_combatant(self)
                            
    def use_rebuild(self):
        """
        Restores health
        """

        hp = self.db.hp
        hpmax = self.db.hpmax
        fp = self.db.fp
        hp_amount = 0
        
        damage = 10 + self.db.guild_level + self.db.wisdom
        cost = damage / 2
        
        if cost > fp:
            return
        
        if hp + damage > hpmax:            
            hp_amount = hpmax-hp
            self.db.hp = hpmax
            self.db.fp -= cost
        else: 
            hp_amount = hpmax-hp
            self.db.hp += max(damage, 0)
            self.db.fp -= cost
            
        self.msg(f"You restore {hp_amount or 0} health for {cost or 0} focus!")
        
    def use_reactive_armor(self):
        """
        Improve your physical resistance
        """
        ep = self.db.ep
        
        power = self.db.guild_level
        
        if self.db.reactive_armor:
            self.msg(f"|rYou already have reactive armor enabled.")
            return
        
        self.db.reactivearmor = True
        self.db.edgedac += power
        self.db.bluntac += power
        self.msg(f"|rYou activate your reactive armor.")
        
        