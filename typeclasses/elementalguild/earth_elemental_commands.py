import math
from random import randint
from evennia import CmdSet, search_tag
from evennia.utils import iter_to_str
from evennia.utils.evtable import EvTable
from evennia import TICKER_HANDLER as tickerhandler
from evennia import logger
from commands.command import Command
from typeclasses.elementalguild.constants_and_helpers import SKILLS_COST

class CmdReactiveArmor(Command):
    """
    Reactive armor enhances your physical resists while lowering others

    Usage:
        reactive armor
        ra
    """

    key = "reactive armor"
    aliases = ["ra"]
    help_category = "earth elemental"

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        if glvl < 5:
            caller.msg(f"|CYou need to be guild level 5 to use reactive armor.")
            return
        
        if not caller.db.reactive_armor:
            caller.db.reactive_armor = True
            activateMsg = f"|C$Your() body hardens, rocky plates forming a protective barrier that absorbs and deflects incoming attacks."
            caller.location.msg_contents(activateMsg, from_obj=caller)
        else:
            caller.db.reactive_armor = False
            deactivateMsg = f"|C$Your() body softens, the rocky plates that once protected $pron(you) now dissipating."
            caller.location.msg_contents(deactivateMsg, from_obj=caller)

        
class CmdTerranRestoration(Command):
    """
    The earth elemental can rebuild their body to restore health, 
    at the cost of focus. The amount of health restored is based on
    the elemental's wisdom and guild level.

    Usage:
        terran restoration
    """

    key = "terran restoration"
    aliases = ["tr", "restore"]
    help_category = "earth elemental"
    guild_level = 4

    def func(self):
        caller = self.caller
        glvl = caller.db.guild_level
        
        if glvl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return
        
        if not caller.cooldowns.ready("rebuild"):
            caller.msg(f"|BNot so fast!")
            return False
        caller.cooldowns.add("rebuild", 4)                
        
        wis = caller.db.wisdom
        strength = caller.db.strength
        hp = caller.db.hp
        hpmax = caller.db.hpmax
        fp = caller.db.fp
        hp_amount = 0
        
        to_heal = math.floor(10 + glvl + strength/2 + wis/2)
        to_heal = randint(int(to_heal/2), to_heal)
        cost = to_heal * 0.5        
        
        if caller.db.fp < cost:
            self.msg(f"|rYou can't seem to focus on rebuilding your form.")
            return
        
        if hp + to_heal > hpmax:            
            hp_amount = hpmax-hp
            caller.db.hp = hpmax
            caller.db.fp -= cost
        else: 
            hp_amount = hpmax-hp
            caller.db.hp += max(to_heal, 0)
            caller.db.fp -= cost
            
        self.msg(f"You restore {hp_amount or 0} health for {cost or 0} focus")
        msg = f"|M$pron(Your) rocky exterior begins to shift and mend. Cracks seal themselves as stones and minerals realign, drawn from the surrounding ground."
        caller.location.msg_contents(msg, from_obj=caller)    
        
class CmdAssimilate(Command):
    """
    Assimilate the corpse of an enemy to restore energy
    """
    
    key = "assimilate" 
    aliases = ["asm"]
    help_category = "earth elemental"
    
    def func(self):
        if not self.args:
            caller = self.caller
            if corpse := caller.location.search("corpse-1"):
                base_power = corpse.db.power
                skill_rank = caller.db.skills.get("assimilate", 0)
                
                # Calculate the power with the skill rank multiplier
                power = base_power * (1 + (skill_rank * 0.1))
                
                caller.addep(power)
                corpse.delete()
                assimilate_msg = f"|M$pron(Your) form glows faintly as it assimilates the energy from the consumed corpse, strengthening $pron(your) rocky exterior."
                caller.location.msg_contents(assimilate_msg, from_obj=caller)
            else:
                caller.msg("Assimilate what?")
   
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
        table.add_row(f"|GAssimilate", 1, 0)
        table.add_row(f"|GReaction", 1, 0)
        table.add_row(f"|GTerran Restoration", 3, "variable")
        table.add_row(f"|GReactive Armor", 7, 0)
        
        caller.msg(str(table))                

class CmdReaction(Command):
    """
    Set the elemental's reaction to a dropping below a certain health threshold.
    
    Usage:
        reaction <percentage>
    """
    
    key = "reaction"
    help_category = "earth elemental"
    
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
        gtrain mineral fortification
    """
    
    key = "gtrain"
    help_category = "Earth Elemental"
    
    def func(self):
        caller = self.caller
        skill = self.args.strip().lower()
        list = ["mineral fortification", "assimilation", "earthen regeneration"]
        
        if skill == "":
                self.msg(f"|gWhat would you like to raise?")
                return
            
        if skill not in list:
            caller.msg(f"|gYou can't raise that.")
            return
        
        skill_gxp = getattr(caller.db, "skill_gxp", 0)
        cost = caller.db.skills[f"{skill}"]+1
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

class Test(Command):
    key = "test2"
    
    def func(self):
        self.msg("Test command")
        cost = self.caller.db.skills["mineral fortification"]+1
        self.msg(f"|gCost: {cost}")
        cost = SKILLS_COST[cost]
        self.msg(f"|gCost2: {cost}")
                
class EarthElementalCmdSet(CmdSet):
    key = "Earth Elemental CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        self.add(CmdAssimilate)
        self.add(CmdTerranRestoration)
        self.add(CmdReactiveArmor)
        self.add(CmdPowers)
        self.add(CmdReaction)
        self.add(CmdGTrain)
        self.add(Test)
