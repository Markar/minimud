#
@dig/teleport Millennium Square;town#01: typeclasses.rooms.Room = west;w;east;e;north;n;south;s
#
@desc |YAs you step into the heart of the town, you're greeted by a mesmerizing blend of the past, present, and future. The central plaza, known as Millennium Square, is a bustling hub of activity. Towering above is a colossal, shimmering obelisk that pulses with an otherworldly energy, its surface etched with ancient runes and futuristic circuitry.|/|/Surrounding the obelisk, the buildings are a chaotic yet harmonious mix of styles. Sleek, metallic skyscrapers with holographic advertisements stand side by side with whimsical, fairy-tale cottages adorned with glowing crystals. The streets are alive with a diverse crowd: humans, elves, cyborgs, and other fantastical beings, all mingling together in a vibrant tapestry of cultures.|/|/Hovering platforms and flying vehicles zip through the air, while below, cobblestone paths wind through lush, enchanted gardens and bustling marketplaces. Street vendors peddle exotic wares, from enchanted artifacts to advanced technological gadgets. The air is filled with the sounds of lively chatter, the hum of machinery, and the occasional burst of magical energy.|/|/In the center of Millennium Square, a swirling vortex serves as a portal to other realms, adding an element of unpredictability to the town. Adventurers and travelers can be seen stepping through, embarking on quests or returning with tales of distant worlds.|/|/The town's chaotic charm is further enhanced by the ever-changing sky, which shifts from a serene blue to a kaleidoscope of colors, reflecting the town's unique blend of sci-fi and fantasy elements. Millennium Square is a place where anything is possible, and every corner holds a new adventure waiting to be discovered.
#
#
#
@dig/teleport Reception Hall;town#02 : typeclasses.rooms.Room = west;w,east;e
#
@desc |yThis is the reception hall.
#
@teleport town#01
#
#
#
@dig/teleport The Nexus Bazaar;town#03 : typeclasses.rooms.NexusBazaar = east;e,west;w
#
@desc |YNestled at the edge of Millennium Square, The Nexus Bazaar is a shop like no other. Its exterior is a blend of sleek, metallic panels and whimsical, fairy-tale architecture, adorned with glowing crystals that pulse in sync with the obelisk's energy. As you step inside, you're greeted by a dazzling array of goods from across time and space.|/|/Shelves made of shimmering, translucent material hold an eclectic mix of items: enchanted artifacts, advanced technological gadgets, and rare, otherworldly curiosities. Holographic displays float above the counters, showcasing the shop's most prized possessions. The air is filled with a faint hum of machinery and the occasional spark of magical energy.|/|/The shopkeeper, a cyborg with a friendly demeanor and a twinkle in their eye, stands behind a counter cluttered with mysterious trinkets and a sleek, digital ledger. They greet each customer with a warm smile and a wealth of knowledge about the shop's diverse inventory.|/|/In one corner, a portal shimmers, offering glimpses of distant realms and promising new adventures to those who dare to step through. The Nexus Bazaar is a place where the past, present, and future converge, and where every visit holds the promise of discovery and wonder.
#
@teleport town#01
#
#
#
@dig/teleport Southbound Pathway;town#04 : typeclasses.rooms.Room = north;n,south;s
#
# @desc |YAs you leave the bustling energy of Millennium Square behind, you find yourself on the Southbound Pathway. The road is a seamless blend of cobblestone and sleek, metallic panels, reflecting the town's unique fusion of old and new. Enchanted lanterns line the path, casting a soft, ethereal glow that guides your way.|/|/To your left, lush, enchanted gardens burst with vibrant flora, their colors shifting in harmony with the ever-changing sky. On your right, futuristic buildings with holographic signs advertise exotic goods and services. The air is filled with a mix of floral scents and the faint hum of advanced machinery, creating a sense of both tranquility and anticipation.
py setattr(here, "key", "Southbound Pathway")
#
#
#
@dig/teleport Western Pathway Junction;town#05 : typeclasses.rooms.Room = north;n,south;s
#
@desc |YHeading west from the Southbound Pathway, you find yourself on the Western Pathway Junction. The road here is a harmonious blend of cobblestone and sleek, metallic panels, reflecting the town's unique fusion of old and new. Enchanted lanterns line the path, casting a soft, ethereal glow that guides your way.|/|/To the north, the road leads back towards the vibrant energy of Millennium Square, where the obelisk pulses with otherworldly power.|/|/To the south, a narrow path veers off, leading towards the tranquil Enchanted Grove, where bioluminescent trees and mystical creatures await. The air is filled with a mix of floral scents and the faint hum of advanced machinery, creating a sense of both tranquility and anticipation.|/|/The Western Pathway Junction is a crossroads of adventure, offering a choice between the bustling energy of Millennium Square and the serene escape of the Enchanted Grove.
#
@teleport town#04
#
#
#
@dig/teleport Road;town#06 : typeclasses.rooms.Room = east;e,west;w;
#
@desc |yBefore the hospital.
#
#
#
@dig/teleport Hospital;town#07 : typeclasses.rooms.Room = north;n,south;s
#
@desc |yThe hospital.
#
@teleport town#06
#
#
#
@dig/teleport Road before the lockers;town#08 : typeclasses.rooms.Room = east;e,west;w
#
@desc |yYou can see lockers to the east.
#
#
#
@dig/teleport Lockers;town#09 : typeclasses.rooms.Room = east;e,west;w
#
@desc |yThe locker room.
#
@teleport town#08
#


