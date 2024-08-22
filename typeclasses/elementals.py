from random import randint, uniform, choice
from evennia.utils import delay
from evennia import TICKER_HANDLER as tickerhandler
from commands.elemental_cmds import ElementalCmdSet
from typeclasses.characters import PlayerCharacter
from typeclasses.elementalguild.earth_elemental_attack import EarthAttack
from typeclasses.elementalguild.attack_emotes import AttackEmotes
from typeclasses.utils import get_article, adjust_ep, adjust_fp, adjust_hp


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
        self.db.hpmax = 50 + (con_increase_amount * self.db.constitution)
        self.db.fpmax = 50 + (int_increase_amount * self.db.intelligence)

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
        self.db.subguild = "earth"
        self.db._wielded = {"left": None, "right": None}
        self.db.emit = 1
        self.db.maxEmit = 1
        self.db.hpregen = 1
        self.db.fpregen = 1
        self.db.epregen = 1
        self.db.strategy = "melee"
        self.at_wield(EarthAttack)
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

        to_me = f"{to_me} ({dam})"
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


# skill_table.add_row(f"|GAir Shield", f"|M{air_shield_cost}", f"|Y{SKILL_RANKS[air_shield]}")
# skill_table.add_row(f"|GWind Slash", f"|M{wind_slash_cost}", f"|Y{SKILL_RANKS[wind_slash]}")
# skill_table.add_row(f"|GWhirlwind", f"|M{whirlwind_cost}", f"|Y{SKILL_RANKS[whirlwind]}")
# skill_table.add_row(f"|GLightning Strike", f"|M{lightning_strike_cost}", f"|Y{SKILL_RANKS[lightning_strike]}")
# skill_table.add_row(f"|GStorm Form", f"|M{storm_form_cost}", f"|Y{SKILL_RANKS[storm_form]}")
# skill_table.add_row(f"|GAir Form", f"|M{air_form_cost}", f"|Y{SKILL_RANKS[air_form]}")
# skill_table.add_row(f"|GTornado", f"|M{tornado_cost}", f"|Y{SKILL_RANKS[tornado]}")
# skill_table.add_row(f"|GZephyr", f"|M{zephyr_cost}", f"|Y{SKILL_RANKS[zephyr]}")


# skill_table.add_row(f"|GEarth Shield", f"|M{earth_shield_cost}", f"|Y{SKILL_RANKS[earth_shield]}")
# skill_table.add_row(f"|GRock Throw", f"|M{rock_throw_cost}", f"|Y{SKILL_RANKS[rock_throw]}")
# skill_table.add_row(f"|GStone Skin", f"|M{stone_skin_cost}", f"|Y{SKILL_RANKS[stone_skin]}")
# skill_table.add_row(f"|GEarthquake", f"|M{earthquake_cost}", f"|Y{SKILL_RANKS[earthquake]}")
# skill_table.add_row(f"|GQuicksand", f"|M{quicksand_cost}", f"|Y{SKILL_RANKS[quicksand]}")
# skill_table.add_row(f"|GEarth Form", f"|M{earth_form_cost}", f"|Y{SKILL_RANKS[earth_form]}")
# skill_table.add_row(f"|GTremor", f"|M{tremor_cost}", f"|Y{SKILL_RANKS[tremor]}")
# skill_table.add_row(f"|GMountain Stance", f"|M{mountain_stance_cost}", f"|Y{SKILL_RANKS[mountain_stance]}")


# skill_table.add_row(f"|GFlame Shield", f"|M{flame_shield_cost}", f"|Y{SKILL_RANKS[flame_shield]}")
# skill_table.add_row(f"|GFireball", f"|M{fireball_cost}", f"|Y{SKILL_RANKS[fireball]}")
# skill_table.add_row(f"|GInferno", f"|M{inferno_cost}", f"|Y{SKILL_RANKS[inferno]}")
# skill_table.add_row(f"|GBlazing Speed", f"|M{blazing_speed_cost}", f"|Y{SKILL_RANKS[blazing_speed]}")
# skill_table.add_row(f"|GEmber Strike", f"|M{ember_strike_cost}", f"|Y{SKILL_RANKS[ember_strike]}")
# skill_table.add_row(f"|GFlame Form", f"|M{flame_form_cost}", f"|Y{SKILL_RANKS[flame_form]}")
# skill_table.add_row(f"|GHeat Wave", f"|M{heat_wave_cost}", f"|Y{SKILL_RANKS[heat_wave]}")
# skill_table.add_row(f"|GFirestorm", f"|M{firestorm_cost}", f"|Y{SKILL_RANKS[firestorm]}")


# skill_table.add_row(f"|GAqua Shield", f"|M{aqua_shield_cost}", f"|Y{SKILL_RANKS[aqua_shield]}")
# skill_table.add_row(f"|GWater Jet", f"|M{water_jet_cost}", f"|Y{SKILL_RANKS[water_jet]}")
# skill_table.add_row(f"|GHealing Waters", f"|M{healing_waters_cost}", f"|Y{SKILL_RANKS[healing_waters]}")
# skill_table.add_row(f"|GTidal Wave", f"|M{tidal_wave_cost}", f"|Y{SKILL_RANKS[tidal_wave]}")
# skill_table.add_row(f"|GIce Shard", f"|M{ice_shard_cost}", f"|Y{SKILL_RANKS[ice_shard]}")
# skill_table.add_row(f"|GWater Form", f"|M{water_form_cost}", f"|Y{SKILL_RANKS[water_form]}")
# skill_table.add_row(f"|GSoothing Mist", f"|M{soothing_mist_cost}", f"|Y{SKILL_RANKS[soothing_mist]}")
# skill_table.add_row(f"|GMaelstrom", f"|M{maelstrom_cost}", f"|Y{SKILL_RANKS[maelstrom]}")
