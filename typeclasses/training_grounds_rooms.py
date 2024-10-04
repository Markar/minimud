from typeclasses.rooms import XYGridRoom
from typeclasses.utils import SpawnMob


class NewbieGoblin(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 2800, 8, 1, "NOVICE_GOBLIN", "training_grounds")


class NewbieRogueApprentice(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 3000, 8, 1, "ROGUE_APPRENTICE", "training_grounds")


class NewbieSkeletalWarrior(XYGridRoom):
    def at_object_creation(self):
        SpawnMob(self, 4200, 10, 1, "SKELETAL_WARRIOR", "training_grounds")


class NewbieNoviceMage(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 3200, 10, 1, "NOVICE_MAGE", "training_grounds")


class MalfunctioningRobot(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 5000, 10, 2, "MALFUNCTIONING_ROBOT", "training_grounds")


class CyberSoldier(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 5500, 11, 2, "CYBER_SOLDIER", "training_grounds")


class AlienScout(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 4800, 10, 2, "ALIEN_SCOUT", "training_grounds")
