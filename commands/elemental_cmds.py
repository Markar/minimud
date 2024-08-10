from random import choice
from evennia import CmdSet, search_tag
from evennia.utils import iter_to_str
from evennia.utils.evtable import EvTable
from evennia import TICKER_HANDLER as tickerhandler
from evennia import logger

from .command import Command

GUILD_LEVEL_COST_DICT = {
    2: 300,
    3: 400,
    4: 648,
    5: 951,
    6: 1529,
    7: 2409,
    8: 3330,
    9: 4645,
    10: 6000,
    11: 7500,
    12: 10000,
    13: 12900,
    14: 16000,
    15: 22500,
    16: 32000,
    17: 47000,
    18: 67000,
    19: 90000,
    20: 120000,
    21: 160000,
    22: 220000,
    23: 295000,
    24: 445000,
    25: 675000,
    26: 950000,
    27: 1300000,
    28: 1900000,
    29: 2900000,
    30: 4200000, 
    31: 4200000000000,
}

class CmdEnableReactiveArmor(Command):
    """
    Reactive armor enhances your physical resists while lowering others

    Usage:
        enable reactive armor
        disable reactive armor
    """

    key = "enable reactive armor"
    help_category = "reactive armor"

    def func(self):
        print(self.caller)
        caller = self.caller
        caller.use_reactive_armor()

class CmdDisableReactiveArmor(Command):
    """
    Reactive armor enhances your physical resists while lowering others

    Usage:
        enable reactive armor
        disable reactive armor
    """

    key = "disable reactive armor"
    help_category = "reactive armor"

    def func(self):
        print(self.caller)
        caller = self.caller
        caller.db.reactive_armor = False
        caller.db.edgedac -= caller.db.guild_level
        caller.db.bluntac -= caller.db.guild_level
        caller.msg(f"|CYou reactive armor dissolves.")
        
class CmdRebuild(Command):
    """
    Restores health

    Usage:
        rebuild
    """

    key = "rebuild"
    help_category = "combat"

    def func(self):
        print(self.caller)
        caller = self.caller
        caller.use_rebuild()


class CmdEmit(Command):
    """
    Changes the power of your attack, costing more energy
    and dealing more damage with higher ranks. New ranks
    unlock every 5 guild levels.
    

    Usage:
        emit 1
        emit 2
    """

    key = "emit"
    help_category = "combat"

    def func(self):
        caller = self.caller
        
        try:
            print(f"emit: args {self.args}")
            print(f"emit: {self.caller}")
            logger.log_info("test logger")
            power = int(self.args.strip())
            if power == 1 and caller.db.guild_level > 0:
                print(f"power = 1, caller.db.guild_level {power} and {caller.db.guild_level}")
                caller.db.emit = 1
            if power == 2 and caller.db.guild_level >= 5:
                print(f"power = 2, caller.db.guild_level {power} and {caller.db.guild_level}")
                caller.db.emit = 2
            if power == 3 and caller.db.guild_level >= 10:
                print(f"power = 2, caller.db.guild_level {power} and {caller.db.guild_level}")
                caller.db.emit = 3
            if power == 4 and caller.db.guild_level >= 15:
                print(f"power = 2, caller.db.guild_level {power} and {caller.db.guild_level}")
                caller.db.emit = 4
            if power == 5 and caller.db.guild_level >= 20:
                print(f"power = 2, caller.db.guild_level {power} and {caller.db.guild_level}")
                caller.db.emit = 5
            if power == 6 and caller.db.guild_level >= 25:
                print(f"power = 2, caller.db.guild_level {power} and {caller.db.guild_level}")
                caller.db.emit = 6
            if power == 7 and caller.db.guild_level >= 30:
                print(f"power = 2, caller.db.guild_level {power} and {caller.db.guild_level}")
                caller.db.emit = 7
            self.msg(f"|rYou set your emit to power level {caller.db.emit}")
        except ValueError:
            print(f"Not an integer for use_emit")
        

