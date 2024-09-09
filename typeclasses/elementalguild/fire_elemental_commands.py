import math
from random import randint, uniform
from evennia import CmdSet
from evennia.utils.evtable import EvTable
from commands.command import Command
from typeclasses.elementalguild.constants_and_helpers import SKILLS_COST
from typeclasses.utils import PowerCommand


class CmdEmberStrike(PowerCommand):
    """
    The fire elemental can strike their enemies with a bolt of fire,
    dealing damage based on their wisdom and guild level.

    Usage:
        ember strike <target>
    """

    key = "ember strike"
    aliases = ["es"]
    help_category = "fire elemental"
    guild_level = 2
    cost = 5

    def _calculate_damage(self, guild_level):
        base_value = 5
        flame_mastery_weight = 10
        wisdom_weight = 0.3
        guild_level_weight = 1
        flame_mastery = self.caller.db.skills.get("flame mastery", 1)
        wisdom = self.caller.traits.wis.value

        damage = (
            base_value
            + (flame_mastery * flame_mastery_weight)
            + (wisdom * wisdom_weight)
            + (guild_level * guild_level_weight)
        )

        # Ensure damage is within the range of 100 to 300
        damage = max(1, min(damage, 100))

        # Adding some randomness to the damage
        damage = int(uniform(damage * 0.55, damage))

        return damage

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        target = caller.search(caller.db.combat_target)

        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return

        if not caller.cooldowns.ready("ember strike"):
            caller.msg(f"|CNot so fast!")
            return False

        if not target:
            target = caller.search(self.args)
            if not target:
                caller.msg("Ember strike who?")
                return
            target.enter_combat(caller)
            caller.enter_combat(target)

        if not caller.db.fp >= self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.cooldowns.add("ember strike", 6)
        caller.cooldowns.add("global_cooldown", 2)

        caller.msg(f"|MYou strike {target} with a bolt of fire.")
        target.msg(f"|M{caller} strikes you with a bolt of fire.")
        caller.location.msg_contents(
            f"|M{caller} strikes {target} with a bolt of fire.",
            exclude=[caller, target],
        )

        damage = self._calculate_damage(glvl)

        target.at_damage(caller, damage, "fire", "ember_strike")


class CmdFirePunch(PowerCommand):
    """
    The fire elemental can punch their enemies with a fist of fire,
    dealing damage based on their wisdom and guild level.

    Usage:
        firepunch <target>
    """

    key = "firepunch"
    aliases = ["fp"]
    help_category = "fire elemental"
    guild_level = 6
    cost = 10

    def _calculate_damage(self, guild_level):
        caller = self.caller
        base_value = 15
        flame_mastery_weight = 10
        wisdom_weight = 0.3
        guild_level_weight = 1
        flame_mastery = caller.db.skills.get("flame mastery", 1)
        wisdom = caller.traits.wis.value

        damage = (
            base_value
            + (flame_mastery * flame_mastery_weight)
            + (wisdom * wisdom_weight)
            + (guild_level * guild_level_weight)
        )

        # Ensure damage is within the range of 100 to 300
        damage = max(1, min(damage, 125))

        # Adding some randomness to the damage
        damage = int(uniform(damage * 0.6, damage))

        return damage

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        target = caller.search(caller.db.combat_target)

        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return

        if not caller.cooldowns.ready("fire_punch"):
            caller.msg(f"|CNot so fast!")
            return False

        if not target:
            target = caller.search(self.args)
            if not target:
                caller.msg("Fire punch who?")
                return
            target.enter_combat(caller)
            caller.enter_combat(target)

        if not caller.db.fp >= self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.cooldowns.add("fire_punch", 6)
        caller.cooldowns.add("global_cooldown", 2)

        caller.msg(f"|MYou punch {target} with a fist of fire.")
        target.msg(f"|M{caller} punches you with a fist of fire.")
        caller.location.msg_contents(
            f"|M{caller} punches {target} with a fist of fire.",
            exclude=[caller, target],
        )

        damage = self._calculate_damage(glvl)

        target.at_damage(caller, damage, "fire", "fire_punch")


