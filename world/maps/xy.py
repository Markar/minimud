"""
An early dungeon.
"""

from evennia.contrib.grid.xyzgrid import xymap_legend
from typeclasses.rooms import XYGridRoom
from evennia import logger


MAP_A = r"""
                       1
 + 0 1 2 3 4 5 6 7 8 9 0
 
 2   #-#-#
     |   |
 1   # T #
     | | |
 0   #-#-#

 + 0 1 2 3 4 5 6 7 8 9 0
                       1
"""
MAP_B = r"""
                       1
 + 0 1 2 3 4 5 6 7 8 9 0

 0   #-T

 + 0 1 2 3 4 5 6 7 8 9 0
                       1
"""


class TransitionToMapB(xymap_legend.MapTransitionNode):
    """Transition to MapB"""

    target_map_xyz = (1, 0, "the small cave")

    symbol = "T"


class TransitionToMapA(xymap_legend.MapTransitionNode):
    """Transition to MapA"""

    target_map_xyz = (2, 1, "xy")
    symbol = "T"


LEGEND_MAP1 = {"T": TransitionToMapB}


PROTOTYPES = {
    (1, 0): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("chessboard", "zone")],
        "key": "SW testroom",
        "desc": "SW  central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (1, 2): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("chessboard", "zone")],
        "key": "nw testroom",
        "desc": "nw central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (2, 0): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("chessboard", "zone")],
        "key": "ne testroom",
        "desc": "ne central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (2, 2): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("chessboard", "zone")],
        "key": "se testroom",
        "desc": "se central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (3, 0): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("chessboard", "zone")],
        "key": "SW testroom",
        "desc": "SW  central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (3, 2): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("chessboard", "zone")],
        "key": "nw testroom",
        "desc": "nw central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
}


XYMAP_DATA = {
    "zcoord": "xy",
    "map": MAP_A,
    "legend": LEGEND_MAP1,
    "prototypes": PROTOTYPES,
    # "options": {"map_visual_range": 1},
}


LEGEND_MAP2 = {"T": TransitionToMapB}

PROTOTYPES_MAP2 = {
    (2, 0): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("chessboard", "zone")],
        "key": "T testroom",
        "desc": "T testroom",
    },
}

XYMAP_DATA_MAP2 = {
    "map": MAP_B,
    "zcoord": "the small cave",
    "legend": LEGEND_MAP2,
    "prototypes": PROTOTYPES_MAP2,
    "options": {"map_visual_range": 1, "map_mode": "scan"},
}
# This is read by the parser
XYMAP_DATA_LIST = [XYMAP_DATA, XYMAP_DATA_MAP2]
