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
        self.db.weight = 50

        delay(60, self.decay, persistent=True)

    def decay(self):
        """
        This function is called when the corpse decays.

        """
        if self and self.location:
            self.location.msg_contents(
                f"The {self.key} decays and disappears.", from_obj=self
            )
            self.delete()
        return


class Capsule(DefaultObject):
    """
    A generator to spawn corpses of mobs

    """

    def at_object_creation(self):
        """
        This function is called (once) when object is created.

        """
        self.db.desc = "a glowing capsule, it looks like it could be eaten"
        self.db.power = 0
        self.db.weight = 10

        delay(600, self.decay, persistent=True)

    def decay(self):
        """
        This function is called when the corpse decays.

        """
        if self:
            self.location.msg_contents(
                f"The {self.key} loses power and fades away.", from_obj=self
            )
            self.delete()
        return
