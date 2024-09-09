import math
from random import uniform, randint
from evennia import CmdSet
from evennia.utils.evtable import EvTable
from commands.command import Command
from typeclasses.elementalguild.constants_and_helpers import SKILLS_COST
from typeclasses.utils import PowerCommand


class CmdEnvelop(Command):
    """
    Drain the corpse of an enemy to restore energy
    """

    key = "envelop"
    aliases = ["en", "env"]
    help_category = "water elemental"

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
                drain_msg = f"|M|M$pron(You) envelop the corpse with tendrils of water, dissolving it into liquid. As the remains merge with $pron(you), $pron(your) body glows with renewed energy, $pron(your) form becoming more vibrant and fluid."
                caller.location.msg_contents(drain_msg, from_obj=caller)
            else:
                caller.msg("Envelop what?")


class CmdReaction(Command):
    """
    Set the elemental's reaction to a dropping below a certain health threshold.

    Usage:
        reaction <percentage>
    """

    key = "reaction"
    help_category = "water elemental"

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


class CmdWaterForm(PowerCommand):
    """
    The elemental transforms its body into a fluid form, allowing it to move more quickly and easily through the water. The elemental's body shimmers with a watery light as it shifts, becoming more fluid and adaptable. The elemental gains a bonus to its movement speed and agility, allowing it to dodge attacks more easily and strike with greater precision.

    Usage:
        water form
    """

    key = "water form"
    aliases = ["waterform", "wf"]
    help_category = "water elemental"
    guild_level = 5
    cost = 50

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level

        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return
        if caller.db.ep < self.cost:
            caller.msg(f"|rYou need at least {self.cost} energy to use this power.")
            return
        if not caller.cooldowns.ready("water_form"):
            caller.msg(f"|BNot so fast!")
            return False
        if not caller.db.water_form:
            caller.db.ep -= self.cost
            caller.db.water_form = True
            caller.cooldowns.add("water_form", 4)
            caller.cooldowns.add("global_cooldown", 2)
            caller.msg(
                f"|MYou transform your body into a fluid form, becoming more agile and adaptable."
            )
            caller.location.msg_contents(
                f"|M{caller} transforms $pron $poss body into a fluid form, becoming more agile and adaptable.",
                exclude=caller,
            )
        else:
            caller.db.water_form = False
            caller.msg(f"|MYou return to your normal form.")
            caller.location.msg_contents(
                f"|M{caller} returns to $pron normal form.", exclude=caller
            )


class CmdAquaShield(PowerCommand):
    """
    The elemental raises its hands, and a shimmering shield of water forms around it, protecting it from harm. The shield absorbs the impact of incoming attacks, reducing the damage the elemental takes. The shield crackles with energy as it absorbs the attack, then dissipates into a fine mist, leaving the elemental unharmed.

    Usage:
        aqua shield
    """

    key = "aqua shield"
    aliases = ["aquashield", "as"]
    help_category = "water elemental"
    guild_level = 5
    cost = 5

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level

        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return

        if not caller.cooldowns.ready("aqua_shield"):
            caller.msg(f"|BNot so fast!")
            return False

        caller.cooldowns.add("aqua_shield", 60)
        caller.cooldowns.add("global_cooldown", 2)

        if caller.db.ep < self.cost:
            caller.msg(f"|rYou need at least {self.cost} energy to use this power.")
            return

        caller.db.aqua_shield = True

        caller.msg(
            f"|MYou raise your hands, and a shimmering shield of water forms around you."
        )
        caller.location.msg_contents(
            f"|M{caller} raises $pron $poss hands, and a shimmering shield of water forms around $obj.",
            exclude=caller,
        )


class CmdIceShield(PowerCommand):
    """
    The elemental raises its hands, and a shimmering shield of ice forms around it, protecting it from harm. The shield absorbs the impact of incoming attacks, reducing the damage the elemental takes. The shield crackles with energy as it absorbs the attack, then dissipates into a fine mist, leaving the elemental unharmed.

    Usage:
        ice shield
    """

    key = "ice shield"
    aliases = ["iceshield", "is"]
    help_category = "water elemental"
    guild_level = 5
    cost = 5

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level

        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return

        if not caller.cooldowns.ready("ice_shield"):
            caller.msg(f"|BNot so fast!")
            return False
        caller.cooldowns.add("ice_shield", 60)
        caller.cooldowns.add("global_cooldown", 2)

        if caller.db.ep < self.cost:
            caller.msg(f"|rYou need at least {self.cost} energy to use this power.")
            return

        caller.db.ice_shield["hits"] = (
            1
            + int(caller.db.guild_level / 10)
            + int(caller.traits.con.value / 10)
            + caller.db.skills.get("aqua resilience", 0)
            + caller.db.skills.get("ice mastery", 0)
        )

        caller.msg(
            f"|MYou raise your hands, and a shimmering shield of ice forms around you."
        )
        caller.location.msg_contents(
            f"|M{caller} raises $pron $poss hands, and a shimmering shield of ice forms around $obj.",
            exclude=caller,
        )


