"""
Prototypes
"""
from random import randint, choice

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
    "energyac": 40,
    "natural_weapon": {
        "name": "claws",
        "damage_type": "edged",
        "damage": 20,
        "speed": 4,
        "energy_cost": 1,
    },
    "exp_reward": 100,
    "drops": [{
        "key": "decaying corpse of a scrawny gnoll.",
        "aliases": ["corpse"],
        "desc": "corpse of a scrawny gnoll",
        "name_color": "r",
        "power": 20
    }],
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
    "drops": [{
        "key": "decaying corpse of a gnoll pup.",
        "aliases": ["corpse"],
        "desc": "corpse of a gnoll pup",
        "name_color": "r",
        "power": 5
    }],
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
    "drops": [{
        "key": "decaying corpse of a decaying skeleton.",
        "aliases": ["corpse"],
        "desc": "corpse of a decaying skeleton",
        "name_color": "r",
        "power": 5
    }],
    "can_attack": True,
}

### Mob drops

# RAW_MEAT = {
#     "key": "raw meat",
#     "desc": "A piece of meat from an animal. It hasn't been cooked.",
#     "tags": [("raw meat", "crafting_material")],
# }
# ANIMAL_HIDE = {
#     "key": "animal hide",
#     "desc": "A section of hide from an animal, suitable for leather-crafting",
#     "tags": [("leather", "crafting_material")],
# }
# DEER_MEAT = {
#     "key": "raw deer meat",
#     "desc": "A piece of meat from a deer. It hasn't been cooked.",
#     "tags": [("raw meat", "crafting_material"), ("venison", "crafting_material")],
# }
# DEER_ANTLER = {
#     "key": "antler",
#     "desc": "A forked antler bone from an adult stag.",
#     "tags": [
#         ("bone", "crafting_material"),
#     ],
# }
