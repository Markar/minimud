from random import choice, uniform
from evennia import AttributeProperty
from evennia.utils import logger
from evennia.contrib.game_systems.containers import ContribContainer
import math

from .objects import Object, ClothingObject


class BareHand:
    """
    A dummy "object" class that provides basic combat functionality for unarmed combat
    """

    damage = 5
    energy_cost = 3
    skill = "unarmed"
    name = "fist"
    speed = 3
    gxp_rate = 5

    def at_pre_attack(self, wielder, **kwargs):
        """
        Validate that this is usable - has ammo, etc.
        """
        # make sure wielder has enough strength left
        # print(f"at_pre_attack on weapon: {wielder} and {wielder.db.ep} and self {self}")
        if wielder.db.ep < self.energy_cost:
            wielder.msg("You are too tired to hit anything.")
            return False
        # can't attack if on cooldown
        if not wielder.cooldowns.ready("attack"):
            wielder.msg("You can't attack again yet.")
            return False

        return True

    def at_attack(self, wielder, target, **kwargs):
        """
        Hit something with your fists!
        """
        damage = wielder.db.natural_weapon.get("damage", 5) or self.damage
        speed = wielder.db.natural_weapon.get("speed", 3) or self.speed
        energy_cost = (
            wielder.db.natural_weapon.get("energy_cost", 3) or self.energy_cost
        )
        name = wielder.db.natural_weapon.get("name", "fist") or self.name

        wielder.db.ep -= energy_cost

        if not damage:
            # the attack failed
            wielder.at_emote(
                f"$conj(swings) $pron(your) {name} at $you(target), but $conj(misses).",
                mapping={"target": target},
            )
        else:
            wielder.at_emote(
                f"$conj(hits) $you(target) with $pron(your) {name}.",
                mapping={"target": target},
            )
            # the attack succeeded! apply the damage
            target.at_damage(wielder, damage, "bludgeon")

        wielder.db.gxp += self.gxp_rate
        wielder.msg(f"[ Cooldown: {speed} seconds ]")
        wielder.cooldowns.add("attack", speed)


class MeleeWeapon(Object):
    """
    Weapons that you hit things with
    """

    speed = AttributeProperty(10)

    def at_pre_attack(self, wielder, **kwargs):
        """
        Validate that this is usable - has ammo, etc.
        """
        self.msg("at_pre_attack MeleeWeapon")
        # make sure wielder has enough strength left
        if wielder.db.ep < self.attributes.get("energy_cost", 0):
            wielder.msg("You are too tired to use this.")
            return False
        # can't attack if on cooldown
        if not wielder.cooldowns.ready("attack"):
            wielder.msg("You can't attack again yet.")
            return False
        # this can only be used if it's being wielded
        if self not in wielder.wielding:
            wielder.msg(
                f"You must be wielding your {self.get_display_name(wielder)} to attack with it."
            )
            return False
        else:
            return True

    def at_attack(self, wielder, target, **kwargs):
        """
        Use this weapon in an attack against a target.
        """
        self.msg("at_attack MeleeWeapon")
        # get the weapon's damage bonus
        damage = self.db.dmg
        # pick a random option from our possible damage types
        damage_type = None
        if damage_types := self.tags.get(category="damage_type", return_list=True):
            print(f"melee at_attack: {choice(damage_types)}")
            damage_type = choice(damage_types)

        # does this require skill to use?
        if skill := self.tags.get(category="skill_class"):
            # use the skill
            result = wielder.use_skill(skill, speed=self.speed)
            # apply the weapon damage as a modifier
            damage = damage * result
            damage = math.ceil(uniform(damage / 2, damage))
        # if no skill required, we are just using our unmodified damage value

        # subtract the energy required to use this
        wielder.db.ep -= self.attributes.get("energy_cost", 0)

        # the attack succeeded! apply the damage
        target.at_damage(wielder, damage, damage_type)

        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("attack", self.speed)


class WearableContainer(ContribContainer, ClothingObject):
    pass
