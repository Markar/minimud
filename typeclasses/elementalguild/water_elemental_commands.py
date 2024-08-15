import math
from random import randint
from evennia import CmdSet, search_tag
from evennia.utils import iter_to_str
from evennia.utils.evtable import EvTable
from evennia import TICKER_HANDLER as tickerhandler
from evennia import logger
from commands.command import Command
        
class CmdRejuvenate(Command):
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
        caller.cooldowns.add("rejuvenate", 3)
                        
        wis = caller.db.wisdom
        con = caller.db.constitution
        intel = caller.db.intelligence
        hp = caller.db.hp
        hpmax = caller.db.hpmax
        fp = caller.db.fp
        hp_amount = 0        
        
        damage = 10 + glvl * 2 + wis
        to_heal = math.floor(10 + glvl*2 + intel/2 + wis/2 + con/2)
        to_heal = randint(int(to_heal/2), to_heal)
        cost = damage * 0.25
        
        if cost > fp:
            self.msg(f"|rYou can't seem to focus on rebuilding your form.")
            return
        
        if hp + damage > hpmax:            
            hp_amount = hpmax-hp
            caller.db.hp = hpmax
            caller.db.fp -= cost
        else: 
            hp_amount = hpmax-hp
            caller.db.hp += max(damage, 0)
            caller.db.fp -= cost
            
        msg = f"As you() concentrate, your() body glows with a soft, blue light, and water swirls around you, knitting wounds and restoring vitality. {hp_amount or 0} health restored for {cost or 0} focus."
        
        caller.location.msg_contents(msg, from_obj=caller)
        

       
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
        
        table = EvTable(f"|cPower", f"|cRank", f"|cCost", border="table")
        table.add_row(f"|GEnvelop", 1, 0)
        table.add_row(f"|GReaction", 1, 0)
        table.add_row(f"|GRejuvenate", 3, 25)
        
        caller.msg(str(table))             
        
class WaterElementalCmdSet(CmdSet):
    key = "Water Elemental CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        self.add(CmdEnvelop)
        self.add(CmdRejuvenate)
        self.add(CmdPowers)
        self.add(CmdReaction)
