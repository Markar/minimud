#
# Evennia batchfile - tutorial_world
#
# Griatch 2011, 2015
#
# This batchfile sets up a starting tutorial area for Evennia.
#
# This uses the custom script parents and code snippets found in the
# same folder as this script; Note that we are not using any
# modifications of the default player character at all (so you don't
# have to change anything in any settings files). We also don't modify
# any of the default command functions (except in states). So bear in
# mind that the full flexibility of Evennia is not used to its maximum
# potential here.
#
# To load this file, place yourself in Limbo (room #2) and load the
# file as user #1 with
#
#     batchcommand contrib.tutorials.tutorial_world.build
#
# If you give the /interactive switch you can step through the
# build process command for command.
#
# The area we are building looks like this:
#
#     ? 03,04
#     |
# +---+----+    +-------------------+    +--------+   +--------+
# |        |    |                   |    |gate    |   |corner  |
# | cliff  +----+   05 bridge       +----+  09    +---+   11   |
# |   02   |    |                   |    |        |   |        |
# +---+----+    +---------------+---+    +---+----+   +---+----+
#     |    \                    |            |   castle   |
#     |     \  +--------+  +----+---+    +---+----+   +---+----+
#     |      \ |under-  |  |ledge   |    |wall    |   |court-  |
#     |       \|ground  +--+  06    |    |  10    +---+yard    |
#     |        |   07   |  |        |    |        |   |   12   |
#     |        +--------+  +--------+    +--------+   +---+----+
#     |                \                                  |
#    ++---------+       \  +--------+    +--------+   +---+----+
#    |intro     |        \ |cell    |    |        |   |temple  |
# o--+   01     |         \|  08    +----+  trap  |   |   13   |
#    |          |          |        |   /|        |   |        |
#    +----+-----+          +--------+  / +--+-+-+-+   +---+----+
#         |                           /     | | |         |
#    +----+-----+          +--------+/   +--+-+-+---------+----+
#    |outro     |          |tomb    |    |antechamber          |
# o--+   16     +----------+  15    |    |       14            |
#    |          |          |        |    |                     |
#    +----------+          +--------+    +---------------------+
#
# There are a few ways we could have gone about building this layout;
# one is to do all the digging in one go first, then go back and add
# all the details. The advantage of this is that the area is
# already there and you can more easily jump ahead in the build file
# to the detail work when you want to update things later. In this
# file we will however build and design it all in sequence; room by
# room. This makes it easier to keep an overview of what is going on
# in each room, tie things to parents, etc.  When building your own
# world you might want to separate your world into a lot more
# individual batch files (maybe one for just a few rooms) for easy
# handling. The numbers mark the order of construction and also the
# unique alias-ids given to each room, to allow safe teleporting and
# linking between them.
#
#------------------------------------------------------------
# Starting to build the tutorial
#
# This is simple welcome text introducing the tutorial.
#------------------------------------------------------------
#
# We start from limbo. Remember that every command in the batchfile
# -must- be separated by at least one comment-line.
@tel #2
#
# Build the intro room (don't forget to also connect the outro room to this later)
#
# Note the unique alias tut#XX we give each room. This is used to
# easily reference this object from other objects in the build script
# without knowing the dbref. One empty line results in a line-break in
# the game, whereas two lines create a new paragraph. The length of the
# lines in the batchfile does not matter, in-game they will fill the
# lines to the width as defined by the
# player's client.
#
@dig Intro;tut#01
 : tutorial_world.rooms.IntroRoom
#
# Open an exit to tutorial. We don't do this in the @dig
# command since we want to describe the exit.
#
@open tutorial;tut : tutorial_world.rooms.TutorialStartExit = tut#01
#
# describe the tutorial exit
#
@desc tutorial =
 This exit leads to the |gEvennia tutorial|n, a small solo game to examine.
 Before going there, you may want to enter |wintro|n to get some general help
 on using the default commands.
#
# now we actually go to the tutorial
#
tutorial
#
# ... and describe it.
#
@desc
 |gWelcome to the Evennia tutorial-world!|n

 This small quest shows some examples of Evennia usage.

 To get into the mood of this miniature quest, imagine you are an adventurer
 out to find fame and fortune. You have heard rumours of an old castle ruin by
 the coast. In its depth a warrior princess was buried together with her
 powerful magical weapon - a valuable prize, if it's true.  Of course this is a
 chance to adventure that you cannot turn down!

 You reach the coast in the midst of a raging thunderstorm. With wind and rain
 screaming in your face you stand where the moor meet the sea along a high,
 rocky coast ...

|gwrite 'begin' to start your quest!|n

#
# Show that the tutorial command works ...
#
@set here/tutorial_info =
 You just tried the |wtutorial|G command. Use it in various rooms to see
what's technically going on and what you could try in each room. The
intro room assigns some properties to your character, like a simple
"health" property used when fighting. Other rooms and puzzles might do
the same. Leaving the tutorial world through any of the normal exit
rooms will clean away all such temporary properties.

If you play this scenario as superuser, you will see a big red
warning.  This warning is generated in the intro-rooms Typeclass.

#------------------------------------------------------------
#
# Outro room
#
# Called from the Intro room; this is a shortcut out of the
# tutorial. There is another outro room at the end showing more text.
# This is the only room we don't give a unique id.
#------------------------------------------------------------
#
@dig/teleport Leaving Tutorial
 : tutorial_world.rooms.OutroRoom
 = exit tutorial;exit;back, start again;start
#
@desc
 You are quitting the Evennia tutorial prematurely! Please come back
 later.
#
@open exit = #2
# This text is what the @tutorial command finds and displays.
@set here/tutorial_info =
 This outro room cleans up properties on the character that was set by
 the tutorial.
