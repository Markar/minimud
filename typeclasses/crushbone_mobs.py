from random import uniform, choice

ORC_PAWN = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "an orc pawn",
    "aliases": ["orc", "pawn"],
    "desc": "A low-ranking orc wielding a rusty sword. It looks eager to prove its worth.",
    "gender": "male",
    "react_as": "aggressive",
    "armor": 5,
    "name_color": "g",
    "level": 8,
    "hp": 100,
    "hpmax": 100,
    "str": 10,
    "natural_weapon": {
        "name": "rusty sword",
        "damage_type": "edged",
        "damage": 8,
        "speed": 5,
        "energy_cost": 0,
        "hits": 2,
    },
    "exp_reward": 8000,
    "can_attack": True,
}
ORC_CENTURION = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "an orc centurion",
    "aliases": ["orc", "centurion"],
    "desc": "A battle-hardened orc wielding a sharp axe. It commands respect among its peers.",
    "gender": "male",
    "react_as": "aggressive",
    "armor": 10,
    "name_color": "r",
    "level": 12,
    "hp": 200,
    "hpmax": 200,
    "str": 20,
    "natural_weapon": {
        "name": "sharp axe",
        "damage_type": "edged",
        "damage": 15,
        "speed": 5,
        "energy_cost": 0,
        "hits": 2,
    },
    "exp_reward": 11750,
    "can_attack": True,
}
ORC_LEGIONNAIRE = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "an orc legionnaire",
    "aliases": ["orc", "legionnaire"],
    "desc": "A seasoned orc warrior wielding a heavy mace. It is a formidable opponent.",
    "gender": "male",
    "react_as": "aggressive",
    "armor": 15,
    "name_color": "r",
    "level": 22,
    "str": 30,
    "natural_weapon": {
        "name": "heavy mace",
        "damage_type": "blunt",
        "damage": 20,
        "speed": 5,
        "energy_cost": 0,
        "hits": 3,
    },
    "exp_reward": 22250,
    "can_attack": True,
}
ORC_SLAVER = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "an orc slaver",
    "aliases": ["orc", "slaver"],
    "desc": "A cruel orc wielding a whip. It takes pleasure in dominating others.",
    "gender": "male",
    "react_as": "aggressive",
    "armor": 5,
    "name_color": "r",
    "level": 16,
    "hp": 400,
    "hpmax": 400,
    "str": 40,
    "natural_weapon": {
        "name": "whip",
        "damage_type": "edged",
        "damage": 25,
        "speed": 5,
        "energy_cost": 0,
        "hits": 2,
    },
    "exp_reward": 16300,
    "can_attack": True,
}
ORC_ORACLE = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "an orc oracle",
    "aliases": ["orc", "oracle"],
    "desc": "A mystical orc wielding a staff. It has a deep connection to dark magic.",
    "gender": "male",
    "react_as": "aggressive",
    "armor": 10,
    "name_color": "r",
    "level": 25,
    "hp": 500,
    "hpmax": 500,
    "str": 50,
    "natural_weapon": {
        "name": "staff",
        "damage_type": "blunt",
        "damage": 30,
        "speed": 5,
        "energy_cost": 0,
    },
    "exp_reward": 19000,
    "can_attack": True,
}
ORC_EMISSARY = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "an orc emissary",
    "aliases": ["orc", "emissary"],
    "desc": "A cunning orc wielding a ceremonial dagger. It is skilled in diplomacy and combat.",
    "gender": "male",
    "react_as": "aggressive",
    "armor": 15,
    "name_color": "r",
    "level": 30,
    "hp": 600,
    "hpmax": 600,
    "str": 60,
    "natural_weapon": {
        "name": "ceremonial dagger",
        "damage_type": "edged",
        "damage": 35,
        "speed": 5,
        "energy_cost": 0,
        "hits": 2,
    },
    "exp_reward": 28150,
    "can_attack": True,
}
ORC_ROYAL_GUARD = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "an orc royal guard",
    "aliases": ["orc", "royal guard"],
    "desc": "A heavily armored orc wielding a large shield and sword. It is sworn to protect the orc royalty.",
    "gender": "male",
    "react_as": "aggressive",
    "armor": 25,
    "name_color": "r",
    "level": 35,
    "hp": 700,
    "hpmax": 700,
    "str": 70,
    "natural_weapon": {
        "name": "large sword",
        "damage_type": "edged",
        "damage": 40,
        "speed": 5,
        "energy_cost": 0,
        "hits": 2,
    },
    "exp_reward": 30820,
    "can_attack": True,
}
ORC_TASKMASTER = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "an orc taskmaster",
    "aliases": ["orc", "taskmaster"],
    "desc": "A brutal orc wielding a spiked club. It oversees the labor of other orcs with an iron fist.",
    "gender": "male",
    "react_as": "aggressive",
    "armor": 20,
    "name_color": "r",
    "level": 16,
    "hp": 800,
    "hpmax": 800,
    "str": 80,
    "natural_weapon": {
        "name": "spiked club",
        "damage_type": "blunt",
        "damage": 45,
        "speed": 5,
        "energy_cost": 0,
        "hits": 2,
    },
    "drops": lambda: uniform(0, 1) < 0.1 and ["LEATHER_WHIP"],
    "exp_reward": 16200,
    "can_attack": True,
}
ORC_TRAINER = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "Orc Trainer",
    "aliases": ["orc", "trainer"],
    "desc": "The orc trainer is a master of combat. He's been training orcs for years and is a formidable opponent.",
    "gender": "male",
    "react_as": "aggressive",
    "armor": 10,
    "name_color": "r",
    "level": 21,
    "hp": 11562,
    "hpmax": 11562,
    "str": 10,
    "natural_weapon": {
        "name": "legendary warhammer",
        "damage_type": "blunt",
        "damage": 30,
        "speed": 5,
        "energy_cost": 0,
        "hits": 2,
    },
    "exp_reward": 21562,
    "drops": lambda: uniform(0, 1) < 0.1 and ["SHINY_BRASS_SHIELD"],
    "can_attack": True,
}

