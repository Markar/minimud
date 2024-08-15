"""
Based on the example character creator EvMenu module
https://github.com/evennia/evennia/blob/main/evennia/contrib/rpg/character_creator/example_menu.py
"""

import inflect
from random import choice
from typeclasses.characters import Character

from evennia.prototypes.spawner import spawn
from evennia.utils import dedent
from evennia.utils.evtable import EvTable
from evennia.objects.models import ObjectDB

_INFLECT = inflect.engine()


#########################################################
#                   Welcome Page
#########################################################


def menunode_welcome(caller):
    """Starting page."""
    # make sure it's a player not a generic character
    if not caller.new_char.is_typeclass("typeclasses.characters.PlayerCharacter"):
        # it's not - swap it
        caller.new_char.swap_typeclass("typeclasses.characters.PlayerCharacter")

    text = dedent(
        """\
        |wWelcome to the Millennium!|n

        This mud is a work in progress, please report any bugs or suggestions and enjoy the game!
    """
    )
    options = {"desc": "Let's begin!", "goto": "menunode_choose_gender"}
    return text, options


#########################################################
#                Gender/Pronouns
#########################################################


def menunode_choose_gender(caller, **kwargs):
    """Base node for appearance options."""
    # this is a new decision step, so save your resume point here
    caller.new_char.db.chargen_step = "menunode_choose_gender"

    text = dedent(
        f"""\
        |wChoose your gender|n
        """
    )

    options = [
        {"desc": f"male", "goto": (_set_gender, {"gender": "male"})},
        {"desc": f"female", "goto": (_set_gender, {"gender": "female"})},
        # once past the first decision, it's also a good idea to include a "back to previous step" option
        # {
        #     "key": ("(Back)", "back", "b"),
        #     "desc": "Go back to stat selection",
        #     "goto": "menunode_points_base",
        # },
    ]

    return text, options


def _set_gender(caller, raw_string, gender, **kwargs):
    """
    Set the 'gender' property and continue
    """
    # verify it's a valid option
    if gender in ("male", "female"):
        caller.new_char.gender = gender
        # return _check_desc(caller, raw_string, **kwargs)
        return "menunode_choose_name"
    else:
        # go back to do it again
        return "menunode_choose_gender"


#########################################################
#                Setting a Description
#########################################################


def _check_desc(caller, raw_string, **kwargs):
    """
    In case the player went back to change earlier decisions, this allows players to skip the
    "enter desc" step if they already did it and go straight to confirming.
    """
    if caller.new_char.db.desc:
        return "menunode_confirm_desc"
    else:
        return "menunode_set_desc"


def menunode_set_desc(caller, raw_string, **kwargs):
    """Setting a description"""
    char = caller.new_char

    # another decision, so save the resume point
    char.db.chargen_step = "menunode_set_desc"

    text = dedent(
        f"""\
        |wYour Appearance|n

        Write up a brief (or not so brief, if that's how you roll) description of your character.
        While this will set your character's initial appearance, you can change it whenver you want
        in-game with the |wsetdesc|n command.
        
        Enter your new description:
        """
    )

    help = "You'll have a chance to change your mind before continuing, plus you can change it in game whenever."
    options = {"key": "_default", "goto": _set_desc}
    return (text, help), options


def _set_desc(caller, raw_string, **kwargs):
    """Cleaning up and applying the description."""
    desc = raw_string.strip()
    caller.new_char.db.desc = desc

    return "menunode_confirm_desc"


def menunode_confirm_desc(caller, raw_string, **kwargs):
    """Confirm the entered description"""
    char = caller.new_char
    char.db.chargen_step = "menunode_confirm_desc"

    text = dedent(
        f"""\
        |wYour Appearance|n

        Is this how you want to look?

        {char.db.desc}
        """
    )

    options = [
        {
            "key": ("Yes", "y"),
            "desc": "Confirm and continue",
            "goto": "menunode_choose_name",
        },
        {
            "key": ("No", "n"),
            "desc": "Go back to a new description",
            "goto": "menunode_set_desc",
        },
        {
            "key": ("(Back)", "back", "b"),
            "desc": "Go back to pronouns",
            "goto": "menunode_choose_gender",
        },
    ]

    return text, options


#########################################################
#                Choosing a Name
#########################################################


def menunode_choose_name(caller, raw_string, **kwargs):
    """Name selection"""
    char = caller.new_char

    # another decision, so save the resume point
    char.db.chargen_step = "menunode_choose_name"

    # check if an error message was passed to the node. if so, you'll want to include it
    # into your "name prompt" at the end of the node text.
    if error := kwargs.get("error"):
        prompt_text = f"{error}. Enter a different name."
    else:
        # there was no error, so just ask them to enter a name.
        prompt_text = "Enter a name here to check if it's available."

    # this will print every time the player is prompted to choose a name,
    # including the prompt text defined above
    text = dedent(
        f"""\
        |wChoose a Name|n

        Please avoid inappropriate names or you will be asked to come up with a new one.

        {prompt_text}
        """
    )

    # help = "You'll have a chance to change your mind before confirming, even if the name is free."
    # since this is a free-text field, we just have the one
    options = {"key": "_default", "goto": _check_charname}
    # return (text, help), options
    return text, options


def _check_charname(caller, raw_string, **kwargs):
    """Check and confirm name choice"""

    # strip any extraneous whitespace from the raw text
    # if you want to do any other validation on the name, e.g. no punctuation allowed, this
    # is the place!
    charname = raw_string.strip()

    # aside from validation, the built-in normalization function from the caller's Account does
    # some useful cleanup on the input, just in case they try something sneaky
    charname = caller.account.normalize_username(charname)

    # check to make sure that the name doesn't already exist
    candidates = Character.objects.filter_family(db_key__iexact=charname)
    if len(candidates):
        # the name is already taken - report back with the error
        return (
            "menunode_choose_name",
            {"error": f"|w{charname}|n is unavailable.\n\nEnter a different name."},
        )
    else:
        # it's free! set the character's key to the name to reserve it
        caller.new_char.key = charname.capitalize()
        # continue on to the confirmation node
        return "menunode_confirm_name"


def menunode_confirm_name(caller, raw_string, **kwargs):
    """Confirm the name choice"""
    char = caller.new_char

    # since we reserved the name by assigning it, you can reference the character key
    # if you have any extra validation or normalization that changed the player's input
    # this also serves to show the player exactly what name they'll get
    text = f"|w{char.key}|n is available! Confirm?"
    # let players change their mind and go back to the name choice, if they want
    options = [
        {"key": ("Yes", "y"), "goto": "menunode_end"},
        {"key": ("No", "n"), "goto": "menunode_choose_name"},
    ]
    return text, options


#########################################################
#                     The End
#########################################################


def menunode_end(caller, raw_string):
    """End-of-chargen cleanup."""
    char = caller.new_char
    # since everything is finished and confirmed, we actually create the starting objects now
    protos = ["tarnished_sword", "wool_leggings", "wool_tunic", "leather_boots"]
    objs = spawn(*protos)
    for obj in objs:
        obj.location = char
        # obj.wear(char, True, quiet=True)
    # get start location
    if newbie := char.search("millennium square", global_search=True, quiet=True):
        char.home = newbie[0]
    # start_location = ObjectDB.objects.get_id(settings.START_LOCATION)
    #596 = cot, #717 = newbie
    # char.location = ObjectDB.objects.get_id(717)
    char.location = newbie[0]

    # clear in-progress status
    caller.new_char.attributes.remove("chargen_step")
    text = dedent(
        """
        Congratulations!

        You have completed character creation. Enjoy the game!
        """
    )
    return text, None