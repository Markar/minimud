from evennia.prototypes import spawner
from typeclasses.rooms import XYGridRoom
from random import randint, uniform
import math
 
class LargeRat(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        rats = spawner.spawn("LARGE_RAT")
        self.tags.add("room", category="mystical_forest")
        con = 16
        level = randint(4, 6)
        xp = level * con
        hp = level * con

        for rat in rats:
            rat.tags.add("mob", category="mystical_forest")
            rat.location = self
            rat.home = self
            rat.db.hp = hp
            rat.db.hpmax = hp
            rat.db.exp_reward = xp
            rat.db.con = con
            rat.db.level = level
            rat.db.natural_weapon['damage'] = math.ceil(randint(level, level*2))
            # rat.db.natural_weapon['hits'] = 2
            
            
class Firebeetle(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        beetles = spawner.spawn("FIRE_BEETLE")
        self.tags.add("room", category="mystical_forest")
        con = 16
        level = randint(6, 9)
        xp = level * con
        hp = level * con

        for beetle in beetles:
            beetle.tags.add("mob", category="mystical_forest")
            beetle.location = self
            beetle.home = self
            beetle.db.hp = hp
            beetle.db.hpmax = hp
            beetle.db.exp_reward = xp
            beetle.db.con = con
            beetle.db.natural_weapon['damage'] = math.ceil(randint(level, level*2))
            
class MossSnake(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        snakes = spawner.spawn("MOSS_SNAKE")
        self.tags.add("room", category="mystical_forest")
        con = 16
        level = randint(3, 4)
        xp = level * con
        hp = level * con

        for snake in snakes:
            snake.tags.add("mob", category="mystical_forest")
            snake.location = self
            snake.home = self
            snake.db.hp = hp
            snake.db.hpmax = hp
            snake.db.exp_reward = xp
            snake.db.con = con
            snake.db.natural_weapon['damage'] = math.ceil(randint(level, level*2))
            
class GoblinScout(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        goblins = spawner.spawn("GOBLIN_SCOUT")
        self.tags.add("room", category="mystical_forest")
        con = 16
        level = randint(5, 7)
        xp = level * con
        hp = level * con

        for goblin in goblins:
            goblin.tags.add("mob", category="mystical_forest")
            goblin.location = self
            goblin.home = self
            goblin.db.hp = hp
            goblin.db.hpmax = hp
            goblin.db.exp_reward = xp
            goblin.db.con = con
            goblin.db.natural_weapon['damage'] = math.ceil(randint(level, level*2))
            
      
class DecayingSkeleton(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        skeletons = spawner.spawn("DECAYING_SKELETON")
        self.tags.add("room", category="mystical_forest")
        con = 16
        level = 3
        hp = level * con
        dmg = math.ceil(randint(level, level*2))
        xp = level * con + dmg

        for skeleton in skeletons:
            skeleton.tags.add("mob", category="mystical_forest")
            skeleton.location = self
            skeleton.home = self
            skeleton.db.hp = hp
            skeleton.db.hpmax = hp
            skeleton.db.exp_reward = xp
            skeleton.db.con = con
            skeleton.db.natural_weapon['damage'] = dmg
            
