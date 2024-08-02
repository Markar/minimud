from random import choice, randint
from evennia import CmdSet, search_tag
from evennia.utils import iter_to_str
from evennia.utils.evtable import EvTable
from evennia import TICKER_HANDLER as tickerhandler
from evennia import logger


import math 
from .command import Command

def get_article(word):
    vowels = "aeiou"
    return "an" if word[0].lower() in vowels else "a"

SKILLS_COST = {
    1800,
    9016,
    25297,
    54353,
    99978,
    166074,
    256675,
    375971,
    528332,
    718332,
    950773,
    1230709,
    1563470,
    1954686,
    2410311,
    2936647,
    3540368,
    4228544,
    5008665,
    5888665,
    6876946,
    7982402,
    9214443,
    10583019,
    12098644
}

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
SKILL_RANKS = {
    0: "Very poor",
    1: "Poor",
    2: "Below average",
    3: "Average",
    4: "Above average",
    5: "Moderate",
    6: "Good",
    7: "Very good",
    8: "High",
    9: "Very high",
    10: "Excellent",
    12: "Exceptional",
    14: "Masterful",
    16: "Supreme",
    17: "God-like"
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
        caller.msg(f"caller: {caller.db.ep}")
        form = self.args.strip().lower()
        try:
            my_glvl = caller.db.guild_level
            caller.db.ep -= my_glvl
            caller.addhp(my_glvl)
            
            form_title = form.title()
            if form == "human":
                print(f"form = human and {caller.db.guild_level}")
                self.msg(f"|rYou morph back into your human form!")
                caller.db.form = "Human"
                return
            if form == "slime":
                self.msg(f"|rYou morph back into your slime form!")
                caller.db.form = "Slime"
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
                
            avian = next((key for key, value in AVIAN_FORMS.items() if value == form), -1)
            if not avian == -1 and my_glvl >= avian:
                self.msg(f"|rYou morph into {get_article(form)} {form_title}!")
                caller.db.form = form_title
                return
                
            self.msg(f"|rYou can't morph into that.")
        except ValueError:
            print(f"You don't know how to use that form.")

class CmdEnergyControl(Command):
    """
    Energy Control enhances your physical resists while lowering others

    Usage:
        energy control
    """

    key = "energy control"
    aliases = ("ec")
    help_category = "Changeling"

    def func(self):
        print(self.caller)
        caller = self.caller
        caller.use_energy_control()

# class CmdDisableEnergyControl(Command):
#     """
#     Reactive armor enhances your physical resists while lowering others

#     Usage:
#         enable energy control
#         disable energy control
#     """

#     key = "disable energy control"
#     help_category = "Changeling"

#     def func(self):
#         print(self.caller)
#         caller = self.caller
#         caller.db.energy_control = False
#         caller.db.edgedac -= caller.db.guild_level
#         caller.db.bluntac -= caller.db.guild_level
#         caller.msg(f"|CYou release your control over energy.")
        
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
        engulf
    """
    key = "engulf"
    help_category = "changeling"

    def func(self):
        print(self.caller)
        caller = self.caller
        target = self.args
        location = caller.location
        
        if combat_script := location.scripts.get("combat"):
            combat_script = combat_script[0]
            combat_script.add_combatant(self, enemy=target)
        else:
            self.msg(f"|YYou are not in combat.")
            return
        target = caller.search(target)
        # if not target:
        #     target = caller.search(target)
        print(f"target: {target}")
        caller.db.combat_target = target
        caller.use_engulf(target)
        
class CmdForms(Command):
    """
    List of forms
    
    Usage:
    forms
    forms <form>, - forms hummingbird
    """
    
    key="forms"
    help_category = "Changeling"
        
    def func(self):
        caller = self.caller
        form = self.args.strip().lower()
        
        if form in REPTILE_FORMS.values() or form in MAMMAL_FORMS.values() or form in AVIAN_FORMS.values():
            form_desc = caller.get_form_help(form)
            caller.msg(f"|G{form_desc}")
            return
        
        my_glvl = caller.db.guild_level
                    
        table = EvTable(f"|cAvian", f"|cMammal", f"|cReptile", f"|cGlvl", border="table")
        for glvl in REPTILE_FORMS:
            if my_glvl >= glvl:
                table.add_row(f"|Y{AVIAN_FORMS[glvl]}", f"|Y{MAMMAL_FORMS[glvl]}", f"|Y{REPTILE_FORMS[glvl]}", glvl)
            else:
                table.add_row(f"|G{AVIAN_FORMS[glvl]}", f"|G{MAMMAL_FORMS[glvl]}", f"|G{REPTILE_FORMS[glvl]}", glvl)
        table.add_row("", "", "", "")
        table.add_row(f"|Yslime", f"|Yhuman", "", 1)
        
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
        cost = GUILD_LEVEL_COST_DICT.get(caller.db.guild_level+1, 0)
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
        title = caller.db.title
        alignment = caller.db.alignment
        my_glvl = caller.db.guild_level or 1
        gxp = caller.db.gxp or 0
        form = caller.db.form or "none"                
        gxp_needed = GUILD_LEVEL_COST_DICT[my_glvl+1]
        ec = caller.db.energy_control or "none"
        if ec:
            ecActive = "Active"
        else:
            ecActive = "Inactive"
        engulfs = caller.db.engulfs or 0
        engulfMax = caller.db.max_engulfs or 0
        
        table = EvTable(f"|c{caller} {title} ({alignment})", border="table")
        table.add_row(f"|GGuild Level: {my_glvl}")
        table.add_row(f"|GGXP: {gxp} / {gxp_needed}")
        table.add_row(f"|GEngulfs: {engulfs} / {engulfMax}")
        table.add_row(f"|GForm: {form}")
        table.add_row(f"|GEnergy Control: {ecActive}")
        
        skill_table = EvTable(f"|cSkills", border="table")
        body_control = getattr(caller.db.skills, "body_control", 0)
        drain = getattr(caller.db.skills, "drain", 0)
        energy_control = getattr(caller.db.skills, "energy_control", 0)
        familiar = getattr(caller.db.skills, "familiar", 0)
        regeneration = getattr(caller.db.skills, "regeneration", 0)
        vibrate = getattr(caller.db.skills, "vibrate", 0)
        
        skill_table.add_row(f"|GBody Control", f"|Y{SKILL_RANKS[body_control]}")
        skill_table.add_row(f"|GDrain", f"|Y{SKILL_RANKS[drain]}")
        skill_table.add_row(f"|GEnergy Control", f"|Y{SKILL_RANKS[energy_control]}")
        skill_table.add_row(f"|GFamiliar", f"|Y{SKILL_RANKS[familiar]}")
        skill_table.add_row(f"|GRegeneration", f"|Y{SKILL_RANKS[regeneration]}")
        skill_table.add_row(f"|GVibrate", f"|Y{SKILL_RANKS[vibrate]}")
        
        caller.msg(str(table))
        caller.msg(str(skill_table))
    
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
            caller.db.guild = "adventurer"
            caller.db.guild_level = 1
            caller.db.gxp = 0
            caller.db.subguild = "none"
            caller.db.form = "none"
            # clear powers if they're enabled so we don't end up with negative stats
            if caller.db.energy_control:
                caller.use_energy_control()
            
            try:
                tickerhandler.remove(interval=6, callback=caller.at_tick, idstring=f"{caller}-regen", persistent=True)
                tickerhandler.remove(interval=60*5, callback=caller.at_engulf_tick, idstring=f"{caller}-superpower", persistent=True)
            except ValueError:
                print(f"tickerhandler.remove failed")
            
            caller.cmdset.delete(ChangelingCmdSet)
            caller.swap_typeclass("typeclasses.characters.PlayerCharacter")
            caller.msg(f"|rYou leave the Changeling guild")
        else:
            caller.msg(f"|rYou are already an adventurer")

class CmdKickstart(Command):
    key = "kickstart"
    
    def func(self):
        caller = self.caller
        caller.kickstart()
            
class CmdAbsorb(Command):
    """
    The corpse of a freshly slain enemy is a rich source of cellular
    material, which can easily be absorbed and converted into protoplasm
    and stamina, serving to replenish some, or all that you may have lost.

    If you so choose, you may also 'fully' absorb the corpse, leaving
    nothing left to decay.
    """
    
    key = "absorb" 
    
    def func(self):
        if not self.args:
            target = self.caller
            self.msg(f"target {target}")
            if corpse := target.location.search("corpse-1"):
                ep = target.db.ep
                epmax = target.db.epmax
                power = corpse.db.power
                
                if ep + power > epmax:
                    target.db.ep = epmax
                else:
                    target.db.ep += max(power, 0)
                corpse.delete()
                self.msg(f"|yYou absorb the corpse and feel its inner power flow through you.")
            
class CmdCellularReconstruction(Command):
    """
    The Changeling's ability to regenerate is a powerful one, but it
    is not without its limits.  The Changeling can regenerate lost
    cells, but it takes time and energy to do so.  The Changeling
    can regenerate up to 10% of their maximum health every 6 seconds.
    
    Usage:
        cellular reconstruction
        cr
        recon
    """
    
    key = "cellular reconstruction"
    aliases = ("cr", "recon")
    cost = 25
    guild_level = 9
    
    def func(self):
        caller = self.caller
        gl = caller.db.guild_level
        if gl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return
        if caller.db.ep < self.cost:
            self.msg(f"|rYou don't have enough energy to use this power.")
            return
        
        regen = caller.db.skills["regeneration"]
        to_heal = math.floor(30 + gl/2 + randint(0, caller.db.wisdom) + regen)

        caller.addhp(to_heal)
        caller.db.ep -= self.cost
        caller.msg(f"|yYou concentrate on your cells and new ones begin to grow and form.")
   
class CmdCellularRegrowth(Command):
    """
    The Changeling's ability to regenerate is a powerful one, but it
    is not without its limits.  The Changeling can regenerate lost
    cells, but it takes time and energy to do so.  The Changeling
    can regenerate up to 10% of their maximum health every 6 seconds.
    This power costs 25 energy points to use and then additional energy
    to sustain the regeneration.
    
    Usage:
        cellular regrowth
    """
    
    key = "cellular regrowth"
    cost = 25
    guild_level = 3
    
    def func(self):
        caller = self.caller
        gl = caller.db.guild_level
        if gl < self.guild_level:
            self.msg(f"|rYou must be at least {self.guild_level} to use this power.")
            return
        if caller.db.ep < self.cost:
            self.msg(f"|rYou don't have enough energy to use this power.")
            return
        
        regen = caller.db.skills["regeneration"]
        to_heal = math.floor(5 + regen/2 + randint(0, regen/2) + gl/8 + randint(0, gl/8))
        to_drain = math.floor(to_heal/3)
        
        # cost to activate
        caller.db.ep -= self.cost
        # set up the regen
        caller.db.regrowth_rate += to_heal
        caller.db.regrowth_cost -= to_drain
        
        caller.msg(f"|yYou begin to reconstruct your lost cells.")
        
class CmdExperiment(Command):
    """
    Advance a level or attribute by spending experience points.

    Enter "experiment" to see what you can learn.

    Usage:
        experiment

    Example:
        experiment body_control
    """

    key = "experiment"
     
    def func(self):
        caller = self.caller
        try:
            skill = self.args.strip().lower()
            list = ["body_control", "drain", "energy_control", "familiar", "regeneration", "vibrate"]
            
            if skill == "":
                self.msg(f"|gWhat would you like to experiment with?")
                return
            
            if skill not in list:
                caller.msg(f"|gYou can't study that.")
                return

            current_skill = getattr(caller.db.skills, skill, 0)
            cost = SKILLS_COST[current_skill+1]
            if caller.db.skillxp < cost:
                self.msg(f"|wYou need {cost-caller.db.skillxp} more experience to advance your level.")
                return
            
            confirm = yield (
                f"It will cost you {cost} experience to advance your level. Confirm? Yes/No"
            )
            if confirm.lower() not in (
                "yes",
                "y",
            ):
                self.msg("Cancelled.")
                return
            caller.db.skillxp -= cost
            setattr(caller.db.skills, skill, current_skill+1)
            caller.msg(f"You grow more powerful ({skill} {current_skill+1})")
            
        except ValueError:
            self.msg("Usage: enhance <body_control>")
            return   
class CmdTest(Command):
    key = "test"
    
    def func(self):
        # msg = self.caller.get_hit_message(self.caller, 4, "fart")
        # print(f"in test: {msg}")
        # self.caller.location.key = "Millennium Square"
        self.caller.cmdset.delete(ChangelingCmdSet)
        
class ChangelingCmdSet(CmdSet):
    key = "Changeling CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        self.add(CmdAbsorb)
        self.add(CmdGAdvance)
        self.add(CmdGuildStatSheet)
        self.add(CmdMorph)
        self.add(CmdEnergyControl)
        self.add(CmdEngulf)
        self.add(CmdForms)
        self.add(CmdTest)
        self.add(CmdKickstart)
        self.add(CmdCellularReconstruction)
        self.add(CmdCellularRegrowth)
        self.add(CmdExperiment)

