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
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of the black rook",
        "desc": "|YOn the square of the chessboard, a towering gnoll stands menacingly. Its hyena-like face snarls, revealing sharp teeth, while its muscular frame is covered in matted fur and crude armor. The gnoll's eyes gleam with a feral intelligence, and it grips a blood-stained spear, ready to strike at any moment.",
    },
    (1, 2): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of the black knight",
        "desc": "|YOn the square of the chessboard, a towering gnoll stands menacingly. Its hyena-like face snarls, revealing sharp teeth, while its muscular frame is covered in matted fur and crude armor. The gnoll's eyes gleam with a feral intelligence, and it grips a blood-stained spear, ready to strike at any moment.",
    },
    (1, 3): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of the black bishop",
        "desc": "|YOn the square of the chessboard, a towering gnoll stands menacingly. Its hyena-like face snarls, revealing sharp teeth, while its muscular frame is covered in matted fur and crude armor. The gnoll's eyes gleam with a feral intelligence, and it grips a blood-stained spear, ready to strike at any moment.",
    },
    (1, 4): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of the black queen",
        "desc": "|YOn the square of the chessboard, a towering gnoll stands menacingly. Its hyena-like face snarls, revealing sharp teeth, while its muscular frame is covered in matted fur and crude armor. The gnoll's eyes gleam with a feral intelligence, and it grips a blood-stained spear, ready to strike at any moment.",
    },
    (1, 5): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of the black king",
        "desc": "|YOn the square of the chessboard, a towering gnoll stands menacingly. Its hyena-like face snarls, revealing sharp teeth, while its muscular frame is covered in matted fur and crude armor. The gnoll's eyes gleam with a feral intelligence, and it grips a blood-stained spear, ready to strike at any moment.",
    },
    (1, 6): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of the black bishop",
        "desc": "|YOn the square of the chessboard, a towering gnoll stands menacingly. Its hyena-like face snarls, revealing sharp teeth, while its muscular frame is covered in matted fur and crude armor. The gnoll's eyes gleam with a feral intelligence, and it grips a blood-stained spear, ready to strike at any moment.",
    },
    (1, 7): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of the black knight",
        "desc": "|YOn the square of the chessboard, a towering gnoll stands menacingly. Its hyena-like face snarls, revealing sharp teeth, while its muscular frame is covered in matted fur and crude armor. The gnoll's eyes gleam with a feral intelligence, and it grips a blood-stained spear, ready to strike at any moment.",
    },
    (1, 8): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of the black rook",
        "desc": "|YOn the square of the chessboard, a towering gnoll stands menacingly. Its hyena-like face snarls, revealing sharp teeth, while its muscular frame is covered in matted fur and crude armor. The gnoll's eyes gleam with a feral intelligence, and it grips a blood-stained spear, ready to strike at any moment.",
    },
    (2, 1): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a black pawn",
        "desc": "|YOn the square of the chessboard, a gnoll pup stands nervously. Its small, hyena-like frame is covered in patchy fur, and it wears a torn blue shirt with greenish yellow pants. The gnoll pup's eyes dart around, filled with a mix of curiosity and fear, as it clutches a small, rusty dagger.",
    },
    (2, 2): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a black pawn",
        "desc": "|YOn the square of the chessboard, a gnoll pup stands nervously. Its small, hyena-like frame is covered in patchy fur, and it wears a torn blue shirt with greenish yellow pants. The gnoll pup's eyes dart around, filled with a mix of curiosity and fear, as it clutches a small, rusty dagger.",
    },
    (2, 3): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a black pawn",
        "desc": "|YOn the square of the chessboard, a gnoll pup stands nervously. Its small, hyena-like frame is covered in patchy fur, and it wears a torn blue shirt with greenish yellow pants. The gnoll pup's eyes dart around, filled with a mix of curiosity and fear, as it clutches a small, rusty dagger.",
    },
    (2, 4): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a black pawn",
        "desc": "|YOn the square of the chessboard, a gnoll pup stands nervously. Its small, hyena-like frame is covered in patchy fur, and it wears a torn blue shirt with greenish yellow pants. The gnoll pup's eyes dart around, filled with a mix of curiosity and fear, as it clutches a small, rusty dagger.",
    },
    (2, 5): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a black pawn",
        "desc": "|YOn the square of the chessboard, a gnoll pup stands nervously. Its small, hyena-like frame is covered in patchy fur, and it wears a torn blue shirt with greenish yellow pants. The gnoll pup's eyes dart around, filled with a mix of curiosity and fear, as it clutches a small, rusty dagger.",
    },
    (2, 6): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a black pawn",
        "desc": "|YOn the square of the chessboard, a gnoll pup stands nervously. Its small, hyena-like frame is covered in patchy fur, and it wears a torn blue shirt with greenish yellow pants. The gnoll pup's eyes dart around, filled with a mix of curiosity and fear, as it clutches a small, rusty dagger.",
    },
    (2, 7): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a black pawn",
        "desc": "|YOn the square of the chessboard, a gnoll pup stands nervously. Its small, hyena-like frame is covered in patchy fur, and it wears a torn blue shirt with greenish yellow pants. The gnoll pup's eyes dart around, filled with a mix of curiosity and fear, as it clutches a small, rusty dagger.",
    },
    (2, 8): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Dark square of a chessboard",
        "desc": "|YOn the square of the chessboard, a gnoll pup stands nervously. Its small, hyena-like frame is covered in patchy fur, and it wears a torn blue shirt with greenish yellow pants. The gnoll pup's eyes dart around, filled with a mix of curiosity and fear, as it clutches a small, rusty dagger.",
    },
    (3, 1): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Light square of a chessboard",
        "desc": "On the light square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (3, 2): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Dark square of a chessboard",
        "desc": "On the dark square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (3, 3): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Light square of a chessboard",
        "desc": "On the light square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (3, 4): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Dark square of a chessboard",
        "desc": "On the dark square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (3, 5): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Light square of a chessboard",
        "desc": "On the light square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (3, 6): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Dark square of a chessboard",
        "desc": "On the dark square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (3, 7): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Light square of a chessboard",
        "desc": "On the light square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (3, 8): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Dark square of a chessboard",
        "desc": "On the dark square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (4, 1): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Light square of a chessboard",
        "desc": "|YOn the square of the chessboard, a towering gnoll stands menacingly. Its hyena-like face snarls, revealing sharp teeth, while its muscular frame is covered in matted fur and crude armor. The gnoll's eyes gleam with a feral intelligence, and it grips a blood-stained spear, ready to strike at any moment.",
    },
    (4, 2): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Dark square of a chessboard",
        "desc": "|YOn the square of the chessboard, a towering gnoll stands menacingly. Its hyena-like face snarls, revealing sharp teeth, while its muscular frame is covered in matted fur and crude armor. The gnoll's eyes gleam with a feral intelligence, and it grips a blood-stained spear, ready to strike at any moment.",
    },
    (4, 3): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Light square of a chessboard",
        "desc": "|YOn the square of the chessboard, a towering gnoll stands menacingly. Its hyena-like face snarls, revealing sharp teeth, while its muscular frame is covered in matted fur and crude armor. The gnoll's eyes gleam with a feral intelligence, and it grips a blood-stained spear, ready to strike at any moment.",
    },
    (4, 4): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Dark square of a chessboard",
        "desc": "|YOn the square of the chessboard, a towering gnoll stands menacingly. Its hyena-like face snarls, revealing sharp teeth, while its muscular frame is covered in matted fur and crude armor. The gnoll's eyes gleam with a feral intelligence, and it grips a blood-stained spear, ready to strike at any moment.",
    },
    (4, 5): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Light square of a chessboard",
        "desc": "|YOn the square of the chessboard, a towering gnoll stands menacingly. Its hyena-like face snarls, revealing sharp teeth, while its muscular frame is covered in matted fur and crude armor. The gnoll's eyes gleam with a feral intelligence, and it grips a blood-stained spear, ready to strike at any moment.",
    },
    (4, 6): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Dark square of a chessboard",
        "desc": "|YOn the square of the chessboard, a towering gnoll stands menacingly. Its hyena-like face snarls, revealing sharp teeth, while its muscular frame is covered in matted fur and crude armor. The gnoll's eyes gleam with a feral intelligence, and it grips a blood-stained spear, ready to strike at any moment.",
    },
    (4, 7): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Light square of a chessboard",
        "desc": "|YOn the square of the chessboard, a towering gnoll stands menacingly. Its hyena-like face snarls, revealing sharp teeth, while its muscular frame is covered in matted fur and crude armor. The gnoll's eyes gleam with a feral intelligence, and it grips a blood-stained spear, ready to strike at any moment.",
    },
    (4, 8): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Dark square of a chessboard",
        "desc": "|YOn the square of the chessboard, a towering gnoll stands menacingly. Its hyena-like face snarls, revealing sharp teeth, while its muscular frame is covered in matted fur and crude armor. The gnoll's eyes gleam with a feral intelligence, and it grips a blood-stained spear, ready to strike at any moment.",
    },
    (5, 1): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Light square of a chessboard",
        "desc": "|YOn the square of the chessboard, a gnoll pup stands nervously. Its small, hyena-like frame is covered in patchy fur, and it wears a torn blue shirt with greenish yellow pants. The gnoll pup's eyes dart around, filled with a mix of curiosity and fear, as it clutches a small, rusty dagger.",
    },
    (5, 2): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Dark square of a chessboard",
        "desc": "|YOn the square of the chessboard, a gnoll pup stands nervously. Its small, hyena-like frame is covered in patchy fur, and it wears a torn blue shirt with greenish yellow pants. The gnoll pup's eyes dart around, filled with a mix of curiosity and fear, as it clutches a small, rusty dagger.",
    },
    (5, 3): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Light square of a chessboard",
        "desc": "|YOn the square of the chessboard, a gnoll pup stands nervously. Its small, hyena-like frame is covered in patchy fur, and it wears a torn blue shirt with greenish yellow pants. The gnoll pup's eyes dart around, filled with a mix of curiosity and fear, as it clutches a small, rusty dagger.",
    },
    (5, 4): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Dark square of a chessboard",
        "desc": "|YOn the square of the chessboard, a gnoll pup stands nervously. Its small, hyena-like frame is covered in patchy fur, and it wears a torn blue shirt with greenish yellow pants. The gnoll pup's eyes dart around, filled with a mix of curiosity and fear, as it clutches a small, rusty dagger.",
    },
    (5, 5): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Light square of a chessboard",
        "desc": "|YOn the square of the chessboard, a gnoll pup stands nervously. Its small, hyena-like frame is covered in patchy fur, and it wears a torn blue shirt with greenish yellow pants. The gnoll pup's eyes dart around, filled with a mix of curiosity and fear, as it clutches a small, rusty dagger.",
    },
    (5, 6): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Dark square of a chessboard",
        "desc": "|YOn the square of the chessboard, a gnoll pup stands nervously. Its small, hyena-like frame is covered in patchy fur, and it wears a torn blue shirt with greenish yellow pants. The gnoll pup's eyes dart around, filled with a mix of curiosity and fear, as it clutches a small, rusty dagger.",
    },
    (5, 7): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Light square of a chessboard",
        "desc": "|YOn the square of the chessboard, a gnoll pup stands nervously. Its small, hyena-like frame is covered in patchy fur, and it wears a torn blue shirt with greenish yellow pants. The gnoll pup's eyes dart around, filled with a mix of curiosity and fear, as it clutches a small, rusty dagger.",
    },
    (5, 8): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Dark square of a chessboard",
        "desc": "|YOn the square of the chessboard, a gnoll pup stands nervously. Its small, hyena-like frame is covered in patchy fur, and it wears a torn blue shirt with greenish yellow pants. The gnoll pup's eyes dart around, filled with a mix of curiosity and fear, as it clutches a small, rusty dagger.",
    },
    (6, 1): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Light square of a chessboard",
        "desc": "On the light square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (6, 2): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Dark square of a chessboard",
        "desc": "On the dark square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (6, 3): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Light square of a chessboard",
        "desc": "On the dark square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (6, 4): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Dark square of a chessboard",
        "desc": "On the dark square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (6, 5): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Light square of a chessboard",
        "desc": "On the light square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (6, 6): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Dark square of a chessboard",
        "desc": "On the light square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (6, 7): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Light square of a chessboard",
        "desc": "On the light square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (6, 8): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Dark square of a chessboard",
        "desc": "On the dark square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (7, 1): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white pawn",
        "desc": "|YOn the square of the chessboard, a towering gnoll stands menacingly. Its hyena-like face snarls, revealing sharp teeth, while its muscular frame is covered in matted fur and crude armor. The gnoll's eyes gleam with a feral intelligence, and it grips a blood-stained spear, ready to strike at any moment.",
    },
    (7, 2): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white pawn",
        "desc": "|YOn the square of the chessboard, a towering gnoll stands menacingly. Its hyena-like face snarls, revealing sharp teeth, while its muscular frame is covered in matted fur and crude armor. The gnoll's eyes gleam with a feral intelligence, and it grips a blood-stained spear, ready to strike at any moment.",
    },
    (7, 3): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white pawn",
        "desc": "|YOn the square of the chessboard, a towering gnoll stands menacingly. Its hyena-like face snarls, revealing sharp teeth, while its muscular frame is covered in matted fur and crude armor. The gnoll's eyes gleam with a feral intelligence, and it grips a blood-stained spear, ready to strike at any moment.",
    },
    (7, 4): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white pawn",
        "desc": "|YOn the square of the chessboard, a towering gnoll stands menacingly. Its hyena-like face snarls, revealing sharp teeth, while its muscular frame is covered in matted fur and crude armor. The gnoll's eyes gleam with a feral intelligence, and it grips a blood-stained spear, ready to strike at any moment.",
    },
    (7, 5): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white pawn",
        "desc": "|YOn the square of the chessboard, a towering gnoll stands menacingly. Its hyena-like face snarls, revealing sharp teeth, while its muscular frame is covered in matted fur and crude armor. The gnoll's eyes gleam with a feral intelligence, and it grips a blood-stained spear, ready to strike at any moment.",
    },
    (7, 6): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white pawn",
        "desc": "|YOn the square of the chessboard, a towering gnoll stands menacingly. Its hyena-like face snarls, revealing sharp teeth, while its muscular frame is covered in matted fur and crude armor. The gnoll's eyes gleam with a feral intelligence, and it grips a blood-stained spear, ready to strike at any moment.",
    },
    (7, 7): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white pawn",
        "desc": "|YOn the square of the chessboard, a towering gnoll stands menacingly. Its hyena-like face snarls, revealing sharp teeth, while its muscular frame is covered in matted fur and crude armor. The gnoll's eyes gleam with a feral intelligence, and it grips a blood-stained spear, ready to strike at any moment.",
    },
    (7, 8): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnoll",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white pawn",
        "desc": "|YOn the square of the chessboard, a towering gnoll stands menacingly. Its hyena-like face snarls, revealing sharp teeth, while its muscular frame is covered in matted fur and crude armor. The gnoll's eyes gleam with a feral intelligence, and it grips a blood-stained spear, ready to strike at any moment.",
    },
    (8, 1): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white rook",
        "desc": "|YOn the square of the chessboard, a gnoll pup stands nervously. Its small, hyena-like frame is covered in patchy fur, and it wears a torn blue shirt with greenish yellow pants. The gnoll pup's eyes dart around, filled with a mix of curiosity and fear, as it clutches a small, rusty dagger.",
    },
    (8, 2): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white knight",
        "desc": "|YOn the square of the chessboard, a gnoll pup stands nervously. Its small, hyena-like frame is covered in patchy fur, and it wears a torn blue shirt with greenish yellow pants. The gnoll pup's eyes dart around, filled with a mix of curiosity and fear, as it clutches a small, rusty dagger.",
    },
    (8, 3): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white bishop",
        "desc": "|YOn the square of the chessboard, a gnoll pup stands nervously. Its small, hyena-like frame is covered in patchy fur, and it wears a torn blue shirt with greenish yellow pants. The gnoll pup's eyes dart around, filled with a mix of curiosity and fear, as it clutches a small, rusty dagger.",
    },
    (8, 4): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white queen",
        "desc": "|YOn the square of the chessboard, a gnoll pup stands nervously. Its small, hyena-like frame is covered in patchy fur, and it wears a torn blue shirt with greenish yellow pants. The gnoll pup's eyes dart around, filled with a mix of curiosity and fear, as it clutches a small, rusty dagger.",
    },
    (8, 5): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white king",
        "desc": "|YOn the square of the chessboard, a gnoll pup stands nervously. Its small, hyena-like frame is covered in patchy fur, and it wears a torn blue shirt with greenish yellow pants. The gnoll pup's eyes dart around, filled with a mix of curiosity and fear, as it clutches a small, rusty dagger.",
    },
    (8, 6): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white bishop",
        "desc": "|YOn the square of the chessboard, a gnoll pup stands nervously. Its small, hyena-like frame is covered in patchy fur, and it wears a torn blue shirt with greenish yellow pants. The gnoll pup's eyes dart around, filled with a mix of curiosity and fear, as it clutches a small, rusty dagger.",
    },
    (8, 7): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white knight",
        "desc": "|YOn the square of the chessboard, a gnoll pup stands nervously. Its small, hyena-like frame is covered in patchy fur, and it wears a torn blue shirt with greenish yellow pants. The gnoll pup's eyes dart around, filled with a mix of curiosity and fear, as it clutches a small, rusty dagger.",
    },
    (8, 8): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardGnollPup",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white rook",
        "desc": "|YOn the square of the chessboard, a gnoll pup stands nervously. Its small, hyena-like frame is covered in patchy fur, and it wears a torn blue shirt with greenish yellow pants. The gnoll pup's eyes dart around, filled with a mix of curiosity and fear, as it clutches a small, rusty dagger.",
    },
}


XYMAP_DATA = {
    "zcoord": "chessboard",
    "map": MAP1,
    # "legend": LEGEND,
    "prototypes": PROTOTYPES,
    # "options": {"map_visual_range": 1},
}
