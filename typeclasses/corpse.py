
import random

from evennia import CmdSet, Command, DefaultObject
from evennia.utils.utils import delay, interactive, repeat


class Corpse(DefaultObject):
    """
    A generator to spawn corpses of mobs

    """

    def at_object_creation(self):
        """
        This function is called (once) when object is created.

        """
        self.db.desc = "a corpse"
        self.db.power = 0
        
        delay(60, self.decay)
    
    def decay(self):
        """
        This function is called when the corpse decays.

        """
        self.location.msg_contents(f"The {self.key} decays and disappears.", from_obj=self)
        self.delete()
        return