class CmdWaterJet(PowerCommand):
    """
    A powerful jet of water shoots from the elemental's hands, striking the target with force. The water crashes into the target, dealing damage and knocking them back. The elemental's body shimmers with a watery light as the attack completes, leaving the target drenched and disoriented.

    Usage:
        water jet <target>
    """

    key = "water jet"
    aliases = ["waterjet", "wj"]
    help_category = "water elemental"
    guild_level = 3
    cost = 5

    def _calculate_damage(self, wave_control, wisdom, guild_level):
        base_value = 5
        wave_control_weight = 10
        wisdom_weight = 0.3
        guild_level_weight = 1

        damage = (
            base_value
            + (wave_control * wave_control_weight)
            + (wisdom * wisdom_weight)
            + (guild_level * guild_level_weight)
        )

        # Ensure damage is within the range of 100 to 300
        damage = max(1, min(damage, 300))

        # Adding some randomness to the damage
        damage = int(uniform(damage * 0.6, damage * 1.4))

        return damage

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        target = caller.search(caller.db.combat_target)

        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return

        if not caller.cooldowns.ready("water_jet"):
            caller.msg(f"|BNot so fast!")
            return False

        if not target:
            target = caller.search(self.args)
            if not target:
                caller.msg("Water jet who?")
                return
            target.enter_combat(caller)
            caller.enter_combat(target)

        if not caller.db.fp >= self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.cooldowns.add("water_jet", 4)
        caller.cooldowns.add("global_cooldown", 2)
        skill_rank = caller.db.skills.get("wave_control", 0)

        caller.msg(f"|MYou shoot a powerful jet of water at {target}.")
        target.msg(f"|M{caller} shoots a powerful jet of water at you.")
        caller.location.msg_contents(
            f"|M{caller} shoots a powerful jet of water at {target}.",
            exclude=[caller, target],
        )

        damage = self._calculate_damage(skill_rank, caller.traits.wis.value, glvl)
        self.msg(f"|gDamage: {damage}")
        target.at_damage(caller, damage, "blunt", "water_jet")


class CmdIceShard(PowerCommand):
    """
    The elemental raises its hands, and a shard of ice forms in front of it. The shard flies at the target with incredible speed, dealing damage and freezing them in place. The elemental's body glows with a cold light as the attack completes, leaving the target shivering and vulnerable.

    Usage:
        ice shard <target>
    """

    key = "ice shard"
    aliases = ["iceshard", "is"]
    help_category = "water elemental"
    guild_level = 1
    cost = 3

    def _calculate_damage(self, wave_control, wisdom, guild_level):
        base_value = 5
        wave_control_weight = 10
        wisdom_weight = 0.3
        guild_level_weight = 1

        damage = (
            base_value
            + (wave_control * wave_control_weight)
            + (wisdom * wisdom_weight)
            + (guild_level * guild_level_weight)
        )

        # Ensure damage is within the range of 100 to 300
        damage = max(1, min(damage, 300))

        # Adding some randomness to the damage
        damage = int(uniform(damage * 0.6, damage * 1.4))

        return damage

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        target = caller.search(caller.db.combat_target)

        if not caller.cooldowns.ready("ice_shard"):
            caller.msg(f"|CNot so fast!")
            return False

        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return

        if not target:
            target = caller.search(self.args)
            if not target:
                caller.msg("Ice shard who?")
                return
            target.enter_combat(caller)
            caller.enter_combat(target)

        if not caller.db.fp >= self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.cooldowns.add("ice_shard", 4)
        caller.cooldowns.add("global_cooldown", 2)
        skill_rank = caller.db.skills.get("wave_control", 0)

        caller.msg(f"|MYou raise your hands, and a shard of ice forms in front of you.")
        target.msg(
            f"|M{caller} raises $pron $poss hands, and a shard of ice forms in front of $obj."
        )
        caller.location.msg_contents(
            f"|M{caller} raises $pron $poss hands, and a shard of ice forms in front of $obj.",
            exclude=[caller, target],
        )

        damage = self._calculate_damage(skill_rank, caller.traits.str.value, glvl)
        self.msg(f"|gDamage: {damage}")
        target.at_damage(caller, damage, "water", "tidal_wave")


