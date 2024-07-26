from random import choice
from evennia import CmdSet, search_tag
from evennia.utils import iter_to_str
from evennia.utils.evtable import EvTable
from evennia import TICKER_HANDLER as tickerhandler
from evennia import logger

from .command import Command

def get_article(word):
    vowels = "aeiou"
    return "an" if word[0].lower() in vowels else "a"

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
    30: 4200000 
}

AVIAN_FORMS = {
   30: "eagle",
   28: "ostrich",
   26: "condor",
   24: "hawk",
   22: "falcon",
   20: "osprey",
   18: "owl",
   16: "kestrel",
   14: "crane",
   12: "raven",
   10: "crow",
    8: "swallow",
    6: "sparrow",
    4: "finch",
    2: "hummingbird"
}

MAMMAL_FORMS = {
    30: "lion",
    28: "tiger",
    26: "jaguar",
    24: "leopard",
    22: "cheetah",
    20: "elephant",
    18: "grizzly bear",
    16: "black bear",
    14: "wolf",
    12: "wolverine",
    10: "badger",
    8: "fox",
    6: "lynx",
    4: "cat",
    2: "rat",
}

REPTILE_FORMS = {
    30: "komodo dragon",  
    28: "anaconda", 
    26: "alligator",      
    24: "crocodile",
    22: "python",
    20: "gila monster",
    18: "cobra",
    16: "caiman",
    14: "viper",
    12: "boa",
    10: "iguana",
     8: "skink",
     6: "gecko",
     4: "teiid",
     2: "anole"
}

class CmdMorph(Command):
    """
    Morph into various things
    
    Usage:
    morph anole
    """

    key = "morph"
    help_category = "Changeling"

    def func(self):
        caller = self.caller
        try:
            form = self.args.strip()

            my_glvl = caller.db.guild_level
            caller.db.ep -= my_glvl
            caller.addhp(my_glvl)
            
            form_title = form.title()
            
            if form == "human":
                print(f"form = human and {caller.db.guild_level}")
                self.msg(f"|rYou morph back into your human form!")
                caller.db.form = "Human"
                return
            
            reptile = next((key for key, value in REPTILE_FORMS.items() if value == form), -1)
            if not reptile == -1 and my_glvl >= reptile:
                self.msg(f"|rYou morph into {get_article(form)} {form_title}!")
                caller.db.form = form_title
                return
     
            mammal = next((key for key, value in MAMMAL_FORMS.items() if value == form), -1)
            if not mammal == -1 and my_glvl >= mammal:
                self.msg(f"|rYou morph into {get_article(form)} {form_title}!")
                caller.db.form = form_title
                return
                
            avian = next((key for key, value in MAMMAL_FORMS.items() if value == form), -1)
            if not avian == -1 and my_glvl >= avian:
                self.msg(f"|rYou morph into {get_article(form)} {form_title}!")
                caller.db.form = form_title
                return
                
            self.msg(f"|rYou can't morph into that.")
        except ValueError:
            print(f"You don't know how to use that form.")

class CmdEnableEnergyControl(Command):
    """
    Energy Control enhances your physical resists while lowering others

    Usage:
        enable energy control
        disable energy control
    """

    key = "enable energy control"
    help_category = "Changeling"

    def func(self):
        print(self.caller)
        caller = self.caller
        caller.use_energy_control()

class CmdDisableEnergyControl(Command):
    """
    Reactive armor enhances your physical resists while lowering others

    Usage:
        enable energy control
        disable energy control
    """

    key = "disable energy control"
    help_category = "Changeling"

    def func(self):
        print(self.caller)
        caller = self.caller
        caller.db.energy_control = False
        caller.db.edgedac -= caller.db.guild_level
        caller.db.bluntac -= caller.db.guild_level
        caller.msg(f"|CYou release your control over energy.")
        
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

class CmdEngulf(Command):
    """
    Engulf is the Changeling's Super Power.  You only get a limited
    number of them per time, rather than having them cost stamina.

    Engulf causes you to enclose the targets entire body within
    your plasmic form, once enclosed you drain their life energy
    away from them, this does severe damage to them and heals
    you greatly.  After engulfing, you are unable to move (or quit) for
    up to 5 rounds, so be careful.

    Usage:
        rebuild
    """

    key = "rebuild"
    help_category = "combat"

    def func(self):
        print(self.caller)
        caller = self.caller
        caller.use_rebuild()
        
class CmdForms(Command):
    """
    List of forms
    
    Usage:
    forms
    """
    
    key="forms"
    help_category = "Changeling"
        
    def func(self):
        caller = self.caller
        my_glvl = caller.db.guild_level
                    
        table = EvTable(f"|cAvian", f"|cMammal", f"|cReptile", f"|cGlvl", border="rows")
        for glvl in REPTILE_FORMS:
            if my_glvl >= glvl:
                table.add_row(f"|Y{AVIAN_FORMS[glvl]}", f"|Y{MAMMAL_FORMS[glvl]}", f"|Y{REPTILE_FORMS[glvl]}", glvl)
            else:
                table.add_row(f"|G{AVIAN_FORMS[glvl]}", f"|G{MAMMAL_FORMS[glvl]}", f"|G{REPTILE_FORMS[glvl]}", glvl)
        
        caller.msg(str(table))
             

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
        
        if caller.db.guild_level >= 7:
            caller.db.engulf_max = 1
        elif caller.db.guild_level >= 14:
            caller.db.engulf_max = 2
        elif caller.db.guild_level >= 30:
            caller.db.engulf_max = 3
              
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
        # self.msg(f"|GEmit: {caller.db.emit or 0}")
        self.msg(f"|GForm: {caller.db.form}")
    
class CmdJoinChangelings(Command):
    """
    Join the Changeling guild
    """
    
    key = "join changelings"
    
    def func(self):
        caller = self.caller
        if caller.db.guild == "adventurer":
            caller.msg(f"|rYou join the Changeling guild")
            caller.swap_typeclass("typeclasses.changelings.Changelings")
        else:
            caller.msg(f"|rYou are already in a guild")
            
class CmdLeaveChangelings(Command):
    """
    Leave the Elementals guild
    """
    
    key = "leave changelings"
    
    def func(self):
        caller = self.caller
        if caller.db.guild == "changeling":
            caller.swap_typeclass("typeclasses.characters.PlayerCharacter")
            caller.db.subguild = "none"
            caller.db.form = "none"
            caller.db.energy_control = "none"
            tickerhandler.remove(interval=6, callback=caller.at_tick, idstring="ticker1", persistent=True)
            tickerhandler.remove(interval=6, callback=caller.at_tick, idstring="ticker1", persistent=True)
            tickerhandler.add(interval=60*5, callback=caller.at_engulf_tick, idstring="markar-engulf", persistent=True)
            caller.cmdset.delete(ChangelingCmdSet)
            caller.msg(f"|rYou leave the Changeling guild")
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
            self.msg(f"target {target}")
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
            
        
class ChangelingCmdSet(CmdSet):
    key = "Changeling CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        self.add(CmdDrain)
        self.add(CmdGAdvance)
        self.add(CmdGuildStatSheet)
        self.add(CmdJoinChangelings)
        self.add(CmdLeaveChangelings)
        self.add(CmdMorph)
        self.add(CmdLeaveChangelings)
        self.add(CmdEnableEnergyControl)
        self.add(CmdDisableEnergyControl)
        self.add(CmdEngulf)
        self.add(CmdForms)

