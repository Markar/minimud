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
import math
from commands.changeling_cmds import ChangelingCmdSet
from typeclasses.characters import PlayerCharacter

from typeclasses.changelingguild.attack_emotes import AttackEmotes

from typeclasses.changelingguild.changeling_attack import ChangelingAttack
from typeclasses.changelingguild.slime import Slime
from typeclasses.changelingguild.human import Human
from typeclasses.changelingguild.anole import Anole
from typeclasses.changelingguild.teiid import Teiid
from typeclasses.changelingguild.gecko import Gecko
from typeclasses.changelingguild.skink import Skink
from typeclasses.changelingguild.iguana import Iguana
from typeclasses.changelingguild.boa import Boa
from typeclasses.changelingguild.viper import Viper
# from typeclasses.changelingguild.caiman import Caiman
# from typeclasses.changelingguild.cobra import Cobra
# from typeclasses.changelingguild.gilamonster import GilaMonster
# from typeclasses.changelingguild.python import Python
# from typeclasses.changelingguild.crocodile import Crocodile
# from typeclasses.changelingguild.alligator import Alligator
# from typeclasses.changelingguild.anaconda import Anaconda
# from typeclasses.changelingguild.komododragon import KomodoDragon
from typeclasses.changelingguild.rat import Rat
from typeclasses.changelingguild.cat import Cat
from typeclasses.changelingguild.lynx import Lynx
from typeclasses.changelingguild.fox import Fox
from typeclasses.changelingguild.badger import Badger
from typeclasses.changelingguild.wolverine import Wolverine
from typeclasses.changelingguild.wolf import Wolf
# from typeclasses.changelingguild.blackbear import BlackBear
# from typeclasses.changelingguild.changeling_attack.grizzlybear import GrizzlyBear
# from typeclasses.changelingguild.elephant import Elephant
# from typeclasses.changelingguild.cheetah import Cheetah
# from typeclasses.changelingguild.leopard import Leopard
# from typeclasses.changelingguild.jaguar import Jaguar
# from typeclasses.changelingguild.tiger import Tiger
# from typeclasses.changelingguild.lion import Lion
from typeclasses.changelingguild.hummingbird import Hummingbird
from typeclasses.changelingguild.finch import Finch
from typeclasses.changelingguild.sparrow import Sparrow
from typeclasses.changelingguild.swallow import Swallow
from typeclasses.changelingguild.crow import Crow
from typeclasses.changelingguild.raven import Raven
from typeclasses.changelingguild.crane import Crane
# from typeclasses.changelingguild.kestrel import Kestrel
# from typeclasses.changelingguild.owl import Owl
# from typeclasses.changelingguild.osprey import Osprey
# from typeclasses.changelingguild.falcon import Falcon
# from typeclasses.changelingguild.hawk import Hawk
# from typeclasses.changelingguild.condor import Condor
# from typeclasses.changelingguild.ostrich import Ostrich
# from typeclasses.changelingguild.eagle import Eagle

FORM_CLASSES = {
    "ChangelingAttack": ChangelingAttack,
    "Slime": Slime,
    "Human": Human,
    "Anole": Anole,
    "Teiid": Teiid,
    "Gecko": Gecko,
    "Skink": Skink,
    "Iguana": Iguana,
    "Boa": Boa,
    "Viper": Viper,
    # "Caiman": Caiman,
    # "Cobra": Cobra,
    # "Gila Monster": GilaMonster,
    # "Python": Python,
    # "Crocodile": Crocodile,
    # "Alligator": Alligator,
    # "Anaconda": Anaconda,
    # "Komodo Dragon": KomodoDragon,
    "Rat": Rat,
    "Cat": Cat,
    "Lynx": Lynx,
    "Fox": Fox,
    "Badger": Badger,
    "Wolverine": Wolverine,
    "Wolf": Wolf,
    # "Black Bear": BlackBear,
    # "Grizzly Bear": GrizzlyBear,
    # "Elephant": Elephant,
    # "Cheetah": Cheetah,
    # "Leopard": Leopard,
    # "Jaguar": Jaguar,
    # "Tiger": Tiger,
    # "Lion": Lion,
    "Hummingbird": Hummingbird,
    "Finch": Finch,
    "Sparrow": Sparrow,
    "Swallow": Swallow,
    "Crow": Crow,
    "Raven": Raven,
    "Crane": Crane,
    # "Kestrel": Kestrel,
    # "Owl": Owl,
    # "Osprey": Osprey,
    # "Falcon": Falcon,
    # "Hawk": Hawk,
    # "Condor": Condor,
    # "Ostrich": Ostrich,
    # "Eagle": Eagle
}



