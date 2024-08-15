from random import randint, uniform
from string import punctuation
from evennia.utils import delay
from evennia.contrib.game_systems.cooldowns import CooldownHandler
from evennia import TICKER_HANDLER as tickerhandler
from evennia.contrib.game_systems.clothing.clothing import (
    ClothedCharacter,
    get_worn_clothes,
)
from commands.elemental_cmds import ElementalCmdSet
from typeclasses.elementalguild.earth_elemental_attack import EarthAttack
from typeclasses.elementals import Elemental
from typeclasses.elementalguild.earth_elemental_commands import CmdTerranRestoration
import math

class EarthElemental(Elemental):
    
    def at_object_creation(self):
        self.cmdset.add(ElementalCmdSet, persistent=True)
        super().at_object_creation()
        con_increase_amount = 12
        int_increase_amount = 5
        self.db.con_increase_amount = con_increase_amount
        self.db.int_increase_amount = int_increase_amount
        self.db.hpmax = 50 + (con_increase_amount * self.db.constitution)        
        self.db.fpmax = 50 + (int_increase_amount * self.db.intelligence)
        
        self.db.guild_level = 1
        self.db.gxp = 0
        self.db.skill_gxp = 0
        self.db.title = "the novice earth elemental"
        
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
        self.db.reaction_percentage = 50
        self.db.hpregen = 1
        self.db.fpregen = 1
        self.db.epregen = 1
        self.db.strategy = "melee"
        self.db.skills = {
            # "stone mastery": 1,
            # "earth resonance": 1,
            "mineral fortification": 1,
            # "geological insight": 1,
            # "seismic awareness": 1,
            # "rock solid defense": 1,
            # "elemental harmony": 1,
            "earthen regeneration": 1,
            "assimilation": 1,
        }
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
        regen = self.db.skills["earthen regeneration"]
        
        if regen < 2: 
            bonus_fp = 0
        if regen < 5:
            bonus_fp = int(uniform(0, regen/2)) #0-2
        if regen < 10:
            bonus_fp = int(uniform(1, regen/2)) #1-3
        if regen < 15:
            bonus_fp = int(uniform(3, regen/3)) #3-5
        if regen < 20:
            bonus_fp = int(uniform(4, regen/3)) #4-6
        
        total_fp_regen = base_fp_regen + bonus_fp
        self.addhp(base_regen)
        self.addfp(base_ep_regen)
        self.addep(total_fp_regen)
            
        
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
        weapon = EarthAttack()
            
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
    
    def at_damage(self, attacker, damage, damage_type=None):
        """
        Apply damage, after taking into account damage resistances.
        """
        glvl = self.db.guild_level
        con = self.db.constitution
        hp = self.db.hp
        hpmax = self.db.hpmax
        skill_level = self.db.skills.get("mineral fortification", 0)
        status = self.get_display_status(self)
        hp_percentage = hp / hpmax
        reaction = int(self.db.reaction_percentage or 1) / 100
        
        # reduction = uniform(1 - 0.1 (con / 200 + glvl / 150))
        # self.msg(f"Reduction: {reduction}")
        # reduction = 0.9
        # damage *= math.round(reduction)
        damage -= self.defense(damage_type)
        
        # Flat damage reduction - 50 con = 5 reduction, glvl 30 = 1.5 reduction
        flat_reduction = con * 0.1 + glvl * 0.05
        
        # Percentage damage reduction 2% per skill level
        percentage_reduction = skill_level * 0.02
        
        # Apply flat reduction
        damage -= flat_reduction
        
        # Apply percentage reduction
        damage *= (1 - percentage_reduction)
        
        # Apply defense reduction
        damage -= self.defense(damage_type)
        
        # apply reactive armor after defense if it's enabled
        if damage_type in ("blunt", "edged") and self.db.reactive_armor:
            reactive_armor_absorbed = uniform(glvl/3, glvl)
            damage -= reactive_armor_absorbed
            self.msg(f"|cYour reactive armor blocks some damage!")            
        
        # Make sure damage is an integer, similar to floor rounding
        damage = int(damage)
        
        # Ensure damage doesn't go below zero
        damage = max(damage, 0)
        
        # Apply the damage to the character
        self.db.hp -= damage
        self.msg(f"You take {damage} damage from {attacker.get_display_name(self)}.")
        attacker.msg(f"You deal {damage} damage to {self.get_display_name(attacker)}.")
    
        # Get the attack emote
        attacker.get_npc_attack_emote(self, damage, self.get_display_name(self))
        self.msg(prompt=status)
        
        # Check if the character is below the reaction percentage
        if hp_percentage < reaction and glvl > 3:
            self.msg(f"|cYou are below {reaction*100}% health!|n")
            self.execute_cmd("terran restoration")
            
        if hp <= 0:
            self.tags.add("unconscious", category="status")
            self.tags.add("lying down", category="status")
            self.msg(
                "You fall unconscious. You can |wrespawn|n or wait to be |wrevive|nd."
            )
            if self.in_combat:
                combat = self.location.scripts.get("combat")[0]
                combat.remove_combatant(self)
                              