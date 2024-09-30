from typeclasses.rooms import XYGridRoom
from typeclasses.utils import SpawnMob
from evennia.contrib.grid.xyzgrid import xymap_legend


class YouTubeRoom(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()


class BadEmpanada(XYGridRoom):
    display_symbol = "M"

    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 9000, 5, 1, "BadEmpanada", "youtube")


class LoganPaul(XYGridRoom):
    display_symbol = "M"

    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 14000, 6, 1, "LoganPaul", "youtube")


class JackSepticEye(XYGridRoom):
    display_symbol = "M"

    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 10000, 6, 1, "JackSepticEye", "youtube")


class Markiplier(XYGridRoom):
    display_symbol = "M"

    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 9000, 8, 1, "Markiplier", "youtube")


class PewDiePie(XYGridRoom):
    display_symbol = "M"

    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 9500, 7, 1, "PewDiePie", "youtube")


class MrBeast(XYGridRoom):
    display_symbol = "M"

    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 15000, 9, 1, "MrBeast", "youtube")


class Ninja(XYGridRoom):
    display_symbol = "M"

    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 11000, 10, 1, "Ninja", "youtube")


class MatPat(XYGridRoom):
    display_symbol = "M"

    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 9000, 11, 1, "MatPat", "youtube")


class Wendigoon(XYGridRoom):
    display_symbol = "M"

    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 8000, 12, 1, "Wendigoon", "youtube")


class MeiMei(XYGridRoom):
    display_symbol = "M"

    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 8000, 13, 1, "MeiMei", "youtube")


class Caseoh(XYGridRoom):
    display_symbol = "M"

    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 10000, 14, 1, "Caseoh", "youtube")


class Dream(XYGridRoom):
    display_symbol = "M"

    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 10000, 15, 1, "Dream", "youtube")
