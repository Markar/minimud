import math
from random import randint, uniform, choice
from evennia.utils import delay, iter_to_str
from evennia import TICKER_HANDLER as tickerhandler
from commands.elemental_cmds import ElementalCmdSet
from typeclasses.elementalguild.air_elemental_attack import AirAttack

from typeclasses.elementals import Elemental


class AirElemental(Elemental):

    def at_object_creation(self):
        self.cmdset.add(ElementalCmdSet, persistent=True)
        super().at_object_creation()
        con_increase_amount = 13
        int_increase_amount = 12
        self.db.con_increase_amount = con_increase_amount
        self.db.int_increase_amount = int_increase_amount
        self.db.hpmax = 50 + (con_increase_amount * self.traits.con.value)
        self.db.fpmax = 50 + (int_increase_amount * self.traits.int.value)

        self.db.guild_level = 1
        self.db.gxp = 0
        self.db.skill_gxp = 0
        self.db.title = "the novice air elemental"

        self.db.natural_weapon = {
            "name": "air_attack",
            "damage_type": "blunt",
            "damage": 12,
            "speed": 3,
            "energy_cost": 10,
        }
        self.db.guild = "elemental"
        self.db.subguild = "air"
        self.db._wielded = {"left": None, "right": None}
        self.db.reaction_percentage = 50
        self.db.hpregen = 1
        self.db.fpregen = 1
        self.db.epregen = 1
        self.db.strategy = "melee"
        self.db.cyclone_armor = {"hits": 0}
        self.db.storm_form = False
        self.db.air_form = False
        self.db.skills = {
            "wind mastery": 1,
            "aerial agility": 1,
            "storm resilience": 1,
            "gale force": 1,
            "zephyr infusion": 1,
            "tempest control": 1,
            "elemental harmony": 1,
        }

        self.at_wield(AirAttack)
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
        if self.db.storm_form:
            chunks.append(f"|gStorm")
        if self.db.air_form:
            chunks.append(f"|gAir")
        if self.db.cyclone_armor["hits"] > 0:
            chunks.append(f"|gCA")

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
        base_ep_regen = self.db.epregen
        base_fp_regen = self.db.fpregen
        regen = self.db.skills["zephyr infusion"]

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

        self.adjust_hp(base_regen)
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
        weapon = AirAttack()

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

        aerial_agility = self.db.skills.get("aerial agility", 1)
        wind_mastery = self.db.skills.get("wind mastery", 1)

        base_dodge = 20
        max_dodge = 80

        dodge = (
            base_dodge
            + (aerial_agility * 2)
            + (glvl * 0.3)
            + (self.db.dexterity * 0.2)
            + (wind_mastery * 0.25)
        )
        # 20 + (22 + 8) + 9 + 16 + 2.5 = 77.5
        if aerial_agility <= 4:
            dodge += 2
        if aerial_agility <= 7:
            dodge += 4
        if aerial_agility <= 10:
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
        con = self.traits.con.value
        hp = self.db.hp
        hpmax = self.db.hpmax

        storm_resilience = self.db.skills.get("storm resilience", 1)
        cyclone_armor = self.db.skills.get("cyclone armor", 1)
        wind_mastery = self.db.skills.get("wind mastery", 1)

        hp_percentage = hp / hpmax
        reaction = int(self.db.reaction_percentage or 1) / 100

        percentage_reduction = 0
        flat_reduction = 0

        dodge = self._calculate_dodge()

        ran = randint(1, 100)
        if ran <= dodge:
            self.msg(f"|cYou dodge the attack!")
            attacker.msg(f"{self.get_display_name(attacker)} dodges your attack!")
            return

        # Flat damage reduction - 50 con = 5 reduction, glvl 30 = 1.5 reduction
        flat_reduction = (
            con * 0.1 + glvl * 0.05 + wind_mastery * 0.05 + storm_resilience
        )

        # Additional damage reduction from cyclone armor
        if self.db.cyclone_armor["hits"] > 0:
            cyclone_armor_reduction = cyclone_armor * 0.03 + storm_resilience * 0.02
            percentage_reduction += cyclone_armor_reduction
            flat_reduction += storm_resilience + storm_resilience + wind_mastery * 0.5

            if self.db.cyclone_armor["hits"] == 1:
                deactivateMsg = f"|C$Your() cyclone armor dissipates, leaving $pron(you) vulnerable to attacks."
                self.location.msg_contents(deactivateMsg, from_obj=self)

            self.db.cyclone_armor["hits"] -= 1
            if randint(1, 100) <= 33:
                self.msg(
                    f"|cYour cyclone armor absorbs the incoming attack, but is weakened by the impact.|n"
                )
            elif randint(1, 100) <= 66:
                self.msg(
                    f"|cA swirling vortex of air forms around you, deflecting the incoming attack with a powerful gust.|n"
                )
            elif randint(1, 100) <= 100:
                self.msg(
                    f"|cThe force of the blow is diminished as the shield of air absorbs the impact, leaving you unharmed and ready to counterattack!|n"
                )

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
