from random import randint, uniform, uniform
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
from typeclasses.changelingguild.reptile.anole import Anole
from typeclasses.changelingguild.reptile.teiid import Teiid
from typeclasses.changelingguild.reptile.gecko import Gecko
from typeclasses.changelingguild.reptile.skink import Skink
from typeclasses.changelingguild.reptile.iguana import Iguana
from typeclasses.changelingguild.reptile.boa import Boa
from typeclasses.changelingguild.reptile.viper import Viper
from typeclasses.changelingguild.reptile.caiman import Caiman
from typeclasses.changelingguild.reptile.cobra import Cobra
from typeclasses.changelingguild.reptile.gilamonster import GilaMonster
from typeclasses.changelingguild.reptile.python import Python
from typeclasses.changelingguild.reptile.crocodile import Crocodile
from typeclasses.changelingguild.reptile.alligator import Alligator
from typeclasses.changelingguild.reptile.anaconda import Anaconda
from typeclasses.changelingguild.reptile.komodo_dragon import KomodoDragon
from typeclasses.changelingguild.mammal.rat import Rat
from typeclasses.changelingguild.mammal.cat import Cat
from typeclasses.changelingguild.mammal.lynx import Lynx
from typeclasses.changelingguild.mammal.fox import Fox
from typeclasses.changelingguild.mammal.badger import Badger
from typeclasses.changelingguild.mammal.wolverine import Wolverine
from typeclasses.changelingguild.mammal.wolf import Wolf
from typeclasses.changelingguild.mammal.black_bear import BlackBear
from typeclasses.changelingguild.mammal.grizzly_bear import GrizzlyBear
from typeclasses.changelingguild.mammal.elephant import Elephant
from typeclasses.changelingguild.mammal.cheetah import Cheetah
from typeclasses.changelingguild.mammal.leopard import Leopard
from typeclasses.changelingguild.mammal.jaguar import Jaguar
from typeclasses.changelingguild.mammal.tiger import Tiger
from typeclasses.changelingguild.mammal.lion import Lion
from typeclasses.changelingguild.avian.hummingbird import Hummingbird
from typeclasses.changelingguild.avian.finch import Finch
from typeclasses.changelingguild.avian.sparrow import Sparrow
from typeclasses.changelingguild.avian.swallow import Swallow
from typeclasses.changelingguild.avian.crow import Crow
from typeclasses.changelingguild.avian.raven import Raven
from typeclasses.changelingguild.avian.crane import Crane
from typeclasses.changelingguild.avian.kestrel import Kestrel
from typeclasses.changelingguild.avian.owl import Owl
from typeclasses.changelingguild.avian.osprey import Osprey
from typeclasses.changelingguild.avian.falcon import Falcon
from typeclasses.changelingguild.avian.hawk import Hawk
from typeclasses.changelingguild.avian.condor import Condor
from typeclasses.changelingguild.avian.ostrich import Ostrich
from typeclasses.changelingguild.avian.eagle import Eagle

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
    "Caiman": Caiman,
    "Cobra": Cobra,
    "Gila Monster": GilaMonster,
    "Python": Python,
    "Crocodile": Crocodile,
    "Alligator": Alligator,
    "Anaconda": Anaconda,
    "Komodo Dragon": KomodoDragon,
    "Rat": Rat,
    "Cat": Cat,
    "Lynx": Lynx,
    "Fox": Fox,
    "Badger": Badger,
    "Wolverine": Wolverine,
    "Wolf": Wolf,
    "Black Bear": BlackBear,
    "Grizzly Bear": GrizzlyBear,
    "Elephant": Elephant,
    "Cheetah": Cheetah,
    "Leopard": Leopard,
    "Jaguar": Jaguar,
    "Tiger": Tiger,
    "Lion": Lion,
    "Hummingbird": Hummingbird,
    "Finch": Finch,
    "Sparrow": Sparrow,
    "Swallow": Swallow,
    "Crow": Crow,
    "Raven": Raven,
    "Crane": Crane,
    "Kestrel": Kestrel,
    "Owl": Owl,
    "Osprey": Osprey,
    "Falcon": Falcon,
    "Hawk": Hawk,
    "Condor": Condor,
    "Ostrich": Ostrich,
    "Eagle": Eagle,
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
        self.db.con_increase_amount = con_increase_amount
        self.db.int_increase_amount = int_increase_amount
        self.db.hpmax = 50 + (con_increase_amount * self.traits.con.value)
        self.db.fpmax = 50 + (int_increase_amount * self.traits.int.value)

        self.db.guild_level = 1
        self.db.gxp = 0
        self.db.skill_gxp = 0
        self.db.title = "the novice changeling"

        self.db.natural_weapon = {
            "name": "punch",
            "damage_type": "blunt",
            "damage": 3,
            "speed": 2,
            "energy_cost": 1,
        }
        self.db.guild = "changeling"
        self.db.subguild = "none"
        self.db._wielded = {"left": None, "right": None}
        self.db.hpregen = 1
        self.db.fpregen = 1
        self.db.epregen = 1
        self.db.regrowth_rate = 0
        self.db.regrowth_cost = 0
        self.db.form = "Human"

        self.db.engulfs = 0
        self.db.max_engulfs = 0
        self.db.skills = {
            "body_control": 1,
            "drain": 1,
            "energy_control": 1,
            "regeneration": 1,
        }
        self.at_wield(ChangelingAttack)
        tickerhandler.add(
            interval=6, callback=self.at_tick, idstring=f"{self}-regen", persistent=True
        )
        tickerhandler.add(
            interval=60 * 5,
            callback=self.at_engulf_tick,
            idstring=f"{self}-superpower",
            persistent=True,
        )

    def kickstart(self):
        self.msg("Kickstarting heartbeat")
        tickerhandler.add(
            interval=6, callback=self.at_tick, idstring=f"{self}-regen", persistent=True
        )
        tickerhandler.add(
            interval=60 * 5,
            callback=self.at_engulf_tick,
            idstring=f"{self}-superpower",
            persistent=True,
        )

    def at_engulf_tick(self):
        self.msg(f"|gYour body ripples and shakes as energy flows into you")
        self.db.engulfs = self.db.max_engulfs

    def at_tick(self):
        glvl = self.db.guild_level
        ep = self.db.ep
        regen_skill = self.db.skills["regeneration"]

        hp = self.db.hp
        hpmax = self.db.hpmax
        base_regen = self.db.hpregen
        base_ep_regen = self.db.epregen
        base_fp_regen = self.db.fpregen
        hp_regen_amt = base_regen

        if self.db.regrowth and hp < hpmax:
            regrowth_rate = int(
                5
                + regen_skill / 2
                + uniform(0, regen_skill / 2)
                + glvl / 8
                + uniform(0, glvl / 8)
            )
            regrowth_cost = int(regrowth_rate / 3)

            if ep >= regrowth_cost and hp < hpmax:
                hp_regen_amt += regrowth_rate
                self.msg(
                    f"|MYou feel the energy flowing through you, knitting your wounds together."
                )
                self.db.ep -= regrowth_cost
            else:
                self.msg(f"|rYou do not have enough energy to regrow.")
                self.db.regrowth = False

        self.adjust_hp(hp_regen_amt)
        self.adjust_fp(base_fp_regen)
        self.adjust_ep(base_ep_regen)

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

    """
    This kicks off the auto attack of the form, which is weapon.at_attack
    The weapon is the form class, which is a subclass of ChangelingAttack
    and has the at_attack method. 
    """

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

    def get_player_attack_hit_message(self, attacker, dam, tn, emote="bite"):
        # attack = FORM_CLASSES[self.db.form].name
        """
        Get the hit message based on the damage dealt. This is the changeling's
        version of the method, defaulting to bite but should be overridden by
        subguilds.

        ex:
            f"{color}$pron(Your) bite causes {tn}{color} to bleed slightly.",
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

        to_me = f"{to_me} ({dam})"
        self.location.msg_contents(to_me, from_obj=self)

        return to_me

    def at_damage(self, attacker, damage, damage_type=None):
        """
        Apply damage to self, after taking into account damage resistances.
        """
        form = FORM_CLASSES[self.db.form]
        # apply dodge
        glvl = self.db.guild_level
        form_dodge = form.dodge
        form_toughness = form.toughness
        ec = self.db.skills["energy_control"]
        base_ec_amt = ec * (glvl / 5)
        ec_amt = math.floor(uniform(base_ec_amt / 2, base_ec_amt))

        dodge = self.db.dexterity / 5 + form_dodge * glvl / 12
        if dodge > 90:
            dodge = 90

        ran = randint(1, 100)
        if ran <= dodge:
            self.msg(f"|cYou dodge the attack!")
            attacker.msg(f"{self.get_display_name(attacker)} dodges your attack!")
            return
        # self.msg(f"{self} takes damage: {damage}")
        # aply toughness
        toughness = form_toughness + glvl / 5 + self.traits.con.value / 10
        # self.msg(f"|cToughness: {toughness}")
        tougness_reduction = math.ceil(uniform(toughness / 2, toughness))
        if glvl < 5:
            tougness_reduction = tougness_reduction / 3
        if glvl < 10:
            tougness_reduction = tougness_reduction / 2
        damage -= math.ceil(tougness_reduction)
        # self.msg(f"|cToughness reduction: {tougness_reduction}")

        # apply armor damage reduction
        damage -= self.defense(damage_type)
        # self.msg(f"|cArmor reduction: {self.defense(damage_type)}")

        # apply energy control reduction
        if self.db.energy_control is True and damage_type in ["edged", "blunt"]:
            damage -= ec_amt
            self.db.ep -= 1
            self.msg(f"|cYou block some damage!")

        # self.msg(f"|cEnergy control reduction: {ec_amt}")
        self.db.hp -= max(damage, 0)
        # self.msg(f"You take {damage} damage from {attacker.get_display_name(self)}.")
        attacker.msg(f"You deal {damage} damage to {self.get_display_name(attacker)}.")
        # The NPC's attack, emoting to the room
        # a scrawny gnoll tears into changeling at_damage Markar with brutal force! -18
        attacker.get_hit_message(self, damage, self.get_display_name(self))

        # status = self.get_display_status(self)
        # self.msg(prompt=status)

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
            self.msg(
                f"|MYou feel the energy receding, flowing back into your core. The crackling sounds of the barrier fade away, and the protective shield dissolves into the air."
            )
            self.db.energy_control = False
            return

        self.db.energy_control = True
        self.db.ep -= 25
        self.msg(
            f"|MAs you focus your mind, a surge of energy begins to flow through your body. You raise your hands, and a shimmering barrier of pure energy forms around you, crackling with power."
        )

    def get_form_help(self, form):
        form_class = FORM_CLASSES[form.title()]
        return form_class.__doc__

    def use_engulf(self, target, **kwargs):
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
            self.msg(f"|CNot so fast!")
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
        if hp > hpmax or fp > fpmax:
            self.msg(f"|rYou may not engulf a creature at this time.\n")
            return

        power = math.ceil(self.db.hpmax * (9 + self.db.guild_level / 7) / 10)
        self.msg(f"engulf power: {power}")
        self.db.hp += power
        self.db.fp += power
        self.db.combat_target.at_damage(self, power)
        self.db.engulfs -= 1
        self.cooldowns.add("engulf", 5)
        self.msg(f"|rYou flow around {target} completely enclosing them in plasma!")

    def get_display_status(self, looker, **kwargs):
        """
        Returns a quick view of the current status of this character
        """

        # print(f"get_display_status: {self}, {self.args}")
        chunks = []
        # prefix the status string with the character's name, if it's someone else checking
        # if looker != self:
        #     chunks.append(self.get_display_name(looker, **kwargs))

        # add resource levels
        hp = math.floor(self.db.hp)
        hpmax = self.db.hpmax
        fp = math.floor(self.db.fp)
        fpmax = self.db.fpmax
        ep = math.floor(self.db.ep)
        epmax = self.db.epmax

        ecVis = ""
        regrowthVis = ""
        if self.db.energy_control:
            ecVis = "EC"
        if self.db.regrowth:
            regrowthVis = "CG"

        chunks.append(
            f"|gHealth: |G{hp}/{hpmax}|g Focus: |G{fp}/{fpmax}|g Energy: |G{ep}/{epmax}|g Form: |G{self.db.form} |gEngulfs: |G{self.db.engulfs}/{self.db.max_engulfs} |Y{ecVis} |Y{regrowthVis}"
        )
        print(f"looker != self {looker} and self {self}")
        if looker != self:
            chunks.append(
                f"|gE: |G{looker.get_display_name(self, **kwargs)} ({looker.db.hp})"
            )

        # get all the current status flags for this character
        if status_tags := self.tags.get(category="status", return_list=True):
            # add these statuses to the string, if there are any
            chunks.append(iter_to_str(status_tags))

        if looker == self:
            # if we're checking our own status, include cooldowns
            all_cooldowns = [
                (key, self.cooldowns.time_left(key, use_int=True))
                for key in self.cooldowns.all
            ]
            all_cooldowns = [f"{c[0]} ({c[1]}s)" for c in all_cooldowns if c[1]]
            if all_cooldowns:
                chunks.append(f"Cooldowns: {iter_to_str(all_cooldowns, endsep=',')}")

        chunks.append(f"\n")
        # glue together the chunks and return
        return " - ".join(chunks)

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