#
# Step back to intro room so we can build from there.
#
start
#------------------------------------------------------------
#
# The cliff
#
#------------------------------------------------------------
#
# This room inherits from a Typeclass called WeatherRoom. It regularly
# and randomly shows some weather effects. Note how we can spread the
# command's arguments over more than one line for easy reading.  We
# also make sure to create plenty of aliases for the room and
# exits. Note the alias tut#02: this unique identifier can be used
# later in the script to always find the way back to this room (for
# example by teleporting and similar). This is necessary since there
# is no way of knowing beforehand what dbref a given room will get in the
# database.
#
@dig/teleport Cliff by the coast;cliff;tut#02
 : tutorial_world.rooms.WeatherRoom
 = begin adventure;begin;start
#
# We define the tutorial message seen when using the tutorial command
#
 @set here/tutorial_info =
 Weather room

 This room inherits from a parent called WeatherRoom. It uses the
 tickerhandler to regularly 'tick and randomly display various
 weather-related messages.

 The room also has 'details' set on it (such as the ruin in the distance), those
 are snippets of text stored on the room that the custom look command
 used for all tutorial rooms can display.
#
@desc
 You stand on the high coast line overlooking a stormy |wsea|n far
 below. Around you the ground is covered in low gray-green grass,
 pushed flat by wind and rain. Inland, the vast dark moors begin, only
 here and there covered in patches of low trees and brushes.

 To the east, you glimpse the ragged outline of a castle |wruin|n. It sits
 perched on a sheer cliff out into the water, isolated from the
 shore. The only way to reach it seems by way of an old hanging bridge,
 anchored not far east from here.
#
# Mood-setting details to look at. This makes use of the custom look
# command in use on tutorial rooms to display extra text strings. It
# adds the detail as a dictionary Attribute on the room.
#
@detail ruin;ruins;castle =
 A fair bit out from the rocky shores you can make out the foggy
 outlines of a ruined castle. The once mighty towers have crumbled and
 it presents a jagged shape against the rainy sky. The ruin is perched
 on its own cliff, only connected to the mainland by means of an old
 hanging bridge starting not far east from you.
#
@detail sea;ocean;waves =
 The gray sea stretches as far as the eye can see to the east. Far
 below you its waves crash against the foot of the cliff. The vast
 inland moor meets the ocean along a high and uninviting coastline of
 ragged vertical stone.

 Once this part of the world might have been beautiful, but now the
 eternal winds and storms have washed it all down into a gray and
 barren wasteland.
#
@detail
#
# This is the well you will come back up from if you end up in the underground.
#
@create/drop Old well;well
#
@desc well =
 The ruins of an old well sit some way off the path. The stone circle
 has collapsed and whereas there is still a chain hanging down the
 hole, it does not look very secure. It is probably a remnant of some
 old settlement back in the day.
#
# It's important to lock the well object or players will be able to
# pick it up and put it in their pocket ...
#
@lock well = get:false()
#
# By setting the lock_msg attribute there will be a nicer error message if people
# try to pick up the well.
#
@set well/get_err_msg =
 You nudge the heavy stones of the well with a foot. There is no way
 you can ever budge this on your own (besides, what would you do with
 all those stones? Start your own quarry?).
#
@set well/tutorial_info =
 This is a normal object, locked with the lock get:false() so that
 Characters can't pick it up. Since the get_err Attribute is also set,
 you get a customized error message when trying to pick it up (that
 is checked and echoed by the 'get' command).
#
@create/drop Wooden sign;sign : tutorial_world.objects.TutorialReadable
#
@desc sign =
 The wooden sign sits at the end of a small eastward path. Beyond it
 is the shore-side anchor of the hanging bridge that connects the main
 land with the castle ruin on its desolate cliff. The sign is not as
 old as the rest of the scenery and the text on it is easily readable.
#
@lock sign = get:false()
#
@set sign/get_err_msg = The sign is securely anchored to the ground.
#
@set sign/readable_text =

 |rWARNING - The bridge is not safe!|n

 Below this official warning, someone has carved some sprawling
 letters into the wood. It reads: "The guardian will not bleed to
 mortal blade."
#
@set sign/tutorial_info =
 This is a readable object, of the Typeclass
 evennia.contrib.tutorials.tutorial_world.objects.TutorialReadable. The sign has a cmdset
 defined on itself, containing only one command, namely 'read'. This
 command is what allows you to 'read sign'. Doing so returns the
 contents of the Attribute 'readable_sign', containing the information
 on the sign.
# Set a climbable object for discovering a hidden exit
#
@create/drop gnarled old tree;tree;trees;gnarled : tutorial_world.objects.TutorialClimbable
#
@desc tree = Only the sturdiest of trees survive at the edge of the
 moor. A small huddling black thing has dug in near the
 cliff edge, eternally pummeled by wind and salt to become an integral
 part of the gloomy scenery.
#
@lock tree = get:false()
#
@set trees/get_err_msg =
 The group of old trees have withstood the eternal wind for hundreds
 of years. You will not uproot them any time soon.
#
@set trees/tutorial_info =
 These are climbable objects; they make for a small puzzle for
 accessing a hidden exit. Climbing the trees allows the
 TutorialClimbable typeclass to assign an Attribute on the character
 that an exit is then looking for.
#
# The text to echo to player if trying 'climb tree'. What
# happens when we do this is that the climb command assigns
# a Tag 'tutorial_climbed_tree' on the climber. The footpath
# exit (created below) is locked with this tag, meaning that
# it can only be seen/traversed by someone first having
# climbed.
#
@set tree/climb_text =
 With some effort you climb one of the old trees.


 The branches are wet and slippery but can easily carry your
 weight. From this high vantage point you can see far and wide.

 ... In fact, you notice |Ya faint yellowish light|n not far to the north,
 beyond the trees. It looks like some sort of building. From this angle
 you can make out a |wfaint footpath|n leading in that direction, all
 but impossible to make out from ground level. You mentally register
 where the footpath starts and will now be able to find it again.


 You climb down again.

