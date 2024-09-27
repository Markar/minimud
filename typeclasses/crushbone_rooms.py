from evennia.prototypes import spawner
from typeclasses.rooms import XYGridRoom
from typeclasses.utils import SpawnMob
from random import randint, uniform
import math


class OrcPawn(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 3500, 6, 2, "ORC_PAWN", "crushbone")


class OrcCenturion(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 5750, 10, 2, "ORC_CENTURION", "crushbone")


class OrcLegionnaire(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 11250, 15, 3, "ORC_LEGIONNAIRE", "crushbone")


class OrcSlaver(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 8100, 11, 2, "ORC_SLAVER", "crushbone")


class OrcOracle(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 9800, 10, 1, "ORC_ORACLE", "crushbone")


class OrcEmissary(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 12150, 12, 2, "ORC_EMISSARY", "crushbone")


class OrcRoyalGuard(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 13820, 15, 2, "ORC_ROYAL_GUARD", "crushbone")


class OrcTaskmaster(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 9200, 12, 2, "ORC_TASKMASTER", "crushbone")


class OrcTrainer(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        if randint(0, 1) > 0.25:
            SpawnMob(self, 11562, 13, 1, "ORC_TRAINER", "crushbone")
            return
        SpawnMob(self, 9200, 12, 2, "ORC_TASKMASTER", "crushbone")


class OrcWarlord(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 15200, 15, 2, "ORC_WARLORD", "crushbone")


class OrcLord(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 18300, 18, 2, "ORC_LORD", "crushbone")


class OrcEmperor(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 20000, 20, 2, "ORC_EMPEROR", "crushbone")
