"""
Prototypes
"""
from random import randint, choice

LARGE_RAT = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "a large rat",
    "aliases": ["rat"],
    "tags": ["large_rat"],
    "desc": "You estimate this rat at about 25 pounds and notice large sharp teeth and claws.",
    "gender": "neutral",
    "react_as": "aggressive",
    "armor": 5,
    "name_color": "r",
    "str": 15,
    "level": 1,
    "natural_weapon": {
        "name": "claws",
        "damage_type": "edged",
        "damage": 3,
        "speed": 4,
        "energy_cost": 1,
    },
    "exp_reward": 45,
    "drops": [{
        "key": "decaying corpse of a large rat.",
        "aliases": ["corpse"],
        "desc": "corpse of a large corpse",
        "name_color": "r",
        "power": 10
    }],
    "can_attack": True,
}

FIRE_BEETLE = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "a fire beetle",
    "aliases": ["bug", "beetle"],
    "desc": "The beetle has a thick yellow shell with black spots, red eyes, and a large pincer. It has 6 legs and makes a clicking sound as it moves around.",
    "gender": "neutral",
    "react_as": "social",
    "armor": 4,
    "name_color": "r",
    "hp": 32,
    "hpmax": 32,
    "str": 10,
    "natural_weapon": {
        "name": "pincer",
        "damage_type": "edged",
        "damage": 5,
        "speed": 4,
        "energy_cost": 1,
    },
    "exp_reward": 25,
    "drops": [{
        "key": "decaying corpse of a fire beetle.",
        "aliases": ["corpse"],
        "desc": "corpse of a fire beetle",
        "name_color": "r",
        "power": 10
    }],
    "can_attack": True,
}

SNAKE = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "",
    "aliases": [""],
    "desc": "",
    "gender": "neutral",
    "react_as": "aggressive",
    "armor": 2,
    "name_color": "r",
    "hp": 16,
    "hpmax": 16,
    "str": 5,
    "natural_weapon": {
        "name": "bite",
        "damage_type": "edged",
        "damage": 2,
        "speed": 2,
        "energy_cost": 1,
    },
    "exp_reward": 20,
    "drops": [{
        "key": "decaying corpse of a .",
        "aliases": ["corpse"],
        "desc": "corpse of a ",
        "name_color": "r",
        "power": 5
    }],
    "can_attack": True,
}

NOVICE_GOBLIN = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "a novice goblin",
    "aliases": ["goblin"],
    "desc": "A small, green-skinned goblin wielding a crude dagger. It looks eager to prove itself in combat.",
    "gender": "male",
    "react_as": "aggressive",
    "armor": 3,
    "name_color": "g",
    "hp": 80,
    "hpmax": 80,
    "str": 8,
    "natural_weapon": {
        "name": "dagger",
        "damage_type": "piercing",
        "damage": 6,
        "speed": 3,
        "energy_cost": 8,
    },
    "exp_reward": 10,
    "drops": [{
        "key": "crude dagger",
        "aliases": ["dagger"],
        "desc": "A small, crude dagger used by goblins.",
        "name_color": "g",
        "power": 5
    }],
    "can_attack": True,
}

ROGUE_APPRENTICE = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "a rogue apprentice",
    "aliases": ["rogue"],
    "desc": "A nimble rogue apprentice, skilled in stealth and quick strikes.",
    "gender": "female",
    "react_as": "aggressive",
    "armor": 5,
    "name_color": "b",
    "hp": 100,
    "hpmax": 100,
    "str": 12,
    "natural_weapon": {
        "name": "short sword",
        "damage_type": "edged",
        "damage": 10,
        "speed": 4,
        "energy_cost": 12,
    },
    "exp_reward": 20,
    "drops": [{
        "key": "short sword",
        "aliases": ["sword"],
        "desc": "A sharp short sword used by rogue apprentices.",
        "name_color": "b",
        "power": 10
    }],
    "can_attack": True,
}

FIRE_BEETLE = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "a fire beetle",
    "aliases": ["beetle"],
    "desc": "A large beetle with a glowing, fiery shell. It emits a dull orange light.",
    "gender": "neutral",
    "react_as": "aggressive",
    "armor": 7,
    "name_color": "r",
    "hp": 120,
    "hpmax": 120,
    "str": 15,
    "natural_weapon": {
        "name": "fiery mandibles",
        "damage_type": "fire",
        "damage": 12,
        "speed": 3,
        "energy_cost": 15,
    },
    "exp_reward": 25,
    "drops": [{
        "key": "fire beetle shell",
        "aliases": ["shell"],
        "desc": "The glowing shell of a fire beetle.",
        "name_color": "r",
        "power": 15
    }],
    "can_attack": True,
}