class CmdFireWhip(PowerCommand):
    """
    The fire elemental can summon a whip of fire to strike their enemies,
    dealing damage based on their wisdom and guild level.

    Usage:
        firewhip <target>
    """

    key = "firewhip"
    aliases = ["fw"]
    help_category = "fire elemental"
    guild_level = 12
    cost = 15

    def _calculate_damage(self, guild_level):
        caller = self.caller
        base_value = 30
        flame_mastery_weight = 10
        wisdom_weight = 0.3
        guild_level_weight = 1
        flame_mastery = caller.db.skills.get("flame mastery", 1)
        wisdom = caller.traits.wis.value

        damage = (
            base_value
            + (flame_mastery * flame_mastery_weight)
            + (wisdom * wisdom_weight)
            + (guild_level * guild_level_weight)
        )

        # Ensure damage is within the range of 100 to 300
        damage = max(1, min(damage, 160))

        # Adding some randomness to the damage
        damage = int(uniform(damage * 0.65, damage * 1.1))

        return damage

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        target = caller.search(caller.db.combat_target)

        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return

        if not caller.cooldowns.ready("firewhip"):
            caller.msg(f"|CNot so fast!")
            return False

        if not target:
            target = caller.search(self.args)
            if not target:
                caller.msg("Firewhip who?")
                return
            target.enter_combat(caller)
            caller.enter_combat(target)

        if not caller.db.fp >= self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.cooldowns.add("firewhip", 6)
        caller.cooldowns.add("global_cooldown", 2)

        caller.msg(f"|MYou summon a whip of fire to strike {target}.")
        target.msg(f"|M{caller} summons a whip of fire to strike you.")
        caller.location.msg_contents(
            f"|M({caller}) summons a whip of fire to strike {target}.",
            exclude=[caller, target],
        )

        damage = self._calculate_damage(glvl)

        target.at_damage(caller, damage, "fire", "fire_whip")


class CmdLavaBurst(PowerCommand):
    """
    The fire elemental can hurl a burst of lava at their enemies,
    dealing damage based on their wisdom and guild level.

    Usage:
        lavaburst <target>
    """

    key = "lavaburst"
    aliases = ["lb"]
    help_category = "fire elemental"
    guild_level = 15
    cost = 20

    def _calculate_damage(self, guild_level):
        caller = self.caller
        base_value = 45
        flame_mastery_weight = 10
        wisdom_weight = 0.3
        guild_level_weight = 1
        flame_mastery = caller.db.skills.get("flame mastery", 1)
        wisdom = caller.traits.wis.value

        damage = (
            base_value
            + (flame_mastery * flame_mastery_weight)
            + (wisdom * wisdom_weight)
            + (guild_level * guild_level_weight)
        )

        # Ensure damage is within the range of 100 to 200
        damage = max(1, min(damage, 200))

        # Adding some randomness to the damage
        damage = int(uniform(damage * 0.7, damage * 1.15))

        return damage

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        target = caller.search(caller.db.combat_target)

        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return

        if not caller.cooldowns.ready("lava_burst"):
            caller.msg(f"|CNot so fast!")
            return False

        if not target:
            target = caller.search(self.args)
            if not target:
                caller.msg("Lavaburst who?")
                return
            target.enter_combat(caller)
            caller.enter_combat(target)

        if not caller.db.fp >= self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.cooldowns.add("lava_burst", 6)
        caller.cooldowns.add("global_cooldown", 2)

        caller.msg(f"|MYou hurl a burst of lava at {target}.")
        target.msg(f"|M{caller} hurls a burst of lava at you.")
        caller.location.msg_contents(
            f"|M{caller} hurls a burst of lava at {target}.",
            exclude=[caller, target],
        )

        damage = self._calculate_damage(glvl)

        target.at_damage(caller, damage, "fire", "lava_burst")


class CmdFireball(PowerCommand):
    """
    The fire elemental can hurl a ball of fire at their enemies,
    dealing damage based on their wisdom and guild level.

    Usage:
        fireball <target>
    """

    key = "fireball"
    aliases = ["fb"]
    help_category = "fire elemental"
    guild_level = 18
    cost = 25

    def _calculate_damage(self, guild_level):
        caller = self.caller
        base_value = 60
        flame_mastery_weight = 10
        wisdom_weight = 0.3
        guild_level_weight = 1
        flame_mastery = caller.db.skills.get("flame mastery", 1)
        wisdom = caller.traits.wis.value

        damage = (
            base_value
            + (flame_mastery * flame_mastery_weight)
            + (wisdom * wisdom_weight)
            + (guild_level * guild_level_weight)
        )

        # Ensure damage is within the range of 100 to 300
        damage = max(1, min(damage, 225))

        # Adding some randomness to the damage
        damage = int(uniform(damage * 0.75, damage * 1.2))

        return damage

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        target = caller.search(caller.db.combat_target)

        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return

        if not caller.cooldowns.ready("fireball"):
            caller.msg(f"|CNot so fast!")
            return False

        if not target:
            target = caller.search(self.args)
            if not target:
                caller.msg("Fireball who?")
                return
            target.enter_combat(caller)
            caller.enter_combat(target)

        if not caller.db.fp >= self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.cooldowns.add("fireball", 6)
        caller.cooldowns.add("global_cooldown", 2)

        caller.msg(f"|MYou hurl a ball of fire at {target}.")
        target.msg(f"|M{caller} hurls a ball of fire at you.")
        caller.location.msg_contents(
            f"|M{caller} hurls a ball of fire at {target}.",
            exclude=[caller, target],
        )

        damage = self._calculate_damage(glvl)

        target.at_damage(caller, damage, "fire", "fireball")


