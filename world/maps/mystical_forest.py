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
       | | | | | |
 2   #-#-#-#-#-#-#
     | | | | | | |
 1   #-#-#-#-#-#-#-#
       | | | | | |
 0   #-#-#-#-#-#-#

 + 0 1 2 3 4 5 6 7 8 9 0
                       1
"""
PROTOTYPES = {
    
    (1, 0): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.LargeRat",
        "tags": [("newbieland", "zone")],
        "key": "Mystic Entrance",
        "desc": "|YYou stand at the entrance of the Mystical Forest. The path ahead is lined with ancient trees whose leaves shimmer with a faint, magical glow. The air is filled with the scent of blooming flowers and the promise of adventure.|n",
    },
    (2, 0): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.Firebeetle",
        "tags": [("newbieland", "zone")],
        "key": "Shimmering Pathway",
        "desc": "|YThe pathway here is illuminated by glowing stones embedded in the ground. The light creates a magical ambiance, guiding you deeper into the forest.|n",
    },
    (3, 0): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.MossSnake",
        "tags": [("newbieland", "zone")],
        "key": "Luminous Clearing",
        "desc": "|YYou find yourself in a clearing bathed in an ethereal light. The ground is covered in soft moss, and the air is filled with the gentle hum of nature.|n",
    },
    (4, 0): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.GoblinScout",
        "tags": [("newbieland", "zone")],
        "key": "Enchanted Brook",
        "desc": "|YA small brook flows through this part of the forest, its waters sparkling in the light. The sound of flowing water is soothing and calming.|n",
    },
    (5, 0): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.DecayingSkeleton",
        "tags": [("newbieland", "zone")],
        "key": "Twilight Grove",
        "desc": "|YThis grove is perpetually bathed in twilight, with the sky a deep indigo and stars twinkling above. The atmosphere is peaceful and serene.|n",
    },
    (6, 0): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.MossSnake",
        "tags": [("newbieland", "zone")],
        "key": "Moonlit Glade",
        "desc": "|YA glade illuminated by the soft glow of the moon. The light creates a magical ambiance, casting long shadows on the ground.|n",
    },
    (7, 0): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.Firebeetle",
        "tags": [("newbieland", "zone")],
        "key": "Starfall Meadow",
        "desc": "|YA wide meadow where the stars seem to fall from the sky, creating a breathtaking display of light. The air is filled with the scent of fresh grass and blooming flowers.|n",
    },
    (8, 0): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.Firebeetle",
        "tags": [("newbieland", "zone")],
        "key": "Eldertree Sanctuary",
        "desc": "|YAn enormous, ancient tree stands here, its branches spreading wide and its trunk thick with age. The tree exudes a sense of wisdom and power.|n",
    },

    
    (1, 1): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.MossSnake",
        "tags": [("newbieland", "zone")],
        "key": "Glowing Glade",
        "desc": "|YYou find yourself in a serene clearing where the trees part to reveal a sky filled with twinkling stars, even during the day. The ground is covered in soft moss, and the air is filled with the gentle hum of nature.|n",
    },
    (2, 1): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.GoblinScout",
        "tags": [("newbieland", "zone")],
        "key": "Enchanted Grove",
        "desc": "|YThis area is dense with ancient trees, their leaves shimmering with a faint magical glow. The air is thick with the scent of blooming flowers and magical energy.|n",
    },
    (3, 1): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.MossSnake",
        "tags": [("newbieland", "zone")],
        "key": "Whispering Woods",
        "desc": "|YThe trees here seem to whisper secrets to those who listen closely. The atmosphere is mysterious, with shadows dancing between the trunks.|n",
    },
    (4, 1): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.GoblinScout",
        "tags": [("newbieland", "zone")],
        "key": "Crystal Stream",
        "desc": "|YA sparkling stream winds through this part of the forest, its waters reflecting the vibrant colors of the flora. The sound of flowing water is soothing and calming.|n",
    },
    (5, 1): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.GoblinScout",
        "tags": [("newbieland", "zone")],
        "key": "Ancient Ruins",
        "desc": "|YThe remnants of an old civilization are scattered here, overgrown with vines and moss. The ruins hint at the forest's long and mysterious history.|n",
    },
    (6, 1): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.MossSnake",
        "tags": [("newbieland", "zone")],
        "key": "Mystic Clearing",
        "desc": "|YThis clearing is bathed in an ethereal light, with glowing flowers and plants that seem to pulse with magical energy. It's a place of tranquility and wonder.|n",
    },
    (7, 1): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.GoblinScout",
        "tags": [("newbieland", "zone")],
        "key": "Fairy Circle",
        "desc": "|YA ring of mushrooms forms a fairy circle here. The air is filled with the soft laughter of unseen fairies, and the ground sparkles with fairy dust.|n",
    },
    (8, 1): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.GoblinScout",
        "tags": [("newbieland", "zone")],
        "key": "Twilight Glade",
        "desc": "|YThis glade is perpetually bathed in twilight, with the sky a deep indigo and stars twinkling above. The atmosphere is peaceful and serene.|n",
    },
    
    (1, 2): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.GoblinScout",
        "tags": [("newbieland", "zone")],
        "key": "Moonlit Path",
        "desc": "|YA narrow path illuminated by the soft glow of the moon winds through the trees. The light creates a magical ambiance, casting long shadows on the ground.|n",
    },
    (2, 2): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.Firebeetle",
        "tags": [("newbieland", "zone")],
        "key": "Sunlit Meadow",
        "desc": "|YA wide meadow bathed in sunlight, with wildflowers swaying gently in the breeze. The air is filled with the scent of fresh grass and blooming flowers.|n",
    },
    (3, 2): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.GoblinScout",
        "tags": [("newbieland", "zone")],
        "key": "Hidden Hollow",
        "desc": "|YA secluded hollow hidden among the trees. The ground is soft and covered in fallen leaves, and the air is cool and refreshing.|n",
    },
    (4, 2): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.Firebeetle",
        "tags": [("newbieland", "zone")],
        "key": "Mystic Pond",
        "desc": "|YA small pond with crystal-clear water that reflects the surrounding trees and sky. The water is said to have magical properties.|n",
    },
    (5, 2): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.GoblinScout",
        "tags": [("newbieland", "zone")],
        "key": "Elder Tree",
        "desc": "|YAn enormous, ancient tree stands here, its branches spreading wide and its trunk thick with age. The tree exudes a sense of wisdom and power.|n",
    },
    (6, 2): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.GoblinScout",
        "tags": [("newbieland", "zone")],
        "key": "Enchanted Thicket",
        "desc": "|YA dense thicket where the trees and bushes are intertwined, creating a natural maze. The air is filled with the sounds of rustling leaves and distant animal calls.|n",
    },
    (7, 2): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.Firebeetle",
        "tags": [("newbieland", "zone")],
        "key": "Glimmering Falls",
        "desc": "|YA beautiful waterfall cascades down a rocky cliff, its waters sparkling in the light. The sound of the falls is both powerful and soothing.|n",
    },
    (8, 2): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.GoblinScout",
        "tags": [("newbieland", "zone")],
        "key": "Ancient Archway",
        "desc": "|YAn old stone archway stands here, covered in moss and vines. It looks like it once led to a grand structure, now long gone.|n",
    },
    
    (1, 3): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.Firebeetle",
        "tags": [("newbieland", "zone")],
        "key": "Hidden Hollow",
        "desc": "|YA secluded hollow hidden among the trees. The ground is soft and covered in fallen leaves, and the air is cool and refreshing.|n",
    },
    (2, 3): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.DecayingSkeleton",
        "tags": [("newbieland", "zone")],
        "key": "Mystic Pond",
        "desc": "|YA small pond with crystal-clear water that reflects the surrounding trees and sky. The water is said to have magical properties.|n",
    },
    (3, 3): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.GoblinScout",
        "tags": [("newbieland", "zone")],
        "key": "Elder Tree",
        "desc": "|YAn enormous, ancient tree stands here, its branches spreading wide and its trunk thick with age. The tree exudes a sense of wisdom and power.|n",
    },
    (4, 3): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.DecayingSkeleton",
        "tags": [("newbieland", "zone")],
        "key": "Enchanted Thicket",
        "desc": "|YA dense thicket where the trees and bushes are intertwined, creating a natural maze. The air is filled with the sounds of rustling leaves and distant animal calls.|n",
    },
    (5, 3): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.GoblinScout",
        "tags": [("newbieland", "zone")],
        "key": "Glimmering Falls",
        "desc": "|YA beautiful waterfall cascades down a rocky cliff, its waters sparkling in the light. The sound of the falls is both powerful and soothing.|n",
    },
    (6, 3): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.DecayingSkeleton",
        "tags": [("newbieland", "zone")],
        "key": "Ancient Archway",
        "desc": "|YAn old stone archway stands here, covered in moss and vines. It looks like it once led to a grand structure, now long gone.|n",
    },
    (7, 3): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.GoblinScout",
        "tags": [("newbieland", "zone")],
        "key": "Moonlit Path",
        "desc": "|YA narrow path illuminated by the soft glow of the moon winds through the trees. The light creates a magical ambiance, casting long shadows on the ground.|n",
    },
    (8, 3): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.MossSnake",
        "tags": [("newbieland", "zone")],
        "key": "Sunlit Meadow",
        "desc": "|YA wide meadow bathed in sunlight, with wildflowers swaying gently in the breeze. The air is filled with the scent of fresh grass and blooming flowers.|n",
    },
    (1, 4): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.LargeRat",
        "tags": [("newbieland", "zone")],
        "key": "Starfall Meadow",
        "desc": "|YA wide meadow where the stars seem to fall from the sky, creating a breathtaking display of light. The air is filled with the scent of fresh grass and blooming flowers.|n",
    },
    (2, 4): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.MossSnake",
        "tags": [("newbieland", "zone")],
        "key": "Eldertree Sanctuary",
        "desc": "|YAn enormous, ancient tree stands here, its branches spreading wide and its trunk thick with age. The tree exudes a sense of wisdom and power.|n",
    },
    (3, 4): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.LargeRat",
        "tags": [("newbieland", "zone")],
        "key": "Mystic Entrance",
        "desc": "|YYou stand at the entrance of the Mystical Forest. The path ahead is lined with ancient trees whose leaves shimmer with a faint, magical glow. The air is filled with the scent of blooming flowers and the promise of adventure.|n",
    },
    (4, 4): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.MossSnake",
        "tags": [("newbieland", "zone")],
        "key": "Shimmering Pathway",
        "desc": "|YThe pathway here is illuminated by glowing stones embedded in the ground. The light creates a magical ambiance, guiding you deeper into the forest.|n",
    },
    (5, 4): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.LargeRat",
        "tags": [("newbieland", "zone")],
        "key": "Luminous Clearing",
        "desc": "|YYou find yourself in a clearing bathed in an ethereal light. The ground is covered in soft moss, and the air is filled with the gentle hum of nature.|n",
    },
    (6, 4): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.LargeRat",
        "tags": [("newbieland", "zone")],
        "key": "Enchanted Brook",
        "desc": "|YA small brook flows through this part of the forest, its waters sparkling in the light. The sound of flowing water is soothing and calming.|n",
    },
    (7, 4): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.MossSnake",
        "tags": [("newbieland", "zone")],
        "key": "Twilight Grove",
        "desc": "|YThis grove is perpetually bathed in twilight, with the sky a deep indigo and stars twinkling above. The atmosphere is peaceful and serene.|n",
    },
    (8, 4): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.mystical_forest_rooms.LargeRat",
        "tags": [("newbieland", "zone")],
        "key": "Moonlit Glade",
        "desc": "|YA glade illuminated by the soft glow of the moon. The light creates a magical ambiance, casting long shadows on the ground.|n",
    }

}



XYMAP_DATA = {
    "zcoord": "mystical_forest",
    "map": MAP1,
    # "legend": LEGEND,
    "prototypes": PROTOTYPES,
    # "options": {"map_visual_range": 1},
}
