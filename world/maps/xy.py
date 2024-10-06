"""
An early dungeon.
"""

from evennia.contrib.grid.xyzgrid import xymap_legend
from typeclasses.rooms import XYGridRoom
from evennia import logger


MAP1 = r"""
                       1
 + 0 1 2 3 4 5 6 7 8 9 0
 
 2   #-#-#
     |   |
 1   | # |
     | u |
 0   #-#-#

 + 0 1 2 3 4 5 6 7 8 9 0
                       1
"""


PROTOTYPES = {
    (1, 0): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "spawn_proto": "DECAYING_SKELETON",
        "tags": [("chessboard", "zone")],
        "key": "SW half of a plaza",
        "desc": "SW  central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (1, 2): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclass.rooms.MobRoomm",
        "spawn_proto": "DECAYING_SKELETON",
        "tags": [("chessboard", "zone")],
        "key": "nw half of a plaza",
        "desc": "nw central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (2, 0): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclass.rooms.MobRoomm",
        "tags": [("chessboard", "zone")],
        "key": "ne half of a plaza",
        "desc": "ne central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (2, 2): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclass.rooms.MobRoomm",
        "tags": [("chessboard", "zone")],
        "key": "se half of a plaza",
        "desc": "se central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (3, 0): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclass.rooms.MobRoomm",
        "tags": [("chessboard", "zone")],
        "key": "SW half of a plaza",
        "desc": "SW  central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (3, 2): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclass.rooms.MobRoomm",
        "tags": [("chessboard", "zone")],
        "key": "nw half of a plaza",
        "desc": "nw central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
}


XYMAP_DATA = {
    "zcoord": "xy",
    "map": MAP1,
    # "legend": LEGEND,
    "prototypes": PROTOTYPES,
    # "options": {"map_visual_range": 1},
}