#------------------------------------------------------------
#
# Outside Evennia Inn (hidden path)
#
#------------------------------------------------------------

#
# We dig the room without moving to it.
#
@dig Outside Evennia Inn;outside inn;tut#03
 : tutorial_world.rooms.WeatherRoom
 = northern path;north;n;path,back to cliff;back;cliff;south;s
#
# Lock exit from view/traverse until we climbed that tree (which is
# when tutorial_climbed_tree Tag gets assigned to us).
#
@lock north = view:tag(tutorial_climbed_tree, tutorial_world) ; traverse:tag(tutorial_climbed_tree, tutorial_world)
#
@desc north =
 This is a hardly visible footpath leading off through the rain-beaten
 grass. It seems to circle the trees northward. You would never had
 noticed it had you not spotted it from up in the tree.
#
@set north/tutorial_info =
 This exit is locked with a lock string that looks like this:

   view:tag(tutorial_climbed_tree, tutorial_world) ; traverse:tag(tutorial_climbed_tree, tutorial_world)

 This checks if Character has a Tag named "tutorial_climbed_tree" and
of the category "tutorial_world" set before it allows itself to be
displayed. This Tag is set by the tree object when the 'climb' command
is used.
#
# Now that the exit is prepared, move to outside inn to continue building.
#
north
#
@desc
 You stand outside a one-story sturdy wooden building. Light flickers
 behind closed storm shutters. Over the door a sign creaks in the wind
 - the writing says |cEvennia Inn|n and the curly letters are
 surrounded by a painted image of some sort of snake.  From inside you
 hear the sound of laughter, singing and loud conversation.
#
# Some details to look at
#
@detail shutters;storm =
 The shutters are closed.
#
@detail inn;sign =
 You think you might have heard of this name before,
 but at the moment you can't recall where from.
#
@detail snake;letters;writing =
 The snake is cartoonish with big googly eyes. It looks somewhat
 like one of those big snakes from the distant jungles - the kind
 squeezes their victims.

#------------------------------------------------------------
#
# The Evennia Inn (hidden path)
#
#------------------------------------------------------------
#
@dig/teleport The Evennia Inn;evennia inn;inn;tut#04
 : tutorial_world.rooms.TutorialRoom
 = enter;in,leave;out
#
@desc The Evennia Inn consists of one large room filled with
 tables. The bardisk extends along the east wall, where multiple
 barrels and bottles line the shelves. The barkeep seems busy handing
 out ale and chatting with the patrons, which are a rowdy and cheerful
 lot, keeping the sound level only just below thunderous. This is a
 rare spot of warmth and mirth on this dread moor.


 Soon you have a beer in hand and are chatting with the locals. Your
 eye falls on a |wbarrel|n in a corner with a few old rusty weapons
 sticking out. There is a sign next to it: |wFree to take|n. A patron
 tells you cheerfully that it's the leftovers from those foolish
 adventurers that challenged the old ruin before you ...

 (to get a weapon from the barrel, use |wget weapon|n)
#
@detail barkeep;man;landlord =
 The landlord is a cheerful fellow, always ready to supply you with
 more beer. He mentions doing some sort of arcane magic known as
 "software development" when not running this place. Whatever that
 means.
#
@set here/tutorial_info =
 Nothing special about this room, only a bonus place to potentially go
 for chatting with other online players. Oh, and don't forget to grab
 a blade if you don't already have one.
#
# Create the weapon rack (the barrel)
#
@create/drop barrel: tutorial_world.objects.TutorialWeaponRack
#
@desc barrel =
 This barrel has the air of leftovers - it contains an assorted
 mess of random weaponry in various states and qualities.
#
@lock barrel = get:false()
#
# Players trying to pickup barrel will receive hint to 'get weapon' instead
#
@set barrel/get_err_msg =
 The barkeep shakes his head. He says: 'Get weapon, not the barrel.'
#
# This id makes sure that we cannot pick more than one weapon from this rack
#
@set barrel/rack_id = "rack_barrel"
#
# Set which weapons are available from this rack. These are prototype-keys
# defined in tutorial_world.objects.WEAPON_PROTOTYPES. We also set a
# message to use when trying to grab a second weapon.
#
@set barrel/available_weapons = ["knife", "dagger", "sword", "club"]
#
@set barrel/no_more_weapons_msg =
    The barkeep shakes his head. He says: 'Sorry pal. We get a lot of needy
    adventurers coming through here. One weapon per person only.'
#
#------------------------------------------------------------
#
# The old bridge
#
#------------------------------------------------------------
#
# Back to cliff
@teleport tut#02
#
# The bridge uses parent tutorial_world.rooms.BridgeRoom, which causes
# the player to take a longer time than expected to cross as they are
# pummeled by wind and a chance to fall off. This room should not have
# regular exits back to the cliff, that is handled by the bridge
# typeclass itself.
#
@dig The old bridge;bridge;east;e;tut#05
 : tutorial_world.rooms.BridgeRoom
 = old bridge;east;e;bridge;hangbridge
#
# put some descriptions on the exit to the bridge
#
@desc bridge =
 The hanging bridge's foundation sits at the edge of the cliff to the
 east - two heavy stone pillars anchor the bridge on this side. The
 bridge sways precariously in the storm.
