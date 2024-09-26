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

from typeclasses.warriorsguild.attack_emotes import AttackEmotes
from typeclasses.warriorsguild.warrior_attack import WarriorAttack


class Warrior(PlayerCharacter):
    """
    The base typeclass for non-player characters, implementing behavioral AI.
    """

    def at_object_creation(self):
        self.cmdset.add(ChangelingCmdSet, persistent=True)
        super().at_object_creation()
        con_increase_amount = 20
        int_increase_amount = 7
        self.db.con_increase_amount = con_increase_amount
        self.db.int_increase_amount = int_increase_amount
        self.db.hpmax = 50 + (con_increase_amount * self.traits.con.value)
        self.db.fpmax = 50 + (int_increase_amount * self.traits.int.value)

        self.db.guild_level = 1
        self.db.gxp = 0
        self.db.skill_gxp = 0
        self.db.title = "the novice warrior"

        self.db.natural_weapon = {
            "name": "punch",
            "damage_type": "blunt",
            "damage": 3,
            "speed": 2,
            "energy_cost": 1,
        }
        self.db.guild = "warrior"
        self.db.subguild = "none"
        self.db._wielded = {"left": None, "right": None}
        self.db.hpregen = 1
        self.db.fpregen = 1
        self.db.epregen = 1
        self.db.form = "Human"

        self.db.engulfs = 0
        self.db.max_engulfs = 0
        self.db.skills = {}
        tickerhandler.add(
            interval=6, callback=self.at_tick, idstring=f"{self}-regen", persistent=True
        )

    def kickstart(self):
        self.msg("Kickstarting heartbeat")
        tickerhandler.add(
            interval=6, callback=self.at_tick, idstring=f"{self}-regen", persistent=True
        )

    def at_tick(self):
        base_regen = 1
        base_ep_regen = 1
        base_fp_regen = 1
        hp_regen_amt = base_regen

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

    """
    This kicks off the auto attack of the form, which is weapon.at_attack
    The weapon is the form class, which is a subclass of ChangelingAttack
    and has the at_attack method. 
    """

    def attack(self, target, weapon, **kwargs):

        if not self.in_combat:
            self.enter_combat(target)
            if target:
                target.enter_combat(self)
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

    def get_player_attack_hit_message(self, attacker, dam, tn, emote="general_weapon"):
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
        # apply dodge
        glvl = self.db.guild_level
        dodge = 10
        damage_reduction = 0

        dodge = self.traits.dex.value / 5 + dodge * glvl / 12
        if dodge > 90:
            dodge = 90

        ran = randint(1, 100)
        if ran <= dodge:
            self.msg(f"|cYou dodge the attack!")
            attacker.msg(f"{self.get_display_name(attacker)} dodges your attack!")
            return

        damage -= math.ceil(damage_reduction)

        # apply armor damage reduction
        damage -= self.defense(damage_type)

        self.db.hp -= max(damage, 0)
        attacker.msg(f"You deal {damage} damage to {self.get_display_name(attacker)}.")

        # The NPC's attack, emoting to the room
        # a scrawny gnoll tears into changeling at_damage Markar with brutal force! -18
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
        hp = int(self.db.hp)
        hpmax = int(self.db.hpmax)
        fp = int(self.db.fp)
        fpmax = int(self.db.fpmax)
        ep = int(self.db.ep)
        epmax = int(self.db.epmax)

        chunks.append(
            f"|gHealth: |G{hp}/{hpmax}|g Focus: |G{fp}/{fpmax}|g Energy: |G{ep}/{epmax}"
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

        if target is not None:
            self.at_emote(
                "changeling $conj(charges) at {target}!", mapping={"target": target}
            )
        location = self.location

        if not (combat_script := location.scripts.get("combat")):
            # there's no combat instance; start one
            from typeclasses.scripts import CombatScript

            location.scripts.add(CombatScript, key="combat")
            combat_script = location.scripts.get("combat")
        combat_script = combat_script[0]
        self.db.combat_target = target
        # adding a combatant to combat just returns True if they're already there, so this is safe
        if not combat_script.add_combatant(self, enemy=target):
            return
        self.attack(target, weapon)

    def can_wear(self, item):
        """
        Check if the character can wear an item
        """
        self.msg(f"can_wear: {item}")
        type = getattr(item, "type", False)

        if not item:
            return False

        if not type or item.type != "clothing":
            self.msg(f"{item} is not clothing, or is too heavy for you to use.")
            return False

        return True
