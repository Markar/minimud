# This is a map of the Crushbone zone, a zone filled with orcs and slavers.

from evennia.contrib.grid.xyzgrid import xymap_legend

MAP1 = r"""
                       1
 + 0 1 2 3 4 5 6 7 8 9 0

 6     #-#-#-#-#-#
       |   |   | |
 5   #-#-#-#-#-#-#-#-#-#
     | | |       \ | | |\
 4   #-#-# #-#-#   #-#-#-#-#
     |     | | |       | | |
 3   #-#   #-#-#-#-#-#-#-#-#
     | |   | | |       | | |
 2   #-#   #-#-#   #-#-#-#-#
     | |           | | |/
 1   #-#-#-#-#-#-#-#-#-#
           | 
 0         #
 
 + 0 1 2 3 4 5 6 7 8 9 0 1 2
                       1 1 1
"""

PROTOTYPES = {
    # entrance
    (4, 0): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Orc Camp Entrance",
        "desc": "|YThe entrance to the orc camp, surrounded by crude huts and a small river. Orc pawns stand guard, watching for intruders. The sound of clashing weapons and orcish laughter fills the air. A wooden signpost points to the various areas of the camp. To the north is the training grounds, where orc taskmasters drill their underlings. To the east is the slaver's camp, where orc slavers plot their next raid. On an island is the castle, where the orc lords hold their meetings. And to the west is the riverbank, where orc pawns patrol the water's edge.",
    },
    # first row
    (1, 1): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_PAWN",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Riverbank West",
        "desc": "|YThe western edge of the river, with orc pawns patrolling the area.",
    },
    (2, 1): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_PAWN",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Riverbank Southwest",
        "desc": "|YThe southwestern bend of the river, where orc pawns keep watch.",
    },
    (3, 1): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "spawn_proto": "ORC_PAWN",
        "tags": [("crushbone", "zone")],
        "key": "Orc Camp",
        "desc": "|YA bustling camp with orc huts and a river running through it.",
    },
    (4, 1): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "spawn_proto": "ORC_PAWN",
        "tags": [("crushbone", "zone")],
        "key": "Training Ground",
        "desc": "|YA training ground on a hill where orcs practice their combat skills.",
    },
    (5, 1): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "spawn_proto": "ORC_PAWN",
        "tags": [("crushbone", "zone")],
        "key": "Training Ground",
        "desc": "|YA training ground on a hill where orcs practice their combat skills.",
    },
    (6, 1): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "spawn_proto": "ORC_SLAVER",
        "tags": [("crushbone", "zone")],
        "key": "Slaver's Hall",
        "desc": "|YA large hall where orc slavers gather and plan their raids.",
    },
    (7, 1): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "spawn_proto": "ORC_TASKMASTER",
        "tags": [("crushbone", "zone")],
        "key": "Training Grounds",
        "desc": "|YAn open area north of the camp where orc taskmasters train their underlings.",
    },
    (8, 1): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "spawn_proto": "ORC_TASKMASTER",
        "tags": [("crushbone", "zone")],
        "key": "Training Grounds",
        "desc": "|YAn open area north of the camp where orc taskmasters train their underlings.",
    },
    (9, 1): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_TASKMASTER",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Training Grounds",
        "desc": "|YAn open area north of the camp where orc taskmasters train their underlings.",
    },
    (10, 1): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_TASKMASTER",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Training Grounds",
        "desc": "|YAn open area north of the camp where orc taskmasters train their underlings.",
    },
    # second row
    (1, 2): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_PAWN",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "River Crossing",
        "desc": "|YA wooden bridge crossing the river, guarded by orc pawns.",
    },
    (2, 2): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_PAWN",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Riverbank North",
        "desc": "|YThe northern side of the river, where orc centurions patrol.",
    },
    (4, 2): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_LORD",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Council Chamber",
        "desc": "|YA chamber where the orc lords hold council meetings.",
    },
    (5, 2): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_LORD",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Lord's Hall",
        "desc": "|YA grand hall where the orc lords gather to discuss matters of the realm.",
    },
    (6, 2): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_EMISSARY",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Emissary's Office",
        "desc": "|YThe office of the orc emissary, where diplomatic matters are handled.",
    },
    (8, 2): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_TASKMASTER",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Training Grounds",
        "desc": "|YAn open area north of the camp where orc taskmasters train their underlings.",
    },
    (9, 2): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_TASKMASTER",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Training Grounds",
        "desc": "|YAn open area north of the camp where orc taskmasters train their underlings.",
    },
    (10, 2): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_TASKMASTER",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Training Grounds",
        "desc": "|YAn open area north of the camp where orc taskmasters train their underlings.",
    },
    (11, 2): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_SLAVER",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Slaver's Camp",
        "desc": "|YA camp filled with tents where orc slavers rest and plan their next moves.",
    },
    (12, 2): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_SLAVER",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Slaver's Camp",
        "desc": "|YA camp filled with tents where orc slavers rest and plan their next moves.",
    },
    # third row
    (1, 3): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_CENTURION",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Wooden Building",
        "desc": "|YAnother small wooden building, serving as a barracks for orc centurions.",
    },
    (2, 3): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_CENTURION",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Wooden Building",
        "desc": "|YA small wooden building used by orc centurions for storage.",
    },
    (4, 3): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_EMPEROR",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Western wall of the castle",
        "desc": "|YTall stone walls surround the castle, with high ranking orcs patrolling the area. The sound of clashing weapons can be heard from within.",
    },
    (5, 3): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_LORD",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Lord's Hall",
        "desc": "|YA grand hall where the orc lords gather to discuss matters of the realm.",
    },
    (6, 3): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_LEGIONNAIRE",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Legionnaire's Post",
        "desc": "|YA heavily fortified post where the orc legionnaires stand watch. The castle is more heavily guarded than expected.",
    },
    (7, 3): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_LEGIONNAIRE",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Legionnaire's Bridge",
        "desc": "|YA sturdy wooden bridge spanning the river, heavily guarded by orc legionnaires. The sound of the rushing water below is almost drowned out by the clanking of armor and the stern commands of the legionnaires.",
    },
    (8, 3): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_LEGIONNAIRE",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Legionnaire's Bridge",
        "desc": "|YA sturdy wooden bridge spanning the river, heavily guarded by orc legionnaires. The sound of the rushing water below is almost drowned out by the clanking of armor and the stern commands of the legionnaires.",
    },
    (9, 3): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "spawn_proto": "ORC_LEGIONNAIRE",
        "tags": [("crushbone", "zone")],
        "key": "Legionnaire's Bridge",
        "desc": "|YA sturdy wooden bridge spanning the river, heavily guarded by orc legionnaires. The sound of the rushing water below is almost drowned out by the clanking of armor and the stern commands of the legionnaires.",
    },
    (10, 3): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_LEGIONNAIRE",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Before a bridge",
        "desc": "|YThe center of the orc zone, before a bridge to a formidable castle where the strongest orcs reside.",
    },
    (11, 3): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_TASKMASTER",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Training Grounds",
        "desc": "|YAn open area north of the camp where orc taskmasters train their underlings.",
    },
    (12, 3): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_TASKMASTER",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Training Grounds",
        "desc": "|YAn open area north of the camp where orc taskmasters train their underlings.",
    },
    # fourth row
    (1, 4): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_CENTURION",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Riverbank North",
        "desc": "|YThe northern side of the river, where orc centurions patrol.",
    },
    (2, 4): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_SLAVER",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Slaver's Camp",
        "desc": "|YA camp filled with tents where orc slavers rest and plan their next moves.",
    },
    (3, 4): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_TASKMASTER",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Tunnel Entrance",
        "desc": "|YThe entrance to the eastern tunnels, guarded by orc taskmasters.",
    },
    (4, 4): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_LORD",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "A royal chamber",
        "desc": "|YA chamber where the orc lords hold council meetings. The room is filled with the sound of orcish laughter and the clinking of goblets.",
    },
    (5, 4): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_ROYAL_GUARD",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Royal Guard Post",
        "desc": "|YA heavily fortified post where the orc royal guards stand watch.",
    },
    (6, 4): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_WARLORD",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Warlord's Quarters",
        "desc": "|YThe private quarters of an orc warlord, filled with trophies from past battles.",
    },
    (8, 4): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_CENTURION",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Riverbank Northeast",
        "desc": "|YThe northeastern bend of the river, where orc centurions roam amongst taskmasters and slavers.",
    },
    (9, 4): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_CENTURION",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Wooden Building ",
        "desc": "|YA small wooden building used by orc centurions for storage.",
    },
    (10, 4): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_CENTURION",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Wooden Building",
        "desc": "|YA small wooden building used by orc centurions for storage. The sound of clashing weapons can be heard from within.",
    },
    (11, 4): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_SLAVER",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Slaver's Camp",
        "desc": "|YA camp filled with tents where orc slavers rest and plan their next moves.",
    },
    (12, 4): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_SLAVER",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Slaver's Camp",
        "desc": "|YOrc slavers gather here to discuss their next raid. The sound of clinking chains can be heard from within the tents.",
    },
    # fifth row
    (1, 5): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_SLAVER",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Riverbank Northwest",
        "desc": "|YThe northwest edge of the river, where orc slavers keep a watchful eye on the waterway.",
    },
    (2, 5): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_CENTURION",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Riverbank North",
        "desc": "|YThe northern side of the river, where orc centurions patrol.",
    },
    (3, 5): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_SLAVER",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Slaver's Hall",
        "desc": "|YA large hall where orc slavers gather and plan their raids.",
    },
    (4, 5): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_LEGIONNAIRE",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Northern Riverbank",
        "desc": "|YThe northern bank of the river, where orc legionnaires stand vigilant. The sound of the river's flow is a constant backdrop to their watchful presence.",
    },
    (5, 5): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_LEGIONNAIRE",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Northern Watchtower",
        "desc": "|YA tall watchtower offering a strategic view of the surrounding area. Orc legionnaires keep a constant lookout for any signs of intruders.",
    },
    (6, 5): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_LEGIONNAIRE",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Northern Patrol Route",
        "desc": "|YA well-trodden path where orc legionnaires patrol regularly. The route is lined with torches that flicker ominously in the night.",
    },
    (7, 5): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_LEGIONNAIRE",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Northern Riverbank",
        "desc": "|YThe northern bank of the river, where orc legionnaires stand vigilant. The sound of the river's flow is a constant backdrop to their watchful presence.",
    },
    (8, 5): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_CENTURION",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Riverbank North",
        "desc": "|YThe northern side of the river, where orc centurions patrol.",
    },
    (9, 5): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_CENTURION",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Riverbank North",
        "desc": "|YThe northern side of the river, where orc centurions patrol.",
    },
    (10, 5): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_CENTURION",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Riverbank North",
        "desc": "|YThe northern side of the river, where orc centurions patrol.",
    },
    # sixth row
    (2, 6): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_CENTURION",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Centurion's Command Post",
        "desc": "|YA command post where orc centurions coordinate their strategies. The room is filled with maps and tactical plans.",
    },
    (3, 6): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_CENTURION",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Centurion's Quarters",
        "desc": "|YThe private quarters of an orc centurion, filled with trophies and battle gear. The room is sparsely furnished, with a large bed and a small desk.",
    },
    (4, 6): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_CENTURION",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Centurion's Armory",
        "desc": "|YAn armory stocked with weapons and armor for the orc centurions. The clang of metal echoes through the room as centurions prepare for battle.",
    },
    (5, 6): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_CENTURION",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Centurion's Training Hall",
        "desc": "|YA large hall where orc centurions train rigorously. The air is thick with the sounds of grunts and the clash of weapons.",
    },
    (6, 6): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_CENTURION",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Centurion's Barracks",
        "desc": "|YThe barracks where orc centurions rest and recover. The room is lined with sturdy bunks and the scent of leather and sweat fills the air.",
    },
    (7, 6): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_LEGIONNAIRE",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Northern Watchtower",
        "desc": "|YA tall watchtower offering a strategic view of the surrounding area. Orc legionnaires keep a constant lookout for any signs of intruders. Centurions and taskmasters can be seen patrolling the area below.",
    },
}

