"""
Prototypes
"""
from random import randint, uniform, choice
LARGE_RAT = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "a large rat",
    "aliases": ["rat"],
    "tags": ["mystical_forest_mob"],
    "desc": "A large, scruffy rat with sharp teeth and a scraggly coat. It looks hungry and aggressive.",
    "gender": "neutral",
    "react_as": "aggressive",
    "armor": 2,
    "name_color": "g",
    "level": 3,
    "hp": 60,
    "hpmax": 60,
    "str": 7,
    "natural_weapon": {
        "name": "bite",
        "damage_type": "edged",
        "damage": 5,
        "speed": 4,
        "energy_cost": 7,
        "hits": 2
    },
    "exp_reward": 8,
    # "drops": [{
    #     "key": "rat pelt",
    #     "aliases": ["pelt"],
    #     "desc": "The scruffy pelt of a giant rat.",
    #     "name_color": "g",
    #     "power": 3
    # }],
    "can_attack": True,
}

FIRE_BEETLE = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "a fire beetle",
    "aliases": ["beetle"],
    "tags": ["mystical_forest_mob"],
    "desc": "A large beetle with a glowing, fiery shell. It emits a dull orange light.",
    "gender": "neutral",
    "react_as": "",
    "armor": 7,
    "name_color": "r",
    "level": 6,
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
    # "drops": [{
    #     "key": "fire beetle shell",
    #     "aliases": ["shell"],
    #     "desc": "The glowing shell of a fire beetle.",
    #     "name_color": "r",
    #     "power": 15
    # }],
    "can_attack": True,
}

GOBLIN_SCOUT = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "a goblin scout",
    "aliases": ["goblin"],
    "tags": ["mystical_forest_mob"],
    "desc": "A small, green-skinned goblin wielding a crude dagger. It looks eager to prove itself in combat.",
    "gender": "male",
    "react_as": "aggressive",
    "armor": 3,
    "name_color": "g",
    "level": 5,
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
    # "drops": [{
    #     "key": "crude dagger",
    #     "aliases": ["dagger"],
    #     "desc": "A small, crude dagger used by goblins.",
    #     "name_color": "g",
    #     "power": 5
    # }],
    "can_attack": True,
}

MOSS_SNAKE = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "a moss snake",
    "aliases": ["snake"],
    "tags": ["mystical_forest_mob"],
    "desc": "A small, slithering snake with dull scales. It looks ready to strike at any moment.",
    "gender": "neutral",
    "react_as": "aggressive",
    "armor": 1,
    "name_color": "y",
    "level": 4,
    "hp": 50,
    "hpmax": 50,
    "str": 6,
    "natural_weapon": {
        "name": "bite",
        "damage_type": "piercing",
        "damage": 4,
        "speed": 5,
        "energy_cost": 6,
    },
    "exp_reward": 7,
    # "drops": [{
    #     "key": "snake fang",
    #     "aliases": ["fang"],
    #     "desc": "A sharp fang from a snake.",
    #     "name_color": "y",
    #     "power": 4
    # }],
    "can_attack": True,
}

DECAYING_SKELETON = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "a decaying skeleton",
    "aliases": ["skeleton"],
    "tags": ["mystical_forest_mob"],
    "desc": "A reanimated skeleton with bones that are brittle and decaying. It wields a rusted sword.",
    "gender": "neutral",
    "react_as": "aggressive",
    "armor": 5,
    "name_color": "w",
    "level": 3,
    "hp": 100,
    "hpmax": 100,
    "str": 12,
    "natural_weapon": {
        "name": "rusted sword",
        "damage_type": "edged",
        "damage": 10,
        "speed": 3,
        "energy_cost": 12,
    },
    "exp_reward": 60,
    # "drops": [{
    #     "key": "rusted sword",
    #     "aliases": ["sword"],
    #     "desc": "A rusted sword wielded by a decaying skeleton.",
    #     "name_color": "w",
    #     "power": 10
    # }],
    "can_attack": True,
}
