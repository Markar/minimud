from evennia.prototypes import spawner
from typeclasses.rooms import XYGridRoom
from random import randint
import math
 
class LargeRat(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        rats = spawner.spawn("LARGE_RAT")
        con = 16
        level = 3
        xp = level * 15
        hp = level * con

        for rat in rats:
            rat.location = self
            rat.home = self
            rat.db.hp = hp
            rat.db.hpmax = hp
            rat.db.exp_reward = xp
            rat.db.con = con
            
            
class Firebeetle(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        beetles = spawner.spawn("FIRE_BEETLE")
        con = 16
        level = 4
        xp = level * con
        hp = level * con

        for beetle in beetles:
            beetle.location = self
            beetle.home = self
            beetle.db.hp = hp
            beetle.db.hpmax = hp
            beetle.db.exp_reward = xp
            beetle.db.con = con
            
class MossSnake(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        snakes = spawner.spawn("MOSS_SNAKE")
        con = 16
        level = 2
        xp = level * con
        hp = level * con

        for snake in snakes:
            snake.location = self
            snake.home = self
            snake.db.hp = hp
            snake.db.hpmax = hp
            snake.db.exp_reward = xp
            snake.db.con = con
            
class GoblinScout(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        goblins = spawner.spawn("GOBLIN_SCOUT")
        con = 16
        level = 5
        xp = level * con
        hp = level * con

        for goblin in goblins:
            goblin.location = self
            goblin.home = self
            goblin.db.hp = hp
            goblin.db.hpmax = hp
            goblin.db.exp_reward = xp
            goblin.db.con = con
            
      
class DecayingSkeleton(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        rogues = spawner.spawn("DECAYING_SKELETON")
        con = 16
        level = 3
        xp = level * con
        hp = level * con

        for rogue in rogues:
            rogue.location = self
            rogue.home = self
            rogue.db.hp = hp
            rogue.db.hpmax = hp
            rogue.db.exp_reward = xp
            rogue.db.con = con
            
