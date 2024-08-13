from random import choice
from evennia import CmdSet, search_tag
from evennia.utils import iter_to_str
from evennia.utils.evtable import EvTable
from evennia import TICKER_HANDLER as tickerhandler
from evennia import logger

from .command import Command
from typeclasses.elementalguild.earth_elemental_commands import EarthElementalCmdSet
from typeclasses.elementalguild.air_elemental_commands import AirElementalCmdSet
from typeclasses.elementalguild.fire_elemental_commands import FireElementalCmdSet
from typeclasses.elementalguild.water_elemental_commands import WaterElementalCmdSet

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
    help_category = "elemental"

    def _adv_level(self):       
        caller = self.caller
        cost = GUILD_LEVEL_COST_DICT[caller.db.guild_level+1]
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
    Display your guild stats
    """

    key = "gscore"
    aliases = ("gs")
    help_category = "elemental"

    def func(self):
        caller = self.caller
        my_glvl = caller.db.guild_level or 1
        gxp_needed = GUILD_LEVEL_COST_DICT[my_glvl+1]
        skill_gxp = caller.db.skill_gxp or 0
        
        self.msg(f"|c{caller} {caller.db.title} ({caller.db.alignment})")
        self.msg(f"|GGuild Level: {caller.db.guild_level or 0}")
        self.msg(f"|GGXP: {caller.db.gxp or 0} / {gxp_needed}")
        # table.add_row(f"|GSkill GXP: {skill_gxp}")
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
            # caller.swap_typeclass("typeclasses.elementals.Elemental")
            caller.swap_typeclass("typeclasses.elementalguild.earth_elemental.EarthElemental", clean_attributes=False)
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
            
            
# class CmdDrain(Command):
#     """
#     Drain the corpse of an enemy to restore energy
#     """
    
#     key = "drain" 
#     aliases = ["dc", "dr"]
#     help_category = "elemental"
    
#     def func(self):
#         if not self.args:
#             target = self.caller
#             corpse = target.location.search("corpse")
#             ep = target.db.ep
#             epmax = target.db.epmax
#             power = corpse.db.power
            
#             if ep + power > epmax:
#                 target.db.ep = epmax
#             else:
#                 target.db.ep += max(power, 0)
#             corpse.delete()
#             self.msg(f"|rYou drain the energy from the corpse and it turns into dust.")
#         else:
#             print(f"status args: {self.caller.search(self.args.strip())}")
#             target = self.caller.search(self.args.strip())
#             if not target:
#                 # no valid object found
#                 return
#             self.msg(f"corpse with args {self.args}")
            
class CmdChooseForm(Command):
    """
    You can choose from earth, fire, water, or air. Earth is more defensive,
    fire is more offensive, water is more balanced, and air is more
    evasive. Once you choose a form, you cannot change it.
    """
    
    key = "chooseform" 
    help_category = "elemental"
    
    def _remove_cmdsets(self):
        caller = self.caller
        if caller.db.subguild == "earth":
            caller.cmdset.delete(FireElementalCmdSet)
            caller.cmdset.delete(WaterElementalCmdSet)
            caller.cmdset.delete(AirElementalCmdSet)
        if caller.db.subguild == "fire":
            caller.cmdset.delete(EarthElementalCmdSet)
            caller.cmdset.delete(WaterElementalCmdSet)
            caller.cmdset.delete(AirElementalCmdSet)
        if caller.db.subguild == "water":
            caller.cmdset.delete(EarthElementalCmdSet)
            caller.cmdset.delete(FireElementalCmdSet)
            caller.cmdset.delete(AirElementalCmdSet)
        if caller.db.subguild == "air":
            caller.cmdset.delete(EarthElementalCmdSet)
            caller.cmdset.delete(FireElementalCmdSet)
            caller.cmdset.delete(WaterElementalCmdSet)
            
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
            caller.swap_typeclass("typeclasses.elementalguild.earth_elemental.EarthElemental", clean_attributes=False, clean_cmdsets=True)
            caller.cmdset.add(EarthElementalCmdSet, persistent=True)
            self._remove_cmdsets()
        if target == "fire":
            caller.db.subguild = "fire"
            caller.msg(f"|rYou choose {caller.db.subguild} as your permanent form.")
            caller.swap_typeclass("typeclasses.elementalguild.fire_elemental.FireElemental", clean_attributes=False, clean_cmdsets=True)
            caller.cmdset.add(FireElementalCmdSet, persistent=True)
            self._remove_cmdsets()
        if target == "water":
            caller.db.subguild = "water"
            caller.msg(f"|bYou choose {caller.db.subguild} as your permanent form.")
            caller.swap_typeclass("typeclasses.elementalguild.water_elemental.WaterElemental", clean_attributes=False, clean_cmdsets=True)
            caller.cmdset.add(WaterElementalCmdSet, persistent=True)
            self._remove_cmdsets()
        if target == "air":
            caller.db.subguild = "air"
            caller.msg(f"|wYou choose {caller.db.subguild} as your permanent form.")            
            caller.swap_typeclass("typeclasses.elementalguild.air_elemental.AirElemental", clean_attributes=False, clean_cmdsets=True)
            caller.cmdset.add(AirElementalCmdSet, persistent=True)
            self._remove_cmdsets()


class CmdTest(Command):
    key = "test"
    
    def func(self):
        caller = self.caller
        caller.msg("test")        
        # caller.cmdset.delete(ElementalCmdSet)
        # caller.cmdset.delete(ElementalCmdSet)
        # caller.cmdset.delete(ElementalCmdSet)
        # caller.cmdset.delete(ElementalCmdSet)
        # caller.cmdset.delete(ElementalCmdSet)
        
        caller.msg("done")
        

        
class ElementalCmdSet(CmdSet):
    key = "Elemental CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        # self.add(CmdDrain)
        self.add(CmdGAdvance)
        self.add(CmdGuildStatSheet)
        self.add(CmdChooseForm)
        self.add(CmdTest)
