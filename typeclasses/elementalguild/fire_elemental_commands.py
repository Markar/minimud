import math
from random import randint
from evennia import CmdSet, search_tag
from evennia.utils import iter_to_str
from evennia.utils.evtable import EvTable
from evennia import TICKER_HANDLER as tickerhandler
from evennia import logger
from commands.command import Command
        
class CmdFlameRenewal(Command):
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
            caller.msg(f"|BNot so fast!")
            return False
        caller.cooldowns.add("flame renewal", 6)
                
        glvl = caller.db.guild_level
        wis = caller.db.wisdom
        intel = caller.db.intelligence
        hp = caller.db.hp
        hpmax = caller.db.hpmax
        fp = caller.db.fp
        hp_amount = 0
        
        to_heal = math.floor(10 + glvl + intel/2 + wis/2)
        to_heal = randint(int(to_heal/2), to_heal)
        cost = to_heal * 0.75
        
        if fp < cost:
            self.msg(f"|rYou can't seem to focus on renewing your form.")
            return
        
        if hp + to_heal > hpmax:            
            hp_amount = hpmax-hp
            caller.db.hp = hpmax
            caller.db.fp -= cost
        else: 
            hp_amount = hpmax-hp
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
        
        table = EvTable(f"|cPower", f"|cRank", f"|cCost", border="table")
        table.add_row(f"|GAbsorb", 1, 0)
        table.add_row(f"|GReaction", 1, 0)
        table.add_row(f"|GFlame Renewal", 3, 25)
        
        caller.msg(str(table)) 
         
class FireElementalCmdSet(CmdSet):
    key = "Fire Elemental CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        self.add(CmdAbsorb)
        self.add(CmdFlameRenewal)
        self.add(CmdReaction)
        self.add(CmdPowers)
