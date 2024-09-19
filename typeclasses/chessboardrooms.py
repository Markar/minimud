from typeclasses.rooms import XYGridRoom
from typeclasses.utils import SpawnMob


class ChessboardGnoll(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 600, 5, 1, "SCRAWNY_GNOLL", "chessboard")


class ChessboardGnollPup(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 400, 3, 1, "GNOLL_PUP", "chessboard")


class ChessboardDecayingSkeleton(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        SpawnMob(self, 400, 3, 1, "DECAYING_SKELETON", "chessboard")
