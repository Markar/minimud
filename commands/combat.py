from random import choice
from evennia import CmdSet
from evennia.utils import iter_to_str
from evennia.utils.evtable import EvTable
from typeclasses.scripts import get_or_create_combat_script
from evennia.contrib.game_systems.clothing.clothing import CmdWear

from .command import Command
from typeclasses.gear import BareHand


class CmdAttack(Command):
    """
    Attack an enemy with your equipped weapon.
    """

    key = "attack"
    aliases = ("att", "hit", "kill")
    help_category = "combat"

    def parse(self):
        """
        Parse for optional weapon
        """
        self.args = self.args.strip()
        self.target = self.args
        self.weapon = None

    def func(self):
        location = self.caller.location
        if not location:
            self.msg("You cannot fight nothingness.")
            return

        if not self.target:
            self.msg("Attack what?")
            return

        if wielded := self.caller.wielding:
            self.msg(f"You are wielding {iter_to_str(wielded)}.")
            weapon = wielded[0]
        else:
            # use our bare hands if we aren't wielding anything
            weapon = BareHand()

        # find our enemy!
        target = self.caller.search(self.target)
        if not target:
            # no valid match
            return
        if not target.db.can_attack:
            # this isn't something you can attack
            self.msg(f"You can't attack {target.get_display_name(self.caller)}.")
            return

            # if we were trying to flee, cancel that
        del self.caller.db.fleeing

        # it's all good! let's get started!
        combat_script = get_or_create_combat_script(location)
        current_fighters = combat_script.fighters

        # adding a combatant to combat just returns True if they're already there, so this is safe
        if not combat_script.add_combatant(self.caller, enemy=target):
            self.msg("You can't fight right now.")
            return

        self.caller.db.combat_target = target

        # execute the actual attack
        self.caller.attack(target, weapon)

        # check if we have auto-attack in settings
        if self.account and (settings := self.account.db.settings):
            if settings.get("auto attack"):
                # let the player know we'll be auto-attacking
                self.msg(f"[ Auto-attack is ON ]")

    def at_post_cmd(self):
        """
        optional post-command auto prompt
        """

        print(f"at_post_cmd {self} and {self.account.db.settings}")
        # check if we have auto-prompt in settings
        if self.account and (settings := self.account.db.settings):
            if settings.get("auto prompt"):
                status = self.caller.get_display_status(self.caller)
                self.msg(prompt=status)


class CmdWield(Command):
    """
    Wield a weapon

    Usage:
        wield <weapon> [in <hand>]

    Example:
        wield sword
        wield dagger in right
    """

    key = "wield"
    aliases = ("hold",)
    help_category = "combat"

    def parse(self):
        """
        Parse for optional weapon
        """
        self.args = self.args.strip()

        # split on the word "in"
        if " in " in self.args:
            self.weapon, self.hand = self.args.split(" in ", maxsplit=1)
        else:
            # no splitter, it's all target
            self.weapon = self.args
            self.hand = None

    def func(self):
        caller = self.caller

        print(f"free hands {caller.free_hands}")
        # check if we have free hands
        if not (hands := caller.free_hands):
            self.msg(
                f"You have no free hands! You are already wielding {iter_to_str(caller.wielding)}."
            )
            return

        # filter for hands matching the optional hand input
        if self.hand:
            hands = [hand for hand in caller.free_hands if self.hand in hand]
            if not hands:
                self.msg(f"You do not have a free {self.hand}.")

        # grab the top hand option
        hand = hands[0]

        weapon = caller.search(self.weapon, location=caller)
        if not weapon:
            # no valid object found
            return

        # try to wield the weapon
        held_in = caller.at_wield(weapon, hand=hand)
        if held_in:
            hand = "hand" if len(held_in) == 1 else "hands"
            # success!
            self.caller.at_emote(
                f"$conj(wields) the {{weapon}} in $pron(your) {iter_to_str(held_in)} {hand}.",
                mapping={"weapon": weapon},
            )


class CmdUnwield(Command):
    """
    Stop wielding a weapon

    Usage:
        unwield <weapon>

    Example:
        unwield dagger
    """

    key = "unwield"
    aliases = ("unhold",)
    help_category = "combat"

    def func(self):
        caller = self.caller

        weapon = caller.search(self.args, location=caller)
        if not weapon:
            # no valid object found
            return

        freed_hands = caller.at_unwield(weapon)
        if freed_hands:
            # success!
            hand = "hand" if len(freed_hands) == 1 else "hands"
            self.caller.at_emote(
                f"$conj(releases) the {{weapon}} from $pron(your) {iter_to_str(freed_hands)} {hand}.",
                mapping={"weapon": weapon},
            )


