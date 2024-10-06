# open mystic forest
@tel newbie#1
@open south;s,north;n = (4, 4, mystical_forest)

# open chessboard
@tel chaos#2
@open chessboard,leave = (5,8,chessboard)

# open training grounds
@tel chaos#3
@open north;n,south;s = (1, 1, training_grounds)

# open crushbone




@tel chaos#1
#
@dig/teleport Path to the Training Grounds;chaos#3 : typeclasses.rooms.Room = west;w,east;e
#
@desc |YThe path to the training grounds in Millennium's Chaos Realm is a corridor of futuristic chaos. The ground is a metallic alloy, interspersed with glowing energy conduits that pulse with an eerie blue light. Holographic signs flicker, displaying cryptic messages and directions. The air hums with the sound of distant machinery and the occasional zap of an energy weapon. As you move forward, the walls shift and change, displaying scenes of past battles and training sessions. Robotic sentinels patrol the area, their red eyes scanning for any signs of intruders. The atmosphere crackles with a sense of high-tech tension, urging you onward to the advanced training grounds where warriors prepare for intergalactic conflicts.
#
@dig/teleport Training Grounds;training_grounds#1 : typeclasses.rooms.Room = north;n,south;s
#
@desc |YYou step into the Training Grounds, a state-of-the-art facility designed to hone the skills of adventurers. The walls are lined with advanced training equipment, from energy-based weapons to magical artifacts, each station offering a unique challenge. |/|/In the center of the room, a large, open space is dedicated to sparring and combat practice. Here, seasoned trainers-both cybernetic warriors and mystical sages-guide newcomers through rigorous drills. The air is filled with the sounds of clashing weapons, bursts of magical energy, and the encouraging shouts of instructors.
#
@open north;n,south;s = (1, 1, training_grounds)
#

#
@tel newbie#1
#

#
s
#
@open north;n = newbie#1 


#
@tel town#37
#
@dig/teleport Shimmering Portal;newbie#1 : typeclasses.rooms.Room = south;s,north;n
#
@desc |YAs you step through the shimmering portal from Millennium, you find yourself at the threshold of the Mystical Forest. The transition is almost seamless, yet the change in atmosphere is palpable. The air here is thick with magic, and the scent of blooming flowers mingles with the earthy aroma of ancient trees. |/|/Before you lies a narrow path, illuminated by glowing stones embedded in the ground. The light creates a magical ambiance, guiding you deeper into the forest. The trees tower above, their leaves shimmering with a faint, ethereal glow. It's as if the forest itself is alive, whispering secrets and welcoming you into its embrace. |/|/You take a cautious step forward, your boots sinking slightly into the soft, moss-covered ground. The sounds of Millennium fade away, replaced by the gentle rustling of leaves and the distant calls of mystical creatures. Every step you take is accompanied by the soft crunch of fallen leaves and the occasional snap of a twig. |/|/As you venture further, the path widens into a serene clearing. Here, the trees part to reveal a sky filled with twinkling stars, even though it's still daylight. The ground is covered in a carpet of vibrant, luminescent flowers that seem to pulse with their own inner light. You can't help but feel a sense of awe and wonder at the beauty surrounding you. |/|/
#
@open south;s,north;n = (4, 4, mystical_forest)
#


#
@tel town#37
#
#
@dig/teleport In front of a chessboard;town#38 : typeclasses.rooms.Room = west;w,east;e
#
@desc |YThe room is dominated by a life-size chessboard, each square large enough to accommodate a full-grown person. On the black and white tiles, gnolls and skeletons clash in a fierce battle. The gnolls, with their hyena-like features and crude armor, snarl and swing their weapons with savage intensity. Opposing them, skeletal warriors, their bones clattering with each movement, wield rusted swords and shields. The air is thick with the sounds of combat, and the eerie glow of torches casts flickering shadows across the scene, making the battle seem almost otherworldly.
#
@open chessboard,leave = (5,8,chessboard)
#



#
@desc |YYou stand before the imposing gates of Castle Crushbone, a fortress that exudes an aura of ancient power and foreboding. The massive stone walls, weathered by time and battle, rise high into the sky, their surfaces etched with the scars of countless sieges. Iron spikes crown the battlements, glinting menacingly in the dim light.|/|/The entrance itself is a grand archway, flanked by towering statues of fierce orc warriors, their eyes seemingly watching your every move. Heavy wooden doors, reinforced with iron bands, stand slightly ajar, creaking ominously with the slightest breeze. Vines and moss cling to the stone, adding a touch of wildness to the otherwise formidable structure.|/|/The air is thick with the scent of damp earth and the faint, metallic tang of old blood. As you step closer, you can hear the distant sounds of clashing weapons and the guttural growls of orcish guards patrolling the inner courtyard. The ground beneath your feet is uneven, littered with broken weapons and the remnants of past battles.|/|/Despite the eerie atmosphere, there is a sense of anticipation in the air, as if the castle itself is waiting for the next brave soul to challenge its depths. Will you dare to enter and face the unknown dangers that lie within Castle Crushbone?


#

@dig/teleport Computer Alley;chaos#5 : typeclasses.rooms.Room = south;s,north;n
#
@desc |YOn the way to Youtube