#
# go to the bridge
#
bridge
#
# Set up properties on bridge room (see contrib.tutorials.tutorial_world.rooms.BridgeRoom)
#
# connect west edge to cliff
#
@set here/west_exit = tut#02
#
# connect other end to gatehouse (we have not created it yet
# but we know it will have alias tut#09 according to our map)
#
@set here/east_exit = tut#09
#
# Fall location is the cliff ledge (created next)
#
@set here/fall_exit = tut#06
#
@set here/tutorial_info =
 All of the bridge is actually a single room that uses a custom cmdset
 to overrule the movement commands. This makes it take several steps to
 cross it despite it being only one room in the database.


 The bridge has no normal exits, instead it has a counter that tracks
 how far out on the bridge the Character is. For the bridge to work it
 needs the names of links to the adjoining rooms, and when the counter
 indicates the Character is leaving the bridge, they are teleported
 there.


 The room also inherits from the weather room to cause the bridge to
 sway at regular intervals. It also implements a timer and a random
 occurrence at every step across the bridge. It might be worth trying
 this passage a few times to see what may happen.  Hint: you can fall
 off!

#------------------------------------------------------------
#
# Ledge under the bridge
#
#------------------------------------------------------------
#
# You only end up at the ledge if you fall off the bridge. It
# has no direct connection to the bridge but we specified
# it as the target of the "fall_exit", which is a special
# feature of the BridgeRoom.
#
@dig/teleport Protruding ledge;cliffledge;ledge;tut#06
 : tutorial_world.rooms.WeatherRoom
#
@set here/tutorial_info =
 This room is stored as an attribute on the 'Bridge' room and used as
 a destination should the player fall off the bridge. It is the only
 way to get to this room. In our example the bridge is relatively
 simple and always drops us to the same ledge; a more advanced
 implementation might implement different locations to end up in
 depending on what happens on the bridge.
#
@desc
 You are on a narrow ledge protruding from the side of the cliff,
 about halfway down.  The air is saturated with salty sea water,
 sprays hitting your face from the crashing waves |wbelow|n.

 The ledge is covered with a few black-grey brushes. Not far from you
 the cliff-face is broken down to reveal a narrow natural opening into
 the cliff. High above you the |wbridge|n sways and creaks in the wind.
#
@detail brush;brushes =
 The brushes covering the ledge are gray and dwarfed from constantly
 being pummeled by salt, rain and wind.
#
@detail below;sea;ocean;waves =
 Below you the gray sea rages, its waves crashing into the cliff so a
 thin mist of salt mixes with the rain even this far above it. You can
 almost imagine the cliff trembling under its onslaught.
#
@detail bridge =
 Partly obscured by the rain you can make out the shape of the hanging
 bridge high above you. There is no way to get back up there from this
 ledge.


#------------------------------------------------------------
#
# Underground passages
#
#------------------------------------------------------------
#
# The underground passages allow the player to get back up to the
# cliff again. If you look at the map, the 'dark cell' also connects
# to here. We'll get to that later.
#
@dig Underground passages;passages;underground;tut#07
 : tutorial_world.rooms.TutorialRoom
 = hole into cliff;hole;passage;cliff
#
# Describe the exit
#
@desc hole into cliff =
 The hole is natural, the soft rock eroded by ages of sea water. The
 opening is small but large enough for you to push through. It looks
 like it expands into a cavern further in.
#
hole
#
@set here/tutorial_info =
 This room acts as a hub for getting the player back to the
 start again, regardless of how you got here.
#
@desc
 The underground cavern system you have entered seems to stretch on
 forever, with criss-crossing paths and natural caverns probably
 carved by water. It is not completely dark, here and there faint
 daylight sifts down from above - the cliff is porous leaving channels
 of air and light up to the surface.


 (some time later)


 You eventually come upon a cavern with a black pool of stale
 water. In it sits a murky bucket, the first remnant of any sort of
 intelligent life down here. The bucket has disconnected from a chain
 hanging down from a circular opening high above. Gray daylight
 simmers down the hole together with rain that ripples the black
 surface of the pool.
#
@detail pool;water =
 The water of the pool is black and opaque. The rain coming down from
 above does not seem to ripple the surface quite as much as it should.
#
@detail bucket =
 The bucket is nearly coming apart, only rusty iron bands holding
 the rotten wood together. It's been down here for a long time.
#
@detail hole;above =
 Whereas the lower edges of the hole seem jagged and natural you can
 faintly make out it turning into a man-made circular shaft higher up.
 It looks like an old well. There must have been much more water
 here once.
#
@detail passages;dark =
 Those dark passages seem to criss-cross the cliff. No need to
 head back into the gloom now that there seems to be a way out.
#
# From the passages we get back up to the cliff, so we
# open up a new exit back there.
#
# connect chain to Cliff.
@open climb the chain;climb;chain = tut#02
#
@desc chain =
 The chain is made of iron. It is rusty but you think it might still
 hold your weight even after all this time. Better hope you don't need
 to do this more times ...

#------------------------------------------------------------
#
# The Dark Cell
#
#------------------------------------------------------------
#
@dig/teleport Dark cell;dark;cell;tut#08
 : tutorial_world.rooms.DarkRoom
#
@set here/tutorial_info =
 Dark room

 The dark room implements a custom "dark" state. This is a very
 restricted state that completely redefines the look command and only
 allows limited interactions.

 Looking around repeatedly will eventually produce hints as to how to
 get out of the dark room.
#
# the description is only seen if the player first finds a
# light source.
#
@desc
 |YThe |yflickering light|Y of your makeshift light reveals a small square
 cell. It does not seem like you are still in the castle, for the
 stone of the walls are chiseled crudely and drip with water and mold.

 One wall holds a solid iron-cast door. While rusted and covered with
 lichen it seems very sturdy. In a corner lies what might have once
 been a bed or a bench but is now nothing more than a pile of splinters,
 one of which you are using for light. One of the walls is covered with a
 thick cover of black roots having broken through the cracks from the
 outside.|n
#
@detail iron-cast door;iron;door;iron-cast =
 The door is very solid and clad in iron. No matter how much you push
 at it, it won't budge. It actually doesn't show any signs of having
 been opened for a very long time.
#
@detail stone walls;walls;stone;stones;wall =
 The walls are dripping with moisture and mold. A network of roots
 have burst through the cracks on one side, bending the stones
 slightly aside. You feel a faint draft from that direction.