class CmdMaelstrom(PowerCommand):
    """
    The elemental raises its hands, and a powerful maelstrom forms around it. The maelstrom swirls with incredible speed, drawing in everything around it and dealing damage to all enemies caught in its path. The elemental's body glows with a watery light as the attack completes, leaving the enemies drenched and disoriented.

    Usage:
        maelstrom
    """

    key = "maelstrom"
    aliases = ["ms"]
    help_category = "water elemental"
    guild_level = 20
    cost = 25

    def _calculate_damage(self, wave_control, guild_level):
        base_value = 50
        wave_control_weight = 10
        wisdom_weight = 0.3
        guild_level_weight = 1

        damage = (
            base_value
            + (wave_control * wave_control_weight)
            + (self.caller.traits.wis.value * wisdom_weight)
            + (guild_level * guild_level_weight)
        )

        # Ensure damage is within the range of 100 to 300
        damage = max(1, min(damage, 300))

        # Adding some randomness to the damage
        damage = int(uniform(damage * 0.6, damage * 1))

        return damage

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        target = caller.search(caller.db.combat_target)

        if not caller.cooldowns.ready("maelstrom"):
            caller.msg(f"|CNot so fast!")
            return False

        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return

        if not target:
            target = caller.search(self.args)
            if not target:
                caller.msg("Maelstrom who?")
                return
            target.enter_combat(caller)
            caller.enter_combat(target)

        if caller.db.ep < self.cost:
            caller.msg(f"|rYou need at least {self.cost} energy to use this power.")
            return

        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.adjust_fp(-self.cost)
        caller.cooldowns.add("maelstrom", 4)
        caller.cooldowns.add("global_cooldown", 2)
        skill_rank = caller.db.skills.get("wave_control", 0)

        caller.msg(
            f"|MYou raise your hands, and a powerful maelstrom forms around you."
        )
        target.msg(
            f"|M{caller} raises $pron $poss hands, and a powerful maelstrom forms around $obj."
        )
        caller.location.msg_contents(
            f"|M{caller} raises $pron $poss hands, and a powerful maelstrom forms around $obj.",
            exclude=[caller, target],
        )
        damage = self._calculate_damage(skill_rank, glvl)
        self.msg(f"|gDamage: {damage}")
        target.at_damage(caller, damage, "edged", "maelstrom")
        damage = self._calculate_damage(skill_rank, glvl)
        self.msg(f"|gDamage: {damage}")
        target.at_damage(caller, damage, "ice", "maelstrom")


class CmdTidalWave(PowerCommand):
    """
    The elemental raises its hands, and a massive wave of water forms behind it. The wave crashes down on the target with tremendous force, dealing damage and knocking them back. The elemental's body glows with a watery light as the attack completes, leaving the target drenched and disoriented.

    Usage:
        tidal wave <target>
    """

    key = "tidal wave"
    aliases = ["tidalwave", "tw"]
    help_category = "water elemental"
    guild_level = 9
    cost = 9

    def _calculate_damage(self, wave_control, wisdom, guild_level):
        base_value = 9
        wave_control_weight = 9
        wisdom_weight = 0.3
        guild_level_weight = 1

        damage = (
            base_value
            + (wave_control * wave_control_weight)
            + (wisdom * wisdom_weight)
            + (guild_level * guild_level_weight)
        )

        # Ensure damage is within the range of 100 to 300
        damage = max(15, min(damage, 300))

        # Adding some randomness to the damage
        damage = int(uniform(damage * 0.6, damage * 1))

        return damage

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        target = caller.search(caller.db.combat_target)

        if not caller.cooldowns.ready("tidal_wave"):
            caller.msg(f"|CNot so fast!")
            return False

        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return

        if not target:
            target = caller.search(self.args)
            if not target:
                caller.msg("Tidal wave who?")
                return
            target.enter_combat(caller)
            caller.enter_combat(target)

        if caller.db.ep < self.cost:
            caller.msg(f"|rYou need at least {self.cost} energy to use this power.")
            return

        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        caller.adjust_fp(-self.cost)
        caller.cooldowns.add("tidal_wave", 4)
        caller.cooldowns.add("global_cooldown", 2)

        caller.msg(
            f"|MYou raise your hands, and a massive wave of water forms behind you."
        )
        target.msg(
            f"|M{caller} raises $pron $poss hands, and a massive wave of water forms behind $obj."
        )
        caller.location.msg_contents(
            f"|M{caller} raises $pron $poss hands, and a massive wave of water forms behind $obj.",
            exclude=[caller, target],
        )

        skill_rank = caller.db.skills.get("wave control", 1)
        damage = self._calculate_damage(skill_rank, caller.traits.str.value, glvl)
        self.msg(f"|gDamage: {damage}")
        target.at_damage(caller, damage, "water", "tidal_wave")