class CmdInferno(PowerCommand):
    """
    The fire elemental can unleash a wave of fire to incinerate their enemies,
    dealing damage based on their wisdom and guild level.

    Usage:
        inferno <target>
    """

    key = "inferno"
    aliases = ["if"]
    help_category = "fire elemental"
    guild_level = 21
    cost = 30

    def _calculate_damage(self, guild_level):
        caller = self.caller
        base_value = 75
        flame_mastery_weight = 10
        wisdom_weight = 0.3
        guild_level_weight = 1
        flame_mastery = caller.db.skills.get("flame mastery", 1)
        wisdom = caller.traits.wis.value

        damage = (
            base_value
            + (flame_mastery * flame_mastery_weight)
            + (wisdom * wisdom_weight)
            + (guild_level * guild_level_weight)
        )

        # Ensure damage is within the range of 100 to 300
        damage = max(1, min(damage, 250))

        # Adding some randomness to the damage
        damage = int(uniform(damage * 0.85, damage * 1.25))

        return damage

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        target = caller.search(caller.db.combat_target)

        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return

        if not caller.cooldowns.ready("inferno"):
            caller.msg(f"|CNot so fast!")
            return False

        if not target:
            target = caller.search(self.args)
            if not target:
                caller.msg("Inferno who?")
                return
            target.enter_combat(caller)
            caller.enter_combat(target)

        if not caller.db.fp >= self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.cooldowns.add("inferno", 6)
        caller.cooldowns.add("global_cooldown", 2)

        caller.msg(f"|MYou unleash a wave of fire at {target}.")
        target.msg(f"|M{caller} unleashes a wave of fire at you.")
        caller.location.msg_contents(
            f"|M{caller} unleashes a wave of fire at {target}.",
            exclude=[caller, target],
        )
        damage = self._calculate_damage(glvl)

        target.at_damage(caller, damage, "fire", "inferno")


class CmdBlazingMaelstrom(PowerCommand):
    """
    The fire elemental can summon a blazing maelstrom, engulfing their enemies in a whirlwind of flames. This devastating ability draws upon the elemental's wisdom and guild level to unleash a torrent of fiery destruction.

    Usage:
        blazing maelstrom <target>
    """

    key = "blazing maelstrom"
    aliases = ["blazingmaelstrom", "bm"]
    help_category = "fire elemental"
    guild_level = 24
    cost = 75

    def _calculate_damage(
        self,
    ):
        caller = self.caller
        base_value = 90
        flame_mastery_weight = 10
        firestorm_control_weight = 10
        wisdom_weight = 1
        guild_level_weight = 1
        flame_mastery = caller.db.skills.get("flame mastery", 1)
        firestorm_control = caller.db.skills.get("firestorm control", 1)
        wisdom = caller.traits.wis.value
        guild_level = caller.db.guild_level

        damage = (
            base_value
            + (firestorm_control * firestorm_control_weight)
            + (flame_mastery * flame_mastery_weight)
            + (wisdom * wisdom_weight)
            + (guild_level * guild_level_weight)
        )

        # Ensure damage is within the range of 20 to 50
        damage = max(10, min(damage, 350)) / 3
        damage = int(uniform(damage * 0.6, damage * 1.2))

        return damage

    def func(self):
        caller = self.caller
        target = caller.search(caller.db.combat_target)
        glvl = caller.db.guild_level
        energy_cost = 10

        if not caller.cooldowns.ready("blazing maelstrom"):
            caller.msg(f"|CNot so fast!")
            return False

        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return

        if not caller.db.fp >= self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        if not caller.db.ep or caller.db.ep <= energy_cost:
            caller.msg("You don't have enough energy to summon a blazing maelstrom.")
            return

        if not target:
            target = caller.search(self.args)
            if not target:
                caller.msg("Blazing maelstrom who?")
                return
            target.enter_combat(caller)
            caller.enter_combat(target)

        caller.adjust_ep(-energy_cost)
        caller.adjust_fp(-self.cost)
        caller.cooldowns.add("blazing maelstrom", 6)
        caller.cooldowns.add("global_cooldown", 2)
        activateMsg = f"|C$Your() hands blaze with fiery energy as you summon a blazing maelstrom, engulfing {target} in a whirlwind of flames."
        caller.location.msg_contents(activateMsg, from_obj=caller)

        # calculate total damage, divide it into 3 parts, add 20% to each part
        damage1 = self._calculate_damage()
        damage2 = self._calculate_damage()
        damage3 = self._calculate_damage()
        self.msg(f"|gDamage1: {damage1}")
        self.msg(f"|gDamage2: {damage2}")
        self.msg(f"|gDamage3: {damage3}")

        target.at_damage(caller, damage1, "fire", "blazing_maelstrom")
        target.at_damage(caller, damage2, "fire", "blazing_maelstrom")
        target.at_damage(caller, damage3, "fire", "blazing_maelstrom")


