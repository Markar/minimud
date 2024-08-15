import math
from random import randint
from evennia import CmdSet, search_tag
from evennia.utils import iter_to_str
from evennia.utils.evtable import EvTable
from evennia import TICKER_HANDLER as tickerhandler
from evennia import logger
from commands.command import Command
        
class CmdAerialRestoration(Command):
    """
    The air elemental can restore their body to restore health, 
    at the cost of focus. The amount of health restored is based on
    the elemental's wisdom and guild level.

    Usage:
        aerial restoration
    """

    key = "aerial restoration"
    help_category = "air elemental"
    aliases = ["ar"]
    guild_level = 4

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        
        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return
        
        if not caller.cooldowns.ready("aerial restoration"):
            caller.msg(f"|BNot so fast!")
            return False
        caller.cooldowns.add("aerial restoration", 4)
        
        wis = caller.db.wisdom
        hp = caller.db.hp
        hpmax = caller.db.hpmax
        fp = caller.db.fp
        
        to_heal = math.floor(10 + glvl * 1.5 + wis/2)
        to_heal = randint(to_heal/2, to_heal)        
        cost = to_heal * 0.5
        
        if fp < cost:
            self.msg(f"|rYou can't seem to focus on restoring your form.")
            return        
        
        if hp + to_heal > hpmax:            
            caller.db.hp = hpmax
            caller.db.fp -= cost
        else: 
            caller.db.hp += max(to_heal, 0)
            caller.db.fp -= cost
            
        msg = f"|M$Your() form shimmers as it draws in surrounding winds. Gentle breezes swirl around it, mending its ethereal body."
        msg2 = f"|M$Your() form becomes more defined and vibrant, as the healing winds restore its strength and vitality."
        
        caller.location.msg_contents(msg, from_obj=caller)
        
class CmdEnvelop(Command):
    """
    Envelop the corpse of an enemy to restore energy
    """
    
    key = "envelop" 
    aliases = ["en", "ev"]
    help_category = "air elemental"
    
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
                caller.msg("Drain what?")

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
        
class CmdPowers(Command):
    """
    List of powers available to the Elemental, their rank, and their cost.
    
    Usage:
        powers
    
    """
    
    key = "powers"
    help_category = "air elemental"
    
    def func(self):
        caller = self.caller
        
        table = EvTable(f"|cPower", f"|cRank", f"|cCost", border="table")
        table.add_row(f"|GEnvelop", 1, 0)
        table.add_row(f"|GReaction", 1, 0)
        table.add_row(f"|GAerial Restoration", 3, 25)
        
        caller.msg(str(table))     
class AirElementalCmdSet(CmdSet):
    key = "Air Elemental CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        self.add(CmdEnvelop)
        self.add(CmdAerialRestoration)
        self.add(CmdPowers)
        self.add(CmdReaction)