class CmdRejuvenate(PowerCommand):
    """
    Water droplets coalesce from the surrounding moisture, swirling around the elemental in a graceful dance. The droplets merge into streams, flowing over the elemental's body, mending cracks and filling gaps with a soothing, liquid touch. The elemental's form becomes more defined and robust, the water infusing it with renewed strength and vitality. As the healing process completes, the elemental stands rejuvenated, its surface glistening with a fresh, revitalized sheen.

     Usage:
         rejuvenate
    """

    key = "rejuvenate"
    aliases = ["rejuv", "rej"]
    help_category = "water elemental"
    guild_level = 4

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level

        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return

        if not caller.cooldowns.ready("rejuvenate"):
            caller.msg(f"|BNot so fast!")
            return False
        caller.cooldowns.add("rejuvenate", 4)

        wis = caller.traits.wis.value
        strength = caller.traits.str.value
        hp = caller.db.hp
        hpmax = caller.db.hpmax
        fp = caller.db.fp
        hp_amount = 0

        to_heal = math.floor(10 + glvl + strength / 2 + wis / 2)
        to_heal = randint(int(to_heal / 2), to_heal)
        to_heal = max(to_heal, 0)
        cost = to_heal * 0.5

        if caller.db.fp < cost:
            self.msg(f"|rYou can't seem to focus on restoring your form.")
            return

        if hp + to_heal > hpmax:
            hp_amount = hpmax - hp
            caller.adjust_hp(hpmax)
            caller.adjust_fp(-cost)
        else:
            hp_amount = hpmax - hp
            caller.db.hp += max(to_heal, 0)
            caller.db.fp -= cost

        msg = f"|MAs $pron(you) concentrate, $pron(your) body glows with a soft, blue light, and water swirls around you, knitting wounds and restoring vitality. {hp_amount or 0} health restored for {cost or 0} focus."

        caller.location.msg_contents(msg, from_obj=caller)


class CmdHealingWaters(PowerCommand):
    """
    The elemental calls upon the power of the water to heal itself, restoring health and energy. The water flows over the elemental's body, mending wounds and revitalizing its form. The elemental's body glows with a soft, blue light as the healing process completes, leaving it refreshed and invigorated.

    Usage:
        healing waters
    """

    key = "healing waters"
    aliases = ["healingwaters", "hw"]
    help_category = "water elemental"
    guild_level = 1

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level

        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return

        if not caller.cooldowns.ready("healing_waters"):
            caller.msg(f"|BNot so fast!")
            return False
        caller.cooldowns.add("healing_waters", 4)

        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        wis = caller.traits.wis.value
        hp = caller.db.hp
        hpmax = caller.db.hpmax
        hp_amount = 0

        to_heal = math.floor(10 + glvl + wis / 2)
        to_heal = randint(int(to_heal / 2), to_heal)
        to_heal = max(to_heal, 0)
        cost = to_heal * 0.5

        if caller.db.fp < cost:
            self.msg(f"|rYou can't seem to focus on restoring your form.")
            return

        if hp + to_heal > hpmax:
            hp_amount = hpmax - hp
            caller.adjust_hp(hpmax)
            caller.adjust_fp(-cost)
        else:
            hp_amount = hpmax - hp
            caller.db.hp += max(to_heal, 0)
            caller.db.fp -= cost

        msg = f"|MAs $pron(you) concentrate, $pron(your) body glows with a soft, blue light, and water swirls around you, knitting wounds and restoring vitality. {hp_amount or 0} health restored for {cost or 0} focus."

        caller.location.msg_contents(msg, from_obj=caller)