class CmdSunburst(PowerCommand):
    """
    The fire elemental can unleash a sunburst to incinerate their enemies, dealing damage based on their wisdom and guild level.

    Usage:
        sunburst <target>
    """

    key = "sunburst"
    aliases = ["sb"]
    help_category = "fire elemental"
    guild_level = 26
    cost = 100
    energy_cost = 10

    def _calculate_damage(self, guild_level):
        caller = self.caller
        base_value = 50
        flame_mastery_weight = 10
        pyroclastic_surge_weight = 10
        ember_infusion_weight = 10

        wisdom_weight = 1
        guild_level_weight = 1
        flame_mastery = caller.db.skills.get("flame mastery", 1)
        pyroclastic_surge = caller.db.skills.get("pyroclastic surge", 1)
        ember_infusion = caller.db.skills.get("ember infusion", 1)
        wisdom = caller.traits.wis.value

        damage = (
            base_value
            + (ember_infusion * ember_infusion_weight)
            + (pyroclastic_surge * pyroclastic_surge_weight)
            + (flame_mastery * flame_mastery_weight)
            + (wisdom * wisdom_weight)
            + (guild_level * guild_level_weight)
        )

        caller.adjust_ep(-self.energy_cost)
        caller.adjust_fp(-self.cost)

        # Ensure damage is within the range of 100 to 350
        damage = max(1, min(damage, 400))

        # Adding some randomness to the damage
        damage = int(uniform(damage * 0.8, damage * 1.6))

        return damage

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        target = caller.search(caller.db.combat_target)

        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return

        if not caller.cooldowns.ready("sunburst"):
            caller.msg(f"|CNot so fast!")
            return False

        if not target:
            target = caller.search(self.args)
            if not target:
                caller.msg("Sunburst who?")
                return
            target.enter_combat(caller)
            caller.enter_combat(target)

        if not caller.db.fp >= self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.cooldowns.add("sunburst", 60)
        caller.cooldowns.add("global_cooldown", 2)

        caller.msg(f"|MYou unleash a sunburst to incinerate {target}.")
        target.msg(f"|M{caller} unleashes a sunburst to incinerate you.")
        caller.location.msg_contents(
            f"|M{caller} unleashes a sunburst to incinerate {target}.",
            exclude=[caller, target],
        )

        damage = self._calculate_damage(glvl)
        target.at_damage(caller, damage, "fire", "sunburst")


class CmdFlamestrike(PowerCommand):
    """
    The fire elemental can strike their enemies with a bolt of fire, dealing damage based on their wisdom and guild level.

    Usage:
        flamestrike <target>
    """

    key = "flamestrike"
    aliases = ["fs"]
    help_category = "fire elemental"
    guild_level = 30
    cost = 100

    def _calculate_damage(self, guild_level):
        caller = self.caller
        base_value = 100
        flame_mastery_weight = 10
        pyroclastic_surge_weight = 10
        ember_infusion_weight = 10

        wisdom_weight = 1
        guild_level_weight = 1

        wisdom = caller.traits.wis.value
        flame_mastery = caller.db.skills.get("flame mastery", 1)
        ember_infusion = caller.db.skills.get("ember infusion", 1)
        pyroclastic_surge = caller.db.skills.get("pyroclastic surge", 1)

        damage = (
            base_value
            + (ember_infusion * ember_infusion_weight)
            + (pyroclastic_surge * pyroclastic_surge_weight)
            + (flame_mastery * flame_mastery_weight)
            + (wisdom * wisdom_weight)
            + (guild_level * guild_level_weight)
        )

        # Ensure damage is within the range of 100 to 300
        damage = max(1, min(damage, 425))

        # Adding some randomness to the damage
        damage = int(uniform(damage * 0.6, damage * 1.6))

        return damage

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        target = caller.search(caller.db.combat_target)

        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return

        if not caller.cooldowns.ready("flamestrike"):
            caller.msg(f"|CNot so fast!")
            return False

        if not target:
            target = caller.search(self.args)
            if not target:
                caller.msg("Flamestrike who?")
                return
            target.enter_combat(caller)
            caller.enter_combat(target)

        if not caller.db.fp >= self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.cooldowns.add("flamestrike", 60)
        caller.cooldowns.add("global_cooldown", 2)

        caller.msg(f"|MYou strike {target} with a pillar of fire.")
        target.msg(f"|M{caller} strikes you with a pillar of fire.")
        caller.location.msg_contents(
            f"|M{caller} strikes {target} with a pillar of fire.",
            exclude=[caller, target],
        )

        damage = self._calculate_damage(glvl)

        target.at_damage(caller, damage, "fire", "flamestrike")


