"""
Prototypes
"""
from random import randint, choice

SCRAWNY_GNOLL = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "a scrawny gnoll",
    "desc": "The gnoll stands about five feet tall, and is wearing a torn blue shirt with greenish yellow pants.",
    "gender": "neutral",
    "react_as": "aggressive",
    "armor": 20,
    "name_color": "r",
    "str": 15,
    "natural_weapon": {
        "name": "claws",
        "damage_type": "slash",
        "damage": 10,
        "speed": 4,
        "energy_cost": 10,
    },
    "exp_reward": 10,
    # randomly generate a list of drop prototype keys when the mob is spawned
    "drops": lambda: ["IRON_DAGGER"] * randint(3, 5) + ["WOOL_TUNIC"] * randint(0, 5),
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
