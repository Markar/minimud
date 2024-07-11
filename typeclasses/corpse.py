
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
        self.db.desc = "a big corpse"
    