class CmdFireForm(PowerCommand):
    """
    The fire elemental can transform into a being of pure flame, increasing their resistance to physical attacks and enhancing their fire-based abilities. While in this form, the elemental's attacks deal additional fire damage, and they gain a bonus to their fire-based skills. The elemental's connection to fire is strengthened, allowing them to channel more energy into their attacks and abilities. The form's strength scales with the elemental's mastery of the skill and its connection to fire.
    """

    key = "fire form"
    aliases = ["ff"]
    help_category = "fire elemental"
    cost = 50
    guild_level = 7

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        if glvl < self.guild_level:
            caller.msg(f"|CYou need to be guild level 7 to use fire form.")
            return
        if caller.db.ep < self.cost:
            caller.msg(f"|rYou need at least {self.cost} energy to use this power.")
            return
        if not caller.db.fire_form:
            caller.db.fire_form = {"duration": 0, "rate": 0}
        if caller.db.fire_form["duration"] > 0:
            caller.msg("You are already in flame form.")
            return
        caller.cooldowns.add("fire_form", 60)
        caller.cooldowns.add("global_cooldown", 2)
        caller.db.fire_form["duration"] = randint(10, 20)
        caller.db.fire_form["rate"] = 1

        caller.adjust_ep(-self.cost)
        caller.msg(
            f"|CYou transform into a being of pure flame, your body radiating intense heat and light."
        )
        caller.location.msg_contents(
            f"|C$You() transform into a being of pure flame, $pron(your) body radiating intense heat and light.",
            from_obj=caller,
        )


class CmdLavaForm(PowerCommand):
    """
    The fire elemental can transform into a being of molten lava, increasing their resistance to physical attacks and enhancing their fire-based abilities. While in this form, the elemental's attacks deal additional fire damage, and they gain a bonus to their fire-based skills. The elemental's connection to fire is strengthened, allowing them to channel more energy into their attacks and abilities. The form's strength scales with the elemental's mastery of the skill and its connection to fire.
    """

    key = "lava form"
    aliases = ["lf"]
    help_category = "fire elemental"
    cost = 75
    guild_level = 14

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        if glvl < self.guild_level:
            caller.msg(f"|CYou need to be guild level 14 to use lava form.")
            return
        if caller.db.ep < self.cost:
            caller.msg(f"|rYou need at least {self.cost} energy to use this power.")
            return
        if not caller.db.lava_form:
            caller.db.lava_form = {"duration": 0, "rate": 0}
        if caller.db.lava_form["duration"] > 0:
            caller.msg("You are already in lava form.")
            return
        caller.cooldowns.add("lava_form", 60)
        caller.cooldowns.add("global_cooldown", 2)
        caller.db.lava_form["duration"] = randint(10, 20)
        caller.db.lava_form["rate"] = 1

        caller.adjust_ep(-self.cost)
        caller.msg(
            f"|CYou transform into a being of molten lava, your body radiating intense heat and light."
        )
        caller.location.msg_contents(
            f"|C$You() transform into a being of molten lava, $pron(your) body radiating intense heat and light.",
            from_obj=caller,
        )


class CmdBurnout(PowerCommand):
    """
    Burnout is a powerful ability that allows the fire elemental to channel their energy into a surge of power, increasing the strength of their fire-based abilities. When activated, the elemental's power reaches its peak, enhancing their connection to fire and boosting the effectiveness of their skills. The elemental's attacks deal additional fire damage, and they gain a bonus to their fire-based skills. The surge of power is swift and intense, providing a burst of destructive energy that scales with the elemental's mastery of the skill and its connection to fire.

    Usage:
        burnout
    """

    key = "burnout"
    help_category = "fire elemental"
    cost = 10
    guild_level = 10

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level

        if not caller.db.burnout["count"] > 0:
            caller.msg(f"|CYou are too tired to use this power.")
            return
        if not caller.cooldowns.ready("burnout"):
            caller.msg(f"|CNot so fast!")
            return False
        if caller.db.ep < self.cost:
            caller.msg(f"|rYou need at least {self.cost} energy to use this power.")
            return
        if glvl < 10:
            caller.msg(f"|CYou need to be guild level 10 to use burnout.")
            return
        if caller.db.burnout["active"]:
            caller.msg(f"|CYour power is already surging.")
            return

        caller.db.ep -= self.cost
        caller.cooldowns.add("burnout", 60)
        caller.cooldowns.add("global_cooldown", 2)
        skill_rank = caller.db.skills.get("elemental harmony", 1)

        self.msg(
            f"|cA radiant aura of elemental energy envelops you, your power surging to new heights!|n"
        )

        caller.db.burnout["active"] = True
        caller.db.burnout["count"] -= 1
        caller.db.burnout["duration"] = 3 + skill_rank * 2


