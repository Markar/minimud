from random import randint, uniform, choice
from evennia.utils import delay
from evennia import TICKER_HANDLER as tickerhandler
from commands.elemental_cmds import ElementalCmdSet
from typeclasses.characters import PlayerCharacter
from typeclasses.elementalguild.earth_elemental_attack import EarthAttack
from typeclasses.elementalguild.attack_emotes import AttackEmotes
from typeclasses.utils import get_article, get_display_name
from evennia.contrib.rpg.buffs import BaseBuff


class Elemental(PlayerCharacter):
    """
    The base typeclass for non-player characters, implementing behavioral AI.
    """

    def at_object_creation(self):
        self.cmdset.add(ElementalCmdSet, persistent=True)
        super().at_object_creation()
        con_increase_amount = 12
        int_increase_amount = 5
        self.db.con_increase_amount = con_increase_amount
        self.db.int_increase_amount = int_increase_amount
        self.db.con_bonus = 0
        self.db.hpmax = 50 + (
            con_increase_amount * (self.traits.con.value + self.db.con_bonus)
        )
        self.db.fpmax = 50 + (int_increase_amount * self.traits.int.value)
        self.db.epmax = 120

        self.db.guild_level = 1
        self.db.gxp = 0
        self.db.skill_gxp = 0
        self.db.title = "the novice Elemental"

        self.db.natural_weapon = {
            "name": "earth_attack",
            "damage_type": "blunt",
            "damage": 12,
            "speed": 3,
            "energy_cost": 10,
        }
        self.db.guild = "elemental"
        self.db._wielded = {"left": None, "right": None}
        self.db.hpregen = 1
        self.db.fpregen = 1
        self.db.epregen = 1
        self.db.strategy = "melee"
        self.db.burnout = {"active": False, "count": 0, "max": 0, "duration": 0}
        self.db.subguild = "earth"

        tickerhandler.add(
            interval=6, callback=self.at_tick, idstring=f"{self}-regen", persistent=True
        )
        tickerhandler.add(
            interval=60 * 2.5,
            callback=self.at_essence_tick,
            idstring=f"{self}-superpower",
            persistent=True,
        )

    def kickstart(self):
        self.msg("Kickstarting heartbeat")

        tickerhandler.add(
            interval=6, callback=self.at_tick, idstring=f"{self}-regen", persistent=True
        )

        tickerhandler.add(
            interval=300,
            callback=self.at_essence_tick,
            idstring=f"{self}-superpower",
            persistent=True,
        )

    def at_burnout_tick(self):
        return

    def at_tick(self):
        base_regen = self.db.hpregen
        base_ep_regen = self.db.epregen
        base_fp_regen = self.db.fpregen

        self.adjust_hp(base_regen)
        self.adjust_fp(base_ep_regen)
        self.adjust_ep(base_fp_regen)

    # property to mimic weapons
    @property
    def speed(self):
        weapon = self.db.natural_weapon
        return weapon.get("speed", 3)

    def at_wield(self, weapon, **kwargs):
        self.msg(f"You cannot wield weapons.")
        return False

    def get_player_attack_hit_message(
        self, attacker, dam, tn, emote="earth_elemental_melee"
    ):
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

        to_me = f"{to_me}"

        if self.key == "Markar":
            to_me += f"({dam})"

        self.location.msg_contents(to_me, from_obj=self)

        return to_me

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
