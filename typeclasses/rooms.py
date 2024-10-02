"""
Room

Rooms are simple containers that has no location of their own.

"""

from evennia.utils import create
from evennia.objects.objects import DefaultRoom
from evennia.contrib.grid.xyzgrid.xyzroom import XYZRoom
from evennia.contrib.grid.wilderness.wilderness import WildernessRoom
from evennia import CmdSet
from .objects import ObjectParent
from .scripts import RestockScript

from commands.shops import ShopCmdSet
from commands.skills import TrainCmdSet

from commands.elemental_cmds import CmdJoinElementals
from commands.elemental_cmds import CmdLeaveElementals
from commands.changeling_cmds import CmdJoinChangelings
from commands.changeling_cmds import CmdLeaveChangelings
from typeclasses.cybercorpsguild.rooms.room_commands import (
    CmdJoinCybercorps,
    CmdLeaveCybercorps,
    CybercorpsWaresRoomCmdSet,
    CybercorpsImplantsRoomCmdSet,
)
from typeclasses.warriorsguild.rooms.room_commands import (
    CmdJoinWarriors,
    CmdLeaveWarriors,
)


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

    def format_appearance(self, appearance, looker, **kwargs):
        """Don't left-strip the appearance string"""
        return appearance.rstrip()


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


class NexusBazaar(Room):
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

        self.db.inventory = [
            ("IRON_CHAUSSES", 3),
            ("IRON_HAUBERK", 3),
            ("LEATHER_BOOTS", 3),
        ]
        self.scripts.add(RestockScript, key="restock", autostart=True)

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


class ElementalRoomCmdSet(CmdSet):
    key = "elemental_room"
    priority = 1

    def at_cmdset_creation(self):
        self.add(CmdJoinElementals())
        self.add(CmdLeaveElementals())


class ElementalGuildJoinRoom(Room):
    def at_object_creation(self):
        print(f"at obj creation, self {self}")
        self.cmdset.add_default(ElementalRoomCmdSet)
        # self.desc = f"
        # As you step into the grand hall of the Elementals Guild, you are immediately enveloped by an aura of ancient power and mystique. The room is vast, with high ceilings adorned with intricate carvings depicting the four elements: earth, air, fire, and water. The walls are lined with glowing crystals that pulse with a soft, ethereal light, casting dancing shadows across the room.

        # At the center of the hall stands a large, circular platform made of polished stone. Surrounding the platform are four towering statues, each representing one of the elemental guardians. The statue of the earth guardian is a massive figure carved from solid rock, its eyes glowing with a deep, emerald light. The air guardian is depicted as a graceful, almost ethereal figure, seemingly made of swirling winds. The fire guardian is a fierce, imposing figure, with flames flickering around its form. The water guardian is a serene, flowing figure, with water cascading down its body.

        # The air is filled with the faint hum of elemental energy, and you can feel the power of the elements coursing through the room. As you approach the platform, a sense of anticipation and excitement builds within you. This is the place where you will take your first steps towards mastering the elements and joining the ranks of the Elementals Guild.
        # "


class ChangelingRoomCmdSet(CmdSet):
    key = "changeling_room"
    priority = 1

    def at_cmdset_creation(self):
        self.add(CmdJoinChangelings())
        self.add(CmdLeaveChangelings())


class ChangelingGuildJoinRoom(Room):
    def at_object_creation(self):
        print(f"at obj creation, self {self}")
        self.cmdset.add_default(ChangelingRoomCmdSet)
        # self.desc = f"
        # As you step into the sleek, metallic chamber of the Changeling Guild, you are immediately struck by the futuristic design and advanced technology that surrounds you. The room is illuminated by a soft, blue glow emanating from the walls, which are embedded with intricate circuitry and holographic displays.

        # In the center of the chamber stands a large, circular console made of a smooth, reflective material. The console is surrounded by a series of floating, transparent screens that display streams of data and complex schematics. The air is filled with a faint hum of machinery and the occasional beep of electronic devices.

        # Around the room, you can see various stations dedicated to different aspects of the changeling’s craft. One station is equipped with advanced genetic modification tools, while another is filled with holographic projectors and disguise equipment. There is even a section dedicated to virtual reality training, where members can practice their shapeshifting abilities in a simulated environment.

        # At the far end of the chamber, a large, imposing figure stands guard. This is the guild’s leader, a master changeling who has perfected the art of transformation. Their form is constantly shifting, flickering between different appearances as they observe you with keen, calculating eyes.

        # As you approach the console, a sense of excitement and anticipation fills you. This is the place where you will learn to harness the power of transformation and join the ranks of the Changeling Guild. The possibilities are endless, and the future is yours to shape.
        # "


class WarriorRoomCmdSet(CmdSet):
    key = "warrior_room"
    priority = 1

    def at_cmdset_creation(self):
        self.add(CmdJoinWarriors())
        self.add(CmdLeaveWarriors())


