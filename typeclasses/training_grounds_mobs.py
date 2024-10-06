"""
Prototypes
"""

from random import randint, uniform, choice


NOVICE_GOBLIN = {
    "spawn_proto": "NOVICE_GOBLIN",
    "typeclass": "typeclasses.characters.NPC",
    "key": "a novice goblin",
    "aliases": ["goblin"],
    "desc": "A small, green-skinned goblin wielding a crude dagger. It looks eager to prove itself in combat.",
    "gender": "male",
    "react_as": "aggressive",
    "armor": 3,
    "name_color": "g",
    "level": 8,
    "hp": 80,
    "hpmax": 80,
    "str": 8,
    "natural_weapon": {
        "name": "dagger",
        "damage_type": "edged",
        "damage": 6,
        "speed": 3,
        "energy_cost": 8,
    },
    "exp_reward": 2800,
    "drops": [
        {
            "key": "crude dagger",
            "aliases": ["dagger"],
            "desc": "A small, crude dagger used by goblins.",
            "name_color": "w",
            "dmg": 5,
            "speed": 2,
            "value": 25,
        }
    ],
    "can_attack": True,
}

ROGUE_APPRENTICE = {
    "spawn_proto": "ROGUE_APPRENTICE",
    "typeclass": "typeclasses.characters.NPC",
    "key": "a rogue apprentice",
    "aliases": ["rogue"],
    "desc": "A nimble rogue apprentice, skilled in stealth and quick strikes.",
    "gender": "female",
    "react_as": "aggressive",
    "armor": 5,
    "name_color": "b",
    "level": 8,
    "hp": 96,
    "hpmax": 96,
    "str": 12,
    "natural_weapon": {
        "name": "short sword",
        "damage_type": "edged",
        "damage": 10,
        "speed": 4,
        "energy_cost": 12,
    },
    "exp_reward": 3000,
    "drops": [
        {
            "key": "short sword",
            "aliases": ["sword"],
            "desc": "A sharp short sword used by rogue apprentices.",
            "name_color": "w",
            "dmg": 10,
            "speed": 3,
            "value": 25,
        }
    ],
    "can_attack": True,
}

SKELETAL_WARRIOR = {
    "spawn_proto": "SKELETAL_WARRIOR",
    "typeclass": "typeclasses.characters.NPC",
    "key": "a skeletal warrior",
    "aliases": ["skeleton"],
    "desc": "A reanimated skeleton wielding a rusted sword. Its bones clatter with each movement.",
    "gender": "neutral",
    "react_as": "aggressive",
    "armor": 8,
    "name_color": "w",
    "level": 10,
    "hp": 160,
    "hpmax": 10,
    "str": 18,
    "natural_weapon": {
        "name": "rusted sword",
        "damage_type": "edged",
        "damage": 14,
        "speed": 3,
        "energy_cost": 18,
    },
    "exp_reward": 4200,
    "drops": [
        {
            "key": "rusted sword",
            "aliases": ["sword"],
            "desc": "A rusted sword wielded by a skeletal warrior.",
            "name_color": "w",
            "power": 10,
            "dmg": 11,
            "speed": 3,
            "value": 50,
        }
    ],
    "can_attack": True,
}

NOVICE_MAGE = {
    "spawn_proto": "NOVICE_MAGE",
    "typeclass": "typeclasses.characters.NPC",
    "key": "a novice mage",
    "aliases": ["mage"],
    "desc": "A novice mage practicing basic spells. It wields a simple wooden staff.",
    "gender": "female",
    "react_as": "aggressive",
    "armor": 4,
    "name_color": "m",
    "level": 10,
    "hp": 90,
    "hpmax": 90,
    "str": 10,
    "natural_weapon": {
        "name": "magic bolt",
        "damage_type": "magic",
        "damage": 8,
        "speed": 5,
        "energy_cost": 10,
    },
    "exp_reward": 3200,
    "drops": [
        {
            "key": "wooden staff",
            "aliases": ["staff"],
            "desc": "A simple wooden staff used by novice mages.",
            "name_color": "w",
            "power": 8,
            "dmg": 7,
            "speed": 4,
            "value": 30,
        }
    ],
    "can_attack": True,
}


MALFUNCTIONING_ROBOT = {
    "spawn_proto": "MALFUNCTIONING_ROBOT",
    "typeclass": "typeclasses.characters.NPC",
    "key": "a malfunctioning robot",
    "aliases": ["robot"],
    "desc": "A malfunctioning robot with sparks flying from its joints. It moves erratically, making it unpredictable in combat.",
    "gender": "neutral",
    "react_as": "aggressive",
    "armor": 6,
    "name_color": "y",
    "level": 10,
    "hp": 100,
    "hpmax": 100,
    "str": 12,
    "natural_weapon": {
        "name": "metal fists",
        "damage_type": "blunt",
        "damage": 10,
        "speed": 3,
        "energy_cost": 12,
    },
    "exp_reward": 5000,
    "drops": [
        {
            "key": "robotic component",
            "aliases": ["component"],
            "desc": "A piece of the malfunctioning robot, still sparking with energy.",
            "name_color": "w",
            "power": 10,
            "value": 10,
        }
    ],
    "can_attack": True,
}

CYBER_SOLDIER = {
    "spawn_proto": "CYBER_SOLDIER",
    "typeclass": "typeclasses.characters.NPC",
    "key": "a cybernetic soldier",
    "aliases": ["soldier"],
    "desc": "A cybernetic soldier equipped with advanced armor and weaponry. Its movements are precise and calculated.",
    "gender": "male",
    "react_as": "aggressive",
    "armor": 10,
    "name_color": "b",
    "level": 11,
    "hp": 150,
    "hpmax": 150,
    "str": 18,
    "natural_weapon": {
        "name": "plasma rifle",
        "damage_type": "energy",
        "damage": 15,
        "speed": 4,
        "energy_cost": 18,
    },
    "exp_reward": 5500,
    "drops": [
        {
            "key": "plasma rifle",
            "aliases": ["rifle"],
            "desc": "An advanced plasma rifle used by cybernetic soldiers.",
            "name_color": "b",
            "power": 20,
            "dmg": 14,
            "speed": 3,
            "value": 50,
        }
    ],
    "can_attack": True,
}

ALIEN_SCOUT = {
    "spawn_proto": "ALIEN_SCOUT",
    "typeclass": "typeclasses.characters.NPC",
    "key": "an alien scout",
    "aliases": ["alien"],
    "desc": "An alien scout with glowing eyes and sleek, otherworldly armor. It moves with agility and grace, making it a formidable opponent.",
    "gender": "neutral",
    "react_as": "aggressive",
    "armor": 8,
    "name_color": "g",
    "level": 10,
    "hp": 130,
    "hpmax": 130,
    "str": 16,
    "natural_weapon": {
        "name": "energy blade",
        "damage_type": "energy",
        "damage": 14,
        "speed": 5,
        "energy_cost": 16,
    },
    "exp_reward": 4800,
    "drops": [
        {
            "key": "alien energy core",
            "aliases": ["core"],
            "desc": "A glowing energy core from the alien scout.",
            "name_color": "g",
            "power": 15,
            "value": 15,
        }
    ],
    "can_attack": True,
}