#
@dig/teleport Road before Gypsy;town#10 : typeclasses.rooms.Room = north;n,south;s
#
@desc |yBefore the Gypsy.
#



#
@dig/teleport Gypsy;town#11 : typeclasses.rooms.Room = east;e,west;w
#
@desc |yThe Gypsy
#
@teleport town#10
#


#
@dig/teleport Road before the Housing office;town#12 : typeclasses.rooms.Room = north;n,south;s
#
@desc |yYou can see the housing office to the east.
#


#
@dig/teleport Housing Office;town#13 : typeclasses.rooms.Room = east;e,west;w
#
@desc |yThe housing office.
#
@teleport town#10
#


#
@dig/teleport Markar's lane;town#14 : typeclasses.rooms.Room = west;w,east;e
#
@desc |yFollowing along Markar's lane, you can see the Chaos realm to the northwest.
#



#
@dig/teleport Markar's lane;town#15 : typeclasses.rooms.Room = west;w,east;e
#
@desc |yFollowing along Markar's lane, you can see the Chaos realm to the north.
#



#
@dig/teleport Entrance to the Chaos realm;town#16 : typeclasses.rooms.Room = north;n,south;s
#
@desc |yStanding before the entrance to the realm of Chaos.
#



#
@dig/teleport Markar's lane;town#17 : typeclasses.rooms.Room = west;w,east;e
#
@desc |yMarkar's lane is the best, you can see Chaos to the northeast.
#


#
@dig/teleport Qfwfq's lane;town#18 : typeclasses.rooms.Room = south;s,north;n
#
@desc |yQfwfq's lane runs north-south through Foundation.
#


#
@dig/teleport Qfwfq's lane;town#19 : typeclasses.rooms.Room = south;s,north;n
#
@desc |yQfwfq's lane runs north-south through Foundation.
#
open east;e,west;w = town#04



#
@dig/teleport Road;town#20 : typeclasses.rooms.Room = west;w,east;e
#
@desc |yRoad to the pub.
#


#
@dig/teleport Road;town#21 : typeclasses.rooms.Room = south;s,north;n
#
@desc |yRoad along Foundation square.
#


#
@dig/teleport Road;town#22 : typeclasses.rooms.Room = south;s,north;n
#
@desc |ySouthwest corner of Foundation square.
#


@dig/teleport Western Pathway Junction;town#23 : typeclasses.rooms.Room = east;e,west;w
#
@desc |YHeading west from the Southbound Pathway, you find yourself on the Western Pathway Junction. The road here is a harmonious blend of cobblestone and sleek, metallic panels, reflecting the town's unique fusion of old and new. Enchanted lanterns line the path, casting a soft, ethereal glow that guides your way.|/|/To the north, the road leads back towards the vibrant energy of Millennium Square, where the obelisk pulses with otherworldly power.|/|/To the south, a narrow path veers off, leading towards the tranquil Enchanted Grove, where bioluminescent trees and mystical creatures await. The air is filled with a mix of floral scents and the faint hum of advanced machinery, creating a sense of both tranquility and anticipation.|/|/The Western Pathway Junction is a crossroads of adventure, offering a choice between the bustling energy of Millennium Square and the serene escape of the Enchanted Grove.
#


@dig/teleport Southbound Pathway;town#24 : typeclasses.rooms.Room = east;e,west;w
#
@desc |YAs you leave the bustling energy of Millennium Square behind, you find yourself on the Southbound Pathway. The road is a seamless blend of cobblestone and sleek, metallic panels, reflecting the town's unique fusion of old and new. Enchanted lanterns line the path, casting a soft, ethereal glow that guides your way.|/|/To your left, lush, enchanted gardens burst with vibrant flora, their colors shifting in harmony with the ever-changing sky. On your right, futuristic buildings with holographic signs advertise exotic goods and services. The air is filled with a mix of floral scents and the faint hum of advanced machinery, creating a sense of both tranquility and anticipation.
py setattr(here, "key", "Southbound Pathway")
#