class CmdFlameShield(PowerCommand):
    """
    Flame Shield is a defensive ability that allows the fire elemental to create a protective barrier of flames around themselves. This shield absorbs incoming damage, reducing the elemental's vulnerability to physical attacks. The shield's strength scales with the elemental's mastery of the skill and its connection to fire.
    """

    key = "flame shield"
    aliases = ["fs"]
    help_category = "fire elemental"
    cost = 50
    guild_level = 5

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        if glvl < self.guild_level:
            caller.msg(f"|CYou need to be guild level 5 to use air shield.")
            return
        if caller.db.ep < self.cost:
            caller.msg(f"|rYou need at least {self.cost} energy to use this power.")
            return
        if not caller.db.flame_shield["hits"] > 0:
            caller.cooldowns.add("flame_shield", 60)
            caller.cooldowns.add("global_cooldown", 2)
            caller.db.flame_shield["hits"] = (
                3
                + caller.db.skills.get("inferno resilience", 1)
                + caller.db.skills.get("pyroclastic surge", 1)
                + caller.db.skills.get("ember infusion", 1)
                + caller.db.skills.get("molten armor", 1)
                + int(caller.traits.con.value / 10)
            )
            caller.adjust_ep(-self.cost)
        self.msg(
            f"|CYou conjure a swirling barrier of flames, enveloping yourself in a blazing shield of fiery protection."
        )

        caller.location.msg_contents(
            f"|C$You() conjure a swirling barrier of flames, enveloping $pron(yourself) in a blazing shield of fiery protection.",
            from_obj=caller,
        )


class CmdHeatWave(PowerCommand):
    """
    Heat Wave is a powerful offensive ability harnessed by fire elementals. This skill taps into the primal energies of fire, allowing the elemental to unleash a wave of intense heat that scorches everything in its path. When activated, the elemental channels the searing essence of fire, causing a burst of flames that damages enemies and drains their energy. The process is swift and devastating, providing a burst of destructive power that scales with the elemental's mastery of the skill and its connection to fire.
    """

    key = "heat wave"
    aliases = ["heatwave", "hw"]
    help_category = "fire elemental"
    guild_level = 9
    cost = 25

    def _calculate_damage(self, guild_level):
        base_value = 15
        ember_infusion_weight = 0.4
        pyroclastic_surge_weight = 0.4
        wisdom_weight = 0.1
        guild_level_weight = 0.1
        ember_infusion = self.caller.db.skills.get("ember infusion", 1)
        pyroclastic_surge = self.caller.db.skills.get("pyroclastic surge", 1)
        wisdom = self.caller.traits.wis.value

        damage = (
            base_value
            + (ember_infusion * ember_infusion_weight)
            + (pyroclastic_surge * pyroclastic_surge_weight)
            + (wisdom * wisdom_weight)
            + (guild_level * guild_level_weight)
        )

        # Ensure damage is within the range of 15 to 40
        damage = max(15, min(damage, 40))

        return damage

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        energy_cost = 30 + glvl * 2
        ember_infusion = caller.db.skills.get("ember infusion", 1)

        if not caller.cooldowns.ready("heat_wave"):
            caller.msg(f"|CNot so fast!")
            return False
        if not caller.db.heat_wave:
            caller.db.heat_wave = {"duration": 0, "rate": 0}
        if caller.db.heat_wave["duration"] > 0:
            caller.msg("You are already unleashing a heat wave.")
            return
        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return
        if not caller.db.ep or caller.db.ep <= energy_cost:
            caller.msg("You don't have enough energy to unleash a heat wave.")
            return

        glvl = caller.db.guild_level
        wis = caller.traits.wis.value

        damage = self._calculate_damage(glvl)
        # Calculate duration
        duration = int(2 + glvl * 0.1 + wis * 0.1 + ember_infusion)
        caller.db.heat_wave["duration"] = randint(duration, duration * 2)
        caller.db.heat_wave["rate"] = damage

        caller.adjust_ep(-energy_cost)
        caller.cooldowns.add("heat_wave", 60)
        caller.cooldowns.add("global_cooldown", 2)
        activateMsg = f"|C$Your() body radiates with an intense heat, and the air around $pron(you) shimmers with fiery energy."
        caller.location.msg_contents(activateMsg, from_obj=caller)


