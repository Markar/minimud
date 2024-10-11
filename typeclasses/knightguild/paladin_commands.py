import math
from random import randint, uniform
from evennia import CmdSet
from commands.command import Command
from evennia.utils.evtable import EvTable
from evennia.utils import delay
from evennia.contrib.rpg.buffs import BaseBuff


class PowerCommand(Command):
    def func(self):
        caller = self.caller
        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False
        caller.cooldowns.add("global_cooldown", 2)


# region Yaulp
class CmdYaulp(PowerCommand):
    """
    Focuses your spiritual energy into a great battle cry, increasing your strength and armor class for four ticks.
    """

    key = "yaulp"
    aliases = ["ya"]
    help_category = "knight"
    guild_level = 3
    cost = 5
    duration = 4

    def func(self):
        caller = self.caller

        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        if not caller.cooldowns.ready("yaulp"):
            caller.msg(f"|CNot so fast!")
            return False

        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False

        caller.db.fp -= self.cost
        caller.msg(
            f"|gYou let out a mighty battle cry, feeling your strength and armor class increase."
        )
        caller.location.msg_contents(
            f"|C{caller.name} lets out a mighty battle cry, looking stronger and more resilient.",
            exclude=caller,
        )

        caller.buffs.add(YaulpBuff)

        caller.cooldowns.add("global_cooldown", 2)
        caller.cooldowns.add("yaulp", 30)


class YaulpBuff(BaseBuff):
    duration = 24
    tickrate = 6
    stacks = 1

    def at_apply(self, initial=True, **kwargs):
        self.owner.traits.str.mod += 4
        self.owner.armor += 3

    def at_remove(self, **kwargs):
        self.owner.traits.str.mod -= 4
        self.owner.armor -= 3


# region Courage
class CmdCourage(PowerCommand):
    """
    Courage allows the Paladin to increase their armor class for a short duration.

    Usage:
        courage

    Example:
        courage
    """

    key = "courage"
    aliases = ["co"]
    help_category = "paladin"
    guild_level = 2
    cost = 12
    duration = 180

    def func(self):
        caller = self.caller

        if caller.db.ep < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        if not caller.cooldowns.ready("courage"):
            caller.msg(f"|CNot so fast!")
            return False

        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False

        caller.db.fp -= self.cost
        caller.msg(f"|gYou feel a surge of courage, bolstering your armor class.")
        caller.location.msg_contents(
            f"|C{caller.name} looks emboldened, their armor class increasing.",
            exclude=caller,
        )

        caller.buffs.add(CourageBuff)

        caller.cooldowns.add("global_cooldown", 2)
        caller.cooldowns.add("courage", 30)


class CourageBuff(BaseBuff):
    duration = 180
    tickrate = 16
    stacks = 1

    def at_apply(self, initial=True, **kwargs):
        self.owner.armor += 3
        self.owner.hpmax = +20
        self.owner.hp = +10

    def at_remove(self, **kwargs):
        self.owner.armor -= 3
        self.owner.hpmax = -20
        self.owner.hp = -10


# region Minor Heal
class CmdMinorHeal(PowerCommand):
    """
    Minor Heal allows the knight to heal themselves or an ally for a small amount of health.

    Usage:
        minorheal <target>

    Example:
        minorheal self
        minorheal ally
    """

    key = "minorheal"
    aliases = ["mheal"]
    help_category = "knight"
    guild_level = 1
    cost = 10
    amount = 10

    def func(self):
        caller = self.caller
        target_name = self.args.strip()

        if not target_name:
            caller.msg("Usage: minorheal <target>")
            return

        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        target = caller.search(target_name)
        if not target:
            return

        if not caller.cooldowns.ready("minorheal"):
            caller.msg(f"|CNot so fast!")
            return False

        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False

        heal_amount = self.amount

        target.adjust_hp(heal_amount)
        caller.db.fp -= self.cost

        caller.msg(
            f"|gYou channel healing energy and restore {heal_amount} health to {target.name}."
        )
        target.msg(
            f"|g{caller.name} channels healing energy and restores {heal_amount} health to you."
        )
        caller.location.msg_contents(
            f"|C{caller.name} channels healing energy and restores {heal_amount} health to {target.name}.",
            exclude=[caller, target],
        )

        caller.cooldowns.add("global_cooldown", 2)
        caller.cooldowns.add("minorheal", 10)


