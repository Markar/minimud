"""
An early dungeon.
"""

from evennia.contrib.grid.xyzgrid import xymap_legend

MAP1 = r"""
                       1
 + 0 1 2 3 4 5 6 7 8 9 0

 8   #-#-#-#-#-#-#-#
     | | | | | | | |
 7   #-#-#-#-#-#-#-#
     | | | | | | | |
 6   #-#-#-#-#-#-#-#
     | | | | | | | |
 5   #-#-#-#-#-#-#-#
     | | | | | | | |
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


class RoadNode(xymap_legend.MapNode):
    display_symbol = "#"
    prototype = {
        "prototype_parent": "xyz_room",
        "tags": [("chessboard", "zone")],
        "key": "A road",
        "desc": "A wide road through Chessboard.",
    }


class GateNode(xymap_legend.MapNode):
    display_symbol = "θ"
    prototype = {
        "prototype_parent": "xyz_room",
        "tags": [("chessboard", "zone")],
        "key": "A road",
        "desc": "The road here leads out of Chessboard and into the wilderness.",
    }


class BuildingNode(xymap_legend.MapNode):
    prototype = {
        "prototype_parent": "xyz_room",
        "key": "Inside",
        "desc": "A building in Chessboard.",
    }


class ShopNode(xymap_legend.MapNode):
    prototype = {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.XYGridShop",
        "key": "Inside",
        "desc": "A shop in Chessboard.",
    }


# LEGEND = {
#     "R": RoadNode,
#     "G": GateNode,
#     "B": BuildingNode,
#     "$": ShopNode,
# }

PROTOTYPES = {
    (1, 1): {
        "typeclass": "typeclasses.rooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of the black rook",
        "desc": "The southwest corner of the Chessboard is wide-open, with a rook present.",
    },
    (1, 2): {
        "typeclass": "typeclasses.rooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of the black knight",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (1, 3): {
        "typeclass": "typeclasses.rooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of the black bishop",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
        "inventory": [
            ("PIE_SLICE", 12),
        ],
    },
    (1, 4): {
        "typeclass": "typeclasses.rooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of the black queen",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (1, 5): {
        "typeclass": "typeclasses.rooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of the black king",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (1, 6): {
        "typeclass": "typeclasses.rooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of the black bishop",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (1, 7): {
        "typeclass": "typeclasses.rooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of the black knight",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (1, 8): {
        "typeclass": "typeclasses.rooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of the black rook",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    
    (2, 1): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a black pawn",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (2, 2): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a black pawn",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (2, 3): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a black pawn",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (2, 4): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a black pawn",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (2, 5): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a black pawn",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (2, 6): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a black pawn",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (2, 7): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a black pawn",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (2, 8): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a black pawn",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    
    (3, 1): {
        "typeclass": "typeclasses.rooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "West half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (3, 2): {
        "typeclass": "typeclasses.rooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (3, 3): {
        "typeclass": "typeclasses.rooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (3, 4): {
        "typeclass": "typeclasses.rooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (3, 5): {
        "typeclass": "typeclasses.rooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (3, 6): {
        "typeclass": "typeclasses.rooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (3, 7): {
        "typeclass": "typeclasses.rooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (3, 8): {
        "typeclass": "typeclasses.rooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    
    (4, 1): {
        "typeclass": "typeclasses.rooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (4, 2): {
        "typeclass": "typeclasses.rooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (4, 3): {
        "typeclass": "typeclasses.rooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (4, 4): {
        "typeclass": "typeclasses.rooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (4, 5): {
        "typeclass": "typeclasses.rooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (4, 6): {
        "typeclass": "typeclasses.rooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (4, 7): {
        "typeclass": "typeclasses.rooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (4, 8): {
        "typeclass": "typeclasses.rooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    
    (5, 1): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (5, 2): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (5, 3): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (5, 4): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (5, 5): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (5, 6): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (5, 7): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (5, 8): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    
    (6, 1): {
        "typeclass": "typeclasses.rooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (6, 2): {
        "typeclass": "typeclasses.rooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (6, 3): {
        "typeclass": "typeclasses.rooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (6, 4): {
        "typeclass": "typeclasses.rooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (6, 5): {
        "typeclass": "typeclasses.rooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (6, 6): {
        "typeclass": "typeclasses.rooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (6, 7): {
        "typeclass": "typeclasses.rooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (6, 8): {
        "typeclass": "typeclasses.rooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "East half of a plaza",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    
    (7, 1): {
        "typeclass": "typeclasses.rooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white pawn",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (7, 2): {
        "typeclass": "typeclasses.rooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white pawn",
        "desc": "The central plaza in Chessboard is wide-open, with at least as many livestock as people.",
    },
    (7, 3): {
        "typeclass": "typeclasses.rooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white pawn",
        "desc": "The white side of the Chessboard, with at least as many livestock as people.",
    },
    (7, 4): {
        "typeclass": "typeclasses.rooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white pawn",
        "desc": "The white side of the Chessboard, with at least as many livestock as people.",
    },
    (7, 5): {
        "typeclass": "typeclasses.rooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white pawn",
        "desc": "The white side of the Chessboard, with at least as many livestock as people.",
    },
    (7, 6): {
        "typeclass": "typeclasses.rooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white pawn",
        "desc": "The white side of the Chessboard, with at least as many livestock as people.",
    },
    (7, 7): {
        "typeclass": "typeclasses.rooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white pawn",
        "desc": "The white side of the Chessboard, with at least as many livestock as people.",
    },
    (7, 8): {
        "typeclass": "typeclasses.rooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white pawn",
        "desc": "The white side of the Chessboard, with at least as many livestock as people.",
    },
    
    (8, 1): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white rook",
        "desc": "The white side of the Chessboard, with at least as many livestock as people.",
    },
    (8, 2): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white knight",
        "desc": "The white side of the Chessboard, with at least as many livestock as people.",
    },
    (8, 3): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white bishop",
        "desc": "The white side of the Chessboard, with at least as many livestock as people.",
    },
    (8, 4): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white queen",
        "desc": "The white side of the Chessboard, with at least as many livestock as people.",
    },
    (8, 5): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white king",
        "desc": "The white side of the Chessboard, with at least as many livestock as people.",
    },
    (8, 6): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white bishop",
        "desc": "The white side of the Chessboard, with at least as many livestock as people.",
    },
    (8, 7): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white knight",
        "desc": "The white side of the Chessboard, with at least as many livestock as people.",
    },
    (8, 8): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white rook",
        "desc": "The white side of the Chessboard, with at least as many livestock as people.",
    },
}


XYMAP_DATA = {
    "zcoord": "chessboard",
    "map": MAP1,
    # "legend": LEGEND,
    "prototypes": PROTOTYPES,
    # "options": {"map_visual_range": 1},
}
