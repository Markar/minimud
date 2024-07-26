"""
An early dungeon.
"""

from evennia.contrib.grid.xyzgrid import xymap_legend

MAP1 = r"""
                       1
 + 0 1 2 3 4 5 6 7 8 9 0

 4   #-#-#-#-#-#-#-#
     | | | | | | | |
 3   #-#-#-#-#-#-#-#
     | | | | | | | |
 2   #-#-#-#-#-#-#-#
     | | | | | | | |
 1   #-#-#-#-#-#-#-#
 
 0  

 + 0 1 2 3 4 5 6 7 8 9 0
                       1
"""

PROTOTYPES = {
    (1, 1): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("newbieland", "zone")],
        "key": "A dirty open field",
        "desc": "You see an open field with sparse vegetation to the south. There are a variety of creatures wandering about, and some of them look quite aggressive."
    },
    (2, 1): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("newbieland", "zone")],
        "key": "A barren field",
        "desc": "The city walls span further east and west here, and the field continues south of here. There is a small cactus here.",
    },
    (3, 1): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("newbieland", "zone")],
        "key": "A barren field",
        "desc": "The noises of the city can be heard through the walls, and the field continues ",
    },
    (4, 1): {
        "typeclass": "typeclasses.rooms.NewbieLargeRat",
        "tags": [("newbieland", "zone")],
        "key": "Before the city gates",
        "desc": "As you leave the city, you see a dirt field in front of you with sparse vegetation. This area around the city is well traveled.",
    },
    (5, 1): {
        "typeclass": "typeclasses.rooms.NewbieSnake",
        "tags": [("newbieland", "zone")],
        "key": "A dirty field",
        "desc": "The city walls continue east, and there are snakes and rats everywhere.",
    },
    (6, 1): {
        "typeclass": "typeclasses.rooms.NewbieLargeRat",
        "tags": [("newbieland", "zone")],
        "key": "A dirt field",
        "desc": "This patch of dirt has a few blades of grass, and not much else. There is a large rat here minding its own business, maybe you should leave it alone.",
    },
    (7, 1): {
        "typeclass": "typeclasses.rooms.NewbieSnake",
        "tags": [("newbieland", "zone")],
        "key": "A dirt field",
        "desc": "There are snakes and rats everywhre, and you see more dangerous creatures further south.",
    },
    (8, 1): {
        "typeclass": "typeclasses.rooms.NewbieLargeRat",
        "tags": [("newbieland", "zone")],
        "key": "The edge of a field",
        "desc": "The city walls come to an end here, and the terrain further east is too difficult to navigate.",
    },
    
    (1, 2): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("newbieland", "zone")],
        "key": "A sparse dirt field",
        "desc": "The dirt field continues here with little vegetation. There are gnolls all over this area, and they look quite aggressive.",
    },
    (2, 2): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("newbieland", "zone")],
        "key": "A dirt field",
        "desc": "The gnolls around here are mostly young, they must be coming from somewhere.",
    },
    (3, 2): {
        "typeclass": "typeclasses.rooms.NewbieLargeRat",
        "tags": [("newbieland", "zone")],
        "key": "A dirt patch",
        "desc": "The field has a few blades of grass and cacti here, but not much else.",
    },
    (4, 2): {
        "typeclass": "typeclasses.rooms.NewbieSnake",
        "tags": [("newbieland", "zone")],
        "key": "A grassy patch",
        "desc": "There are some tough weeds growing here, surviving the harsh environment of traveler's boots and trodding gnolls.",
    },
    (5, 2): {
        "typeclass": "typeclasses.rooms.NewbieSnake",
        "tags": [("newbieland", "zone")],
        "key": "A cactus patch",
        "desc": "There is a small clump of cacti here. Their spikes must be able to discourage the adventurers and gnolls from trodding over them.",
    },
    (6, 2): {
        "typeclass": "typeclasses.rooms.NewbieLargeRat",
        "tags": [("newbieland", "zone")],
        "key": "A dirt field",
        "desc": "The large field continues here, and you can make out more aggressive creeatures to the south. Fortunately they haven't seen you yet.",
    },
    (7, 2): {
        "typeclass": "typeclasses.rooms.NewbieSnake",
        "tags": [("newbieland", "zone")],
        "key": "A dirt patch",
        "desc": "There are snakes and rats all around you, but they don't appear aggressive.",
    },
    (8, 2): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("newbieland", "zone")],
        "key": "Before the rocks",
        "desc": "Craggy rocks make it too difficult to travel further east, but the field continues south.",
    },
    
    (1, 3): {
        "typeclass": "typeclasses.rooms.ChessboardDecayingSkeleton",
        "tags": [("newbieland", "zone")],
        "key": "A dirt field",
        "desc": "The field has little vegetation here, and you see the crags continue west.",
    },
    (2, 3): {
        "typeclass": "typeclasses.rooms.NewbieLargeRat",
        "tags": [("newbieland", "zone")],
        "key": "A dirt field",
        "desc": "The field is open and flat all around you. You see hear the clacking of skeletons nearby.",
    },
    (3, 3): {
        "typeclass": "typeclasses.rooms.ChessboardDecayingSkeleton",
        "tags": [("newbieland", "zone")],
        "key": "An abandoned tent",
        "desc": "There is an abandoned tent here. An adventurer must have tried to set up camp, but maybe they ran into trouble?",
    },
    (4, 3): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("newbieland", "zone")],
        "key": "East half of a plaza",
        "desc": "The gnolls and skeletons are all around you at this part of the field. They don't appear to be bothering each other.",
    },
    (5, 3): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("newbieland", "zone")],
        "key": "An open field",
        "desc": "There are some boxes and crates here, but they have alredy been pillaged.",
    },
    (6, 3): {
        "typeclass": "typeclasses.rooms.NewbieLargeRat",
        "tags": [("newbieland", "zone")],
        "key": "A dirty field",
        "desc": "There is tattered clothing scattered across the ground here, and you hear the sounds of skeletons, gnolls, and rats all around you.",
    },
    (7, 3): {
        "typeclass": "typeclasses.rooms.ChessboardDecayingSkeleton",
        "tags": [("newbieland", "zone")],
        "key": "Refuse covered field",
        "desc": "This area must be a resting place for some of the creatures here. The smell is terrible, and there are remnants of destroyed boxes and tattered clothing on the ground.",
    },
    (8, 3): {
        "typeclass": "typeclasses.rooms.NewbieLargeRat",
        "tags": [("newbieland", "zone")],
        "key": "East half of a plaza",
        "desc": "The craggy rocks continue, blocking your path further east. You area beyond the rocks looks more like a desert.",
    },
    
    (1, 4): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("newbieland", "zone")],
        "key": "West of the city",
        "desc": "The city is far behind you at this point, but you can still make out the gates to the northeast. ",
    },
    (2, 4): {
        "typeclass": "typeclasses.rooms.NewbieLargeRat",
        "tags": [("newbieland", "zone")],
        "key": "South of the city",
        "desc": "There is more vegetation and weeds growing here. This part of the field must be less traveled.",
    },
    (3, 4): {
        "typeclass": "typeclasses.rooms.NewbieFirebeetle",
        "tags": [("newbieland", "zone")],
        "key": "East half of a plaza",
        "desc": "You hear the click-clack of beetles nearby. These beetles are larger than you're used to and emit a dull orange light.",
    },
    (4, 4): {
        "typeclass": "typeclasses.rooms.ChessboardGnoll",
        "tags": [("newbieland", "zone")],
        "key": "South of the city",
        "desc": "The city gates are far to the north, but you could probably outrun any foes from here. There is a larger gnoll here, and he's out for blood.",
    },
    (5, 4): {
        "typeclass": "typeclasses.rooms.NewbieFirebeetle",
        "tags": [("newbieland", "zone")],
        "key": "East half of a plaza",
        "desc": "You hear the click-clack of fire beetles around you, and this area is alight with the glow coming from them.",
    },
    (6, 4): {
        "typeclass": "typeclasses.rooms.NewbieLargeRat",
        "tags": [("newbieland", "zone")],
        "key": "A small camp",
        "desc": "There are a couple of small tents here, with a few boxes and supplies. Nobody is home right now, but they must be nearby to have left their things out in the open.",
    },
    (7, 4): {
        "typeclass": "typeclasses.rooms.NewbieFirebeetle",
        "tags": [("newbieland", "zone")],
        "key": "Beetle nest",
        "desc": "There's a nest in the ground where fire beetles retreat to. They don't seem aggressive, but they look strong and it may be best to leave them alone.",
    },
    (8, 4): {
        "typeclass": "typeclasses.rooms.NewbieLargeRat",
        "tags": [("newbieland", "zone")],
        "key": "Craggy rocks",
        "desc": "The rocks toward the east are getting smaller and less dense. The city is far to the northwest from here.",
    },
}


XYMAP_DATA = {
    "zcoord": "newbieland",
    "map": MAP1,
    # "legend": LEGEND,
    "prototypes": PROTOTYPES,
    # "options": {"map_visual_range": 1},
}