# region Light Heal
class CmdLightHeal(PowerCommand):
    """
    Light Heal allows the Paladin to heal themselves or an ally for a moderate amount of health.

    Usage:
        lightheal <target>

    Example:
        lightheal self
        lightheal ally
    """

    key = "lightheal"
    aliases = ["lheal"]
    help_category = "paladin"
    guild_level = 6
    cost = 25

    def func(self):
        caller = self.caller
        target_name = self.args.strip()

        if not target_name:
            caller.msg("Usage: lightheal <target>")
            return

        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        target = caller.search(target_name)
        if not target:
            return

        if not caller.cooldowns.ready("lightheal"):
            caller.msg(f"|CNot so fast!")
            return False

        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False

        heal_amount = randint(25, 33)

        target.adjust_hp(heal_amount)
        caller.db.fp -= self.cost

        caller.msg(
            f"|gYou channel healing energy and restore {heal_amount} health to {target.name}."
        )
        target.msg(
            f"|g{caller.name} channels healing energy and restores {heal_amount} health to you."
        )
        caller.location.msg_contents(
            f"|C{caller.name} channels healing energy and restores {heal_amount} health to {target.name}.",
            exclude=[caller, target],
        )

        caller.cooldowns.add("global_cooldown", 2)
        caller.cooldowns.add("lightheal", 10)


# region Ward Undead
class WardUndead(PowerCommand):
    """
    Ward Undead allows the Paladin to deal damage to undead creatures in the room.

    Usage:
        wardundead

    Example:
        wardundead
    """

    key = "wardundead"
    aliases = ["wu"]
    help_category = "paladin"
    guild_level = 7
    cost = 30

    def func(self):
        caller = self.caller
        target = caller.db.target

        if not target:
            caller.msg(f"|rYou must have a target to use this power.")
            return

        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        if not caller.cooldowns.ready("wardundead"):
            caller.msg(f"|CNot so fast!")
            return False

        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False

        if not target.db.undead:
            caller.msg(f"|rYou must target an undead creature to use this power.")

        caller.db.fp -= self.cost
        caller.msg(
            f"|gYou channel divine energy, dealing damage to undead creatures in the room."
        )
        caller.location.msg_contents(
            f"|C{caller.name} channels divine energy, dealing damage to undead creatures in the room.",
            exclude=caller,
        )

        target.db.hp -= 41

        caller.cooldowns.add("global_cooldown", 2)
        caller.cooldowns.add("wardundead", 10)


# region Poison
class CmdPoison(PowerCommand):
    """
    Poison allows the Paladin to apply a poison effect to a target, dealing damage over time.

    Usage:
        poison <target>

    Example:
        poison enemy
    """

    key = "poison"
    aliases = ["poi"]
    help_category = "paladin"
    guild_level = 1
    cost = 5
    duration = 10
    tickrate = 5
    damage = 5

    def func(self):
        caller = self.caller
        target_name = self.args.strip()

        if not target_name:
            caller.msg("Usage: poison <target>")
            return

        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        target = caller.search(target_name)
        if not target:
            return

        if not caller.cooldowns.ready("poison"):
            caller.msg(f"|CNot so fast!")
            return False

        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False

        caller.db.fp -= self.cost

        caller.msg(f"|gYou apply a poison effect to {target.name}.")
        target.msg(f"|r{caller.name} applies a poison effect to you.")
        caller.location.msg_contents(
            f"|C{caller.name} applies a poison effect to {target.name}.",
            exclude=[caller, target],
        )

        target.buffs.add(Poison)

        caller.cooldowns.add("global_cooldown", 2)
        caller.cooldowns.add("poison", 30)


