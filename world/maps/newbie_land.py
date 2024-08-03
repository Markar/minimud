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
        "key": "A sparring arena",
        "desc": "You find yourself in a spacious sparring arena, with padded floors and walls to ensure safety. Training dummies and holographic targets are scattered around, ready for practice.",
    },
    (2, 1): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("newbieland", "zone")],
        "key": "A weapon training room",
        "desc": "This room is filled with racks of various weapons, from swords to energy blasters. Trainers are available to guide you through different combat techniques and weapon handling.",
    },
    (3, 1): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("newbieland", "zone")],
        "key": "A tactical training area",
        "desc": "The tactical training area is designed for strategy and teamwork exercises. Obstacles and cover points are set up to simulate real combat scenarios.",
    },
    (4, 1): {
        "typeclass": "typeclasses.rooms.NewbieLargeRat",
        "tags": [("newbieland", "zone")],
        "key": "A defensive training zone",
        "desc": "This zone focuses on defensive maneuvers and techniques. Shields and barriers are available for practice, and instructors demonstrate how to effectively block and parry attacks.",
    },
    (5, 1): {
        "typeclass": "typeclasses.rooms.NewbieSnake",
        "tags": [("newbieland", "zone")],
        "key": "An agility training course",
        "desc": "The agility training course is filled with obstacles designed to test your speed and reflexes. From climbing walls to dodging moving targets, this area helps improve your agility.",
    },
    (6, 1): {
        "typeclass": "typeclasses.rooms.NewbieLargeRat",
        "tags": [("newbieland", "zone")],
        "key": "A strength training room",
        "desc": "This room is equipped with weights and resistance machines to build your physical strength. Trainers are on hand to assist with proper form and technique.",
    },
    (7, 1): {
        "typeclass": "typeclasses.rooms.NewbieSnake",
        "tags": [("newbieland", "zone")],
        "key": "A magic training chamber",
        "desc": "The magic training chamber is filled with arcane symbols and enchanted objects. Here, you can practice your spells and magical abilities under the guidance of experienced mages.",
    },
    (8, 1): {
        "typeclass": "typeclasses.rooms.NewbieLargeRat",
        "tags": [("newbieland", "zone")],
        "key": "A meditation and recovery area",
        "desc": "After intense training, this area offers a peaceful environment for meditation and recovery. Soft mats and calming music help you relax and rejuvenate your mind and body.",
    },
        
    (1, 2): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("newbieland", "zone")],
        "key": "A combat simulation room",
        "desc": "This room is equipped with advanced holographic projectors that create realistic combat scenarios. Perfect for practicing your skills in a controlled environment.",
    },
    (2, 2): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("newbieland", "zone")],
        "key": "A melee training area",
        "desc": "The melee training area is filled with various melee weapons and dummies. Here, you can practice your close combat techniques under the guidance of experienced trainers.",
    },
    (3, 2): {
        "typeclass": "typeclasses.rooms.NewbieLargeRat",
        "tags": [("newbieland", "zone")],
        "key": "A ranged training zone",
        "desc": "This zone is designed for practicing ranged attacks. Targets of different sizes and distances are set up to help you improve your accuracy and precision.",
    },
    (4, 2): {
        "typeclass": "typeclasses.rooms.NewbieSnake",
        "tags": [("newbieland", "zone")],
        "key": "A stealth training room",
        "desc": "The stealth training room is dimly lit and filled with obstacles. Here, you can practice moving silently and avoiding detection.",
    },
    (5, 2): {
        "typeclass": "typeclasses.rooms.NewbieSnake",
        "tags": [("newbieland", "zone")],
        "key": "A magic practice area",
        "desc": "This area is dedicated to practicing magical spells and abilities. Enchanted targets and spellbooks are available to help you refine your magical prowess.",
    },
    (6, 2): {
        "typeclass": "typeclasses.rooms.NewbieLargeRat",
        "tags": [("newbieland", "zone")],
        "key": "A defensive tactics room",
        "desc": "The defensive tactics room is equipped with shields and barriers. Trainers demonstrate how to effectively use defensive maneuvers to protect yourself in combat.",
    },
    (7, 2): {
        "typeclass": "typeclasses.rooms.NewbieSnake",
        "tags": [("newbieland", "zone")],
        "key": "A healing and support training area",
        "desc": "This area focuses on healing and support skills. Practice your healing spells and learn how to support your allies in battle.",
    },
    (8, 2): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("newbieland", "zone")],
        "key": "A strategy and planning room",
        "desc": "The strategy and planning room is filled with maps and tactical boards. Here, you can plan your next moves and learn about different combat strategies.",
    },

    (1, 3): {
        "typeclass": "typeclasses.rooms.ChessboardDecayingSkeleton",
        "tags": [("newbieland", "zone")],
        "key": "A history and lore library",
        "desc": "This library contains books and scrolls about the history and lore of Millennium. A great place to learn about the world and its secrets.",
    },
    (2, 3): {
        "typeclass": "typeclasses.rooms.NewbieLargeRat",
        "tags": [("newbieland", "zone")],
        "key": "A creature study room",
        "desc": "The creature study room is filled with information about the various creatures you may encounter. Learn about their strengths, weaknesses, and behaviors.",
    },
    (3, 3): {
        "typeclass": "typeclasses.rooms.ChessboardDecayingSkeleton",
        "tags": [("newbieland", "zone")],
        "key": "A potion and alchemy lab",
        "desc": "This lab is equipped with all the tools and ingredients needed for potion-making and alchemy. Experiment with different recipes and create powerful concoctions.",
    },
    (4, 3): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("newbieland", "zone")],
        "key": "A combat tactics classroom",
        "desc": "In this classroom, experienced instructors teach various combat tactics and strategies. Learn how to outsmart your opponents and gain the upper hand in battle.",
    },
    (5, 3): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("newbieland", "zone")],
        "key": "A weapon crafting workshop",
        "desc": "The weapon crafting workshop is filled with tools and materials for creating and upgrading weapons. Learn the art of weapon crafting and enhance your arsenal.",
    },
    (6, 3): {
        "typeclass": "typeclasses.rooms.NewbieLargeRat",
        "tags": [("newbieland", "zone")],
        "key": "A survival skills training area",
        "desc": "This area focuses on essential survival skills. Learn how to find food, build shelters, and navigate the wilderness.",
    },
    (7, 3): {
        "typeclass": "typeclasses.rooms.ChessboardDecayingSkeleton",
        "tags": [("newbieland", "zone")],
        "key": "A first aid and medical training room",
        "desc": "The first aid and medical training room is equipped with medical supplies and training dummies. Learn how to provide first aid and treat injuries in the field.",
    },
    (8, 3): {
        "typeclass": "typeclasses.rooms.NewbieLargeRat",
        "tags": [("newbieland", "zone")],
        "key": "A communication and teamwork training area",
        "desc": "This area focuses on improving communication and teamwork skills. Practice working with others and learn how to coordinate effectively in combat.",
    },

    (1, 4): {
        "typeclass": "typeclasses.rooms.ChessboardGnollPup",
        "tags": [("newbieland", "zone")],
        "key": "A physical fitness training room",
        "desc": "The physical fitness training room is equipped with various exercise equipment. Improve your strength, endurance, and agility through rigorous workouts.",
    },
    (2, 4): {
        "typeclass": "typeclasses.rooms.NewbieLargeRat",
        "tags": [("newbieland", "zone")],
        "key": "A meditation and focus room",
        "desc": "This room provides a quiet space for meditation and focus exercises. Enhance your mental clarity and concentration.",
    },
    (3, 4): {
        "typeclass": "typeclasses.rooms.NewbieFirebeetle",
        "tags": [("newbieland", "zone")],
        "key": "A technology and gadget lab",
        "desc": "The technology and gadget lab is filled with advanced tech and gadgets. Learn how to use and create various technological devices.",
    },
    (4, 4): {
        "typeclass": "typeclasses.rooms.ChessboardGnoll",
        "tags": [("newbieland", "zone")],
        "key": "A combat simulation room",
        "desc": "This room is equipped with advanced holographic projectors that create realistic combat scenarios. Perfect for practicing your skills in a controlled environment.",
    },
    (5, 4): {
        "typeclass": "typeclasses.rooms.NewbieFirebeetle",
        "tags": [("newbieland", "zone")],
        "key": "A ranged training zone",
        "desc": "This zone is designed for practicing ranged attacks. Targets of different sizes and distances are set up to help you improve your accuracy and precision.",
    },
    (6, 4): {
        "typeclass": "typeclasses.rooms.NewbieLargeRat",
        "tags": [("newbieland", "zone")],
        "key": "A melee training area",
        "desc": "The melee training area is filled with various melee weapons and dummies. Here, you can practice your close combat techniques under the guidance of experienced trainers.",
    },
    (7, 4): {
        "typeclass": "typeclasses.rooms.NewbieFirebeetle",
        "tags": [("newbieland", "zone")],
        "key": "A defensive tactics room",
        "desc": "The defensive tactics room is equipped with shields and barriers. Trainers demonstrate how to effectively use defensive maneuvers to protect yourself in combat.",
    },
    (8, 4): {
        "typeclass": "typeclasses.rooms.NewbieLargeRat",
        "tags": [("newbieland", "zone")],
        "key": "A magic practice area",
        "desc": "This area is dedicated to practicing magical spells and abilities. Enchanted targets and spellbooks are available to help you refine your magical prowess.",
    }
}


XYMAP_DATA = {
    "zcoord": "newbieland",
    "map": MAP1,
    # "legend": LEGEND,
    "prototypes": PROTOTYPES,
    # "options": {"map_visual_range": 1},
}
