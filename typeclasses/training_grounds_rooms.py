from evennia.prototypes import spawner
from typeclasses.rooms import XYGridRoom
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
            
class NewbieGoblin(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        goblins = spawner.spawn("NOVICE_GOBLIN")
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
            
      
class NewbieRogueApprentice(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        rogues = spawner.spawn("ROGUE_APPRENTICE")
        con = 16
        level = 1
        xp = level * con
        hp = level * con

        for rogue in rogues:
            rogue.location = self
            rogue.home = self
            rogue.db.hp = hp
            rogue.db.hpmax = hp
            rogue.db.exp_reward = xp
            rogue.db.con = con
            
class NewbieSkeletalWarrior(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        skeletons = spawner.spawn("SKELETAL_WARRIOR")
        con = 16
        level = 10
        xp = level * con
        hp = level * con

        for skeleton in skeletons:
            skeleton.location = self
            skeleton.home = self
            skeleton.db.hp = hp
            skeleton.db.hpmax = hp
            skeleton.db.exp_reward = xp
            skeleton.db.con = con

class NewbieNoviceMage(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        mages = spawner.spawn("NOVICE_MAGE")
        con = 16
        level = 6
        xp = level * con
        hp = level * con

        for mage in mages:
            mage.location = self
            mage.home = self
            mage.db.hp = hp
            mage.db.hpmax = hp
            mage.db.exp_reward = xp
            mage.db.con = con
            
class MalfunctioningRobot(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        robots = spawner.spawn("MALFUNCTIONING_ROBOT")
        con = 16
        level = 6
        xp = level * con
        hp = level * con

        for robot in robots:
            robot.location = self
            robot.home = self
            robot.db.hp = hp
            robot.db.hpmax = hp
            robot.db.exp_reward = xp
            robot.db.con = con
            
class CyberSoldier(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        soldiers = spawner.spawn("CYBER_SOLDIER")
        con = 16
        level = 10
        xp = level * con
        hp = level * con

        for soldier in soldiers:
            soldier.location = self
            soldier.home = self
            soldier.db.hp = hp
            soldier.db.hpmax = hp
            soldier.db.exp_reward = xp
            soldier.db.con = con
            
            
class AlienScout(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        scouts = spawner.spawn("ALIEN_SCOUT")
        con = 16
        level = 8
        xp = level * con
        hp = level * con

        for scout in scouts:
            scout.location = self
            scout.home = self
            scout.db.hp = hp
            scout.db.hpmax = hp
            scout.db.exp_reward = xp
            scout.db.con = con