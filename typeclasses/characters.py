from random import randint, choice
from evennia.prototypes import spawner, prototypes
from evennia.prototypes.spawner import spawn
from string import punctuation
from evennia import AttributeProperty
from evennia.utils import lazy_property, iter_to_str, delay, logger
from evennia.contrib.rpg.traits import TraitHandler
from evennia.contrib.game_systems.clothing.clothing import (
    ClothedCharacter,
    get_worn_clothes,
)
from evennia.contrib.game_systems.cooldowns import CooldownHandler
from world.prototypes import MOB_CORPSE, IRON_DAGGER
import math
from .objects import ObjectParent

_IMMOBILE = ("sitting", "lying down", "unconscious")
_MAX_CAPACITY = 10
            
# LOOK INTO RESTORING THESE STATUSES

class Character(ObjectParent, ClothedCharacter):
    """
    The base typeclass for all characters, both player characters and NPCs
    """

    gender = AttributeProperty("plural")

    @property
    def in_combat(self):
        """Return True if in combat, otherwise False"""
        if not (location := self.location):
            # can't be in combat if we're nowhere!
            return False
        if not (combat_script := location.scripts.get("combat")):
            # there is no combat instance in this location
            return False

        # return whether we're in the combat instance's combatants
        return self in combat_script[0].fighters

    @property
    def can_flee(self):
        """
        Calculates chance of escape.

        Returns:
            True if you can flee, otherwise False
        """
        # use dex as a fallback for unskilled
        if not (evade := self.use_skill("evasion")):
            evade = self.db.dexterity
        # if you have more focus, you can escape more easily
        if (randint(0, 99) - self.db.fp) < evade:
            return True
        else:
            self.msg("You can't find an opportunity to escape.")
            return False

    @lazy_property
    def traits(self):
        # this adds the handler as .traits
        return TraitHandler(self)

    @lazy_property
    def cooldowns(self):
        return CooldownHandler(self, db_attribute="cooldowns")

    @property
    def wielding(self):
        """Access a list of all wielded objects"""
        return [obj for obj in self.attributes.get("_wielded", {}).values() if obj]

    @property
    def free_hands(self):
        return [
            key for key, val in self.attributes.get("_wielded", {}).items() if not val
        ]

    def defense(self, damage_type=None):
        """
        Get the total armor defence from equipped items and natural defenses
        """
        print(f"in defense {self} {damage_type}")
        defense_objs = get_worn_clothes(self) + [self]
        armor = sum(
            [obj.attributes.get("armor", 0) for obj in defense_objs]
        )
        if damage_type:
            armor += sum(
                [obj.attributes.get(f"{damage_type}ac", 0) for obj in defense_objs]
            )
            typeac = self.attributes.get(f"{damage_type}ac", 0)
            armor += self.attributes.get(f"{damage_type}ac", 0)

        return armor

    def at_object_creation(self):
        self.db.level = 1
        self.db.strength = 1
        self.db.dexterity = 1
        self.db.intelligence = 1
        self.db.wisdom = 1
        self.db.constitution = 1
        self.db.charisma = 1
        # resource stats
        self.db.hp = 50
        self.db.hpmax = 50
        self.db.hpregen = 1
        self.db.fp = 50
        self.db.fpmax = 50
        self.db.fpregen = 1
        self.db.ep = 50
        self.db.epmax = 50
        
        self.db.ac_types = {
            "edged": 0,
            "blunt": 0,
            "cold": 0,
            "fire": 0,
            "acid": 0,
            "poison": 0,
            "mind": 0,
            "lightning": 0,
            "energy": 0,  
        }

    def at_pre_move(self, destination, **kwargs):
        """
        Called by self.move_to when trying to move somewhere. If this returns
        False, the move is immediately cancelled.
        """
        # check if we have any statuses that prevent us from moving
        if statuses := self.tags.get(_IMMOBILE, category="status", return_list=True):
            self.msg(
                f"You can't move while you're {iter_to_str(sorted(statuses), endsep='or')}."
            )
            return False

        # check if we're in combat
        # if self.in_combat:
        #     self.msg("You can't leave while in combat.")
        #     return False

        return super().at_pre_move(destination, **kwargs)

    def at_post_move(self, source_location, **kwargs):
        """
        optional post-move auto prompt
        """
        super().at_post_move(source_location, **kwargs)
        if self.in_combat:
            combat = self.location.scripts.get("combat")[0]
            combat.remove_combatant(self)
        # check if we have auto-prompt in settings
        if self.account and (settings := self.account.db.settings):
            if settings.get("auto prompt"):
                status = self.get_display_status(self)
                self.msg(prompt=status)

    def at_damage(self, attacker, damage, damage_type=None):
        """
        Apply damage, after taking into account damage resistances.
        """
        # GENERALL NOT USED - OVERRIDEN BY NPC / PC / GUILD versions
  
        # apply armor damage reduction
        damage -= self.defense(damage_type)
        if damage < 0:
            damage = 0
        self.db.hp -= max(damage, 0)
        self.msg(f"You take {damage} damage from {attacker.get_display_name(self)}. Character")
        attacker.msg(f"You deal {damage} damage to {self.get_display_name(attacker)}.")
        if self.db.hp <= 0:
            # if self.in_combat:
            combat = self.location.scripts.get("combat")[0]
            combat.remove_combatant(self)

    def at_emote(self, message, **kwargs):
        """
        Execute a room emote as ourself.

        This acts as a wrapper to `self.location.msg_contents` to avoid boilerplate validation.
        """
        # if there is nothing to send or nowhere to send it to, cancel
        if not message or not self.location:
            return
        # add period to punctuation-less emotes
        if message[-1] not in punctuation:
            message += "."
        if kwargs.get("prefix", True) and not message.startswith("$You()"):
            message = f"$You() {message}"
        mapping = kwargs.get("mapping", None)

        self.location.msg_contents(text=message, from_obj=self, mapping=mapping)

    def at_wield(self, weapon, **kwargs):
        """
        Wield a weapon in one or both hands
        """
        # fetch the wielded info and detach from the DB
        wielded = self.attributes.get("_wielded", {})
        if wielded:
            wielded.deserialize()

        # which hand (or "hand") we'll wield it in
        # get all available hands
        free = self.free_hands

        if hand := kwargs.get("hand"):
            # if a specific hand was requested, check if it's available
            if hand not in free:
                # check if this is even a valid hand by trying to get what's in it
                if not (weap := wielded.get(hand)):
                    # no weapon was got, so it's not there
                    self.msg(f"You do not have a {hand}.")
                else:
                    # a weapon was found, provide this information
                    self.msg(
                        f"You are already wielding {weap.get_display_name(self)} in your {key}."
                    )
                return
        elif not free:
            # there are no hands available to wield this
            self.msg(f"Your hands are full.")
            return
        # handle two-handed weapons
        if weapon.tags.has("two_handed", category="wielded"):
            if len(free) < 2:
                # not enough free hands to hold this
                self.msg(
                    f"You need two hands free to wield {weapon.get_display_name(self)}."
                )
                return
            # put the weapon as wielded in the first two hands
            hands = free[:2]
            for hand in hands:
                wielded[hand] = weapon
        else:
            # check handedness first, then find a hand
            if main_hand := self.db.handedness:
                hand = main_hand if main_hand in free else free[0]
            else:
                hand = free[0]
            # put the weapon as wielded in the hand
            hands = [hand]
            wielded[hand] = weapon

        # update the character with the new wielded info
        self.db._wielded = wielded
        # return the list of hands that are now holding the weapon
        return hands

    def at_unwield(self, weapon, **kwargs):
        """
        Stop wielding a weapon
        """
        # fetch the wielded info and detach from the DB
        wielded = self.attributes.get("_wielded", {})
        if wielded:
            wielded.deserialize()

        # can't unwield a weapon you aren't wielding
        if weapon not in wielded.values():
            self.msg("You are not wielding that.")
            return

        # replace weapon with an instance of a bare hand
        freed = []
        for hand, weap in wielded.items():
            if weap == weapon:
                # create a correctly-named fist
                wielded[hand] = None
                # append the hand to the list of freed hands
                freed.append(hand)

        # update the character with the new wielded info
        self.db._wielded = wielded
        # return the list of hands that are no longer holding the weapon
        return freed

    def use_skill(self, skill_name, *args, **kwargs):
        """
        Attempt to use a skill, applying any stat bonus as necessary.
        """
        # handle cases where this was called but there's no skill being used
        if not skill_name:
            return 1
        # if we don't have the skill, we can't use it
        if not (skill_trait := self.traits.get(skill_name)):
            return 0
        # check if this skill has a related base stat
        stat_bonus = 0
        if stat := getattr(skill_trait, "stat", None):
            # get the stat to be a modifier
            stat_bonus = self.attributes.get(stat, 0)
        # finally, return the skill plus stat
        return skill_trait.value + stat_bonus

    def at_attack(self, wielder, target, **kwargs):
        """
        attack with your natural weapon
        """
        weapon = self.db.natural_weapon
        damage = weapon.get("damage", 0)
        speed = weapon.get("speed", 10)
        skill = weapon.get("skill")
        # attack with your natural attack skill - whatever that is
        self.msg(f"attack with natural attack: {skill and speed: {speed}}")
        result = self.use_skill(weapon.get("skill"), speed=speed)
        # apply the weapon damage as a modifier to skill
        self.msg(f"damage = damage * result: {damage}")
        damage = damage * result
        damage = randint(damage/2, damage)
        # subtract the energy required to use this
        self.db.ep -= weapon.get("energy_cost", 5)
        if not damage:
            # the attack failed
            self.at_emote(
                f"$conj(swings) $pron(your) {weapon.get('name')} at $you(target), but $conj(misses).",
                mapping={"target": target},
            )
        else:
            verb = weapon.get("damage_type", "hits")
            wielder.at_emote(
                f"$conj({verb}) $you(target) with $pron(your) {weapon.get('name')}.",
                mapping={"target": target},
            )
            # the attack succeeded! apply the damage
            target.at_damage(wielder, damage, weapon.get("damage_type"))
        wielder.msg(f"[ Cooldown: {speed} seconds ]")
        wielder.cooldowns.add("attack", speed)

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
        chunks.append(
            f"|gHealth: |G{hp}/{hpmax}|g Focus: |G{fp}/{fpmax} Energy: |G{ep}/{epmax}|g"
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

        # glue together the chunks and return
        return " - ".join(chunks)

    def at_character_arrive(self, chara, **kwargs):
        """
        Respond to the arrival of a character
        """
        pass

    def at_character_depart(self, chara, destination, **kwargs):
        """
        Respond to the departure of a character
        """
        pass

    def revive(self, reviver, **kwargs):
        """
        Revive a defeated character at partial health.
        """
        # this function receives the actor doing the revive so you could implement your own skill check
        # however, we don't have any relevant skills
        if self.tags.has("unconscious"):
            self.tags.remove("unconscious")
            self.tags.remove("lying down")
            # this sets the current HP to 20% of the max, a.k.a. one fifth
            self.db.hp = self.db.hpmax // 5
            self.msg(prompt=self.get_display_status(self))
    
    def get_emote(self, target, dam, display_name=None):
        color = "|r"
        tn = display_name

        return [
            f"{color}{self}{color} swings and misses, hitting nothing but air. {dam}",
            f"{color}{self}{color}'s hit causes minor bruises on {tn}{color} {dam}.",
            f"{color}{self}{color}'s hit causes {tn}{color} to bleed slightly. {dam}",
            f"{color}{self}{color} $conj(strike) {tn}{color} with a powerful blow! {dam}",
            f"{color}{self}{color}'s hit causes {tn}{color} to bleed profusely. {dam}",
            f"{color}{self}{color}'s hit cracks {tn}{color}'s bones! {dam}",
            f"{color}{self}{color} $conj(pummel) {tn}{color} with relentless force! {dam}",
            f"{color}{self}{color} $conj(smash) {tn}{color}'s limbs! {dam}",
            f"{color}{self}{color} $conj(crush) {tn}{color} like a bug! {dam}",
            f"{color}{self}{color} $conj(hit) {tn}{color} so hard that blood spatters around the room! {dam}",
            f"{color}{self}{color} $conj(tear) into {tn}{color} with brutal force! {dam}",
        ]
    def get_hit_message(self, target, dam, display_name ):

        msgs = self.get_emote(target, dam, display_name)
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
            
        self.location.msg_contents(to_me, from_obj=self)
                    
        return to_me


class PlayerCharacter(Character):
    """
    The typeclass for all player characters, including special player-feedback features.
    """

    def at_object_creation(self):
        super().at_object_creation()
        self.tags.add("player", category="status")
        self.db.title = "the title less"
        self.db.alignment = "neutral"
        self.db.stat_points = 5
        self.db.con_increase_amount = 9
        self.db.int_increase_amount = 8
        self.db.guild = "adventurer"
        self.db.natural_weapon = {
            "name": "fist",
            "damage_type": "blunt",
            "damage": 5,
            "speed": 3,
            "energy_cost": 1
        }
      
        # initialize hands
        self.db._wielded = {"left": None, "right": None}

    def get_display_name(self, looker, **kwargs):
        """
        Adds color to the display name.
        """
        name = super().get_display_name(looker, **kwargs)
        if looker == self:
            # special color for our own name
            return f"|c{name}|n"
        return f"|g{name}|n"

    def at_pre_object_receive(self, object, source_location, **kwargs):
        """
        Called before picking something up or being given something. If this returns
        False, the move is immediately cancelled.
        """
        # check if we have any statuses that prevent us from moving
        if len([obj for obj in self.contents if not obj.db.worn]) > _MAX_CAPACITY:
            self.msg("You can't carry any more things.")
            source_location.msg(
                f"{self.get_display_name(source_location)} can't carry any more things."
            )
            return False
        return super().at_pre_object_receive(object, source_location, **kwargs)

    def at_damage(self, attacker, damage, damage_type=None):
        """
        Apply damage, after taking into account damage resistances.
        """
        # GENERALLY NOT CALLED - OVERRIDEN BY GUILD VERSION
        self.msg(f"at_damage in PC")
        # apply armor damage reduction
        damage -= self.defense(damage_type)
        if damage < 0:
            damage = 0
        self.db.hp -= max(damage, 0)
        # self.msg(f"You take {damage} damage from {attacker.get_display_name(self)} PC.")
        # attacker.msg(f"You deal {damage} damage to {self.get_display_name(attacker)}.")
        # self.get_hit_message(attacker, damage, f"PC at_damage {self.get_display_name(attacker)}")
        attacker.get_hit_message(attacker, damage, f"PC at_damage {self.get_display_name(attacker)}")
        
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
            

    def attack(self, target, weapon, **kwargs):
        """
        Execute an attack

        Args:
            target (Object or None): the entity being attacked. if None, attempts to use the combat_target db attribute
            weapon (Object): the object dealing damage
        """
        self.msg(f"PC atack: {self} and {target} and {weapon}")
        # can't attack if we're not in combat!
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

        print(f"weapon {weapon}")
        # attack with the weapon
        weapon.at_attack(self, target)

        status = self.get_display_status(target)
        self.msg(prompt=status)

        # check if we have auto-attack in settings
        if self.account and (settings := self.account.db.settings):
            if settings.get("auto attack") and (speed := weapon.speed):
                # queue up next attack; use None for target to reference stored target on execution
                delay(speed + 1, self.attack, None, weapon, persistent=True)

    def use_heal(self):
        """
        Restores health
        """
        hp = self.db.hp
        hpmax = self.db.hpmax
        ep = self.db.ep
        epmax = self.db.epmax
        hp_amount = 0
        ep_amount = 0
        
        damage = 50
        if hp + damage > hpmax:            
            hp_amount = hpmax-hp
            self.db.hp = hpmax
        else: 
            hp_amount = hpmax-hp
            self.db.hp += max(damage, 0)
            
        if ep + damage > epmax:
            ep_amount = epmax-ep
            self.db.ep = epmax
        else: 
            ep_amount = epmax-ep
            self.db.ep += max(damage, 0)
            
        self.msg(f"You restore {hp_amount or 0} health and {ep_amount or 0} energy!")

    def use_fireball(self, target, **kwargs):
        """
        Attempt to cast fireball
        """
        if not target:
            self.msg(f"|GTarget whom?")
            return

        if not self.db.combat_target:
            self.enter_combat(target)
        else:
            self.db.combat_target = target
        target.enter_combat(self)
        if not self.cooldowns.ready("fireball"):
            self.msg(f"|BNot so fast!")
            return False

        damage = 80
        self.msg(f"|RYou cast fireball!")

        target.at_damage(self, damage, "fire")
        self.cooldowns.add("fireball", 1)

    def respawn(self):
        """
        Resets the character back to the spawn point with full health.
        """
        self.tags.remove("unconscious", category="status")
        self.tags.remove("lying down", category="status")
        self.db.hp = self.db.hpmax
        self.move_to(self.home)
        self.msg(prompt=self.get_display_status(self))


class NPC(Character):
    """
    The base typeclass for non-player characters, implementing behavioral AI.
    """

    # defines what color this NPC's name will display in
    name_color = AttributeProperty("w")

    # property to mimic weapons
    @property
    def speed(self):
        weapon = self.db.natural_weapon
        if not weapon:
            return 10
        return weapon.get("speed", 10)

    def at_object_creation(self):
        super().at_object_creation()
        
    def get_display_name(self, looker, **kwargs):
        """
        Adds color to the display name.
        """
        name = super().get_display_name(looker, **kwargs)
        return f"|{self.name_color}{name}|n"

    def at_character_arrive(self, chara, **kwargs):
        """
        Respond to the arrival of a character
        """
        if "aggressive" in self.attributes.get("react_as", "") and chara.tags.has("player", "status"):
            delay(1, self.enter_combat, chara)

    def at_character_depart(self, chara, destination, **kwargs):
        """
        Respond to the departure of a character
        """
        if chara == self.db.following:
            # find an exit that goes the same way
            exits = [
                x
                for x in self.location.contents_get(content_type="exit")
                if x.destination == destination
            ]
            if exits:
                # use the exit
                self.execute_cmd(exits[0].name)

    def at_respawn(self):
        print(f"at_respawn in npc: {self} and home {self.home}")
        self.use_heal()
        # self.move_to(self.home)
        self.move_to(self.home, False, None, True, True, True, "teleport")
                  
    def at_damage(self, attacker, damage, damage_type=None, emote="bite"):
        """
        Apply damage, after taking into account damage resistances.
        """
        # apply armor damage reduction
        damage -= self.defense(damage_type)
        if damage < 0:
            damage = 0
        self.db.hp -= max(damage, 0)
        self.msg(f"You take {damage} damage from {attacker.get_display_name(self)} NPC.")
        # this sends the hit_msg FROM the player TO the room with the damage AFTER reduction by npc
        # this comes from the changelings class, where the emotes live
        attacker.get_hit_message(attacker, damage, f"{self.get_display_name(attacker)}", emote)
        
        if self.db.hp <= 0:
            self.tags.add("defeated", category="status")
            # we've been defeated!
            if combat_script := self.location.scripts.get("combat"):
                combat_script = combat_script[0]
                if not combat_script.remove_combatant(self):
                    # something went wrong...
                    return
                
                # create loot drops
                corpse = {
                    "key": f"|Ya decaying corpse of {self}",
                    "typeclass": "typeclasses.corpse.Corpse",
                    "desc": f"|YThe decaying corpse of {self} lies here. It looks heavy, and full of nutrients.|n",
                    "location": self.location,
                    "power": self.db.level * 8
                }
                
                corpses = spawner.spawn(corpse)
                # for corpse in corpses:
                #     delay(10, corpse.delete)
                #     self.location.msg_contents(f"A {corpse.key} appears.", from_obj=self)
                
                if self.db.drops:
                    objs = spawn(*list(self.db.drops))
                    for obj in objs:
                        obj.location = self.location
                self.move_to(None, False, None, True, True, True, "teleport")
                delay(10, self.at_respawn)
                return
            
        if not self.db.combat_target:
            self.enter_combat(attacker)
        else:
            self.db.combat_target = attacker


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
        print(f"set combat_target")
        self.db.combat_target = target
        # adding a combatant to combat just returns True if they're already there, so this is safe
        if not combat_script.add_combatant(self, enemy=target):
            return
        print(f"before npc attack")
        self.attack(target, weapon)
          

    def attack(self, target, weapon, **kwargs):
        # can't attack if we're not in combat, or if we're fleeing
        if not self.in_combat or self.db.fleeing:
            return
        # if target is not set, use stored target
        if not target:
            # make sure there's a stored target
            if not (target := self.db.combat_target):
                return
        # verify that target is still here
        if self.location != target.location:
            return
        # make sure that we can use our chosen weapon
        if not (hasattr(weapon, "at_pre_attack") and hasattr(weapon, "at_attack")):
            return
        if not weapon.at_pre_attack(self):
            return

        # attack with the weapon
        weapon.at_attack(self, target)
        # queue up next attack; use None for target to reference stored target on execution
        delay(weapon.speed + 1, self.attack, None, weapon, persistent=True)

    def at_pre_attack(self, wielder, **kwargs):
        """
        NPCs can use themselves as their weapon data; verify that they can attack
        """
        if self != wielder:
            return
        if not (weapon := self.db.natural_weapon):
            return
        # make sure wielder has enough strength left
        self.msg(f"ep pre-attack: {self.db.ep}")
        if self.db.ep < weapon.get("energy_cost", 5):
            return False
        # can't attack if on cooldown
        if not wielder.cooldowns.ready("attack"):
            return False

        return True

    def at_attack(self, wielder, target, **kwargs):
        """
        attack with your natural weapon
        """
        weapon = self.db.natural_weapon
        damage = weapon.get("damage", 0)
        speed = weapon.get("speed", 10)
        # attack with your natural attack skill - whatever that is
        result = self.use_skill(weapon.get("skill"), speed=speed)
        # apply the weapon damage as a modifier to skill
        damage = damage * result
        damage = randint(damage/2, damage)
        # subtract the energy required to use this
        # self.db.ep -= weapon.get("energy_cost", 5)
        # if not damage:
        #     # the attack failed
        #     self.at_emote(
        #         f"$conj(swings) $pron(your) {weapon.get('name')} at $you(target), but $conj(misses).",
        #         mapping={"target": target},
        #     )
        # else:
        #     verb = weapon.get("damage_type", "hits")
        #     wielder.at_emote(
        #         f"$conj({verb}) $you(target) with $pron(your) {weapon.get('name')}.",
        #         mapping={"target": target},
        #     )
            # the attack succeeded! apply the damage
        target.at_damage(wielder, damage, weapon.get("damage_type"))
        wielder.msg(f"[ Cooldown: {speed} seconds ]")
        wielder.cooldowns.add("attack", speed)
    
        
    def use_heal(self):
        """
        Restores health
        """

        print(f"NPC heals itself {self}")
        self.db.hp = self.db.hpmax
        self.db.ep = self.db.epmax
        
        
        
