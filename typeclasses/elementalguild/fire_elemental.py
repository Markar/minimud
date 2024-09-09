import math
from random import randint, uniform, choice
from evennia.utils import delay, iter_to_str
from evennia import TICKER_HANDLER as tickerhandler
from commands.elemental_cmds import ElementalCmdSet
from typeclasses.elementalguild.fire_elemental_attack import FireAttack
from typeclasses.elementalguild.attack_emotes import AttackEmotes
from typeclasses.elementals import Elemental


class FireElemental(Elemental):

    def at_object_creation(self):
        self.cmdset.add(ElementalCmdSet, persistent=True)
        super().at_object_creation()
        con_increase_amount = 10
        int_increase_amount = 15
        self.db.con_increase_amount = con_increase_amount
        self.db.int_increase_amount = int_increase_amount
        self.db.hpmax = 50 + (con_increase_amount * self.traits.con.value)
        self.db.fpmax = 50 + (int_increase_amount * self.traits.int.value)

        self.db.guild_level = 1
        self.db.gxp = 0
        self.db.skill_gxp = 0
        self.db.title = "the novice fire elemental"

        self.db.natural_weapon = {
            "name": "fire_attack",
            "damage_type": "fire",
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

    def at_tick(self):
        base_regen = self.db.hpregen
        bonus_hp = 0
        base_ep_regen = self.db.epregen
        bonus_ep = 0
        base_fp_regen = self.db.fpregen
        bonus_fp = 0
        regen = self.db.skills.get("ember infusion")

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

        if self.db.heat_wave["duration"] > 0:
            rate = self.db.heat_wave["rate"]
            bonus_fp += uniform(rate / 2, rate + 1)
            if self.db.heat_wave["duration"] == 1:
                deactivateMsg = f"|C$Your() body cools down, and the air around $pron(you) returns to normal."
                self.location.msg_contents(deactivateMsg, from_obj=self)
            self.db.heat_wave["duration"] -= 1

        total_hp_regen = base_regen + bonus_hp
        total_fp_regen = base_fp_regen + bonus_fp
        total_ep_regen = base_ep_regen + bonus_ep

        self.adjust_hp(total_hp_regen)
        self.adjust_fp(total_fp_regen)
        self.adjust_ep(total_ep_regen)

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

    def _calculate_dodge(self):
        glvl = self.db.guild_level

        blazing_speed = self.db.skills.get("blazing speed", 1)
        base_dodge = 1
        max_dodge = 40

        dodge = (
            base_dodge + (blazing_speed * 2) + (glvl * 0.3) + (self.db.dexterity * 0.2)
        )

        if blazing_speed <= 4:
            dodge += 2
        if blazing_speed <= 7:
            dodge += 4
        if blazing_speed <= 10:
            dodge += 6
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
        glvl = self.db.guild_level
        hp = self.db.hp
        hpmax = self.db.hpmax
        damage -= self.defense(damage_type)
        inferno_resilience = self.db.skills.get("inferno resilience", 1)
        molten_armor = self.db.skills.get("molten armor", 1)

        hp_percentage = hp / hpmax
        reaction = int(self.db.reaction_percentage or 1) / 100

        percentage_reduction = 0
        flat_reduction = 0

        dodge = self._calculate_dodge()

        ran = randint(1, 100)
        if ran <= dodge:
            self.msg(f"You dodge the attack!")
            attacker.msg(f"{self.get_display_name(attacker)} dodges your attack!")
            return

        # Flat damage reduction - 50 con = 5 reduction, glvl 30 = 1.5 reduction
        flat_reduction = self.traits.con.value * 0.1 + glvl * 0.05 + inferno_resilience

        # Additional damage reduction from cyclone armor
        if self.db.flame_shield["hits"] > 0:
            flame_shield_reduction = molten_armor * 0.03 + inferno_resilience * 0.02
            percentage_reduction += flame_shield_reduction
            flat_reduction += molten_armor + inferno_resilience

            if self.db.flame_shield["hits"] == 1:
                deactivateMsg = f"|C$Your() flame shield flickers and fades, leaving only a wisp of smoke behind."
                self.location.msg_contents(deactivateMsg, from_obj=self)

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
