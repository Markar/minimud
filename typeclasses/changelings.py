from random import randint, uniform, uniform
from evennia.utils import lazy_property, iter_to_str, delay, logger
from evennia.contrib.rpg.traits import TraitHandler
from evennia.contrib.game_systems.cooldowns import CooldownHandler
from evennia import TICKER_HANDLER as tickerhandler
import math
from commands.changeling_cmds import ChangelingCmdSet
from typeclasses.characters import PlayerCharacter

from typeclasses.changelingguild.attack_emotes import AttackEmotes
from typeclasses.changelingguild.changeling_constants_and_helpers import FORM_CLASSES
from typeclasses.utils import geHealthStatus


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
            "energy_dissipation": 1,
            "regeneration": 1,
        }
        self.db.body_control = {
            "active": False,
            "amount": 0,
            "boostedStat": None,
            "nerfedStat": None,
        }
        self.db.ec = {
            "active": False,
            "duration": 0,
        }
        self.db.ed = {
            "active": False,
            "duration": 0,
        }
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

    def at_docwagon_tick(self):
        return

    def at_tick(self):
        glvl = self.db.guild_level
        ep = self.db.ep
        regen_skill = getattr(self.db, "skills", {}).get("regeneration", 1)

        hp = self.db.hp
        hpmax = self.db.hpmax
        base_regen = 1
        base_ep_regen = 1
        base_fp_regen = 1
        hp_regen_amt = base_regen

        ec_active = getattr(self.db, "ec", {}).get("active", False)
        ec_duration = getattr(self.db, "ec", {}).get("duration", 0)
        ed_active = getattr(self.db, "ed", {}).get("active", False)
        ed_duration = getattr(self.db, "ed", {}).get("duration", 0)

        # tick down EC duration
        if ec_active:
            if ec_duration < 1:
                self.msg(f"|cYour energy control fades.")
                setattr(self.db, "ec", {"active": False, "duration": 0})
            elif ec_duration == 10:
                self.msg(f"|cYou sense your energy control is fading.")
                setattr(self.db, "ec", {"active": True, "duration": ec_duration - 1})
            else:
                setattr(self.db, "ec", {"active": True, "duration": ec_duration - 1})

        # tick down ED duration
        if ed_active:
            if ed_duration < 1:
                self.msg(f"|cYour energy dissipation fades.")
                setattr(self.db, "ed", {"active": False, "duration": 0})
            elif ed_duration == 10:
                self.msg(f"|cYou sense your energy dissipation is fading.")
                setattr(self.db, "ed", {"active": True, "duration": ed_duration - 1})
            else:
                setattr(self.db, "ed", {"active": True, "duration": ed_duration - 1})

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

        ep_bonus = regen_skill / 2 + glvl / 10

        self.adjust_hp(hp_regen_amt)
        self.adjust_fp(base_fp_regen)
        self.adjust_ep(base_ep_regen + ep_bonus)

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
        # can't attack if we're not in combat!
        # Loop through the form classes and assign the appropriate weapon
        if self.db.form in FORM_CLASSES:
            weapon = FORM_CLASSES[self.db.form]()

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

        if self.key == "Markar":
            to_me = f"{to_me} {dam}"
        else:
            to_me = f"{to_me}"

        self.location.msg_contents(to_me, from_obj=self)
        print(f"to_me: {to_me} ({dam})")

        return to_me

    def at_damage(self, attacker, damage, damage_type=None):
        """
        Apply damage to self, after taking into account damage resistances.
        """
        form = FORM_CLASSES[self.db.form]
        glvl = self.db.guild_level
        form_dodge = form.dodge
        form_toughness = form.toughness
        ec = getattr(self.db, "skills", {}).get("energy_control", 1)
        ed = getattr(self.db, "skills", {}).get("energy_dissipation", 1)

        # if(energy_diss_skill <= 2) energy_diss = (guild_level * 2) + random(guild_level/2) + random(30) + 2*energy_diss_skill;
        # if(energy_diss_skill <= 5) energy_diss = (guild_level * 2) + random(guild_level/2) + random(40) + 2*energy_diss_skill;
        # if(admin || energy_diss_skill >=7)
        # energy_diss = 2*energy_diss_skill + (guild_level * 2) + random(guild_level/2) + random(50) + random(2*energy_diss_skill);
        #     energy_diss = (guild_level * 2) + random(guild_level/2) + random(30) + random(2 * energy_diss_skill);
        #     return;
        if ec <= 2:
            ec_amt = (glvl * 2) + uniform(0, glvl / 2) + uniform(0, 30) + (ec * 2)
        if ec <= 5:
            ec_amt = (glvl * 2) + uniform(0, glvl / 2) + uniform(0, 40) + (ec * 2)
        if ec >= 7:
            ec_amt = (
                (glvl * 2)
                + uniform(0, glvl / 2)
                + uniform(0, 50)
                + uniform(0, 2 * ec)
                + (ec * 2)
            )

        if ed < 3:
            ed_amt = (glvl * 2) + uniform(0, glvl / 2) + uniform(ed, glvl) + ed
        elif ed < 6:
            ed_amt = (
                (glvl * 2) + uniform(0, glvl / 2) + uniform(ed, glvl * 1.5) + 2 * ed
            )
        else:
            ed_amt = (
                (glvl * 2) + uniform(0, glvl / 2) + uniform(ed, glvl * 2) + 2.5 * ed
            )

        dodge = self.traits.dex.value / 5 + form_dodge * glvl / 12
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
        ec_active = getattr(self.db, "ec", {}).get("active", False)
        ed_active = getattr(self.db, "ed", {}).get("active", False)

        if ec_active and damage_type in ["edged", "blunt"]:
            damage -= ec_amt

        if ed_active and damage_type in [
            "energy",
            "lightning",
            "fire",
            "cold",
            "acid",
            "poison",
            "radiation",
            "mind",
        ]:
            damage -= ed_amt
            self.db.ep -= 1
            self.msg(f"|cYou block some damage!")

        self.db.hp -= max(damage, 0)
        # self.msg(f"You take {damage} damage from {attacker.get_display_name(self)}.")
        # attacker.msg(f"You deal {damage} damage to {self.get_display_name(attacker)}.")
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

    def get_form_help(self, form):
        form_class = FORM_CLASSES[form.title()]
        return form_class.__doc__

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

        ec_active = getattr(self.db, "ec", {}).get("active", False)

        ecVis = ""
        edVis = ""
        regrowthVis = ""
        if ec_active:
            ecVis = "EC"
        if self.db.energy_dissipation:
            edVis = "ED"
        if self.db.regrowth:
            regrowthVis = "CG"

        chunks.append(
            f"|gHealth: |G{hp}/{hpmax}|g Focus: |G{fp}/{fpmax}|g Energy: |G{ep}/{epmax}|g Form: |G{self.db.form} |gEngulfs: |G{self.db.engulfs}/{self.db.max_engulfs} |Y{ecVis} |Y {edVis} |Y{regrowthVis}"
        )

        if looker != self:
            chunks.append(f"|gE: |G{looker.get_display_name(self, **kwargs)}")
            hpPct = looker.db.hp / looker.db.hpmax
            status = geHealthStatus(self, hpPct)
            chunks.append(f"|gH: |G{status}")
            if self.key == "Markar":
                chunks.append(f"{looker.db.hp} / {looker.db.hpmax}")
            # append mob's health status ({looker.db.hp})

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
            self.at_emote("$conj(charges) at {target}!", mapping={"target": target})
        location = self.location

        if not (combat_script := location.scripts.get("combat")):
            # there's no combat instance; start one
            from typeclasses.scripts import CombatScript

            print("changeling combat script not found")

            location.scripts.add(CombatScript, key="combat")

        combat_script = location.scripts.get("combat")
        print(f"changeling 1 combat script: {combat_script}")
        combat_script = combat_script[0]
        print(f"changeling 2 combat script: {combat_script}")

        self.db.combat_target = target

        print(f"changeling combat target: {target}")
        # adding a combatant to combat just returns True if they're already there, so this is safe
        if not combat_script.add_combatant(self, enemy=target):
            print(f"combat script add combatant failed")
            return
        self.attack(target, weapon)

    def can_wear(self, item):
        """
        Check if the character can wear an item
        """
        armor = getattr(item.db, "armor", False)
        type = getattr(item.db, "type", False)
        allowed_types = ["light"]

        if not item:
            return False

        if not item.db.clothing_type:
            self.msg(f"{item} is not wearable.")
            return False

        if armor and type not in allowed_types:
            self.msg(f"You can't wear that kind of armor.")
            return False

        return True