class CmdFlameRenewal(PowerCommand):
    """
    The fire elemental can rebuild their body to restore health,
    at the cost of focus. The amount of health restored is based on
    the elemental's wisdom and guild level.

    Usage:
        flame renewal
    """

    key = "flame renewal"
    aliases = ["fr"]
    help_category = "fire elemental"
    guild_level = 4

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level

        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return

        if not caller.cooldowns.ready("flame renewal"):
            caller.msg(f"|CNot so fast!")
            return False
        caller.cooldowns.add("flame renewal", 6)

        glvl = caller.db.guild_level
        wis = caller.traits.wis.value
        intel = caller.traits.int.value
        hp = caller.db.hp
        hpmax = caller.db.hpmax
        fp = caller.db.fp
        hp_amount = 0

        to_heal = math.floor(10 + glvl + intel / 2 + wis / 2)
        to_heal = randint(int(to_heal / 2), to_heal)
        cost = to_heal * 2

        if fp < cost:
            self.msg(f"|rYou can't seem to focus on renewing your form.")
            return

        if hp + to_heal > hpmax:
            hp_amount = hpmax - hp
            caller.db.hp = hpmax
            caller.db.fp -= cost
        else:
            hp_amount = hpmax - hp
            caller.db.hp += max(to_heal, 0)
            caller.db.fp -= cost

        heal_msg = f"|M$pron(Your) wounds start to close as the flames burn away impurities and regenerate $pron(your) form."
        caller.location.msg_contents(heal_msg, from_obj=caller)
        self.msg(f"")
        self.msg(f"You restore {hp_amount or 0} health for {cost or 0} focus")


class CmdAbsorb(Command):
    """
    Absorb the corpse of an enemy to restore energy
    """

    key = "absorb"
    aliases = ["ab"]
    help_category = "fire elemental"

    def func(self):
        if not self.args:
            caller = self.caller
            if corpse := caller.location.search("corpse-1"):
                ep = caller.db.ep
                epmax = caller.db.epmax
                power = corpse.db.power

                if ep + power > epmax:
                    caller.db.ep = epmax
                else:
                    caller.db.ep += max(power, 0)
                corpse.delete()
                drain_msg = f"|M$pron(You) engulf a fallen corpse in flames, reducing it to ashes. As the body burns, $pron(you) absorb the released energy, $pron(your) flames growing brighter and more intense, restoring $pron(your) vitality and power."
                caller.location.msg_contents(drain_msg, from_obj=caller)
            else:
                caller.msg("Absorb what?")


class CmdReaction(Command):
    """
    Set the elemental's reaction to dropping below a certain health threshold.

    Usage:
        reaction <percentage>
    """

    key = "reaction"
    help_category = "fire elemental"

    def func(self):
        caller = self.caller
        args = self.args.strip()

        if not self.args:
            caller.msg("Usage: reaction <percentage>")
            return

        if not args.isdigit():
            caller.msg("Invalid percentage")
            return

        caller.db.reaction_percentage = args
        caller.msg(f"Reaction set to {args}.")


class CmdGTrain(Command):
    """
    Train your guild skills by spending skill experience points. Each rank
    increases your effectiveness in that skill.

    Usage:
        gtrain <skill>

    Example:
        gtrain flame mastery
    """

    key = "gtrain"
    help_category = "fire elemental"

    def func(self):
        caller = self.caller
        skill = self.args.strip().lower()
        list = caller.db.skills.keys()

        if skill == "":
            self.msg(f"|gWhat would you like to raise?")
            return

        if skill not in list:
            caller.msg(f"|gYou can't raise that.")
            return

        skill_gxp = getattr(caller.db, "skill_gxp", 0)
        cost = caller.db.skills[f"{skill}"]
        cost = SKILLS_COST[cost]

        if skill_gxp < cost:
            self.msg(f"|wYou need {cost-skill_gxp} more experience to train {skill}.")
            return

        confirm = yield (
            f"It will cost you {cost} experience to advance {skill}. Confirm? Yes/No"
        )
        if confirm.lower() not in (
            "yes",
            "y",
        ):
            self.msg("Cancelled.")
            return

        setattr(caller.db, "skill_gxp", skill_gxp - cost)
        caller.db.skills[skill] += 1
        caller.msg(f"|yYou grow more experienced in {skill}")


