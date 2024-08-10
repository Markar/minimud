from random import randint, uniform, choice
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
from typeclasses.elementalguild.attack_emotes import AttackEmotes

class Elemental(PlayerCharacter):
    """
    The base typeclass for non-player characters, implementing behavioral AI.
    """

    def at_object_creation(self):
        self.cmdset.add(ElementalCmdSet, persistent=True)
        super().at_object_creation()
        con_increase_amount = 12
        int_increase_amount = 5
        self.db.con_increase_amount = 12
        self.db.int_increase_amount = 5
        self.db.hpmax = 50 + (12 * self.db.constitution)        
        self.db.fpmax = 50 + (5 * self.db.intelligence)
        
        self.db.guild_level = 1
        self.db.gxp = 0
        self.db.skill_gxp = 0
        self.db.title = "the novice Elemental"        
        
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
        tickerhandler.add(interval=6, callback=self.at_tick, idstring=f"{self}-regen", persistent=True)
    
    def kickstart(self):
        self.msg("Kickstarting heartbeat")
        tickerhandler.add(interval=6, callback=self.at_tick, idstring=f"{self}-regen", persistent=True)
        
    def addhp(self, amount):
        hp = self.db.hp
        hpmax = self.db.hpmax
        
        if hp + amount > hpmax:
            amt = hpmax - hp
            self.db.hp += max(amt, 0)
            return
        else: 
            self.db.hp += max(amount, 0)
    
    def addfp(self, amount):
        fp = self.db.fp
        fpmax = self.db.fpmax
        
        if fp + amount > fpmax:
            amt = fpmax - fp
            self.db.fp += max(amt, 0)
            return
        else:
            self.db.fp += max(amount, 0)
    
    def addep(self, amount):
        ep = self.db.ep
        epmax = self.db.epmax
        
        if ep + amount > epmax:
            amt = epmax - ep
            self.db.ep += max(amt, 0)
            return
        if ep < epmax + amount:
            self.db.ep += max(amount, 0)
        
    def at_tick(self):
        base_regen = self.db.hpregen
        base_ep_regen = self.db.epregen
        base_fp_regen = self.db.fpregen
        
        self.addhp(base_regen)
        self.addfp(base_ep_regen)
        self.addep(base_fp_regen)
            
        
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

        weapon.at_attack(self, target)

        status = self.get_display_status(target)
        self.msg(prompt=status)

        # check if we have auto-attack in settings
        if self.account and (settings := self.account.db.settings):
            if settings.get("auto attack") and (speed := weapon.speed):
                # queue up next attack; use None for target to reference stored target on execution
                delay(speed + 1, self.attack, None, weapon, persistent=True)
    
    def get_player_attack_hit_message(self, attacker, dam, tn, emote="earth_elemental_melee"):
        """
        Get the hit message based on the damage dealt. This is the elemental's
        version of the method, defaulting to the earth elemental version but 
        should be overridden by subguilds.
        
        ex: 
            f"{color}$You() hurl a handful of dirt, but it scatters harmlessly.",
        """
        
        msgs = AttackEmotes.get_emote(attacker, emote, tn, which="left")
        
        if dam <= 0:
            to_me = msgs[0]
        elif 1 <= dam <= 5:
            to_me = msgs[1]
        elif 6 <= dam <= 12:
            to_me = msgs[2]
        elif 13 <= dam <= 20:
            to_me = msgs[3]
        elif 21 <= dam <= 30:
            to_me = msgs[4]
        elif 31 <= dam <= 50:
            to_me = msgs[5]
        elif 51 <= dam <= 80:
            to_me = msgs[6]
        elif 81 <= dam <= 140:
            to_me = msgs[7]
        elif 141 <= dam <= 225:
            to_me = msgs[8]
        elif 225 <= dam <= 325:
            to_me = msgs[9]
        else:
            to_me = msgs[10]
            
        self.msg(f"to_me {to_me}")
        to_me = f"{to_me} ({dam})"
        self.location.msg_contents(to_me, from_obj=self)
                    
        return to_me
    
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
        
        attacker.get_npc_attack_emote(self, damage, self.get_display_name(self))
            
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
        
        
    def enter_combat(self, target, **kwargs):
        """
        initiate combat against another character
        """
        if weapons := self.wielding:
            weapon = weapons[0]
        else:
            weapon = self

        self.at_emote("$conj(charges) at {target}!", mapping={"target": target})
        location = self.location

        if not (combat_script := location.scripts.get("combat")):
            # there's no combat instance; start one
            from typeclasses.scripts import CombatScript
            location.scripts.add(CombatScript, key="combat")
            combat_script = location.scripts.get("combat")
        combat_script = combat_script[0]
        self.db.combat_target = target
        # adding a combatant to combat just returns True if they're already there, so this is safe
        # if not combat_script.add_combatant(self, enemy=target):
        #     return
        self.attack(target, weapon)