#
@dig/teleport Road south of center;town#25 : typeclasses.rooms.Room = east;e,west;w
#
@desc |YAs you venture south from the western pathway junction, the cobblestone path narrows, flanked by ancient oak trees whose branches form a natural canopy overhead. The air is filled with the scent of blooming wildflowers, and the distant sound of a babbling brook adds a serene ambiance. Sunlight filters through the leaves, casting dappled shadows on the ground, creating a tranquil and inviting atmosphere.
#


#
@dig/teleport Road south of center;town#26 : typeclasses.rooms.Room = north;n,south;s
#
@desc |yYou can make out the entrance to the realm of Science to the east.
#
open north;n,south;s = town#08
#


#
@dig/teleport Southern Pathway;town#27 : typeclasses.rooms.Room = south;s,north;n
#
@desc |YAs you venture south from the western pathway junction, the cobblestone path narrows, flanked by ancient oak trees whose branches form a natural canopy overhead. The air is filled with the scent of blooming wildflowers, and the distant sound of a babbling brook adds a serene ambiance. Sunlight filters through the leaves, casting dappled shadows on the ground, creating a tranquil and inviting atmosphere.
#


#
@dig/teleport Southern Trail;town#28 : typeclasses.rooms.Room = south;s,north;n
#
@desc |YContinuing south, the pathway transitions from cobblestones to a soft dirt trail. Tall grasses sway gently in the breeze, and vibrant butterflies flit from flower to flower. The sound of rustling leaves and chirping birds creates a peaceful melody. Ahead, the trail curves slightly, hinting at new discoveries just around the bend.
#


#
@dig/teleport George's road;town#29 : typeclasses.rooms.Room = south;s,north;n
#
@desc |yAlong George's south in the southwest corner of town.
#


#
@dig/teleport Witching corner;town#30 : typeclasses.rooms.Room = west;w,east;e
#
@desc |yThis is the witching corner, where Witches like to practice.
#


#
@dig/teleport Newbie Way;town#31 : typeclasses.rooms.Room = east;e,west;w
#
@desc |yNewbieland is visible to the south.
#


#
@dig/teleport Newbie Way;town#32 : typeclasses.rooms.Room = east;e,west;w
#
@desc |yNewbieland is visible to the southwest.
#


#
@dig/teleport Newbie Way;town#33 : typeclasses.rooms.Room = east;e,west;w
#
@desc |yThe southeastern corner of town. Newbieland is visible to the southwest.
#


#
@dig/teleport Flimsy's path;town#34 : typeclasses.rooms.Room = north;n,south;s
#
@desc |yAlong Flimsy's path, running north-south on the eastern side of town.
#


#
@dig/teleport Flimsy's path;town#35 : typeclasses.rooms.Room = north;n,south;s
#
@desc |yAlong Flimsy's path, running north-south on the eastern side of town.
#


#
@dig/teleport Along Newbie Way;town#36 : typeclasses.rooms.Room = south;s,north;n
#
@desc |yNewbieland is visible to the south.
#


#
@dig/teleport Newcomer's Haven';town#37 : typeclasses.rooms.Room = south;s,north;n
#
@desc |YWelcome to the Newcomer's Haven, the perfect starting point for adventurers in Millennium. This area is a harmonious blend of sci-fi and fantasy elements, designed to ease new players into the vibrant world. The streets are lined with quaint, futuristic cottages, each equipped with basic amenities and a touch of magical charm. Holographic signposts guide you through the bustling marketplace, where vendors offer simple yet essential gear for your journey.|/|/At the heart of the Newcomer's Haven stands the Adventurer's Guild, a grand building where you can learn the basics of combat, magic, and exploration. The guild's trainers are eager to help you hone your skills and prepare for the challenges ahead. Nearby, you can find the Elementals Guild and the Changeling Guild, each offering unique paths for aspiring adventurers.|/|/In the center of the Haven, a grand fountain emits a soothing, ethereal glow, providing a peaceful spot for rest and reflection. Friendly NPCs, including wise wizards and tech-savvy engineers, are always ready to offer advice, quests, and training. The atmosphere is welcoming and safe, with low-level creatures like docile robo-pets and playful sprites roaming the area, perfect for honing your skills.|/|/Newcomer's Haven is not just a place to start your adventure; it's a community where you can meet fellow adventurers, form alliances, and prepare for the exciting challenges that await in the wider world of Millennium.
#