SKELETAL_WARRIOR = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "a skeletal warrior",
    "aliases": ["skeleton"],
    "desc": "A reanimated skeleton wielding a rusted sword. Its bones clatter with each movement.",
    "gender": "neutral",
    "react_as": "aggressive",
    "armor": 8,
    "name_color": "w",
    "hp": 150,
    "hpmax": 150,
    "str": 18,
    "natural_weapon": {
        "name": "rusted sword",
        "damage_type": "edged",
        "damage": 14,
        "speed": 3,
        "energy_cost": 18,
    },
    "exp_reward": 30,
    "drops": [{
        "key": "rusted sword",
        "aliases": ["sword"],
        "desc": "A rusted sword wielded by a skeletal warrior.",
        "name_color": "w",
        "power": 10
    }],
    "can_attack": True,
}

NOVICE_MAGE = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "a novice mage",
    "aliases": ["mage"],
    "desc": "A novice mage practicing basic spells. It wields a simple wooden staff.",
    "gender": "female",
    "react_as": "aggressive",
    "armor": 4,
    "name_color": "p",
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
    "exp_reward": 15,
    "drops": [{
        "key": "wooden staff",
        "aliases": ["staff"],
        "desc": "A simple wooden staff used by novice mages.",
        "name_color": "p",
        "power": 8
    }],
    "can_attack": True,
}

ENEMY_7 = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "a large rat",
    "aliases": ["rat"],
    "desc": "A large, aggressive rat with sharp teeth and a scruffy coat.",
    "gender": "neutral",
    "react_as": "aggressive",
    "armor": 2,
    "name_color": "g",
    "hp": 60,
    "hpmax": 60,
    "str": 7,
    "natural_weapon": {
        "name": "bite",
        "damage_type": "piercing",
        "damage": 5,
        "speed": 4,
        "energy_cost": 7,
    },
    "exp_reward": 8,
    "drops": [{
        "key": "rat pelt",
        "aliases": ["pelt"],
        "desc": "The scruffy pelt of a large rat.",
        "name_color": "g",
        "power": 3
    }],
    "can_attack": True,
}



NOVICE_ARCHER = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "a novice archer",
    "aliases": ["archer"],
    "desc": "A novice archer practicing their aim with a basic bow.",
    "gender": "male",
    "react_as": "aggressive",
    "armor": 3,
    "name_color": "y",
    "hp": 70,
    "hpmax": 70,
    "str": 9,
    "natural_weapon": {
        "name": "bow",
        "damage_type": "piercing",
        "damage": 7,
        "speed": 5,
        "energy_cost": 9,
    },
    "exp_reward": 12,
    "drops": [{
        "key": "basic bow",
        "aliases": ["bow"],
        "desc": "A basic bow used by novice archers.",
        "name_color": "y",
        "power": 7
    }],
    "can_attack": True,
}

MALFUNCTTIONING_ROBOT = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "a malfunctioning robot",
    "aliases": ["robot"],
    "desc": "A malfunctioning robot with sparks flying from its joints. It moves erratically, making it unpredictable in combat.",
    "gender": "neutral",
    "react_as": "aggressive",
    "armor": 6,
    "name_color": "s",
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
    "exp_reward": 20,
    "drops": [{
        "key": "robotic component",
        "aliases": ["component"],
        "desc": "A piece of the malfunctioning robot, still sparking with energy.",
        "name_color": "s",
        "power": 10
    }],
    "can_attack": True,
}

CYBER_SOLDIER = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "a cybernetic soldier",
    "aliases": ["soldier"],
    "desc": "A cybernetic soldier equipped with advanced armor and weaponry. Its movements are precise and calculated.",
    "gender": "male",
    "react_as": "aggressive",
    "armor": 10,
    "name_color": "b",
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
    "exp_reward": 35,
    "drops": [{
        "key": "plasma rifle",
        "aliases": ["rifle"],
        "desc": "An advanced plasma rifle used by cybernetic soldiers.",
        "name_color": "b",
        "power": 20
    }],
    "can_attack": True,
}

ALIEN_SCOUT = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "an alien scout",
    "aliases": ["alien"],
    "desc": "An alien scout with glowing eyes and sleek, otherworldly armor. It moves with agility and grace, making it a formidable opponent.",
    "gender": "neutral",
    "react_as": "aggressive",
    "armor": 8,
    "name_color": "g",
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
    "exp_reward": 30,
    "drops": [{
        "key": "alien energy core",
        "aliases": ["core"],
        "desc": "A glowing energy core from the alien scout.",
        "name_color": "g",
        "power": 15
    }],
    "can_attack": True,
}

