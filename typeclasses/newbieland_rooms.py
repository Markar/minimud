from typeclasses.rooms import XYGridRoom
from evennia.prototypes import spawner
from random import randint
import math
 
class NewbieLargeRat(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        rats = spawner.spawn("LARGE_RAT")
        con = 18
        level = 1
        xp = level * 15
        hp = level * con

        for rat in rats:
            rat.location = self
            rat.home = self
            rat.db.hp = hp
            rat.db.hpmax = hp
            rat.db.exp_reward = xp
            rat.db.con = con
            rat.db.natural_weapon['damage'] = math.ceil(randint(1, 4))
            
            
class NewbieFirebeetle(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        beetles = spawner.spawn("FIRE_BEETLE")
        con = 16
        level = 2
        xp = level * con
        hp = level * con

        for beetle in beetles:
            beetle.location = self
            beetle.home = self
            beetle.db.hp = hp
            beetle.db.hpmax = hp
            beetle.db.exp_reward = xp
            beetle.db.con = con
            beetle.db.natural_weapon['damage'] = math.ceil(randint(1, 6))
            
class NewbieSnake(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        snakes = spawner.spawn("SNAKE")
        con = 16
        level = 1
        xp = level * con
        hp = level * con

        for snake in snakes:
            snake.location = self
            snake.home = self
            snake.db.hp = hp
            snake.db.hpmax = hp
            snake.db.exp_reward = xp
            snake.db.con = con
            snake.db.natural_weapon['damage'] = math.ceil(randint(1, 4))