#
# The crumbling wall is in fact an advanced type of Exit, all we need to do is
# to supply it with a destination.
#
@create/drop root-covered wall;wall;roots;wines;root : tutorial_world.objects.CrumblingWall
#
#
# This destination is auto-assigned to the exit when its puzzle is solved
# connect to the Underground passages
@set root-covered wall/destination = tut#07
#
@lock roots = get:false()
#
# (the crumbling wall describes itself, so we don't do it here)
@set here/tutorial_info =
 This room presents a puzzle that has to be solved in order to get out
 of the room. The root-covered wall is in fact an advanced Exit-type
 object that is locked until the puzzle is solved.

#------------------------------------------------------------
#
# Castle Gate
# We are done with the underground, describe castle.
#------------------------------------------------------------
#
# We are done building the underground passages, let's
# head back up to ground level. We teleport to the bridge
# and continue from there.
#
@teleport tut#05
#
# The bridge room should not have any normal exits from it, that is
# handled by the bridge itself. So we teleport away from it. The
# ruined gatehouse is also the east_exit target for the bridge as
# we recall.
#
@dig/teleport Ruined gatehouse;gatehouse;tut#09
 : tutorial_world.rooms.TutorialRoom
 = , Bridge over the abyss;bridge;abyss;west;w
#
@set here/tutorial_info =
 This is part of a four-room area patrolled by a mob: the guardian of
 the castle. The mob initiates combat if the player stays in the same
 room for long enough.

 Combat itself is a very simple affair which takes advantage of the
 strength of the weapon you use, but dictates a fixed skill for you and
 your enemy. The enemy is quite powerful, so don't stick around too
 long ...
#
@desc
 The old gatehouse is near collapse. Part of its northern wall has
 already fallen down, together with parts of the fortifications in
 that direction.  Heavy stone pillars hold up sections of ceiling, but
 elsewhere the flagstones are exposed to open sky. Part of a heavy
 portcullis, formerly blocking off the inner castle from attack, is
 sprawled over the ground together with most of its frame.

 |wEast|n the gatehouse leads out to a small open area surrounded by
 the remains of the castle.  There is also a standing archway
 offering passage to a path along the old |wsouth|nern inner wall.
#
@detail portcullis;fall;fallen;grating =
 This heavy iron grating used to block off the inner part of the gate house, now it has fallen
 to the ground together with the stone archway that once help it up.
#
# We lock the bridge exit for the mob, so it don't wander out on the bridge. Only
# traversing objects controlled by an account (i.e. Characters) may cross the bridge.
#
@lock bridge = traverse:has_account()

#------------------------------------------------------------
#
# Along the southern inner wall (south from gatehouse)
#
#------------------------------------------------------------

@dig Along inner wall;inner wall;along;tut#10
 : tutorial_world.rooms.WeatherRoom
 = Standing archway;archway;south;s,ruined gatehouse;gatehouse;north;n
#
@desc standing archway =
 It seems the archway leads off into a series of dimly lit rooms.
#
archway
#
@set here/tutorial_info =
 This is part of a four-room area patrolled by a mob; the guardian of
 the castle. The mob initiates combat if the player stays in the same
 room for long enough.

 Combat itself is a very simple affair which takes advantage of the
 strength of the weapon you use, but dictates a fixed skill for you and
 your enemy.
#
@desc
 What appears at first sight to be a series of connected rooms
 actually turns out to be collapsed buildings so mashed together by
 the ravages of time that they all seem to lean on each other and
 against the outer wall. The whole scene is directly open to the sky.

 The buildings make a half-circle along the main wall, here and there
 broken by falling stone and rubble. At one end (the |wnorth|nern) of
 this half-circle is the entrance to the castle, the ruined
 gatehouse. |wEast|nwards from here is some sort of open courtyard.

#------------------------------------------------------------
#
# Corner of castle (east from gatehouse)
#
#------------------------------------------------------------
# back to castle gate
@teleport tut#09
#
@dig/teleport Corner of castle ruins;corner;tut#11
 : tutorial_world.rooms.TutorialRoom
 = castle corner;corner;east;e,gatehouse;west;w
#
@desc
 The ruins opens up to the sky in a small open area, lined by
 columns. The open area is dominated by a huge stone |wobelisk|n in its
 center, an ancient ornament miraculously still standing.

 Previously one could probably continue past the obelisk and eastward
 into the castle keep itself, but that way is now completely blocked
 by fallen rubble. To the |wwest|n is the gatehouse and entrance to
 the castle, whereas |wsouth|nwards the columns make way for a wide
 open courtyard.
#
@set here/tutorial_info =
 This is part of a four-room area patrolled by a mob; the guardian of
 the castle. The mob initiates combat if the player stays in the same
 room for long enough.

 Combat itself is a very simple affair which takes advantage of the
 strength of the weapon you use, but dictates a fixed skill for you and
 your enemy.
#
@create/drop obelisk:tutorial_world.objects.Obelisk
#
@lock obelisk = get:false()
#
@set obelisk/get_err_msg = It's way too heavy for anyone to move.
#
# Set the puzzle clues on the obelisk. The order should correspond
# to the ids later checked by the antechamber puzzle.
#
@set obelisk/puzzle_descs = ("You can briefly make out the image of |ba woman with a blue bird|n.", "You for a moment see the visage of |ba woman on a horse|n.", "For the briefest moment you make out an engraving of |ba regal woman wearing a crown|n.", "You think you can see the outline of |ba flaming shield|n in the stone.", "The surface for a moment seems to portray |ba sharp-faced woman with white hair|n.")