class CmdGAdvance(Command):
    """
    Advance a level or attribute by spending experience points.

    Enter "advance" to see what you can learn.

    Usage:
        gadvance

    Example:
        gadvance
    """

    key = "gadvance"
    aliases = ("gadv")

    def _adv_level(self):
        print(f"adv level {self} and caller: {self.caller}")        
        caller = self.caller
        cost = GUILD_LEVEL_COST_DICT[caller.db.guild_level+1]
        print(f"cost{cost} and gxp: {caller.db.gxp}")
        if caller.db.gxp < cost:
            self.msg(f"|wYou need {cost - caller.db.gxp} more experience to advance.")
            return
        else:
            caller.db.gxp -= cost
            caller.db.guild_level += 1
            caller.db.epmax += 10
            self.msg(f"|rYou grow more powerful.")
              
    def func(self):
        caller = self.caller
        caller.msg(f"|G{caller}")
        print(f"in advance function")

        self._adv_level()
        print(f"after _adv_level {caller.db.gxp}")

class CmdGuildStatSheet(Command):
    """
    View your character's current stats.
    """

    key = "gscore"
    aliases = ("gs")

    def func(self):
        caller = self.caller
        self.msg(f"|c{caller} {caller.db.title} ({caller.db.alignment})")
        self.msg(f"|GGuild Level: {caller.db.guild_level or 0}")
        self.msg(f"|GGXP: {caller.db.gxp or 0}")
        self.msg(f"|GEmit: {caller.db.emit or 0}")
        self.msg(f"|GForm: {caller.db.subguild}")
    
class CmdJoinElementals(Command):
    """
    Join the Elementals guild
    """
    
    key = "join elementals"
    
    def func(self):
        caller = self.caller
        if caller.db.guild == "adventurer":
            caller.msg(f"|rYou join the Elementals guild")
            caller.swap_typeclass("typeclasses.elementals.Elemental")
        else:
            caller.msg(f"|rYou are already in a guild")
            
class CmdLeaveElementals(Command):
    """
    Leave the Elementals guild
    """
    
    key = "leave elementals"
    
    def func(self):
        caller = self.caller
        if caller.db.guild == "elemental":
            caller.swap_typeclass("typeclasses.characters.PlayerCharacter")
            caller.cmdset.delete(ElementalCmdSet)
            caller.msg(f"|rYou leave the Elementals guild")
        else:
            caller.msg(f"|rYou are already an adventurer")
            
            
class CmdDrain(Command):
    """
    Drain the corpse of an enemy to restore energy
    """
    
    key = "drain" 
    
    def func(self):
        if not self.args:
            target = self.caller
            corpse = target.location.search("corpse")
            ep = target.db.ep
            epmax = target.db.epmax
            power = corpse.db.power
            
            if ep + power > epmax:
                target.db.ep = epmax
            else:
                target.db.ep += max(power, 0)
            corpse.delete()
            self.msg(f"|rYou drain the energy from the corpse and it turns into dust.")
        else:
            print(f"status args: {self.caller.search(self.args.strip())}")
            target = self.caller.search(self.args.strip())
            if not target:
                # no valid object found
                return
            self.msg(f"corpse with args {self.args}")
            
class CmdChooseForm(Command):
    """
    Choose your permanent form
    """
    
    key = "chooseform" 
    
    def func(self):
        target = self.args.strip()
        caller = self.caller
        if caller.db.guild_level > 5:
            caller.msg(f"|rYou have already chosen {caller.db.subguild} as your permanent form.")
            return
        if not target:
            self.msg(f"|rYou can choose earth, fire, water, or air.")
            return
        
        if target == "earth":
            caller.db.subguild = "earth"
            caller.msg(f"|yYou choose {caller.db.subguild} as your permanent form.")
        if target == "fire":
            caller.db.subguild = "fire"
            caller.msg(f"|rYou choose {caller.db.subguild} as your permanent form.")
        if target == "water":
            caller.db.subguild = "water"
            caller.msg(f"|bYou choose {caller.db.subguild} as your permanent form.")
        if target == "air":
            caller.db.subguild = "air"
            caller.msg(f"|wYou choose {caller.db.subguild} as your permanent form.")


        
class ElementalCmdSet(CmdSet):
    key = "Elemental CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        self.add(CmdDrain)
        self.add(CmdRebuild)
        self.add(CmdGAdvance)
        self.add(CmdEmit)
        self.add(CmdGuildStatSheet)
        self.add(CmdChooseForm)
        self.add(CmdEnableReactiveArmor)
        self.add(CmdDisableReactiveArmor)
