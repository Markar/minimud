SKILLS_COST = [
    0,  # Total: 0
    1800,  # Total: 1800
    9016,  # Total: 10,816
    25297,  # Total: 36,113
    54353,  # Total: 90,466
    99978,  # Total: 190,444
    166074,  # Total: 356,518
    256675,  # Total: 613,193
    375971,  # Total: 989,164
    528332,  # Total: 1,517,496
    718332,  # Total: 2,235,828
    950773,  # Total: 3,186,601
    1230709,  # Total: 4,417,310
    1563470,  # Total: 5,980,780
    1954686,  # Total: 7,935,466
    2410311,  # Total: 10,345,777
    2936647,  # Total: 13,282,424
    3540368,  # Total: 16,822,792
    4228544,  # Total: 21,051,336
    5008665,  # Total: 26,060,001
    5888665,  # Total: 31,948,666
    6876946,  # Total: 38,825,612
    7982402,  # Total: 46,808,014
    9214443,  # Total: 56,022,457
    10583019,  # Total: 66,605,476
    12098644,  # Total: 78,704,120
]

GUILD_LEVEL_COST_DICT = {
    2: 300,  # Total: 300
    3: 400,  # Total: 700
    4: 648,  # Total: 1,348
    5: 951,  # Total: 2,299
    6: 1529,  # Total: 3,828
    7: 2409,  # Total: 6,237
    8: 3330,  # Total: 9,567
    9: 4645,  # Total: 14,212
    10: 6000,  # Total: 20,212
    11: 7500,  # Total: 27,712
    12: 10000,  # Total: 37,712
    13: 12900,  # Total: 50,612
    14: 16000,  # Total: 66,612
    15: 22500,  # Total: 89,112
    16: 32000,  # Total: 121,112
    17: 47000,  # Total: 168,112
    18: 67000,  # Total: 235,112
    19: 90000,  # Total: 325,112
    20: 120000,  # Total: 445,112
    21: 160000,  # Total: 605,112
    22: 220000,  # Total: 825,112
    23: 295000,  # Total: 1,120,112
    24: 445000,  # Total: 1,565,112
    25: 675000,  # Total: 2,240,112
    26: 950000,  # Total: 3,190,112
    27: 1300000,  # Total: 4,490,112
    28: 1900000,  # Total: 6,390,112
    29: 2900000,  # Total: 9,290,112
    30: 4200000,  # Total: 13,490,112
    31: 4200000000000,  # Total: 4200013490112
}


SKILL_RANKS = {
    0: "Very poor",
    1: "Poor",
    2: "Below average",
    3: "Average",
    4: "Above average",
    5: "Moderate",
    6: "Good",
    7: "Very good",
    8: "High",
    9: "Very high",
    10: "Excellent",
    12: "Exceptional",
    14: "Masterful",
    16: "Supreme",
    17: "God-like",
}


def get_article(word):
    vowels = "aeiou"
    return "an" if word[0].lower() in vowels else "a"


TITLES = [
    "",  # 0
    "the New Recruit",
    "the Warrior",
    "the Fighter",
    "the Skilled Warrior",
    "the Seasoned Warrior",
    "the Veteran Warrior",
    "the Elite Warrior",
    "the Master Warrior",
    "the Grandmaster Warrior",
    "the Legendary Warrior",
    "the Mythical Warrior",
    "the Supreme Warrior",
    "the Godlike Warrior",
    "the Ultimate Warrior",
    "the Warrior King",
    "the Warrior Emperor",
    "the Warrior God",
    "the Warrior Deity",
    "the Warrior Legend",
    "the Warrior Overlord",
    "the Warrior Master",
    "the Warrior Champion",
    "the Warrior Hero",
    "the Warrior Titan",
    "the Warrior God",
    "the Warrior Deity",
    "the Warrior Legend",
    "the Warrior Overlord",
    "the Warrior Master",
    "the Warrior Champion",
]