# Create the mobile. This is its start location.
@create/drop Ghostly apparition;ghost;apparition;fog : tutorial_world.mob.Mob
#
# Set its home to this location
#
@sethome ghost = tut#11
#
@lock ghost = get:false()
#
@set ghost/get_err_msg = Your fingers just pass straight through it!
#
@set ghost/desc_alive =
 This ghostly shape could momentarily be mistaken for a thick fog had
 it not moved with such determination and giving echoing hollow
 screams as it did. The shape is hard to determine, now and then it
 seems to form limbs and even faces that fade away only moments
 later. The thing reeks of almost tangible spite at your
 presence. This must be the ruin's eternal guardian.
#
@set ghost/desc_dead =
 The ghostly apparition is nothing but a howling on the wind, an eternal
 cold spot that can never be fully eradicated from these walls. While harmless
 in this state, there is no doubt that it shall eventually return to this plane
 to continue its endless haunting.
#
# We set the ghost to send defeated enemies to the Dark Cell
#
@set ghost/send_defeated_to = tut#08
#
@set ghost/defeat_msg =
 You fall to the ground, defeated. As you do, the ghostly apparition dives
 forward and engulf you.


 The world turns black.
#
@set ghost/defeat_msg_room =
 %s falls to the ground, defeated. For a moment their fallen form is
 engulfed by the swirling mists of the ghostly apparition. When they
 raise lift, the ground is empty!
#
@set ghost/weapon_ineffective_msg =
 Your weapon just passes through the swirling mist of the ghostly apparition, causing no effect!
#
@set ghost/hit_msg =
 The ghostly apparition howls and writhes, shifts and shivers.
#
@set ghost/death_msg =
 After the last strike, the ghostly apparition seems to collapse
inwards. It fades and becomes one with the mist. Its howls rise to a
ear-shattering crescendo before quickly fading away to be nothing more
than the lonely cries of the cold, salty wind.
#
# Give the enemy some random echoes (echoed at irregular intervals)
#
@set ghost/irregular_msgs =
 ["The foggy thing gives off a high-pitched shriek.",
  "For a moment the fog wraps around a nearby pillar.",
  "The fog drifts lower to the ground as if looking for something.",
  "The fog momentarily takes on a reddish hue.",
  "The fog temporarily fills most of the area as it changes shape.",
  "You accidentally breathes in some of the fog - you start coughing from the cold moisture."]
#

# give the enemy a tentacle weapon
#
@create foggy tentacles;tentacles:tutorial_world.objects.TutorialWeapon
#
# Make the enemy's weapon good - hits at 70% of attacks, but not good at parrying.
#
@set foggy tentacles/hit = 0.7
#
@set foggy tentacles/parry = 0.1
#
@set foggy tentacles/damage = 5
#
# Actually give the enemy its weapon
#
@teleport/quiet tentacles = ghost
#
# Start the mob
#
mobon ghost

#------------------------------------------------------------
#
# The courtyard
#
#------------------------------------------------------------
#
@dig/teleport Overgrown courtyard;courtyard;tut#12
 : tutorial_world.rooms.WeatherRoom
 = courtyard;south;s,castle corner;north;n
#
# Connect west exit to the inner wall
@open along inner wall;wall;along;west;w, overgrown courtyard;courtyard;east;e = tut#10
#
@set here/tutorial_info =
 This is part of a four-room area patrolled by a mob; the guardian of
 the castle. The mob initiates combat if the player stays in the same
 room for long enough.

 Combat itself is a very simple affair which takes advantage of the
 strength of the weapon you use, but dictates a fixed skill for you and
 your enemy.
#
@desc
 The inner courtyard of the old castle is littered with debris and
 overgrown with low grass and patches of thorny vines. There is a
 collapsed structure close to the gatehouse that looks like a stable.

 |wNorth|nwards is a smaller area cornered in the debris, adorned with
 a large obelisk-like thing. To the |wwest|n the castle walls loom
 over a mess of collapsed buildings. On the opposite, |weast|nern side
 of the yard is a large building with a curved roof that seem to have
 withstood the test of time better than many of those around it, it
 looks like some sort of temple.
#
@detail stables;stable;building =
 The building is empty, if it was indeed once a stable it was abandoned long ago.

#------------------------------------------------------------
#
# The temple
#
#------------------------------------------------------------
#
@dig/teleport The ruined temple;temple;in;tut#13
 : tutorial_world.rooms.TutorialRoom
 = ruined temple;temple;east;e, overgrown courtyard;courtyard;outside;out;west;w
#
@desc
 This building seems to have survived the ravages of time better than
 most of the others. Its arched roof and wide spaces suggests that
 this is a temple or church of some kind.


 The wide hall of the temple stretches before you. At the far edge is
 a stone altar with no clear markings. Despite its relatively good
 condition, the temple is empty of all furniture or valuables, like it
 was looted or its treasures moved ages ago.

 Stairs lead down to the temple's dungeon on either side of the
 altar. A gaping door opening shows the a wide courtyard to the west.
#
@detail altar =
 The altar is a massive stone slab. It might once have had ornate decorations
 but time and the salty air has broken everything down into dust.
#
@detail ceiling =
 The dome still looming intact above you is a marvel of engineering.

#------------------------------------------------------------
#
# Antechamber - below the temple
#
#------------------------------------------------------------
#
@dig Antechamber;antechamber;tut#14
 : tutorial_world.rooms.TutorialRoom
 =  stairs down;stairs;down;d, up the stairs to ruined temple;stairs;temple;up;u
#
@desc stairs down =
 The stairs are worn by the age-old passage of feet.
#
# Lock the antechamber so the ghost cannot get in there.
@lock stairs down = traverse:has_account()
#
# Go down
#
stairs down
#
@desc
 This chamber lies almost directly under the main altar of the
 temple. The passage of aeons is felt here and you also sense you are
 close to great power.

 The sides of the chamber are lined with stone archways, these are
 entrances to the |wtombs|n of what must have been influential
 families or individual heroes of the realm. Each is adorned by a
 stone statue or symbol of fine make. They do not seem to be ordered
 in any particular order or rank.
