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


class CmdSpells(Command):
    """
    List of spells available to the Shadow Knight, their rank, and their cost.

    Usage:
        spells

    """

    key = "spells"
    help_category = "shadow knight"

    def func(self):
        caller = self.caller

        table = EvTable(f"|cSpell", f"|cRank", f"|cCost", border="table")
        table.add_row(f"|GLifetap", 2, 10)
        table.add_row(f"|GSiphon Strength", 3, 5)
        table.add_row(f"|GDisease Cloud", 3, 5)

        caller.msg(str(table))


# region CmdSet
class ShadowKnightCmdSet(CmdSet):
    key = "Shadow Knight CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        self.add(CmdSpells)
        self.add(CmdLifetap)
        self.add(CmdDiseaseCloud)
        self.add(CmdSiphonStrength)


# region Lifetap
class CmdLifetap(PowerCommand):
    """
    Drain the life force of your enemy, healing yourself for the damage dealt.
    """

    key = "lifetap"
    aliases = ["lt"]
    help_category = "shadow_knight"
    guild_level = 3
    cost = 9

    def func(self):
        caller = self.caller
        target = caller.db.target

        if not target:
            caller.msg(f"|rYou must have a target to use this power.")
            return

        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        if not caller.cooldowns.ready("lifetap"):
            caller.msg(f"|CNot so fast!")
            return False

        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False

        caller.adjust_fp(-self.cost)
        caller.msg(
            f"|gYou reach out with your shadowy powers, draining the life force from {target.name}."
        )
        target.msg(
            f"|r{caller.name} reaches out with their shadowy powers, draining your life force."
        )
        caller.location.msg_contents(
            f"|C{caller.name} reaches out with their shadowy powers, draining the life force from {target.name}.",
            exclude=[caller, target],
        )

        damage = 5
        caller.adjust_hp(damage)
        target.db.hp -= damage


class CmdDiseaseCloud(PowerCommand):
    """
    Infect the target with a cloud of disease, causing damage over time.
    """

    key = "disease cloud"
    aliases = ["dc"]
    help_category = "shadow_knight"
    guild_level = 5
    cost = 12

    def func(self):
        caller = self.caller
        target = caller.db.target

        if not target:
            caller.msg(f"|rYou must have a target to use this power.")
            return

        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        if not caller.cooldowns.ready("disease_cloud"):
            caller.msg(f"|CNot so fast!")
            return False

        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False

        caller.adjust_fp(-self.cost)
        caller.msg(f"|gYou conjure a cloud of disease, infecting {target.name}.")
        target.msg(f"|r{caller.name} conjures a cloud of disease, infecting you.")
        caller.location.msg_contents(
            f"|C{caller.name} conjures a cloud of disease, infecting {target.name}.",
            exclude=[caller, target],
        )

        caller.cooldowns.add("disease_cloud", 10)
        caller.cooldowns.add("global_cooldown", 2)


class DiseaseCloud(BaseBuff):
    ...
    # this buff will tick 6 times between application and cleanup.
    duration = 10
    tickrate = 3
    damage = 6
    stacks = 1
    type = "disease"

    def at_tick(self, initial, **kwargs):
        self.owner.adjust_hp(-self.damage)
        self.owner.location.msg_contents(
            f"|G{self.actor} doubles over in pain.".format(
                actor=self.owner, damage=self.damage
            )
        )
        if self.ticknum == 5:
            self.owner.msg(f"GYour stomach feels better.")


class CmdSiphonStrength(PowerCommand):
    """
    Drain the strength of your enemy, reducing their damage dealt.
    """

    key = "siphon strength"
    aliases = ["ss"]
    help_category = "shadow_knight"
    guild_level = 7
    cost = 5
    duration = 180

    def func(self):
        caller = self.caller
        target = caller.db.target

        if not target:
            caller.msg(f"|rYou must have a target to use this power.")
            return

        if caller.db.fp < self.cost:
            caller.msg(f"|rYou need at least {self.cost} focus to use this power.")
            return

        if not caller.cooldowns.ready("siphon_strength"):
            caller.msg(f"|CNot so fast!")
            return False

        if not caller.cooldowns.ready("global_cooldown"):
            caller.msg(f"|CNot so fast!")
            return False

        caller.adjust_fp(-self.cost)
        caller.msg(
            f"|gYou reach out with your shadowy powers, siphoning the strength from {target.name}."
        )
        target.msg(
            f"|r{caller.name} reaches out with their shadowy powers, siphoning your strength."
        )
        caller.location.msg_contents(
            f"|C{caller.name} reaches out with their shadowy powers, siphoning the strength from {target.name}.",
            exclude=[caller, target],
        )

        damage = 3
        target.db.strength -= damage
        caller.traits.str.mod += damage
        target.msg(f"|rYour strength is reduced by {damage}.")
        caller.msg(f"|g{target.name}'s strength is reduced by {damage}.")

        delay(self.duration, end_siphon_strength, persistent=True)

        caller.cooldowns.add("siphon_strength", 10)
        caller.cooldowns.add("global_cooldown", 2)

        def end_siphon_strength():
            target.db.strength += damage
            caller.traits.str.mod -= damage
            target.msg(f"|rYour strength returns to normal.")
            caller.msg(f"|g{target.name}'s strength returns to normal.")
