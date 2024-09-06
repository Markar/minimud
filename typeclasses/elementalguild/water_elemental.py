import math
from random import uniform, randint
from evennia.utils import delay, iter_to_str
from evennia import TICKER_HANDLER as tickerhandler
from commands.elemental_cmds import ElementalCmdSet
from typeclasses.elementalguild.water_elemental_attack import WaterAttack
from typeclasses.elementalguild.attack_emotes import AttackEmotes
from typeclasses.elementals import Elemental


class WaterElemental(Elemental):
    def at_object_creation(self):
        self.cmdset.add(ElementalCmdSet, persistent=True)
        super().at_object_creation()
        con_increase_amount = 12
        int_increase_amount = 5
        self.db.con_increase_amount = con_increase_amount
        self.db.int_increase_amount = int_increase_amount
        self.db.hpmax = 50 + (con_increase_amount * self.traits.con.value)
        self.db.fpmax = 50 + (int_increase_amount * self.traits.int.value)

        self.db.guild_level = 1
        self.db.gxp = 0
        self.db.skill_gxp = 0
        self.db.title = "the novice water elemental"

        self.db.natural_weapon = {
            "name": "water_attack",
            "damage_type": "blunt",
            "damage": 12,
            "speed": 3,
            "energy_cost": 10,
        }
        self.db.guild = "elemental"
        self.db.subguild = "water"
        self.db._wielded = {"left": None, "right": None}
        self.db.reaction_percentage = 50
        self.db.maxEmit = 1
        self.db.hpregen = 1
        self.db.fpregen = 1
        self.db.epregen = 1
        self.db.strategy = "melee"
        self.db.skills = {
            "water mastery": 1,
            "fluid agility": 1,
            "aqua resilience": 1,
            "tidal force": 1,
            "ice mastery": 1,
            "aqua infusion": 1,
            "wave control": 1,
            "elemental synergy": 1,
        }

        self.at_wield(WaterAttack)
        tickerhandler.add(
            interval=6, callback=self.at_tick, idstring=f"{self}-regen", persistent=True
        )

    def kickstart(self):
        self.msg("Kickstarting heartbeat")
        tickerhandler.add(
            interval=6, callback=self.at_tick, idstring=f"{self}-regen", persistent=True
        )

    def get_display_status(self, looker, **kwargs):
        """
        Returns a quick view of the current status of this character
        """

        chunks = []

        # add resource levels
        hp = int(self.db.hp)
        hpmax = int(self.db.hpmax)
        fp = int(self.db.fp)
        fpmax = int(self.db.fpmax)
        ep = int(self.db.ep)
        epmax = int(self.db.epmax)
        burnout_count = self.db.burnout["count"]
        burnout_max = self.db.burnout["max"]

        chunks.append(
            f"|gHealth: |G{hp}/{hpmax}|g Focus: |G{fp}/{fpmax}|g Energy: |G{ep}/{epmax}|g"
        )
        if self.db.burnout["count"] > 0:
            chunks.append(f"|YBurnout: |G{burnout_count}/{burnout_max}|n")
        if self.db.burnout["active"]:
            chunks.append(f"|YB")
        if self.db.aqua_shield == True:
            chunks.append(f"|YAS")

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

    def at_tick(self):
        base_hp_regen = self.db.hpregen
        base_ep_regen = self.db.epregen
        base_fp_regen = self.db.fpregen
        regen = self.db.skills["aqua infusion"]

        if regen < 2:
            bonus_fp = 0
        if regen < 5:
            bonus_fp = int(uniform(0, regen / 2))  # 0-2
        if regen < 10:
            bonus_fp = int(uniform(1, regen / 2))  # 1-3
        if regen < 15:
            bonus_fp = int(uniform(3, regen / 3))  # 3-5
        if regen < 20:
            bonus_fp = int(uniform(4, regen / 3))  # 4-6

        total_fp_regen = base_fp_regen + bonus_fp
        self.adjust_hp(base_hp_regen)
        self.adjust_fp(base_ep_regen)
        self.adjust_ep(total_fp_regen)

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
        weapon = WaterAttack()

        if not self.in_combat:
            self.enter_combat(target)
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

    def _calculate_dodge(self):
        glvl = self.db.guild_level

        fluid_agility = self.db.skills.get("aerial agility", 1)

        base_dodge = 0
        max_dodge = 50

        water_form_bonus = 0
        if self.db.water_form:
            water_form_bonus = 10

        dodge = (
            base_dodge
            + water_form_bonus
            + (fluid_agility * 1.5)
            + (glvl * 0.2)
            + (self.db.dexterity * 0.1)
        )
        # 20 + 9 + 16 + 6 + 3 = 54
        if fluid_agility <= 4:
            dodge += 1
        if fluid_agility <= 7:
            dodge += 2
        if fluid_agility <= 10:
            dodge += 3
        if glvl >= 10:
            dodge += 1
        if glvl >= 20:
            dodge += 2
        if glvl >= 30:
            dodge += 3
        if dodge > max_dodge:
            dodge = max_dodge

        return dodge

    def at_damage(self, attacker, damage, damage_type=None):
        """
        Apply damage, after taking into account damage resistances.
        """
        self.msg(f"at damage in water elemental")
        glvl = self.db.guild_level
        con = self.traits.con.value
        hp = self.db.hp
        hpmax = self.db.hpmax
        aqua_resilience = self.db.skills.get("aqua resilience", 0)
        water_mastery = self.db.skills.get("water mastery", 0)

        hp_percentage = hp / hpmax
        reaction = int(self.db.reaction_percentage or 1) / 100

        percentage_reduction = 0
        flat_reduction = 0

        # Calculate dodge
        dodge = self._calculate_dodge()
        ran = randint(1, 100)
        if ran <= dodge:
            self.msg(f"|cYou dodge the attack!")
            attacker.msg(f"{self.get_display_name(attacker)} dodges your attack!")
            return

        # # Flat damage reduction - 50 con = 5 reduction, glvl 30 = 1.5 reduction
        flat_reduction = (
            con * 0.1 + glvl * 0.05 + aqua_resilience * 0.1 + water_mastery * 0.05
        )

        # # Percentage damage reduction 2% per skill level
        percentage_reduction = aqua_resilience * 0.02

        # apply aqua_shield after defense if it's enabled
        if self.db.aqua_shield:
            water_shield_absorbed = uniform(aqua_resilience / 3, aqua_resilience)
            damage -= water_shield_absorbed
            self.msg(f"|cYour water shield blocks some damage!")

        # Apply randomized flat reduction
        damage -= uniform(flat_reduction / 2, flat_reduction)

        # Apply percentage reduction
        damage *= 1 - percentage_reduction

        # Apply (worn) defense reduction
        damage -= self.defense(damage_type)

        # randomize damage
        damage = uniform(damage / 2, damage)

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

        # Check if the character is below the reaction percentage
        if hp_percentage < reaction and glvl > 3:
            self.msg(f"|cYou are below {reaction*100}% health!|n")
            self.execute_cmd("rejuvenate")

        if hp <= 0:
            self.tags.add("unconscious", category="status")
            self.tags.add("lying down", category="status")
            self.msg(
                "You fall unconscious. You can |wrespawn|n or wait to be |wrevive|nd."
            )
            if self.in_combat:
                combat = self.location.scripts.get("combat")[0]
                combat.remove_combatant(self)