#
@set here/tutorial_info =
 This is the second part of a puzzle involving the Obelisk in the
 castle's north-east corner. The correct exit to use will vary
 depending on which scene was shown on the Obelisk surface.

 Each tomb is a teleporter room and is keyed to a number corresponding
 to the scene last shown on the obelisk (now stored on player). If the
 number doesn't match, the tomb is a trap that teleports to a second
 Teleporter room describing how you fall in a trap - that room then
 directly relay you on to the Dark Cell. If correct, the tomb
 teleports to the Ancient Tomb treasure chamber.
#
# We create all the tombs. These all teleport to the dark cell
# except one which is the one decided by the scene shown by the
# Obelisk last we looked.
#
@dig Blue bird tomb
 : tutorial_world.rooms.TeleportRoom
 = Blue bird tomb;bird;blue;stone
#
@desc Blue bird tomb =
The entrance to this tomb is decorated with a very lifelike blue bird.
#
Blue bird tomb
#
@set here/puzzle_value = 0
#
@set here/failure_teleport_to = tut#08
#
@set here/success_teleport_to = tut#15
#
@set here/failure_teleport_msg =
 The tomb is dark. You fumble your way through it. You think you can
 make out a coffin in front of you in the gloom.


 |rSuddenly you hear a distinct 'click' and the ground abruptly
 disappears under your feet! You fall ... things go dark. |n


 ...


 ... You come to your senses. You lie down. On stone floor. You
 shakily come to your feet. Somehow you suspect that you are not under
 the tomb anymore, like you were magically snatched away.

 The air is damp. Where are you?
#
@set here/success_teleport_msg =
 The tomb is dark. You fumble your way through it. You think you can
 make out a coffin in front of you in the gloom.

 The coffin comes into view. On and around it are chiseled scenes of a
 stern woman in armor. They depict great heroic deeds. This is clearly
 the tomb of some sort of ancient heroine - it must be the goal you
 have been looking for!
#
@tel tut#14
#
@dig Tomb of woman on horse
 : tutorial_world.rooms.TeleportRoom
 = Tomb of woman on horse;horse;riding;
#
@desc Tomb of woman on horse =
The entrance to this tomb depicts a scene of a strong
warrior woman on a black horse. She shouts and brandishes
a glowing weapon as she charges down a hill towards
some enemy not depicted.
#
Tomb of woman on horse
#
@set here/puzzle_value = 1
#
@set here/failure_teleport_to = tut#08
#
@set here/success_teleport_to = tut#15
#
@set here/failure_teleport_msg =
 The tomb is dark. You fumble your way through it. You think you can
 make out a coffin in front of you in the gloom.


 |rSuddenly you hear a distinct 'click' and the ground abruptly
 disappears under your feet! You fall ... things go dark. |n


 ...


 ... You come to your senses. You lie down. On stone floor. You
 shakily come to your feet. Somehow you suspect that you are not under
 the tomb anymore, like you were magically snatched away.

 The air is damp. Where are you?
#
@set here/success_teleport_msg =
 The tomb is dark. You fumble your way through it. You think you can
 make out a coffin in front of you in the gloom.

 The coffin comes into view. On and around it are chiseled scenes of a
 stern woman in armor. They depict great heroic deeds. This is clearly
 the tomb of some sort of ancient heroine - it must be the goal you
 have been looking for!
#
@tel tut#14
#
@dig Tomb of the crowned queen
 : tutorial_world.rooms.TeleportRoom
 = Tomb of the crowned queen;crown;queen
#
@desc Tomb of the crowned queen =
The entrance to this tomb shows a beautiful mural of a queen ruling
from her throne, respectful subjects kneeling before her. On her head
is a crown that seems to shine with magical power.
#
Tomb of the crowned queen
#
@set here/puzzle_value = 2
#
@set here/failure_teleport_to = tut#08
#
@set here/success_teleport_to = tut#15
#
@set here/failure_teleport_msg =
 The tomb is dark. You fumble your way through it. You think you can
 make out a coffin in front of you in the gloom.


 |rSuddenly you hear a distinct 'click' and the ground abruptly
 disappears under your feet! You fall ... things go dark. |n


 ...


 ... You come to your senses. You lie down. On stone floor. You
 shakily come to your feet. Somehow you suspect that you are not under
 the tomb anymore, like you were magically snatched away.

 The air is damp. Where are you?
#
@set here/success_teleport_msg =
 The tomb is dark. You fumble your way through it. You think you can
 make out a coffin in front of you in the gloom.

 The coffin comes into view. On and around it are chiseled scenes of a
 stern woman in armor. They depict great heroic deeds. This is clearly
 the tomb of some sort of ancient heroine - it must be the goal you
 have been looking for!
#
@tel tut#14
#
@dig Tomb of the shield
 : tutorial_world.rooms.TeleportRoom
 = Tomb of the shield;shield
#
@desc Tomb of the shield =
This tomb shows a warrior woman fighting shadowy creatures from the
top of a hill. Her sword lies broken on the ground before her but she
fights on with her battered shield - the scene depicts her just as she
rams the shield into an enemy in wild desperation.
#
Tomb of the shield
#
@set here/puzzle_value = 3
#
@set here/failure_teleport_to = tut#08
#
@set here/success_teleport_to = tut#15
#
@set here/failure_teleport_msg =
 The tomb is dark. You fumble your way through it. You think you can
 make out a coffin in front of you in the gloom.


 |rSuddenly you hear a distinct 'click' and the ground abruptly
 disappears under your feet! You fall ... things go dark. |n


 ...


 ... You come to your senses. You lie down. On stone floor. You
 shakily come to your feet. Somehow you suspect that you are not under
 the tomb anymore, like you were magically snatched away.

 The air is damp. Where are you?