XYMAP_DATA = {
    "zcoord": "crushbone",
    "map": MAP1,
    # "legend": LEGEND,
    "prototypes": PROTOTYPES,
    # "options": {"map_visual_range": 1},
}


MAP_B = r"""
                       1
 + 0 1 2 3 4 5 6 7 8 9 0
 
 2   #-#-#
     | | |
 1   B-#-#
     | | |
 0   #-#-#

 + 0 1 2 3 4 5 6 7 8 9 0
                       1
"""
PROTOTYPES_MAP2 = {
    (1, 0): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "AMBASSADOR_DVINN",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("chessboard", "zone")],
        "key": "Ambassador's Quarters",
        "desc": "|YNear the throne of the orc emperor, the ambassador from the dark elves resides. The room is filled with dark tapestries and strange artifacts.",
    },
    (2, 0): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("chessboard", "zone")],
        "key": "Castle Crushbone.",
        "desc": "|YA small alcove in the second floor of castle Crushbone. The walls are lined with tapestries and the floor is covered in a thick red carpet.",
    },
    (3, 0): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "LORD_DARISH",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("chessboard", "zone")],
        "key": "Lord Darish's Quarters",
        "desc": "|YThe quarters of Lord Darish, a powerful orc warrior. He is here to discuss matters of the realm with the orc emperor.",
    },
    (1, 1): {
        "prototype_parent": "xyz_room",
        "spawn_proto": [
            {"name": "ORC_EMPEROR", "count": 1, "chance": 15, "returnEarly": True},
            {"name": "ORC_ORACLE", "count": 1, "chance": 100},
        ],
        "typeclass": "typeclasses.rooms.SpecialMobRoom",
        "tags": [("crushbone", "zone")],
        "key": "Emperor's Throne Room",
        "desc": "|YThe majestic throne room of the orc emperor, adorned with banners and treasures. The orc oracle is here, performing a ritual to divine the future of the realm. The emperor sits on his throne, listening intently to the oracle's words.",
    },
    (2, 1): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("chessboard", "zone")],
        "key": "The Great Hall",
        "desc": "|YThe great hall of castle Crushbone, where the orc lords gather to discuss matters of the realm. There is a feast laid out on a long table, with goblets of wine and platters of roasted meat.",
    },
    (3, 1): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("chessboard", "zone")],
        "key": "Above the drawbridge",
        "desc": "|YOverlooking the orc camp, a window in the castle wall provides a view of the surrounding area. The drawbridge can be seen below, with orc legionnaires patrolling the area.",
    },
    (1, 2): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_EMISSARY",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("chessboard", "zone")],
        "key": "Emissary's Office",
        "desc": "|YThe office of the orc emissary, where diplomatic matters are handled. The room is filled with maps and scrolls, detailing the orc's alliances and enemies.",
    },
    (2, 2): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "ORC_ROYAL_GUARD",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("chessboard", "zone")],
        "key": "Royal Guard Post",
        "desc": "|YThe royal guard post, where the orc royal guards stand watch. The room is filled with weapons and armor, and the guards are armed to the teeth. They stand at attention, ready to defend the emperor at a moment's notice.",
    },
    (3, 2): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("chessboard", "zone")],
        "key": "Stairwell to the second floor",
        "desc": "|YThere is a stairwell leading down to the first floor of the castle. You can hear the sound of orcish voices echoing up from below. Against the west wall is a large tapestry depicting a battle between orcs and humans.",
    },
}


class MobNode(xymap_legend.MapNode):
    prototype = {
        "prototype_parent": "xyz_room",
        "key": "Inside",
        "desc": "A mob in Mobland.",
    }


LEGEND = {
    "B": MobNode,
}

XYMAP_DATA_MAP2 = {
    "map": MAP_B,
    "zcoord": "crushbone_second_level",
    "prototypes": PROTOTYPES_MAP2,
    "legend": LEGEND,
    # "options": {"map_visual_range": 1, "map_mode": "scan"},
}


XYMAP_DATA_LIST = [XYMAP_DATA, XYMAP_DATA_MAP2]
