from evennia.prototypes import spawner
from typeclasses.rooms import XYGridRoom
from random import randint, uniform

class NewbieGoblin(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        goblins = spawner.spawn("NOVICE_GOBLIN")
        self.tags.add("room", category="training_grounds")
        con = 16
        level = randint(7, 9)
        xp = level * con
        hp = level * con

        for goblin in goblins:
            goblin.tags.add("mob", category="training_grounds")
            goblin.location = self
            goblin.home = self
            goblin.db.hp = hp
            goblin.db.hpmax = hp
            goblin.db.exp_reward = xp
            goblin.db.con = con
            goblin.db.natural_weapon['damage'] = randint(level, level*2)
            
      
class NewbieRogueApprentice(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        rogues = spawner.spawn("ROGUE_APPRENTICE")
        self.tags.add("room", category="training_grounds")
        con = 16
        level = randint(8, 10)
        xp = level * con
        hp = level * con

        for rogue in rogues:
            rogue.tags.add("mob", category="training_grounds")
            rogue.location = self
            rogue.home = self
            rogue.db.hp = hp
            rogue.db.hpmax = hp
            rogue.db.exp_reward = xp
            rogue.db.con = con
            rogue.db.natural_weapon['damage'] = randint(level, level*2)
            
class NewbieSkeletalWarrior(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        skeletons = spawner.spawn("SKELETAL_WARRIOR")
        self.tags.add("room", category="training_grounds")
        con = 16
        level = randint(13, 16)
        xp = level * con
        hp = level * con

        for skeleton in skeletons:
            skeleton.tags.add("mob", category="training_grounds")
            skeleton.location = self
            skeleton.home = self
            skeleton.db.hp = hp
            skeleton.db.hpmax = hp
            skeleton.db.exp_reward = xp
            skeleton.db.con = con
            skeleton.db.natural_weapon['damage'] = randint(level, level*2)

class NewbieNoviceMage(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        mages = spawner.spawn("NOVICE_MAGE")
        self.tags.add("room", category="training_grounds")
        con = 16
        level = randint(9, 12)
        xp = level * con
        hp = level * con

        for mage in mages:
            mage.tags.add("mob", category="training_grounds")
            mage.location = self
            mage.home = self
            mage.db.hp = hp
            mage.db.hpmax = hp
            mage.db.exp_reward = xp
            mage.db.con = con
            mage.db.natural_weapon['damage'] = 10
            mage.db.natural_weapon['damage'] = randint(level, level*2)
            
class MalfunctioningRobot(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        robots = spawner.spawn("MALFUNCTIONING_ROBOT")
        self.tags.add("room", category="training_grounds")
        con = 16
        level = randint(14, 17)
        xp = level * con
        hp = level * con

        for robot in robots:
            robot.tags.add("mob", category="training_grounds")
            robot.location = self
            robot.home = self
            robot.db.hp = hp
            robot.db.hpmax = hp
            robot.db.exp_reward = xp
            robot.db.con = con
            robot.db.natural_weapon['damage'] = randint(level, level*2)
            
class CyberSoldier(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        soldiers = spawner.spawn("CYBER_SOLDIER")
        self.tags.add("room", category="training_grounds")
        con = 16
        level = randint(17, 20)
        xp = level * con
        hp = level * con

        for soldier in soldiers:
            soldier.tags.add("mob", category="training_grounds")
            soldier.location = self
            soldier.home = self
            soldier.db.hp = hp
            soldier.db.hpmax = hp
            soldier.db.exp_reward = xp
            soldier.db.con = con
            soldier.db.natural_weapon['damage'] = randint(level, level*2)
            
            
class AlienScout(XYGridRoom):
    def at_object_creation(self):
        super().at_object_creation()
        scouts = spawner.spawn("ALIEN_SCOUT")
        self.tags.add("room", category="training_grounds")
        con = 16
        level = randint(18, 22)
        xp = level * con
        hp = level * con

        for scout in scouts:
            scout.tags.add("mob", category="training_grounds")
            scout.location = self
            scout.home = self
            scout.db.hp = hp
            scout.db.hpmax = hp
            scout.db.exp_reward = xp
            scout.db.con = con
            scout.db.natural_weapon['damage'] = randint(level, level*2)