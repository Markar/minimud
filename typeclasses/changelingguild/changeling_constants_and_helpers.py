from typeclasses.changelingguild.changeling_attack import ChangelingAttack
from typeclasses.changelingguild.slime import Slime
from typeclasses.changelingguild.human import Human
from typeclasses.changelingguild.reptile.anole import Anole
from typeclasses.changelingguild.reptile.teiid import Teiid
from typeclasses.changelingguild.reptile.gecko import Gecko
from typeclasses.changelingguild.reptile.skink import Skink
from typeclasses.changelingguild.reptile.iguana import Iguana
from typeclasses.changelingguild.reptile.boa import Boa
from typeclasses.changelingguild.reptile.viper import Viper
from typeclasses.changelingguild.reptile.caiman import Caiman
from typeclasses.changelingguild.reptile.cobra import Cobra
from typeclasses.changelingguild.reptile.gilamonster import GilaMonster
from typeclasses.changelingguild.reptile.python import Python
from typeclasses.changelingguild.reptile.crocodile import Crocodile
from typeclasses.changelingguild.reptile.alligator import Alligator
from typeclasses.changelingguild.reptile.anaconda import Anaconda
from typeclasses.changelingguild.reptile.komodo_dragon import KomodoDragon
from typeclasses.changelingguild.mammal.rat import Rat
from typeclasses.changelingguild.mammal.cat import Cat
from typeclasses.changelingguild.mammal.lynx import Lynx
from typeclasses.changelingguild.mammal.fox import Fox
from typeclasses.changelingguild.mammal.badger import Badger
from typeclasses.changelingguild.mammal.wolverine import Wolverine
from typeclasses.changelingguild.mammal.wolf import Wolf
from typeclasses.changelingguild.mammal.black_bear import BlackBear
from typeclasses.changelingguild.mammal.grizzly_bear import GrizzlyBear
from typeclasses.changelingguild.mammal.elephant import Elephant
from typeclasses.changelingguild.mammal.cheetah import Cheetah
from typeclasses.changelingguild.mammal.leopard import Leopard
from typeclasses.changelingguild.mammal.jaguar import Jaguar
from typeclasses.changelingguild.mammal.tiger import Tiger
from typeclasses.changelingguild.mammal.lion import Lion
from typeclasses.changelingguild.avian.hummingbird import Hummingbird
from typeclasses.changelingguild.avian.finch import Finch
from typeclasses.changelingguild.avian.sparrow import Sparrow
from typeclasses.changelingguild.avian.swallow import Swallow
from typeclasses.changelingguild.avian.crow import Crow
from typeclasses.changelingguild.avian.raven import Raven
from typeclasses.changelingguild.avian.crane import Crane
from typeclasses.changelingguild.avian.kestrel import Kestrel
from typeclasses.changelingguild.avian.owl import Owl
from typeclasses.changelingguild.avian.osprey import Osprey
from typeclasses.changelingguild.avian.falcon import Falcon
from typeclasses.changelingguild.avian.hawk import Hawk
from typeclasses.changelingguild.avian.condor import Condor
from typeclasses.changelingguild.avian.ostrich import Ostrich
from typeclasses.changelingguild.avian.eagle import Eagle

FORM_CLASSES = {
    "ChangelingAttack": ChangelingAttack,
    "Slime": Slime,
    "Human": Human,
    "Anole": Anole,
    "Teiid": Teiid,
    "Gecko": Gecko,
    "Skink": Skink,
    "Iguana": Iguana,
    "Boa": Boa,
    "Viper": Viper,
    "Caiman": Caiman,
    "Cobra": Cobra,
    "Gila Monster": GilaMonster,
    "Python": Python,
    "Crocodile": Crocodile,
    "Alligator": Alligator,
    "Anaconda": Anaconda,
    "Komodo Dragon": KomodoDragon,
    "Rat": Rat,
    "Cat": Cat,
    "Lynx": Lynx,
    "Fox": Fox,
    "Badger": Badger,
    "Wolverine": Wolverine,
    "Wolf": Wolf,
    "Black Bear": BlackBear,
    "Grizzly Bear": GrizzlyBear,
    "Elephant": Elephant,
    "Cheetah": Cheetah,
    "Leopard": Leopard,
    "Jaguar": Jaguar,
    "Tiger": Tiger,
    "Lion": Lion,
    "Hummingbird": Hummingbird,
    "Finch": Finch,
    "Sparrow": Sparrow,
    "Swallow": Swallow,
    "Crow": Crow,
    "Raven": Raven,
    "Crane": Crane,
    "Kestrel": Kestrel,
    "Owl": Owl,
    "Osprey": Osprey,
    "Falcon": Falcon,
    "Hawk": Hawk,
    "Condor": Condor,
    "Ostrich": Ostrich,
    "Eagle": Eagle,
}

SKILLS_COST = [
    0,
    1800,
    9016,
    25297,
    54353,
    99978,
    166074,
    256675,
    375971,
    528332,
    718332,
    950773,
    1230709,
    1563470,
    1954686,
    2410311,
    2936647,
    3540368,
    4228544,
    5008665,
    5888665,
    6876946,
    7982402,
    9214443,
    10583019,
    12098644,
]

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

AVIAN_FORMS = {
    30: "eagle",
    28: "ostrich",
    26: "condor",
    24: "hawk",
    22: "falcon",
    20: "osprey",
    18: "owl",
    16: "kestrel",
    14: "crane",
    12: "raven",
    10: "crow",
    8: "swallow",
    6: "sparrow",
    4: "finch",
    2: "hummingbird",
}

MAMMAL_FORMS = {
    30: "lion",
    28: "tiger",
    26: "jaguar",
    24: "leopard",
    22: "cheetah",
    20: "elephant",
    18: "grizzly bear",
    16: "black bear",
    14: "wolf",
    12: "wolverine",
    10: "badger",
    8: "fox",
    6: "lynx",
    4: "cat",
    2: "rat",
}

REPTILE_FORMS = {
    30: "komodo dragon",
    28: "anaconda",
    26: "alligator",
    24: "crocodile",
    22: "python",
    20: "gila monster",
    18: "cobra",
    16: "caiman",
    14: "viper",
    12: "boa",
    10: "iguana",
    8: "skink",
    6: "gecko",
    4: "teiid",
    2: "anole",
}

TITLES = [
    "Novice Shapeshifter",
    "Apprentice Morph",
    "Form Weaver",
    "Skinchanger",
    "Mimic",
    "Doppelganger",
    "Illusionist",
    "Chameleon",
    "Metamorph",
    "Shape Adept",
    "Transmuter",
    "Form Master",
    "Morphing Savant",
    "Shapeshifter",
    "Expert Changeling",
    "Master of Disguise",
    "Form Manipulator",
    "Shapeshifting Virtuoso",
    "Transfiguration Expert",
    "Changeling Elite",
    "Form Architect",
    "Shapeshifting Maestro",
    "Transmutation Master",
    "Changeling Supreme",
    "Form Grandmaster",
    "Shapeshift Overlord",
    "Transfiguration Sage",
    "Quantum Morph",
    "Nanform Shifter",
    "Eternal Shapeshifter",
    "Galatic Form Overlord",
    "Universal Morph",
    "Multiversal Shifter",
    "Cosmic Form Master",
    "Infinite Shapeshifter",
    "Omniversal Morph",
    "Omniform Shifter",
    "Omnipresent Form Master",
    "Omnipotent Shapeshifter",
    "Omniscient Morph",
    "Omnipresent Shifter",
    "Omnipotent Form Master",
    "Omniscient Shapeshifter",
]
