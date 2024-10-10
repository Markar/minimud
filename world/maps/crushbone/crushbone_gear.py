# region CRUSHBONE
DWARVEN_RINGMAIL_TUNIC = {
    "typeclass": "typeclasses.objects.ClothingObject",
    "key": "Dwarven Ringmail Tunic",
    "desc": "A ringmail tunic skillfully crafted by dwarves. Noone knows how it ended up in the hands of an orc. It provides extra protection from fire, cold, and magic.",
    "armor": 12,
    "fireac": 8,
    "coldac": 8,
    "magicac": 8,
    "value": 1000,
    "clothing_type": "chestguard",
    "type": "medium",
}
SHINY_BRASS_SHIELD = {
    "typeclass": "typeclasses.objects.ClothingObject",
    "key": "shiny brass shield",
    "desc": "A shiny brass shield.",
    "armor": 10,
    "magicac": 10,
    "value": 800,
    "clothing_type": "shield",
    "type": "medium",
}
DWARVEN_TWO_HANDED_AXE = {
    "typeclass": "typeclasses.gear.MeleeWeapon",
    "key": "Dwarven Two-Handed Axe",
    "desc": "A massive two-handed axe crafted by dwarves. It is a formidable weapon, capable of cleaving through armor and bone with ease.",
    "tags": [
        ("edged", "damage_type"),
        ("blunt", "damage_type"),
        ("two_handed", "wielded"),
    ],
    "value": 1200,
    "energy_cost": 5,
    "speed": 6,
    "dmg": 35,  # 30/tick
}
DWARVEN_AXE = {
    "typeclass": "typeclasses.gear.MeleeWeapon",
    "key": "Dwarven Axe",
    "desc": "A dwarven axe.",
    "tags": [("edged", "damage_type"), ("blunt", "damage_type")],
    "value": 800,
    "energy_cost": 5,
    "speed": 4,
    "dmg": 20,  # 30/tick
}
DRAGOON_DIRK = {
    "typeclass": "typeclasses.gear.MeleeWeapon",
    "key": "Dragoon Dirk",
    "desc": "A dragoon dirk.",
    "tags": [("edged", "damage_type")],
    "value": 1000,
    "energy_cost": 3,
    "speed": 3,
    "dmg": 15,  # 30/tick
}
LEATHER_WHIP = {
    "typeclass": "typeclasses.gear.MeleeWeapon",
    "key": "Leather Whip",
    "desc": "A leather whip.",
    "tags": [("edged", "damage_type")],
    "value": 500,
    "energy_cost": 2,
    "speed": 3,
    "dmg": 12,  # 24/tick
}
