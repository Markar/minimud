"""

Admin commands

"""

from django.conf import settings

from .command import Command
from evennia.server.models import ServerConfig
from evennia.utils import class_from_module, evtable, logger, search
from evennia import TICKER_HANDLER as tickerhandler
from evennia import CmdSet, search_tag

COMMAND_DEFAULT_CLASS = class_from_module(settings.COMMAND_DEFAULT_CLASS)

PERMISSION_HIERARCHY = [p.lower() for p in settings.PERMISSION_HIERARCHY]

# limit members for API inclusion
__all__ = (

    "CmdCheckTickers",
)

# class CmdCheckTickers(Command):
#     """
#     Choose your permanent form
#     """
    
#     key = "checktickers" 
#     locks = "cmd:perm(checktickers) or perm(Admin)"
#     help_category = "Admin"
    
#     def func(self):    
#         all = tickerhandler.all()
#         self.msg(f"all tickers: {all}")

# class CmdAddTicker(Command):
#     """
#     Choose your permanent form
#     """
    
#     key = "addticker" 
#     locks = "cmd:perm(checktickers) or perm(Admin)"
#     help_category = "Admin"
    
#     def func(self):    
#         self.caller.msg("add ticker")
#         tickerhandler.add(interval=2, callback=self.caller.at_tick, idstring="ticker1", persistent=True)

# class CmdRemoveTicker(Command):
#     """
#     Choose your permanent form
#     """
    
#     key = "removeticker" 
#     locks = "cmd:perm(removeticker) or perm(Admin)"
#     help_category = "Admin"
    
#     def func(self):    
#         self.caller.msg("remove ticker")
#         target = self.args.strip()
#         tickerhandler.remove(interval=2, callback=self.caller.at_tick, idstring=f"{target}", persistent=True)
        
# class CmdDeleteByWord(Command):
#     """
#     DELETE everything by tag
#     """
    
#     key="deletebytag"
#     locks = "cmd:perm(checktickets) or perm(Admin)"
#     help_category = "Admin"
    
#     def func(self):
#         self.msg("delete by tag")
#         objs = search_tag("chessboard")
#         print(f"objs: {objs}")
#         for tag in objs:
#             print(f"tag: {tag.key}")
            
class AdminCmdSet(CmdSet):
    key = "Admin CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        # self.add(CmdCheckTickers)
        # self.add(CmdAddTicker)
        # self.add(CmdRemoveTicker)
        # self.add(CmdDeleteByWord)