#
@set here/success_teleport_msg =
 The tomb is dark. You fumble your way through it. You think you can
 make out a coffin in front of you in the gloom.

 The coffin comes into view. On and around it are chiseled scenes of a
 stern woman in armor. They depict great heroic deeds. This is clearly
 the tomb of some sort of ancient heroine - it must be the goal you
 have been looking for!
#
@tel tut#14
#
@dig Tomb of the hero
 : tutorial_world.rooms.TeleportRoom
 = Tomb of the hero;knight;hero;monster;beast
#
@desc Tomb of the hero =
The entrance to this tomb shows a mural of an aging woman in a
warrior's outfit. She has white hair yet her sword-arm shows no sign
of weakness and her pose is straight. Children are gathered around her
feet and men and women from all the land come to seek the wisdom and
strength of the legendary hero.
#
Tomb of the hero
#
@set here/puzzle_value = 4
#
@set here/failure_teleport_to = tut#08
#
@set here/success_teleport_to = tut#15
#
@set here/failure_teleport_msg =
 The tomb is dark. You fumble your way through it. You think you can
 make out a coffin in front of you in the gloom.


 |rSuddenly you hear a distinct 'click' and the ground abruptly
 disappears under your feet! You fall ... things go dark. |n


 ...


 ... You come to your senses. You lie down. On stone floor. You
 shakily come to your feet. Somehow you suspect that you are not under
 the tomb anymore, like you were magically snatched away.

 The air is damp. Where are you?
#
@set here/success_teleport_msg =
 The tomb is dark. You fumble your way through it. You think you can
 make out a coffin in front of you in the gloom.

 The coffin comes into view. On and around it are chiseled scenes of a
 stern woman in armor. They depict great heroic deeds. This is clearly
 the tomb of some sort of ancient heroine - it must be the goal you
 have been looking for!
#
# back to antechamber
@tel tut#14
#
#------------------------------------------------------------
#
# The ancient tomb
#
# This is the real tomb, the goal of the adventure. It is not
# directly accessible from the Antechamber but you are
# teleported here only if you solve the puzzle of the Obelisk.
#
#------------------------------------------------------------
#
@dig/teleport Ancient tomb;tut#15
 : tutorial_world.rooms.TutorialRoom
 =  ,back to antechamber;antechamber;back
#
@desc
 Apart from the ornate sarcophagus, the tomb is bare from extra decorations.
 This is the resting place of a warrior with little patience for
 glamour and trinkets. You have reached the end of your quest.
#
@set here/tutorial_info =
 Congratulations, you have reached the end of this little tutorial
 scenario. Just grab the mythical weapon (get weapon) and the exit
 will open.

 You can end the quest here or go back through the tutorial rooms to
 explore further. You will find this weapon works better against the
 castle's guardian than any of the others you have found ...
#
# The sarcophagus is a "weapon rack" from which you can extract one
# single weapon.
#
@create/drop Stone sarcophagus;sarcophagus;stone : tutorial_world.objects.TutorialWeaponRack
#
@desc stone =
 The lid of the coffin is adorned with a stone statue in full size.
The weapon held by the stone hands looks very realistic ...

 The hands of the statue close on what seems to be a real weapon
rather than one in stone.  This must be the hero's legendary weapon!
The prize you have been looking for!

 (try |wget weapon|n)
#
@set sarcophagus/rack_id = rack_sarcophagus
#
@set sarcophagus/available_weapons = ["ornate longsword","warhammer","rune axe","thruning","slayer waraxe","ghostblade","hawkblade"]
#
@set sarcophagus/no_more_weapons_msg =
 The tomb has already granted you all the might it will ever do.
#
@set sarcophagus/get_weapon_msg =
 Trembling you carefully release the weapon from the stone to test
 its weight. You are finally holding your prize,

  The |c%s|n

 in your hands!

 |gThis concludes the Evennia tutorial. From here you can either
 continue to explore the castle (hint: this weapon works better
 against the castle guardian than any you might have found earlier) or
 you can choose to exit.|n

#------------------------------------------------------------
#
# Outro - end of the tutorial
#
# This cleans all temporary attributes set on the Character
# by the tutorial, removes weapons and items etc.
#
#------------------------------------------------------------
#
@dig End of tutorial;end;tut#16
 : tutorial_world.rooms.OutroRoom
 = Exit tutorial;exit;end
#
# All weapons from the rack gets an automatic alias the same as the
# rack_id. This we can use to check if any such weapon is in inventory
# before unlocking the exit.
#
@lock Exit tutorial = view:tag(rack_sarcophagus, tutorial_world) ; traverse:tag(rack_sarcophagus, tutorial_world)
#
# to tutorial outro
@tel tut#16
#
# we want to clear the weapon-rack ids on the character when exiting.
@set here/wracklist = ["rack_barrel", "rack_sarcophagus"]
#
# this room quits the tutorial and cleans up all variables that were set.
@desc
 |gThanks for trying out this little Evennia tutorial!


 The game play given here is of course just scraping the surface of
 what can be done with Evennia. The tutorial focuses more on showing
 various techniques than to supply any sort of novel storytelling or
 gaming challenge.  The full README and source code for the tutorial
 world can be found under |wcontrib/tutorials/tutorial_world|g.


 If you went through the tutorial quest once, it can be interesting to
 do it again to explore the various possibilities and rooms you might
 not have come across yet, maybe with the source/build code next to
 you.  If you play as superuser (user #1) the mobile will ignore you
 and teleport rooms etc will not affect you (this will also disable all
 locks, so keep that in mind when checking functionality).|n
#
@set here/tutorial_info =
 This room cleans up all temporary attributes and tags that were put
 on the character during the tutorial. Hope you enjoyed the play
 through!
#
# Tie this back to Limbo
#
@open exit back to Limbo;limbo;exit;back = #2
#
@tel #2