class WarriorGuildJoinRoom(Room):
    def at_object_creation(self):
        print(f"at obj creation, self {self}")
        self.cmdset.add_default(WarriorRoomCmdSet)
        # self.desc = f"
        # As you step into the grand hall of the Warriors Guild, you are immediately enveloped by an aura of strength and camaraderie. The room is vast, with high ceilings adorned with banners depicting the guild’s emblem: a crossed sword and shield. The walls are lined with suits of armor and weapons, each one a testament to the martial prowess of the guild’s members.

        # At the center of the hall stands a large, circular platform made of polished stone. Surrounding the platform are four towering statues, each representing a different warrior archetype. The knight is a figure clad in gleaming plate armor, wielding a massive sword and shield. The berserker is a fierce, muscular warrior, brandishing a massive axe and roaring in battle. The archer is a lithe, agile figure, drawing back a bow with deadly precision. The mage is a cloaked figure, surrounded by crackling energy and arcane symbols.

        # The air is filled with the sound of clashing weapons and the shouts of sparring warriors. As you approach the platform, a sense of anticipation and excitement builds within you. This is the place where you will take your first steps towards mastering the art of combat and joining the ranks of the Warriors Guild.
        # "


class CybercorpsRoomCmdSet(CmdSet):
    key = "cybercorps_room"
    priority = 1

    def at_cmdset_creation(self):
        self.add(CmdJoinCybercorps())
        self.add(CmdLeaveCybercorps())


class CybercorpsGuildJoinRoom(Room):
    def at_object_creation(self):
        print(f"at obj creation, self {self}")
        self.cmdset.add_default(CybercorpsRoomCmdSet)


class CybercorpsWaresRoom(Room):
    def at_object_creation(self):
        print(f"at obj creation, self {self}")
        self.cmdset.add_default(CybercorpsWaresRoomCmdSet)
        # @desc |YAs you step into the CyberCorps Wares Shop, the atmosphere shifts to one of sleek sophistication and cutting-edge technology. The shop is a marvel of modern design, with walls lined with polished metal and illuminated by soft, ambient lighting that highlights the high-tech merchandise on display.|/|/The entrance is flanked by two holographic displays, welcoming you with animated advertisements showcasing the latest in cybernetic enhancements and advanced weaponry. The floor is a seamless expanse of dark, reflective material that seems to absorb sound, creating a hushed, almost reverent atmosphere.|/|/To your left, a series of glass cases house an array of cybernetic implants, each one more advanced than the last. From neural interfaces that enhance cognitive functions to biomechanical limbs that offer superhuman strength, the selection is both impressive and intimidating. Each item is accompanied by a holographic information panel, detailing its specifications and potential applications.|/|/On the right, a wall of weaponry catches your eye. Sleek plasma rifles, compact laser pistols, and formidable gauss cannons are displayed with meticulous care. The weapons are mounted on illuminated racks, each one casting a soft glow that accentuates their lethal beauty. Interactive displays allow you to examine the weapons in detail, providing information on their capabilities and customization options.|/|/In the center of the shop, a circular counter staffed by impeccably dressed androids offers personalized assistance. Their synthetic voices are calm and precise, ready to answer any questions and guide you through the purchasing process. Behind the counter, a large screen displays real-time data feeds and promotional videos, showcasing the latest innovations from CyberCorps.|/|/The back of the shop features a private consultation area, where clients can discuss their needs and receive expert advice on the best enhancements and equipment for their specific requirements. Comfortable seating and a serene ambiance make this area a welcome respite from the high-tech hustle of the main shop floor.|/|/Throughout the shop, the air is filled with a subtle hum of advanced machinery and the faint scent of ozone, a reminder of the powerful technology that surrounds you. The overall effect is one of awe and excitement, a testament to the cutting-edge advancements that CyberCorps has to offer. This is not just a shop; it is a gateway to a future where the line between human and machine is increasingly blurred.


class CybercorpsImplantRoom(Room):
    def at_object_creation(self):
        print(f"at obj creation, self {self}")
        self.cmdset.add_default(CybercorpsImplantsRoomCmdSet)


class CybercorpsShop(Room):
    """
    A grid-aware room that has built-in shop-related functionality.
    """

    def at_object_creation(self):
        """
        Initialize the shop inventory and commands
        """
        super().at_object_creation()

        # add the shopping commands to the room
        self.cmdset.delete(ShopCmdSet)
        self.cmdset.delete(ShopCmdSet)
        self.cmdset.delete(ShopCmdSet)
        self.cmdset.add(ShopCmdSet, persistent=True)
        # create an invisible, inaccessible storage object
        self.db.storage = create.object(
            key="shop storage",
            locks="view:perm(Builder);get:perm(Builder);search:perm(Builder)",
            home=self,
            location=self,
        )

        self.db.inventory = [
            ("CYBER_CHESTGUARD", 3),
            ("CYBER_LEG_GUARDS", 3),
            ("CYBER_BOOTS", 3),
        ]
        self.scripts.add(RestockScript, key="restock", autostart=True)

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