class CmdGhelp(Command):
    """
    Display the help file for the fire elemental guild.

    Usage:
        ghelp
    """

    key = "ghelp"
    help_category = "fire elemental"

    def func(self):
        caller = self.caller
        skill = self.args.strip().lower()
        if skill == "":
            caller.msg(
                "|cFire Elemental Guild|n\n\n"
                "The Fire Elemental Guild is a group of beings that have learned to harness the power of fire to enhance their physical abilities and combat prowess.\n\n"
                "Usage:\n"
                "    ghelp <skill>\n"
            )
            return
        if skill == "flame mastery":
            caller.msg(
                "|cFlame Mastery|n\n\n"
                "Enhances the elemental's control over fire, increasing the damage dealt by fire-based attacks.\n\n"
                "Usage:\n"
                "    flame mastery\n"
                "    fm\n"
            )
            return
        if skill == "inferno resilience":
            caller.msg(
                "|cInferno Resilience|n\n\n"
                "Increases the elemental's resistance to fire-based attacks.\n\n"
                "Usage:\n"
                "    inferno resilience\n"
                "    ir\n"
            )
            return
        if skill == "blazing speed":
            caller.msg(
                "|cBlazing Speed|n\n\n"
                "Enhances the elemental's speed, allowing for faster movement and attacks.\n\n"
                "Usage:\n"
                "    blazing speed\n"
                "    bs\n"
            )
            return
        if skill == "pyroclastic surge":
            caller.msg(
                "|cPyroclastic Surge|n\n\n"
                "Increases the elemental's energy regeneration rate.\n\n"
                "Usage:\n"
                "    pyroclastic surge\n"
                "    ps\n"
            )
            return
        if skill == "molten armor":
            caller.msg(
                "|cMolten Armor|n\n\n"
                "Increases the elemental's physical defense, reducing the damage taken from physical attacks.\n\n"
                "Usage:\n"
                "    molten armor\n"
                "    ma\n"
            )
            return
        if skill == "ember infusion":
            caller.msg(
                "|cEmber Infusion|n\n\n"
                "Enhances the elemental's passive regeneration.\n\n"
                "Usage:\n"
                "    ember infusion\n"
                "    ei\n"
            )
            return
        if skill == "firestorm control":
            caller.msg(
                "|cFirestorm Control|n\n\n"
                "Allows the elemental to control firestorms, dealing damage to all enemies in the area.\n\n"
                "Usage:\n"
                "    firestorm control\n"
                "    fc\n"
            )
            return
        if skill == "elemental synergy":
            caller.msg(
                "|cElemental Synergy|n\n\n"
                "Increases the elemental's overall power, enhancing the effects of other skills.\n\n"
                "Usage:\n"
                "    elemental synergy\n"
                "    es\n"
            )
            return


class CmdPowers(Command):
    """
    List of powers available to the Elemental, their rank, and their cost.

    Usage:
        powers

    """

    key = "powers"
    help_category = "fire elemental"

    def func(self):
        caller = self.caller

        table = EvTable(f"|cPower", f"|cRank", f"|cCost", f"|cType", border="table")
        # utility
        table.add_row(f"|GAbsorb", 1, 0, "Utility")
        table.add_row(f"|GReaction", 1, 0, "Utility")
        table.add_row(f"|GBurnout", 10, 10, "Utility")
        # healing
        table.add_row(f"|GFlame Renewal", 3, 25, "Healing")
        table.add_row(f"|GHeat Wave", 9, 75, "Healing")
        # damage
        table.add_row(f"|GEmber Strike", 2, 5, "Damage")
        table.add_row(f"|GFire Punch", 6, 10, "Damage")
        table.add_row(f"|GFire Whip", 12, 15, "Damage")
        table.add_row(f"|GLava Burst", 15, 20, "Damage")
        table.add_row(f"|GFireball", 18, 25, "Damage")
        table.add_row(f"|GInferno", 21, 30, "Damage")
        table.add_row(f"|GBlazing Maelstrom", 24, 75, "Damage")
        table.add_row(f"|GSunburst", 26, 100, "Damage")
        table.add_row(f"|GFlamestrike", 30, 125, "Damage")
        # forms
        table.add_row(f"|GFire Form", 15, 50, "Form")
        table.add_row(f"|GLava form", 25, 100, "Form")

        caller.msg(str(table))


class FireElementalCmdSet(CmdSet):
    key = "Fire Elemental CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        self.add(CmdAbsorb)
        self.add(CmdReaction)
        self.add(CmdBurnout)

        self.add(CmdFlameRenewal)
        self.add(CmdHeatWave)

        self.add(CmdFlameShield)

        self.add(CmdFireForm)
        self.add(CmdLavaForm)

        self.add(CmdEmberStrike)
        self.add(CmdFirePunch)
        self.add(CmdFireWhip)
        self.add(CmdLavaBurst)
        self.add(CmdFireball)
        self.add(CmdInferno)
        self.add(CmdBlazingMaelstrom)
        self.add(CmdSunburst)
        self.add(CmdFlamestrike)

        self.add(CmdPowers)
        self.add(CmdGhelp)
        self.add(CmdGTrain)