ORC_WARLORD = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "an orc warlord",
    "aliases": ["orc", "warlord"],
    "desc": "A fearsome orc wielding a massive battle axe. It commands legions with ruthless efficiency.",
    "gender": "male",
    "react_as": "aggressive",
    "armor": 35,
    "name_color": "r",
    "level": 25,
    "hp": 900,
    "hpmax": 900,
    "str": 90,
    "natural_weapon": {
        "name": "battle axe",
        "damage_type": "edged",
        "damage": 50,
        "speed": 5,
        "energy_cost": 0,
        "hits": 2,
    },
    "exp_reward": 28300,
    "can_attack": True,
}
ORC_LORD = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "an orc lord",
    "aliases": ["orc", "lord"],
    "desc": "A powerful orc wielding an enchanted sword. It is a master of both strategy and combat.",
    "gender": "male",
    "react_as": "aggressive",
    "armor": 30,
    "name_color": "r",
    "level": 28,
    "hp": 1000,
    "hpmax": 1000,
    "str": 100,
    "natural_weapon": {
        "name": "enchanted sword",
        "damage_type": "edged",
        "damage": 55,
        "speed": 5,
        "energy_cost": 0,
        "hits": 2,
    },
    "exp_reward": 28300,
    "can_attack": True,
}
ORC_EMPEROR = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "Emperor Crush",
    "aliases": ["orc", "emperor"],
    "desc": "The supreme ruler of the orcs, wielding a legendary warhammer. It is a terrifying presence on the battlefield.",
    "gender": "male",
    "react_as": "aggressive",
    "armor": 18,
    "name_color": "r",
    "level": 35,
    "hp": 1500,
    "hpmax": 1500,
    "str": 120,
    "natural_weapon": {
        "name": "legendary warhammer",
        "damage_type": "blunt",
        "damage": 70,
        "speed": 5,
        "energy_cost": 0,
        "hits": 3,
    },
    "exp_reward": 35000,
    "drops": lambda: uniform(0, 1) < 0.1 and ["DWARVEN_RINGMAIL_TUNIC"],
    "can_attack": True,
}

LORD_DARISH = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "Lord Darish",
    "aliases": ["orc", "darish", "lord"],
    "desc": "A powerful orc, here to discuss plans with the emperor.",
    "gender": "male",
    "react_as": "aggressive",
    "armor": 18,
    "name_color": "r",
    "level": 25,
    "hp": 1500,
    "hpmax": 1500,
    "str": 120,
    "natural_weapon": {
        "name": "dwarven two-handed axe",
        "damage_type": "edged",
        "damage": 70,
        "speed": 5,
        "energy_cost": 0,
        "hits": 2,
    },
    "exp_reward": 25000,
    "drops": lambda: uniform(0, 1) < 0.1
    and choice(("DWARVEN_TWO_HANDED_AXE", "DWARVEN_AXE")),
    "can_attack": True,
}

AMBASSADOR_DVINN = {
    "typeclass": "typeclasses.characters.NPC",
    "key": "Ambassador Dvinn",
    "aliases": ["dark elf", "dvinn", "ambassador", "elf"],
    "desc": "A dark elf ambassador, here to negotiate with the orcs.",
    "gender": "male",
    "react_as": "aggressive",
    "armor": 20,
    "name_color": "b",
    "level": 20,
    "hp": 1200,
    "hpmax": 1200,
    "str": 80,
    "natural_weapon": {
        "name": "dragoon dirk",
        "damage_type": "edged",
        "damage": 60,
        "speed": 5,
        "energy_cost": 0,
    },
    "exp_reward": 20000,
    "drops": lambda: uniform(0, 1) < 0.1 and ["DRAGOON_DIRK"],
    "can_attack": True,
}