class CmdSootingMist(PowerCommand):
    """
    The elemental calls upon the power of the water to heal itself, restoring health and energy. The water flows over the elemental's body, mending wounds and revitalizing its form. The elemental's body glows with a soft, blue light as the healing process completes, leaving it refreshed and invigorated.

    Usage:
        soothing mist
    """

    key = "soothing mist"
    aliases = ["soothingmist", "sm"]
    help_category = "water elemental"
    guild_level = 1
    cost = 3

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level

        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return

        if not caller.cooldowns.ready("soothing_mist"):
            caller.msg(f"|BNot so fast!")
            return False
        caller.cooldowns.add("soothing_mist", 4)

        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        wis = caller.traits.wis.value
        hp = caller.db.hp
        hpmax = caller.db.hpmax
        hp_amount = 0

        to_heal = math.floor(10 + glvl + wis / 2)
        to_heal = randint(int(to_heal / 2), to_heal)
        to_heal = max(to_heal, 0)
        cost = to_heal * 0.5

        if caller.db.fp < cost:
            self.msg(f"|rYou can't seem to focus on restoring your form.")
            return

        if hp + to_heal > hpmax:
            hp_amount = hpmax - hp
            caller.adjust_hp(hpmax)
            caller.adjust_fp(-cost)
        else:
            hp_amount = hpmax - hp
            caller.db.hp += max(to_heal, 0)
            caller.db.fp -= cost

        msg = f"|MAs $pron(you) concentrate, $pron(your) body glows with a soft, blue light, and water swirls around you, knitting wounds and restoring vitality. {hp_amount or 0} health restored for {cost or 0} focus."

        caller.location.msg_contents(msg, from_obj=caller)


class CmdAbyssalRecovery(PowerCommand):
    """
    The elemental calls upon the power of the water to heal itself, restoring health and energy. The water flows over the elemental's body, mending wounds and revitalizing its form. The elemental's body glows with a soft, blue light as the healing process completes, leaving it refreshed and invigorated.

    Usage:
        abyssal recovery
    """

    key = "abyssal recovery"
    aliases = ["abyssalrecovery", "ar"]
    help_category = "water elemental"
    guild_level = 23

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level

        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return

        if not caller.cooldowns.ready("abyssal_recovery"):
            caller.msg(f"|BNot so fast!")
            return False
        caller.cooldowns.add("abyssal_recovery", 4)

        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        wis = caller.traits.wis.value
        hp = caller.db.hp
        hpmax = caller.db.hpmax
        hp_amount = 0

        to_heal = math.floor(10 + glvl + wis / 2)
        to_heal = randint(int(to_heal / 2), to_heal)
        to_heal = max(to_heal, 0)
        cost = to_heal * 0.5

        if caller.db.fp < cost:
            self.msg(f"|rYou can't seem to focus on restoring your form.")
            return

        if hp + to_heal > hpmax:
            hp_amount = hpmax - hp
            caller.adjust_hp(hpmax)
            caller.adjust_fp(-cost)
        else:
            hp_amount = hpmax - hp
            caller.db.hp += max(to_heal, 0)
            caller.db.fp -= cost

        msg = f"|MAs $pron(you) concentrate, $pron(your) body glows with a soft, blue light, and water swirls around you, knitting wounds and restoring vitality. {hp_amount or 0} health restored for {cost or 0} focus."

        caller.location.msg_contents(msg, from_obj=caller)


class CmdPowers(Command):
    """
    List of powers available to the Elemental, their rank, and their cost.

    Usage:
        powers

    """

    key = "powers"
    help_category = "elemental"

    def func(self):
        caller = self.caller

        table = EvTable(f"|cPower", f"|cRank", f"|cCost", f"|cType", border="table")
        table.add_row(f"|GEnvelop", 1, 0, "Utility")
        table.add_row(f"|GReaction", 1, 0, "Utility")
        table.add_row(f"|GWater Form", 11, 0, "Utility")

        table.add_row(f"|GAqua Shield", 5, 50, "Defense")
        table.add_row(f"|GIce Shield", 15, 50, "Defense")

        table.add_row(f"|GRejuvenate", 3, 25, "Healing")
        table.add_row(f"|GHealing Waters", 9, 0, "Healing")
        table.add_row(f"|GSoothing Mist", 15, 0, "Healing")
        table.add_row(f"|GAbyssal Recovery", 23, 0, "Healing")

        table.add_row(f"|GWater Jet", 4, 10, "Attack")
        table.add_row(f"|GIce Shard", 12, 15, "Attack")
        table.add_row(f"|GMaelstrom", 20, 25, "Attack")
        table.add_row(f"|GTidal Wave", 29, 40, "Attack")

        caller.msg(str(table))


