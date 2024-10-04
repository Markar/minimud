from evennia.prototypes import spawner
from typeclasses.rooms import XYGridRoom
from typeclasses.utils import SpawnMob
from random import randint, uniform
import math


class OrcPawn(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 8000, 8, 2, "ORC_PAWN", "crushbone")


class OrcCenturion(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 11750, 12, 2, "ORC_CENTURION", "crushbone")


class OrcLegionnaire(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 22250, 22, 3, "ORC_LEGIONNAIRE", "crushbone")


class OrcSlaver(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 16300, 16, 2, "ORC_SLAVER", "crushbone")


class OrcOracle(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 19800, 20, 1, "ORC_ORACLE", "crushbone")


class LordDarish(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 25000, 25, 2, "LORD_DARISH", "crushbone")


class OrcEmissary(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 28150, 28, 2, "ORC_EMISSARY", "crushbone")


class OrcRoyalGuard(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 30820, 30, 2, "ORC_ROYAL_GUARD", "crushbone")


class OrcTaskmaster(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 16200, 16, 2, "ORC_TASKMASTER", "crushbone")


class OrcTrainer(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        if randint(0, 1) > 0.25:
            SpawnMob(self, 21562, 21, 1, "ORC_TRAINER", "crushbone")
            return
        SpawnMob(self, 17200, 17, 2, "ORC_TASKMASTER", "crushbone")


class OrcWarlord(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 25200, 25, 2, "ORC_WARLORD", "crushbone")


class OrcLord(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 28300, 28, 2, "ORC_LORD", "crushbone")


class OrcEmperor(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 35000, 35, 3, "ORC_EMPEROR", "crushbone")
