from typeclasses.rooms import XYGridRoom
from evennia.prototypes import spawner
from random import randint
import math
 
# class ChessboardMob(XYGridRoom):
#     def at_object_creation(self):
#         super().at_object_creation()

class ChessboardGnoll(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        gnolls = spawner.spawn("SCRAWNY_GNOLL")
        con = 18
        level = randint(3, 5)
        xp = level * 15
        hp = level * con

        for gnoll in gnolls:
            gnoll.location = self
            gnoll.home = self
            gnoll.db.hp = hp
            gnoll.db.hpmax = hp
            gnoll.db.exp_reward = xp
            gnoll.db.con = con
            gnoll.db.natural_weapon['damage'] = math.ceil(randint(1, 12) * level / 3)
            
            
class ChessboardGnollPup(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        gnolls = spawner.spawn("GNOLL_PUP")
        con = 20
        level = 1
        xp = level * con
        hp = level * con

        for gnoll in gnolls:
            gnoll.location = self
            gnoll.home = self
            gnoll.db.hp = hp
            gnoll.db.hpmax = hp
            gnoll.db.exp_reward = xp
            gnoll.db.con = con
            gnoll.db.natural_weapon['damage'] = math.ceil(randint(1, 12) * level / 3)
            
class ChessboardDecayingSkeleton(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        skeletons = spawner.spawn("DECAYING_SKELETON")
        con = 18
        level = 2
        xp = level * con
        hp = level * con

        for skeleton in skeletons:
            skeleton.location = self
            skeleton.home = self
            skeleton.db.hp = hp
            skeleton.db.hpmax = hp
            skeleton.db.exp_reward = xp
            skeleton.db.con = con
            skeleton.db.natural_weapon['damage'] = math.ceil(randint(1, 18) * level / 3)