#
@dig/teleport The main lobby of the Elementals guild;elementals#1 : typeclasses.rooms.ElementalGuildJoinRoom = west;w,east;e
#
@desc |YAs you step into the grand hall of the Elementals Guild, you are immediately enveloped by an aura of ancient power and mystique. The room is vast, with high ceilings adorned with intricate carvings depicting the four elements: earth, air, fire, and water. The walls are lined with glowing crystals that pulse with a soft, ethereal light, casting dancing shadows across the room.|/|/At the center of the hall stands a large, circular platform made of polished stone. Surrounding the platform are four towering statues, each representing one of the elemental guardians. The statue of the earth guardian is a massive figure carved from solid rock, its eyes glowing with a deep, emerald light. The air guardian is depicted as a graceful, almost ethereal figure, seemingly made of swirling winds. The fire guardian is a fierce, imposing figure, with flames flickering around its form. The water guardian is a serene, flowing figure, with water cascading down its body.|/|/The air is filled with the faint hum of elemental energy, and you can feel the power of the elements coursing through the room. As you approach the platform, a sense of anticipation and excitement builds within you. This is the place where you will take your first steps towards mastering the elements and joining the ranks of the Elementals Guild.
#


#
@tel town#16
#
@dig/teleport The main lobby of the Changeling guild;changelings#1 : typeclasses.rooms.ChangelingGuildJoinRoom = west;w,east;e
#
@desc |YAs you step into the sleek, metallic chamber of the Changeling Guild, you are immediately struck by the futuristic design and advanced technology that surrounds you. The room is illuminated by a soft, blue glow emanating from the walls, which are embedded with intricate circuitry and holographic displays.|/|/In the center of the chamber stands a large, circular console made of a smooth, reflective material. The console is surrounded by a series of floating, transparent screens that display streams of data and complex schematics. The air is filled with a faint hum of machinery and the occasional beep of electronic devices.|/|/Around the room, you can see various stations dedicated to different aspects of the changeling's craft. One station is equipped with advanced genetic modification tools, while another is filled with holographic projectors and disguise equipment. There is even a section dedicated to virtual reality training, where members can practice their shapeshifting abilities in a simulated environment.|/|/At the far end of the chamber, a large, imposing figure stands guard. This is the guild's leader, a master changeling who has perfected the art of transformation. Their form is constantly shifting, flickering between different appearances as they observe you with keen, calculating eyes.|/|/As you approach the console, a sense of excitement and anticipation fills you. This is the place where you will learn to harness the power of transformation and join the ranks of the Changeling Guild. The possibilities are endless, and the future is yours to shape.
#

#
@tel town#26
#
@dig/teleport Along the road in Neon Nexus;town#38 : typeclasses.rooms.Room = east;e,west;w
@desc |YAs you step into the futuristic district, the skyline transforms into a dazzling array of sleek, towering structures adorned with holographic advertisements. The air is a blend of floral fragrances and the subtle hum of advanced machinery, creating an atmosphere that is both serene and charged with anticipation. Ahead, the cityscape gradually gives way to the open expanse beyond, hinting at the adventures that await outside the urban sprawl.
#

#
@tel town#38
#
@dig/teleport The edge of Neon Nexus;town#39 : typeclasses.rooms.Room = east;e,west;w
#
@desc |YAs you approach the edge of the futuristic district, the towering buildings begin to thin out, giving way to a vast, open expanse. The transition is marked by a grand archway, shimmering with holographic patterns that dance and shift in mesmerizing sequences. Beyond the archway, the landscape transforms dramatically.|/|/The ground beneath your feet changes from smooth, polished streets to a metallic pathway that hums with energy. On either side, sleek, aerodynamic vehicles zip by on elevated tracks, their lights leaving trails of neon in the air. The sky above is a canvas of swirling colors, with distant planets and stars visible through the translucent dome that shields this part of the city.|/|/As you step through the archway, you are greeted by the sight of towering spires and domes, each adorned with intricate designs and glowing with an inner light. The air is filled with the soft hum of advanced machinery and the occasional whoosh of a passing hovercraft. Exotic flora, with bioluminescent blooms, line the pathway, casting a gentle, otherworldly glow.|/|/In the distance, you can see the entrance to a bustling spaceport, where ships of all shapes and sizes are docked, ready to take off to distant worlds. The atmosphere is charged with excitement and possibility, as travelers and adventurers prepare for their next journey. The exit from the city is not just a departure; it is an invitation to explore the unknown, to venture into the vast expanse of the universe beyond.
#

