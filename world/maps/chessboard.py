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


PROTOTYPES = {
    # region Black pieces
    (1, 1): {
        "typeclass": "typeclasses.chessboardrooms.UndeadRook",
        "tags": [("chessboard", "zone")],
        "key": "Square of the black rook",
        "desc": "|YOn the square of the chessboard, a massive, hulking figure stands menacingly. Its body is covered in rotting flesh, and its eyes glow with an eerie light. The rook's movements are slow and deliberate, and its claws are sharp and deadly.",
    },
    (1, 2): {
        "typeclass": "typeclasses.chessboardrooms.UndeadKnight",
        "tags": [("chessboard", "zone")],
        "key": "Square of the black knight",
        "desc": "|YAn undead knight stands on the square of the chessboard, its armor rusted and its sword stained with blood. The knight's eyes glow with an eerie light, and its movements are swift and deadly.",
    },
    (1, 3): {
        "typeclass": "typeclasses.chessboardrooms.UndeadBishop",
        "tags": [("chessboard", "zone")],
        "key": "Square of the black bishop",
        "desc": "|YThe bishop is a tall, gaunt figure, its body covered in rotting flesh and its eyes glowing with an eerie light.",
    },
    (1, 4): {
        "typeclass": "typeclasses.chessboardrooms.UndeadQueen",
        "tags": [("chessboard", "zone")],
        "key": "Square of the black queen",
        "desc": "|YThe queen is a tall, imposing figure, her body covered in rotting flesh and her eyes glowing with an eerie light. She moves with a grace and speed that belies her undead nature.",
    },
    (1, 5): {
        "typeclass": "typeclasses.chessboardrooms.UndeadKing",
        "tags": [("chessboard", "zone")],
        "key": "Square of the black king",
        "desc": "|YThe king looks regal and imposing, his body covered in rotting flesh and his eyes glowing with an eerie light. He looks around with a sense of authority, ordering his minions to do his bidding.",
    },
    (1, 6): {
        "typeclass": "typeclasses.chessboardrooms.UndeadBishop",
        "tags": [("chessboard", "zone")],
        "key": "Square of the black bishop",
        "desc": "|YThe room is filled with the sound of clattering bones as the bishop moves across the chessboard. Its eyes glow with an eerie light, and its movements are swift and deadly.",
    },
    (1, 7): {
        "typeclass": "typeclasses.chessboardrooms.UndeadKnight",
        "tags": [("chessboard", "zone")],
        "key": "Square of the black knight",
        "desc": "|YOn this square of the chessboard, an undead knight stands menacingly. Its armor is rusted and its sword stained with blood. The knight's eyes glow with an eerie light, and its movements are swift and deadly.",
    },
    (1, 8): {
        "typeclass": "typeclasses.chessboardrooms.UndeadRook",
        "tags": [("chessboard", "zone")],
        "key": "Square of the black rook",
        "desc": "|YThe undead rook stands on the square of the chessboard, its massive form covered in rotting flesh. Its eyes glow with an eerie light, and its movements are slow and deliberate.",
    },
    (2, 1): {
        "typeclass": "typeclasses.chessboardrooms.UndeadPawn",
        "tags": [("chessboard", "zone")],
        "key": "Square of a black pawn",
        "desc": "|The room is filled with the sound of clattering bones as the pawn moves across the chessboard. Its eyes glow with an eerie light, and its movements are swift and deadly.",
    },
    (2, 2): {
        "typeclass": "typeclasses.chessboardrooms.UndeadPawn",
        "tags": [("chessboard", "zone")],
        "key": "Square of a black pawn",
        "desc": "|YThe pawn is a small, skeletal figure, its bones clattering with each movement. Its eyes glow with an eerie light, and its movements are swift and deadly.",
    },
    (2, 3): {
        "typeclass": "typeclasses.chessboardrooms.UndeadPawn",
        "tags": [("chessboard", "zone")],
        "key": "Square of a black pawn",
        "desc": "|YThe pawn is a small, skeletal figure, its bones clattering with each movement. He looks for an opening to strike, his eyes glowing with an eerie light.",
    },
    (2, 4): {
        "typeclass": "typeclasses.chessboardrooms.UndeadPawn",
        "tags": [("chessboard", "zone")],
        "key": "Square of a black pawn",
        "desc": "|YThe pawn is a small, skeletal figure, its bones clattering with each movement. He looks for an opening to strike, his eyes glowing with an eerie light.",
    },
    (2, 5): {
        "typeclass": "typeclasses.chessboardrooms.UndeadPawn",
        "tags": [("chessboard", "zone")],
        "key": "Square of a black pawn",
        "desc": "|YThe pawn wields a rusty dagger, looking around for orders to follow. He seems eager to prove his worth, his eyes glowing with an eerie light.",
    },
    (2, 6): {
        "typeclass": "typeclasses.chessboardrooms.UndeadPawn",
        "tags": [("chessboard", "zone")],
        "key": "Square of a black pawn",
        "desc": "|YThis pawn appears confued and lost, its eyes darting around the room. It clutches a small, rusty dagger, ready to strike at any moment.",
    },
    (2, 7): {
        "typeclass": "typeclasses.chessboardrooms.UndeadPawn",
        "tags": [("chessboard", "zone")],
        "key": "Square of a black pawn",
        "desc": "|YWielding a rusty dagger, the pawn looks around for orders to follow. He seems eager to prove his worth, his eyes glowing with an eerie light.",
    },
    (2, 8): {
        "typeclass": "typeclasses.chessboardrooms.UndeadPawn",
        "tags": [("chessboard", "zone")],
        "key": "Dark square of a chessboard",
        "desc": "|YOn the edge of the chessboard, a pawn stands nervously. Its small, skeletal frame is covered in patchy flesh, and it clutches a small, rusty dagger.",
    },
    # region Regular board
    (3, 1): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Light square of a chessboard",
        "desc": "|YOn the light square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (3, 2): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Dark square of a chessboard",
        "desc": "|YOn the dark square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (3, 3): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Light square of a chessboard",
        "desc": "|YOn the light square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (3, 4): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Dark square of a chessboard",
        "desc": "|YOn the dark square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (3, 5): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Light square of a chessboard",
        "desc": "|YOn the light square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (3, 6): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Dark square of a chessboard",
        "desc": "|YOn the dark square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (3, 7): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Light square of a chessboard",
        "desc": "|YOn the light square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (3, 8): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Dark square of a chessboard",
        "desc": "|YOn the dark square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
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
        "desc": "|YOn the light square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (6, 2): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Dark square of a chessboard",
        "desc": "|YOn the dark square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (6, 3): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Light square of a chessboard",
        "desc": "|YOn the dark square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (6, 4): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Dark square of a chessboard",
        "desc": "|YOn the dark square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (6, 5): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Light square of a chessboard",
        "desc": "|YOn the light square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (6, 6): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Dark square of a chessboard",
        "desc": "|YOn the light square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (6, 7): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Light square of a chessboard",
        "desc": "|YOn the light square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    (6, 8): {
        "typeclass": "typeclasses.chessboardrooms.ChessboardDecayingSkeleton",
        "tags": [("chessboard", "zone")],
        "key": "Dark square of a chessboard",
        "desc": "|YOn the dark square of the chessboard, a decaying skeleton lies sprawled, its bony fingers still clutching a rusted sword. The hollow eye sockets seem to stare into the void, and tattered remnants of armor cling to its frame, telling tales of battles long forgotten.",
    },
    # region  White pieces
    (7, 1): {
        "typeclass": "typeclasses.chessboardrooms.GnomePawn",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white pawn",
        "desc": "|YA diminutive gnome stands on the square of the chessboard, his eyes scanning the room for any sign of danger. The gnome's movements are swift and precise, and his small hands grip a blood-stained dagger, ready to strike at any moment.",
    },
    (7, 2): {
        "typeclass": "typeclasses.chessboardrooms.GnomePawn",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white pawn",
        "desc": "|YA small gnome pawn waits for orders on the square of the chessboard. His eyes dart around the room, looking for any sign of danger. The gnome stands ready to defend his allies.",
    },
    (7, 3): {
        "typeclass": "typeclasses.chessboardrooms.GnomePawn",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white pawn",
        "desc": "|YThe pawn is a small, gnome-like figure, its eyes scanning the room for any sign of danger. The gnome's movements are swift and precise, and his small hands grip a blood-stained dagger, ready to strike at any moment.",
    },
    (7, 4): {
        "typeclass": "typeclasses.chessboardrooms.GnomePawn",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white pawn",
        "desc": "|YThe gnome looks suprisingly fierce, his eyes scanning the chessboard for potential threats. His small stature belies his strength. ",
    },
    (7, 5): {
        "typeclass": "typeclasses.chessboardrooms.GnomePawn",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white pawn",
        "desc": "|YThe gnome stands guard on the square of the chessboard, his eyes scanning the room for any sign of danger. Loyal to his king and queen, the gnome is ready to defend his allies at a moment's notice.",
    },
    (7, 6): {
        "typeclass": "typeclasses.chessboardrooms.GnomePawn",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white pawn",
        "desc": "|YThe gnome stands ready to battle the undead forces on the square of the chessboard. His eyes are sharp and alert, and his movements are swift and precise. ",
    },
    (7, 7): {
        "typeclass": "typeclasses.chessboardrooms.GnomePawn",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white pawn",
        "desc": "|YThe gnome stands with his allies, ready to protect the king and queen. The undead forces will not get past him.",
    },
    (7, 8): {
        "typeclass": "typeclasses.chessboardrooms.GnomePawn",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white pawn",
        "desc": "|YRecruited from Steamfont Mountains, the gnome is ready to aid the dwarves in their battle against the undead. His eyes are sharp and alert, and his movements are swift and precise.",
    },
    (8, 1): {
        "typeclass": "typeclasses.chessboardrooms.DwarfRook",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white rook",
        "desc": "|YA dwarven warrior stands on the square of the chessboard, his armor gleaming in the dim light. His eyes are sharp and alert, and his movements are swift and precise. The dwarf's axe is stained with blood, and he looks around with a sense of authority, ready to defend his allies at a moment's notice.",
    },
    (8, 2): {
        "typeclass": "typeclasses.chessboardrooms.HighElfKnight",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white knight",
        "desc": "|YOn the square of the chessboard, a high elf knight stands proudly. His armor is finely crafted, and his eyes gleam with a fierce intelligence. The knight's movements are swift and graceful, and his sword is sharp and deadly.",
    },
    (8, 3): {
        "typeclass": "typeclasses.chessboardrooms.WoodElfBishop",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white bishop",
        "desc": "|YThe bishop is a tall, slender figure, his body covered in finely crafted armor. The elf protects the king and queen with his life, his fierce eyes scanning the room for any sign of danger.",
    },
    (8, 4): {
        "typeclass": "typeclasses.chessboardrooms.WoodElfQueen",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white queen",
        "desc": "|YThe queen is a tall, regal figure, her body covered in finely crafted armor. Her eyes gleam with a fierce intelligence, and her movements are swift and graceful. The queen is a formidable opponent, and she will stop at nothing to protect her king.",
    },
    (8, 5): {
        "typeclass": "typeclasses.chessboardrooms.HighElfKing",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white king",
        "desc": "|YThe king looks regal and imposing, his body covered in finely crafted armor. His eyes gleam with a fierce intelligence, and his movements are swift and precise. The king is a formidable opponent, and he will stop at nothing to protect his queen.",
    },
    (8, 6): {
        "typeclass": "typeclasses.chessboardrooms.WoodElfBishop",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white bishop",
        "desc": "|YThe elven bishop looks around the room with a sense of authority, his eyes scanning for any sign of danger. His movements are swift and graceful, and his sword is sharp and deadly.",
    },
    (8, 7): {
        "typeclass": "typeclasses.chessboardrooms.HighElfKnight",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white knight",
        "desc": "|YOn the square of the chessboard, a high elf knight stands proudly. His armor is finely crafted, and his eyes gleam with a fierce intelligence. The knight's movements are swift and graceful, and his sword is sharp and deadly.",
    },
    (8, 8): {
        "typeclass": "typeclasses.chessboardrooms.DwarfRook",
        "tags": [("chessboard", "zone")],
        "key": "Square of a white rook",
        "desc": "|YA dwarven warrior stands on the square of the chessboard, his armor gleaming in the dim light. His eyes are sharp and alert, and his movements are swift and precise. The dwarf's axe is stained with blood, and he looks around with a sense of authority, ready to defend his allies at a moment's notice.",
    },
}


XYMAP_DATA = {
    "zcoord": "chessboard",
    "map": MAP1,
    # "legend": LEGEND,
    "prototypes": PROTOTYPES,
    # "options": {"map_visual_range": 1},
}
