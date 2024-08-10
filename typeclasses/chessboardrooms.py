from typeclasses.rooms import XYGridRoom
from evennia.prototypes import spawner
from random import randint, uniform
import math

class ChessboardGnoll(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        gnolls = spawner.spawn("SCRAWNY_GNOLL")
        self.tags.add("room", category="chessboard")
        con = 18
        level = randint(5, 7)
        xp = level * con
        hp = level * con

        for gnoll in gnolls:
            gnoll.tags.add("mob", category="chessboard")
            gnoll.location = self
            gnoll.home = self
            gnoll.db.hp = hp
            gnoll.db.hpmax = hp
            gnoll.db.exp_reward = xp
            gnoll.db.con = con
            gnoll.db.natural_weapon['damage'] = math.ceil(randint(level, level*2))
            
            
class ChessboardGnollPup(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        gnolls = spawner.spawn("GNOLL_PUP")
        self.tags.add("room", category="chessboard")
        con = 20
        level = 2
        xp = level * con
        hp = level * con

        for gnoll in gnolls:
            gnoll.tags.add("mob", category="chessboard")
            gnoll.location = self
            gnoll.home = self
            gnoll.db.hp = hp
            gnoll.db.hpmax = hp
            gnoll.db.exp_reward = xp
            gnoll.db.con = con
            gnoll.db.natural_weapon['damage'] = math.ceil(randint(6, 8) )
            
class ChessboardDecayingSkeleton(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        skeletons = spawner.spawn("DECAYING_SKELETON")
        self.tags.add("room", category="chessboard")
        con = 18
        level = 2
        xp = level * con
        hp = level * con

        for skeleton in skeletons:
            skeleton.tags.add("mob", category="chessboard")
            skeleton.location = self
            skeleton.home = self
            skeleton.db.hp = hp
            skeleton.db.hpmax = hp
            skeleton.db.exp_reward = xp
            skeleton.db.con = con
            skeleton.db.natural_weapon['damage'] = math.ceil(randint(6, 8) )