@tel town#39
#
@dig/teleport The edge of the city;town#40 : typeclasses.rooms.Room = south;s,north;n
#
@desc |YAs you head south, the sleek, polished surfaces of the futuristic district give way to a grittier, more industrial landscape. Neon lights flicker above narrow alleyways, casting eerie shadows on the walls. The air is thick with the scent of ozone and the distant hum of machinery. Ahead, the skyline is dominated by towering megacorporation buildings and the occasional flash of cybernetic enhancements. The atmosphere is charged with a sense of danger and intrigue, hinting at the shadowy underworld that lies within this part of the city.
#
@tel town#40
#
@dig/teleport The Cybercorps Mega Corporation;town#41 : typeclasses.rooms.CybercorpsGuildJoinRoom = south;s,north;n
#
@desc |yAs you approach the entrance to the CyberCorps Mega Corporation, the atmosphere shifts dramatically. The building itself is a monolithic structure of steel and glass, towering above the surrounding cityscape. Its facade is adorned with sleek, reflective panels that shimmer in the ambient light, giving it an almost otherworldly appearance.|/|/The entrance is flanked by two massive, automated security gates, each emblazoned with the CyberCorps logo-a stylized, interlocking circuit pattern that pulses with a faint blue glow. As you draw closer, the gates slide open with a smooth, almost silent motion, revealing a grand foyer beyond.|/|/Inside, the foyer is a testament to the corporation's technological prowess. The floor is a seamless expanse of polished black marble, interspersed with glowing lines of circuitry that pulse rhythmically underfoot. Towering columns of glass and steel rise to the ceiling, supporting a vast, transparent dome that offers a breathtaking view of the sky above.|/|/Holographic displays hover in mid-air, projecting real-time data streams, corporate propaganda, and advertisements for the latest cybernetic enhancements. The air is filled with a subtle hum of machinery and the occasional beep of security scanners.|/|/To the left, a sleek reception desk staffed by impeccably dressed androids greets visitors, their synthetic voices offering assistance with a level of precision and politeness that only machines can achieve. To the right, a series of high-speed elevators, each with a glowing interface, stand ready to whisk employees and visitors to their destinations within the sprawling complex.|/|/The overall effect is one of awe and intimidation, a clear message that CyberCorps is a place of power and innovation, where the future is being forged one byte at a time. The entrance is not just a gateway to a building; it is a portal to a world where technology reigns supreme, and the line between human and machine is increasingly blurred.
#
@tel town#41
#
@dig/teleport The Cybercorps Mega Corporation;town#42 : typeclasses.rooms.CybercorpsWaresRoom = east;e,west;w
#
@desc |yAs you step into the CyberCorps Wares Shop, the atmosphere shifts to one of sleek sophistication and cutting-edge technology. The shop is a marvel of modern design, with walls lined with polished metal and illuminated by soft, ambient lighting that highlights the high-tech merchandise on display.|/|/The entrance is flanked by two holographic displays, welcoming you with animated advertisements showcasing the latest in cybernetic enhancements and advanced weaponry. The floor is a seamless expanse of dark, reflective material that seems to absorb sound, creating a hushed, almost reverent atmosphere.|/|/To your left, a series of glass cases house an array of cybernetic implants, each one more advanced than the last. From neural interfaces that enhance cognitive functions to biomechanical limbs that offer superhuman strength, the selection is both impressive and intimidating. Each item is accompanied by a holographic information panel, detailing its specifications and potential applications.|/|/On the right, a wall of weaponry catches your eye. Sleek plasma rifles, compact laser pistols, and formidable gauss cannons are displayed with meticulous care. The weapons are mounted on illuminated racks, each one casting a soft glow that accentuates their lethal beauty. Interactive displays allow you to examine the weapons in detail, providing information on their capabilities and customization options.|/|/In the center of the shop, a circular counter staffed by impeccably dressed androids offers personalized assistance. Their synthetic voices are calm and precise, ready to answer any questions and guide you through the purchasing process. Behind the counter, a large screen displays real-time data feeds and promotional videos, showcasing the latest innovations from CyberCorps.|/|/The back of the shop features a private consultation area, where clients can discuss their needs and receive expert advice on the best enhancements and equipment for their specific requirements. Comfortable seating and a serene ambiance make this area a welcome respite from the high-tech hustle of the main shop floor.|/|/Throughout the shop, the air is filled with a subtle hum of advanced machinery and the faint scent of ozone, a reminder of the powerful technology that surrounds you. The overall effect is one of awe and excitement, a testament to the cutting-edge advancements that CyberCorps has to offer. This is not just a shop; it is a gateway to a future where the line between human and machine is increasingly blurred.