class CmdGTrain(Command):
    """
    Train your guild skills by spending skill experience points. Each rank
    increases your effectiveness in that skill.

    Usage:
        gtrain <skill>

    Example:
        gtrain water mastery
    """

    key = "gtrain"
    help_category = "Water Elemental"

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
    help_category = "water elemental"

    def func(self):
        caller = self.caller
        skill = self.args.strip().lower()
        if skill == "":
            caller.msg(
                "|Water Elemental Guild|n\n\n"
                "The Water Elemental Guild is a group of beings that have learned to harness the power of water to enhance their physical abilities and combat prowess.\n\n"
                "Usage:\n"
                "    ghelp <skill>\n"
            )
            return
        if skill == "water mastery":
            caller.msg(
                "|Water Mastery|n\n\n"
                "Water Mastery is the foundation of the Water Elemental's power. It allows the elemental to manipulate water in a variety of ways, from creating weapons to healing wounds.\n\n"
                "Usage:\n"
                "    gtrain water mastery\n"
            )
            return
        if skill == "fluid agility":
            caller.msg(
                "|Fluid Agility|n\n\n"
                "Fluid Agility allows the Water Elemental to move with grace and speed, dodging attacks and striking with precision.\n\n"
                "Usage:\n"
                "    gtrain fluid agility\n"
            )
            return
        if skill == "aqua resilience":
            caller.msg(
                "|Aqua Resilience|n\n\n"
                "Aqua Resilience enhances the Water Elemental's ability to absorb damage, reducing the impact of physical attacks.\n\n"
                "Usage:\n"
                "    gtrain aqua resilience\n"
            )
            return
        if skill == "tidal force":
            caller.msg(
                "|Tidal Force|n\n\n"
                "Tidal Force increases the Water Elemental's strength, allowing it to deal more damage with its attacks.\n\n"
                "Usage:\n"
                "    gtrain tidal force\n"
            )
            return
        if skill == "hydro armor":
            caller.msg(
                "|Hydro Armor|n\n\n"
                "Hydro Armor surrounds the Water Elemental with a protective layer of water, reducing the impact of physical attacks.\n\n"
                "Usage:\n"
                "    gtrain hydro armor\n"
            )
            return
        if skill == "aqua infusion":
            caller.msg(
                "|Aqua Infusion|n\n\n"
                "Aqua Infusion enhances the Water Elemental's ability to heal itself, restoring health and energy more quickly.\n\n"
                "Usage:\n"
                "    gtrain aqua infusion\n"
            )
            return
        if skill == "wave control":
            caller.msg(
                "|Wave Control|n\n\n"
                "Wave Control allows the Water Elemental to manipulate water in large quantities, creating powerful area-of-effect attacks.\n\n"
                "Usage:\n"
                "    gtrain wave control\n"
            )
            return
        if skill == "elemental synergy":
            caller.msg(
                "|Elemental Synergy|n\n\n"
                "Elemental Synergy enhances the Water Elemental's ability to work in harmony with other elements, increasing the effectiveness of combined elemental attacks.\n\n"
                "Usage:\n"
                "    gtrain elemental synergy\n"
            )
            return


class WaterElementalCmdSet(CmdSet):
    key = "Water Elemental CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        self.add(CmdEnvelop)
        self.add(CmdReaction)
        self.add(CmdWaterForm)

        self.add(CmdAquaShield)
        self.add(CmdIceShield)

        self.add(CmdRejuvenate)
        self.add(CmdHealingWaters)
        self.add(CmdSootingMist)
        self.add(CmdAbyssalRecovery)

        self.add(CmdWaterJet)
        self.add(CmdMaelstrom)
        self.add(CmdTidalWave)
        self.add(CmdPowers)

        self.add(CmdGTrain)
        self.add(CmdGhelp)
