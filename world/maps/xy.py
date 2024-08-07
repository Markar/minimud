"""
An early dungeon.
"""

from evennia.contrib.grid.xyzgrid import xymap_legend

MAP1 = r"""
                       1
 + 0 1 2 3 4 5 6 7 8 9 0

 1   #-#
     | |
 0   #-#

 + 0 1 2 3 4 5 6 7 8 9 0
                       1
"""

PROTOTYPES = {
    (1, 0): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "SW half of a plaza",
        "desc": "SW  central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (1, 1): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "nw half of a plaza",
        "desc": "nw central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (2, 1): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "ne half of a plaza",
        "desc": "ne central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (2, 0): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "se half of a plaza",
        "desc": "se central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
}


XYMAP_DATA = {
    "zcoord": "chessboard",
    "map": MAP1,
    # "legend": LEGEND,
    "prototypes": PROTOTYPES,
    # "options": {"map_visual_range": 1},
}
