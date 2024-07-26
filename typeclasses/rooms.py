"""
Room

Rooms are simple containers that has no location of their own.

"""
from evennia import search_object
from evennia.utils import create, iter_to_str, logger, delay
from evennia.objects.objects import DefaultRoom
from evennia.contrib.grid.xyzgrid.xyzroom import XYZRoom
from evennia.contrib.grid.wilderness.wilderness import WildernessRoom
from evennia.prototypes import spawner
from random import randint
import math
from .objects import ObjectParent
from .scripts import RestockScript

from commands.shops import ShopCmdSet
from commands.skills import TrainCmdSet

class RoomParent(ObjectParent):
    """
    A mixin for logic that should be applied to all rooms.
    """

    def at_object_receive(self, mover, source_location, move_type=None, **kwargs):
        """
        Apply extra hooks when an object enters this room, so things (e.g. NPCs) can react.
        """
        super().at_object_receive(mover, source_location, **kwargs)
        # only react if the arriving object is a character
        if "character" in mover._content_types:
            for obj in self.contents_get(content_type="character"):
                if obj == mover:
                    # don't react to ourself
                    continue
                obj.at_character_arrive(mover, **kwargs)

    def at_object_leave(self, mover, destination, **kwargs):
        """
        Apply extra hooks when an object enters this room, so things (e.g. NPCs) can react.
        """
        super().at_object_leave(mover, destination, **kwargs)
        if combat := self.scripts.get("combat"):
            combat = combat[0]
            combat.remove_combatant(mover)
        # only react if the arriving object is a character
        if "character" in mover._content_types:
            for obj in self.contents_get(content_type="character"):
                if obj == mover:
                    # don't react to ourself
                    continue
                obj.at_character_depart(mover, destination, **kwargs)

    def get_display_footer(self, looker, **kwargs):
        """
        Shows a list of commands available here to the viewer.
        """

        cmd_keys = [
            f"|w{cmd.key}|n"
            for cmdset in self.cmdset.all()
            for cmd in cmdset
            if cmd.access(looker, "cmd")
        ]
        if cmd_keys:
            return f"Special commands here: {', '.join(cmd_keys)}"
        else:
            return ""


class Room(RoomParent, DefaultRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """

    pass


class OverworldRoom(RoomParent, WildernessRoom):
    """
    A subclass of the Wilderness contrib's room, applying the local RoomParent mixin
    """

    def get_display_header(self, looker, **kwargs):
        """
        Displays a minimap above the room description, if there is one.
        """
        if not self.ndb.minimap:
            self.ndb.minimap = self.db.minimap
        return self.ndb.minimap or ""

    def at_server_reload(self, **kwargs):
        """
        Saves the current ndb desc to db so it's still available after a reload
        """
        self.db.desc = self.ndb.active_desc
        self.db.minimap = self.ndb.minimap


class XYGridRoom(RoomParent, XYZRoom):
    """
    A subclass of the XYZGrid contrib's room, applying the local RoomParent mixin
    """

    pass        

class XYGridShop(XYGridRoom):
    """
    A grid-aware room that has built-in shop-related functionality.
    """

    def at_object_creation(self):
        """
        Initialize the shop inventory and commands
        """
        super().at_object_creation()
        # add the shopping commands to the room
        self.cmdset.add(ShopCmdSet, persistent=True)
        # create an invisible, inaccessible storage object
        self.db.storage = create.object(
            key="shop storage",
            locks="view:perm(Builder);get:perm(Builder);search:perm(Builder)",
            home=self,
            location=self,
        )
        self.scripts.add(RestockScript, key="restock", autostart=False)

    def add_stock(self, obj):
        """
        Adds new objects to the shop's sale stock
        """
        if storage := self.db.storage:
            # only do this if there's a storage location set
            obj.location = storage
            # price is double the sale value
            val = obj.db.value or 0
            obj.db.price = val * 2
            return True
        else:
            return False


class XYGridTrain(XYGridRoom):
    """
    A grid-aware room that has built-in shop-related functionality.
    """

    def at_object_creation(self):
        """
        Initialize the shop inventory and commands
        """
        super().at_object_creation()
        # add the shopping commands to the room
        self.cmdset.add(TrainCmdSet, persistent=True)


class XYZShopNTrain(XYGridTrain, XYGridShop):
    """
    A room where you can train AND shop!
    """

    pass


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