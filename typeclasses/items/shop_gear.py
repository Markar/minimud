### Crafted prototypes which might be useful to access in other places, such as shops
IRON_DAGGER = {
    "typeclass": "typeclasses.gear.MeleeWeapon",
    "key": "iron dagger",
    "desc": "A keen-edged dagger, made of iron.",
    "tags": [
        ("pierce", "damage_type"),
        ("slash", "damage_type"),
        ("knife", "crafting_tool"),
    ],
    "value": 20,
    "energy_cost": 3,
    "speed": 3,
    "dmg": 50,
}

TARNISHED_SWORD = {
    "typeclass": "typeclasses.gear.MeleeWeapon",
    "key": "tarnished sword",
    "desc": "The sword is a simple, unadorned weapon, clearly showing signs of age and wear. Its once-shiny blade is now dull and tarnished, with small nicks and scratches marring its surface. The hilt is wrapped in worn leather, providing a somewhat comfortable grip despite its rough appearance. Though it lacks the gleam and sharpness of a more formidable weapon, this sword still holds a certain charm, a testament to its history and the battles it has seen. For a new adventurer, it serves as a reliable, if humble, companion on the journey ahead.",
    "tags": [("edged", "damage_type"), ("edged", "damage_type")],
    "value": 30,
    "energy_cost": 5,
    "speed": 3,
    "dmg": 20,
}

IRON_SWORD = {
    "typeclass": "typeclasses.gear.MeleeWeapon",
    "key": "iron sword",
    "desc": "A one-handed sword made of iron.",
    "tags": [("pierce", "damage_type"), ("slash", "damage_type")],
    "value": 30,
    "energy_cost": 5,
    "speed": 7,
    "dmg": 40,
}

IRON_GREATSWORD = {
    "typeclass": "typeclasses.gear.MeleeWeapon",
    "key": "iron greatsword",
    "desc": "A two-handed iron greatsword.",
    "tags": [
        ("slash", "damage_type"),
        ("bludgeon", "damage_type"),
        ("two_handed", "wielded"),
    ],
    "value": 50,
    "energy_cost": 10,
    "speed": 12,
    "dmg": 60,
}

# IRON_HAUBERK = {
#     "typeclass": "typeclasses.objects.ClothingObject",
#     "key": "iron hauberk",
#     "desc": "A standard iron chainmail tunic.",
#     "armor": 4,
#     "value": 500,
#     "clothing_type": "chestguard",
#     "type": "heavy",
# }

# IRON_CHAUSSES = {
#     "typeclass": "typeclasses.objects.ClothingObject",
#     "key": "iron chausses",
#     "desc": "A pair of mail chausses constructed from iron.                                           ",
#     "armor": 3,
#     "value": 350,
#     "clothing_type": "legguard",
#     "type": "heavy",
# }

# LEATHER_BOOTS = {
#     "typeclass": "typeclasses.objects.ClothingObject",
#     "key": "leather boots",
#     "desc": "A sturdy pair of leather boots.",
#     "armor": 1,
#     "value": 200,
#     "clothing_type": "shoes",
#     "type": "light",
# }

SMALL_BAG = {
    "typeclass": "typeclasses.gear.WearableContainer",
    "key": "small bag",
    "desc": "A small leather bag.",
    "capacity": 10,
    "value": 5,
    "clothing_type": "accessory",
}
MEDIUM_BAG = {
    "typeclass": "typeclasses.gear.WearableContainer",
    "key": "medium bag",
    "desc": "A medium leather bag.",
    "capacity": 20,
    "value": 15,
    "clothing_type": "accessory",
}
LARGE_BAG = {
    "typeclass": "typeclasses.gear.WearableContainer",
    "key": "large bag",
    "desc": "A large leather bag.",
    "capacity": 30,
    "value": 30,
    "clothing_type": "accessory",
}

"""
Cybercorps Guild Shop Gear
"""
CYBER_CHESTGUARD = {
    "typeclass": "typeclasses.objects.ClothingObject",
    "key": "Nanofiber Vest",
    "desc": "A high-tech chestguard made from reinforced nanofiber and titanium alloy, offering superior protection and integrated with advanced sensors for enhanced situational awareness.",
    "armor": 6,
    "value": 750,
    "clothing_type": "chestguard",
    "type": "medium",
}

CYBER_LEG_GUARDS = {
    "typeclass": "typeclasses.objects.ClothingObject",
    "key": "Nanofiber pants",
    "desc": "A pair of advanced leg guards constructed from reinforced nanofiber and titanium alloy, designed for maximum protection and mobility.",
    "armor": 3,
    "value": 500,
    "clothing_type": "legguard",
    "type": "medium",
}

CYBER_BOOTS = {
    "typeclass": "typeclasses.objects.ClothingObject",
    "key": "Nanofiber boots",
    "desc": "A pair of high-tech boots made from reinforced nanofiber and titanium alloy, designed for maximum durability and enhanced agility. Integrated with shock absorbers and traction control for optimal performance.",
    "armor": 2,
    "value": 400,
    "clothing_type": "footwear",
    "type": "medium",
}
