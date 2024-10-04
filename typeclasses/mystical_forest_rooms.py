from typeclasses.rooms import XYGridRoom
from typeclasses.utils import SpawnMob


class LargeRat(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 50, 1, 1, "LARGE_RAT", "mystical_forest")


class Firebeetle(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 150, 2, 1, "FIRE_BEETLE", "mystical_forest")


class MossSnake(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 60, 1, 1, "MOSS_SNAKE", "mystical_forest")


class GoblinScout(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 130, 2, 1, "GOBLIN_SCOUT", "mystical_forest")


class DecayingSkeleton(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 80, 1, 1, "DECAYING_SKELETON", "mystical_forest")
