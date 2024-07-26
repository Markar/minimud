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
    "key": "a snake",
    "aliases": ["snake"],
    "desc": "A snake.",
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
        "key": "decaying corpse of a snake.",
        "aliases": ["corpse"],
        "desc": "corpse of a snake",
        "name_color": "r",
        "power": 5
    }],
    "can_attack": True,
}