class CmdFlee(Command):
    """
    Attempt to escape from combat.

    Usage:
        flee
    """

    key = "flee"
    help_category = "combat"

    def func(self):
        caller = self.caller

        if not caller.in_combat:
            self.msg("You are not in combat.")
            return

        if not caller.can_flee:
            # this does its own error messaging
            return

        exits = caller.location.contents_get(content_type="exit")
        if not exits:
            self.msg("There is nowhere to flee to!")
            return

        if combat_script := caller.location.scripts.get("combat"):
            combat_script = combat_script[0]
            if not combat_script.remove_combatant(self.caller):
                self.msg("You cannot leave combat.")

        self.caller.db.fleeing = True
        self.msg("You flee!")
        flee_dir = choice(exits)
        self.execute_cmd(flee_dir.name)

    def at_post_cmd(self):
        """
        optional post-command auto prompt
        """
        # check if we have auto-prompt in settings
        if self.account and (settings := self.account.db.settings):
            if settings.get("auto prompt"):
                status = self.caller.get_display_status(self.caller)
                self.msg(prompt=status)


class CmdHeal(Command):
    """
    Restores health

    Usage:
        heal
    """

    key = "heal"
    help_category = "combat"

    def func(self):
        print(self.caller)
        caller = self.caller
        if caller.key != "Markar":
            caller.msg("You can't do that.")
            return

        caller.use_heal()


class CmdWearNew(CmdWear):
    """
    Wear an item of clothing

    Usage:
        wear <item>
    """

    key = "wear"
    help_category = "combat"

    def func(self):
        caller = self.caller
        item = caller.search(self.args)

        if not item:
            return

        if not item.db.clothing_type:
            self.msg("You can't wear that.")
            return

        if not caller.can_wear(item):
            return

        super().func()


# class CmdFireball(Command):
#     """
#     Casts a fireball

#     Usage:
#         fireball
#     """

#     key = "fireball"
#     help_category = "combat"

#     def func(self):
#         print(f"self.caller: {self.caller}")
#         print(f"self.args: {self.args}")
#         caller = self.caller
#         target = self.args
#         location = self.caller.location
#         cscript = location.scripts.get("combat")[0]
#         cscript.add_combatant(self, enemy=target)
#         print(f"location: {cscript}")

#         target = caller.search(target)
#         print(f"target: {target}")
#         caller.db.combat_target = target
#         # if caller.in_combat:
#         caller.use_fireball(target)


class CmdRespawn(Command):
    """
    Return to the center of town when defeated, with full health.

    Usage:
        respawn
    """

    key = "respawn"
    help_category = "combat"

    def func(self):
        caller = self.caller

        if not caller.tags.has("unconscious", category="status"):
            self.msg("You are not defeated.")
            return
        caller.respawn()


class CmdRevive(Command):
    """
    Revive another player who has been defeated. They will recover partial health.

    Usage:
        revive <player>
    """

    key = "revive"
    help_category = "combat"

    def func(self):
        caller = self.caller

        if not self.args:
            self.msg("Revive who?")
            return

        target = caller.search(self.args.strip())
        if not target:
            return

        if not target.tags.has("unconscious", category="status"):
            self.msg(f"{target.get_display_name(caller)} is not defeated.")
            return

        target.revive(caller)


class CmdStatus(Command):
    key = "status"
    aliases = ("hp", "stat")
    # target is the target of the status command

    def func(self):
        # self.enemy = self.args
        # enemy = self.caller.search(self.target)

        if not self.args:
            target = self.caller
            status = target.get_display_status(self.caller)
        else:
            print(f"status args: {self.caller.search(self.args.strip())}")
            target = self.caller.search(self.args.strip())
            if not target:
                # no valid object found
                return
            status = target.get_display_status(self.caller)
            self.msg(status)


class CombatCmdSet(CmdSet):
    key = "Combat CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        self.add(CmdAttack)
        self.add(CmdFlee)
        self.add(CmdWield)
        self.add(CmdUnwield)
        self.add(CmdRevive)
        self.add(CmdRespawn)
        self.add(CmdStatus)
        # self.add(CmdFireball)
        self.add(CmdHeal)
        self.add(CmdWearNew)