class Changelings(PlayerCharacter):
    """
    The base typeclass for non-player characters, implementing behavioral AI.
    """

    def at_object_creation(self):
        self.cmdset.add(ChangelingCmdSet, persistent=True)
        super().at_object_creation()
        con_increase_amount = 10
        int_increase_amount = 7
        
        self.db.guild_level = 1
        self.db.gxp = 0
        self.db.skillxp = 0
        self.db.title = "the novice changeling"
        self.db.con_increase_amount = con_increase_amount
        self.db.hpmax = 50 + (con_increase_amount * self.db.constitution)
        self.db.int_increase_amount = int_increase_amount
        self.db.fpmax = 50 + (int_increase_amount * self.db.intelligence)
        self.db.natural_weapon = {
            "name": "punch",
            "damage_type": "blunt",
            "damage": 3,
            "speed": 2,
            "energy_cost": 1
        }
        self.db.guild = "changeling"
        self.db.form = "human"
        self.db._wielded = {"left": None, "right": None}
        self.db.hpregen = 1
        self.db.fpregen = 1
        self.db.epregen = 1
        self.db.regrowth_rate = 0
        self.db.regrowth_cost = 0
        self.db.form = "Human"
        self.db.subguild = "none"
        self.db.engulfs = 0
        self.db.max_engulfs = 0
        self.db.skills = {
            "body_control": 0,
            "drain": 0,
            "energy_control": 0,
            "familiar": 0,
            "regeneration": 0,
            "vibrate": 0
        }
        self.at_wield(ChangelingAttack)
        tickerhandler.add(interval=6, callback=self.at_tick, idstring=f"{self}-regen", persistent=True)
        tickerhandler.add(interval=60*5, callback=self.at_engulf_tick, idstring=f"{self}-superpower", persistent=True)
    
    def kickstart(self):
        self.msg("Kickstarting heartbeat")
        tickerhandler.add(interval=6, callback=self.at_tick, idstring=f"{self}-regen", persistent=True)
        tickerhandler.add(interval=60*5, callback=self.at_engulf_tick, idstring=f"{self}-superpower", persistent=True)
        
    def addhp(self, amount):
        hp = self.db.hp
        hpmax = self.db.hpmax
        
        if hp + amount > hpmax:
            self.db.hp = hpmax
        else: 
            self.db.hp += max(amount, 0)
    
    def addfp(self, amount):
        fp = self.db.fp
        fpmax = self.db.fpmax
        
        if fp + amount > fpmax:
            self.db.fp = fpmax
            return
        else:
            self.db.fp += max(amount, 0)
    
    def addep(self, amount):
        ep = self.db.ep
        epmax = self.db.epmax
        
        if ep + amount > epmax:
            self.db.ep = epmax
            return
        if ep < epmax + amount:
            self.db.ep += max(amount, 0)
    
    def at_engulf_tick(self):
        self.msg(f"|gYour body ripples and shakes as energy flows into you")
        self.db.engulfs = self.db.max_engulfs
    
    def at_tick(self):
        regrowth_rate = self.db.regrowth_rate
        regrowth_cost = self.db.regrowth_cost
        ep = self.db.ep
        
        if not ep > regrowth_cost: 
            self.msg(f"|rYou do not have enough energy to regrow.")
            self.db.regrowth_rate = 0
            self.db.regrowth_cost = 0
            return
        
        if regrowth_cost:
            self.addep(-self.db.regrowth_cost)
            
        if regrowth_rate:
            self.addhp(self.db.regrowth_rate)
                    
        # self.msg(f"|R{self.db.hpregen} {self.db.fpregen} {self.db.epregen}")
        self.addhp(self.db.hpregen)
        self.addfp(self.db.fpregen)
        self.addep(self.db.epregen)
            
        
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
        # Loop through the form classes and assign the appropriate weapon
        if self.db.form in FORM_CLASSES:
            weapon = FORM_CLASSES[self.db.form]()
        
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
    
    def get_hit_message(self, attacker, dam, tn):
        attack = FORM_CLASSES[self.db.form].name

        msgs = AttackEmotes.get_emote(attacker, attack, tn, which="left")
        if dam == 0:
            to_me = msgs[0]
        elif 1 <= dam <= 5:
            to_me = msgs[1]
        elif 6 <= dam <= 12:
            to_me = msgs[2]
        elif 13 <= dam <= 20:
            to_me = msgs[3]
        elif 21 <= dam <= 30:
            to_me = msgs[4]
        elif 31 <= dam <= 40:
            to_me = msgs[5]
        elif 41 <= dam <= 50:
            to_me = msgs[6]
        elif 51 <= dam <= 60:
            to_me = msgs[7]
        elif 61 <= dam <= 75:
            to_me = msgs[8]
        elif 76 <= dam <= 90:
            to_me = msgs[9]
        else:
            to_me = msgs[10]
            
        to_me = f"{to_me} ({dam})"
        self.location.msg_contents(to_me, from_obj=self)
                    
        return to_me

    def get_form_help(self, form):
        form_class = FORM_CLASSES[form.title()]
        return form_class.__doc__
    
    def at_damage(self, attacker, damage, damage_type=None):
        """
        Apply damage, after taking into account damage resistances.
        """
        # apply armor damage reduction
        damage -= self.defense(damage_type)
        if self.db.energy_control:
            self.msg(f"|cYou block some damage!")
            if damage_type in ["edged", "blunt"]:
                damage -= self.db.guild_level
            self.db.ep -= 1
            
        self.db.hp -= max(damage, 0)
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
                            

        
    def use_energy_control(self):
        """
        Improve your physical resistance
        """
        
        if self.db.energy_control:
            self.msg(f"|MYou feel the energy receding, flowing back into your core. The crackling sounds of the barrier fade away, and the protective shield dissolves into the air.")
            self.db.energy_control = False
            return
        
        self.db.energy_control = True
        self.db.ep -= 25
        self.msg(f"|MAs you focus your mind, a surge of energy begins to flow through your body. You raise your hands, and a shimmering barrier of pure energy forms around you, crackling with power.")
        
    def use_engulf(self, target,  **kwargs):
        """
        Engulf your target
        """
        self.msg(f"self engulf {self}")
        if not target:
            self.msg(f"|GTarget whom?")
            return

        if not self.db.combat_target:
            self.enter_combat(target)
        else:
            self.db.combat_target = target
        target.enter_combat(self)
        if not self.cooldowns.ready("engulf"):
            self.msg(f"|BNot so fast!")
            return False
        
        self.db.combat_target = target
        # execute the actual attack
        
        hp = self.db.hp
        hpmax = self.db.hpmax
        fp = self.db.fp
        fpmax = self.db.fpmax
        
        if self.db.engulfs < 1:
            self.msg(f"|rYou do not have the strength to engulf at this time.\n")
            return
        if  hp > hpmax or fp > fpmax:
            self.msg(f"|rYou may not engulf a creature at this time.\n")
            return
            
        power = math.ceil(self.db.hpmax * (9 + self.db.guild_level/7) / 10)
        self.msg(f"engulf power: {power}")
        self.db.hp += power
        self.db.fp += power
        self.db.combat_target.at_damage(self, power)
        self.cooldowns.add("engulf", 5)
        self.msg(f"|rYou flow around {target} completely enclosing them in plasma!")
        