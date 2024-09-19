"""
Prototypes
"""

from random import randint, uniform, choice

SCRAWNY_GNOLL = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "a scrawny gnoll",
    "aliases": ["gnoll"],
    "tags": ["gnoll"],
    "desc": "The gnoll stands about five feet tall, and is wearing a torn blue shirt with greenish yellow pants.",
    "gender": "neutral",
    "react_as": "aggressive",
    "armor": 5,
    "name_color": "r",
    "str": 15,
    "level": lambda: randint(3, 5),
    "energyac": 0,
    "natural_weapon": {
        "name": "claws",
        "damage_type": "edged",
        "damage": 20,
        "speed": 4,
        "energy_cost": 1,
    },
    "exp_reward": 100,
    "can_attack": True,
}

GNOLL_PUP = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "a gnoll pup",
    "aliases": ["gnoll", "pup"],
    "desc": "The gnoll stands about three feet tall, and is wearing a torn blue shirt with greenish yellow pants.",
    "gender": "neutral",
    "react_as": "aggressive",
    "armor": 2,
    "name_color": "r",
    "hp": 100,
    "hpmax": 100,
    "str": 10,
    "natural_weapon": {
        "name": "claws",
        "damage_type": "edged",
        "damage": 5,
        "speed": 4,
        "energy_cost": 10,
    },
    "exp_reward": 5,
    "can_attack": True,
}

GNOLL_WARLORD = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "a gnoll warlord",
    "aliases": ["gnoll", "warlord"],
    "desc": "The gnoll warlord stands over six feet tall, clad in spiked armor and wielding a massive battle axe.",
    "gender": "male",
    "react_as": "aggressive",
    "armor": 10,
    "name_color": "r",
    "hp": 300,
    "hpmax": 300,
    "str": 20,
    "natural_weapon": {
        "name": "battle axe",
        "damage_type": "edged",
        "damage": 2,
        "speed": 2,
        "energy_cost": 15,
    },
    "exp_reward": 50,
    "drops": [
        {
            "key": "gnoll warlord's battle axe",
            "aliases": ["axe"],
            "desc": "A massive battle axe once wielded by a gnoll warlord.",
            "name_color": "r",
            "power": 30,
        }
    ],
    "can_attack": True,
}

DECAYING_SKELETON = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "a decaying skeleton",
    "aliases": ["skeleton"],
    "desc": "The decaying skeleton cackles as soon as it sees you.",
    "gender": "neutral",
    "react_as": "aggressive",
    "armor": 2,
    "name_color": "r",
    "hp": 100,
    "hpmax": 100,
    "str": 15,
    "natural_weapon": {
        "name": "dagger",
        "damage_type": "edged",
        "damage": 5,
        "speed": 2,
        "energy_cost": 5,
    },
    "exp_reward": 5,
    "can_attack": True,
}
