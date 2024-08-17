from random import randint, uniform, choice
from evennia.utils import delay
from evennia import TICKER_HANDLER as tickerhandler
from commands.elemental_cmds import ElementalCmdSet
from typeclasses.elementalguild.fire_elemental_attack import FireAttack
from typeclasses.elementalguild.attack_emotes import AttackEmotes
from typeclasses.elementals import Elemental
from typeclasses.utils import adjust_ep, adjust_fp, adjust_hp


class FireElemental(Elemental):

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
        self.db.title = "the novice fire elemental"

        self.db.natural_weapon = {
            "name": "fire_attack",
            "damage_type": "blunt",
            "damage": 12,
            "speed": 3,
            "energy_cost": 10,
        }
        self.db.guild = "elemental"
        self.db.subguild = "fire"
        self.db._wielded = {"left": None, "right": None}
        self.db.reaction_percentage = 50
        self.db.hpregen = 1
        self.db.fpregen = 1
        self.db.epregen = 1
        self.db.strategy = "melee"
        self.db.skills = {
            "flame mastery": 1,
            "inferno resilience": 1,
            "blazing speed": 1,
            "pyroclastic surge": 1,
            "molten armor": 1,
            "ember infusion": 1,
            "firestorm control": 1,
            "elemental synergy": 1,
        }

        self.at_wield(FireAttack)
        tickerhandler.add(
            interval=6, callback=self.at_tick, idstring=f"{self}-regen", persistent=True
        )

    def kickstart(self):
        self.msg("Kickstarting heartbeat")
        tickerhandler.add(
            interval=6, callback=self.at_tick, idstring=f"{self}-regen", persistent=True
        )

    def at_tick(self):
        base_regen = self.db.hpregen
        base_ep_regen = self.db.epregen
        base_fp_regen = self.db.fpregen

        adjust_hp(base_regen)
        adjust_fp(base_ep_regen)
        adjust_ep(base_fp_regen)

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

    def get_player_attack_hit_message(
        self, attacker, dam, tn, emote="fire_elemental_melee"
    ):
        """
        Get the hit message based on the damage dealt. This is the elemental's
        version of the method, defaulting to the earth elemental version but
        should be overridden by subguilds.

        ex:
            f"{color}$You() swipe at {tn}{color} with a fiery claw, leaving scorch marks.",
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
        Apply damage, after taking into account damage resistances.
        """
        glvl = self.db.guild_level
        status = self.get_display_status(self)
        damage -= self.defense(damage_type)

        self.msg(f"You take {damage} damage from {attacker.get_display_name(self)}.")
        attacker.msg(f"You deal {damage} damage to {self.get_display_name(attacker)}.")

        self.db.hp -= max(damage, 0)
        attacker.get_npc_attack_emote(self, damage, self.get_display_name(self))
        self.msg(prompt=status)

        if glvl > 3:
            hp = self.db.hp
            hpmax = self.db.hpmax
            hp_percentage = hp / hpmax
            reaction = int(self.db.reaction_percentage or 1) / 100

            if hp_percentage < reaction:
                self.execute_cmd("flame renewal")

        if self.db.hp <= 0:
            self.tags.add("unconscious", category="status")
            self.tags.add("lying down", category="status")
            self.msg(
                "You fall unconscious. You can |wrespawn|n or wait to be |wrevive|nd."
            )
            if self.in_combat:
                combat = self.location.scripts.get("combat")[0]
                combat.remove_combatant(self)