class Poison(BaseBuff):
    ...
    # this buff will tick 6 times between application and cleanup.
    duration = 30
    tickrate = 5
    damage = 5
    stacks = 1
    type = "poison"

    def at_tick(self, initial, **kwargs):
        self.owner.adjust_hp(-self.damage)
        self.owner.location.msg_contents(
            f"|GPoison courses through {self.owner.key}'s body, dealing {self.damage} damage."
        )
        if self.ticknum == 5:
            self.owner.msg(f"|GThe poison effect wears off.")


# region Cure Poison
class CmdCurePoison(PowerCommand):
    """
    Cure Poison allows the Paladin to remove a poison effect from a target.

    Usage:
        curepoison <target>

    Example:
        curepoison enemy
    """

    key = "curepoison"
    aliases = ["cp"]
    help_category = "paladin"
    guild_level = 1
    cost = 20

    def func(self):
        caller = self.caller
        target_name = self.args.strip()

        buff = caller.buffs.get("poison")
        self.msg(f"buff: {buff}")

        if not target_name:
            caller.msg("Usage: curepoison <target>")
            return

        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        target = caller.search(target_name)
        if not target:
            return

        if not caller.cooldowns.ready("curepoison"):
            caller.msg(f"|CNot so fast!")
            return False

        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False

        caller.db.fp -= self.cost

        caller.msg(f"|gYou cure the poison effect from {target.name}.")
        target.msg(f"|r{caller.name} cures the poison effect from you.")
        caller.location.msg_contents(
            f"|C{caller.name} cures the poison effect from {target.name}.",
            exclude=[caller, target],
        )

        # target.buffs.dispel("poison")

        caller.cooldowns.add("global_cooldown", 2)
        caller.cooldowns.add("curepoison", 30)


# region Holy Armor
class CmdHolyArmor(PowerCommand):
    """
    Holy Armor allows the Paladin to increase their armor class for a short duration.

    Usage:
        holyarmor

    Example:
        holyarmor
    """

    key = "holyarmor"
    aliases = ["ha"]
    help_category = "paladin"
    guild_level = 8
    cost = 20
    duration = 180

    def func(self):
        caller = self.caller

        if caller.db.ep < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        if not caller.cooldowns.ready("holyarmor"):
            caller.msg(f"|CNot so fast!")
            return False

        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False

        caller.db.fp -= self.cost
        caller.msg(f"|gYou feel a surge of courage, bolstering your armor class.")
        caller.location.msg_contents(
            f"|C{caller.name} looks emboldened, their armor class increasing.",
            exclude=caller,
        )

        caller.buffs.add(HolyArmorBuff)

        caller.cooldowns.add("global_cooldown", 2)
        caller.cooldowns.add("holyarmor", 30)


class HolyArmorBuff(BaseBuff):
    duration = 180
    tickrate = 6
    stacks = 1

    def at_apply(self, initial=True, **kwargs):
        self.owner.armor += 6

    def at_remove(self, **kwargs):
        self.owner.armor -= 6


# region Spells
class CmdSpells(Command):
    """
    List of spells available to the Paladin, their rank, and their cost.

    Usage:
        spells

    """

    key = "spells"
    help_category = "paladin"

    def func(self):
        caller = self.caller

        table = EvTable(f"|cSpell", f"|cRank", f"|cCost", border="table")
        table.add_row(f"|GMinor Heal", 1, 10)
        table.add_row(f"|GCourage", 2, 12)
        table.add_row(f"|GYaulp", 3, 5)
        table.add_row(f"|GPoison", 4, 5)
        table.add_row(f"|GCure Poison", 5, 5)
        table.add_row(f"|GLight Heal", 6, 25)
        table.add_row(f"|GWard Undead", 7, 30)
        table.add_row(f"|GHoly Armor", 8, 20)

        caller.msg(str(table))


# region CmdSet
class PaladinCmdSet(CmdSet):
    key = "Paladin CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        self.add(CmdSpells)
        self.add(CmdMinorHeal)
        self.add(CmdYaulp)
        self.add(CmdPoison)
        self.add(CmdCourage)
        self.add(CmdCurePoison)
        self.add(CmdHolyArmor)
        self.add(WardUndead)
