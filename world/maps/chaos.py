@tel town#15
#
@dig/teleport A vortex of swirling light and energy;chaos#1 : typeclasses.rooms.Room = enter,vortex
#
@desc |yYou step through the swirling vortex and find yourself in the heart of the realm. The air crackles with energy, and the sky above shifts through a kaleidoscope of colors. The ground beneath your feet is uneven, made up of jagged rocks and patches of strange, glowing vegetation. In the distance, you can see twisted, otherworldly structures that defy the laws of physics. The atmosphere is thick with an eerie, almost tangible sense of unpredictability.|/|/Amidst the chaos, the swirling vortex you entered through remains a constant, its shimmering surface offering a way back to the familiar safety of your town. The vortex pulses gently, as if beckoning you to return whenever you are ready.|/|/You can jump through the vortex to get back to the safety of Nexus, or you can choose to explore the realm.
#


#
@dig/teleport In front of a chessboard;chaos#2 : typeclasses.rooms.Room = east;e,west;w
#
@desc |GThe room is dominated by a life-size chessboard, each square large enough to accommodate a full-grown person. On the black and white tiles, gnolls and skeletons clash in a fierce battle. The gnolls, with their hyena-like features and crude armor, snarl and swing their weapons with savage intensity. Opposing them, skeletal warriors, their bones clattering with each movement, wield rusted swords and shields. The air is thick with the sounds of combat, and the eerie glow of torches casts flickering shadows across the scene, making the battle seem almost otherworldly.
#
@open chessboard,leave = (1,1,chessboard)
#
chessboard
#
@open leave = chaos#2
#


#
@dig/teleport An entrance to training grounds;chaos#3 : typeclasses.rooms.Room = west;w,east;e
#
@desc |GThe room is dominated by a life-size chessboard, each square large enough to accommodate a full-grown person. On the black and white tiles, gnolls and skeletons clash in a fierce battle. The gnolls, with their hyena-like features and crude armor, snarl and swing their weapons with savage intensity. Opposing them, skeletal warriors, their bones clattering with each movement, wield rusted swords and shields. The air is thick with the sounds of combat, and the eerie glow of torches casts flickering shadows across the scene, making the battle seem almost otherworldly.
#
@open enter,leave = (1,1,training_grounds)
#





#
@dig/teleport An entrance to Crushbone;chaos#4 : typeclasses.rooms.Room = north;n,south;s
#
@desc |GThe entrance Crushbone Keep
#
@open enter = (1,1,crushbone)
#
enter
#
@open leave = chaos#4

@tel (8,2,crushbone)
#
@dig/teleport Trainer's Hill;crushbone#1 : typeclasses.rooms.SpecialMobRoom = up;u,down;d
#
@desc |YAs you climb the hill, you see a large, open area at the top. The ground is covered in patches of grass and wildflowers, and the air is filled with the sound of birdsong. At the center of the hilltop, a large, flat rock serves as a natural platform, overlooking the surrounding landscape. From this vantage point, you can see the entire training grounds, with its various obstacles and training areas.
#
