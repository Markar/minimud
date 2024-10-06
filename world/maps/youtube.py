"""
An early dungeon.
"""

from evennia.contrib.grid.xyzgrid import xymap_legend

MAP = r"""
                       1
 + 0 1 2 3 4 5 6 7 8 9 0
 
 4   M-#-#-M-#-#-#-M
     | |   | | |   |
 3   #-M   M-#-M   #
     | |       |   |
 2   #-M-#-M   #-#-#
     | |   |   |   |
 1   #-M   M-#-M   #
     |     | |     |
 0   M-#-#-#-#-#-#-M
      
 + 0 1 2 3 4 5 6 7 8 9 0
                       1
"""


PROTOTYPES = {
    (1, 0): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "PewDiePie",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "PewDiePie's Throne",
        "desc": "|YIn this grand square, a throne made of gaming consoles and meme artifacts stands tall. PewDiePie, the king of YouTube, sits upon it, his signature brofist emblem glowing behind him. The room is filled with references to his iconic videos, from barrels to tambourines, creating an atmosphere of chaotic creativity.",
    },
    (2, 0): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Influencer Alley",
        "desc": "|YThis bustling alleyway is lined with neon signs, trendy cafes, and social media booths. Influencers of all kinds gather here, sharing stories, taking selfies, and collaborating on projects. The room is a vibrant and energetic space, reflecting the diverse and dynamic world of online content creation.",
    },
    (3, 0): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Influencer Lounge",
        "desc": "|YA luxurious lounge filled with plush couches, sparkling chandeliers, and exclusive VIP areas. Influencers relax and socialize here, sipping cocktails and discussing the latest trends. The room is a glamorous and sophisticated space, perfect for networking and unwinding after a long day of content creation.",
    },
    (4, 0): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Influencer Studio",
        "desc": "|YA state-of-the-art studio equipped with cameras, lights, and green screens. Influencers film videos, record podcasts, and stream live content here, showcasing their talents to the world. The room is a creative and dynamic space, inspiring guests to create and share their own unique content.",
    },
    (5, 0): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Influencer Gallery",
        "desc": "|YA modern art gallery filled with digital displays, interactive installations, and multimedia exhibits. Influencers showcase their work here, from paintings and sculptures to virtual reality experiences. The room is a vibrant and eclectic space, celebrating the creativity and innovation of online content creators.",
    },
    (6, 0): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Influencer Theater",
        "desc": "|YA high-tech theater with a giant screen, surround sound, and stadium seating. Influencers host screenings, premieres, and live events here, entertaining audiences with their latest projects. The room is an immersive and engaging space, inviting guests to experience the magic of online entertainment.",
    },
    (7, 0): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Influencer Arcade",
        "desc": "|YA retro arcade filled with classic games, neon lights, and nostalgic memorabilia. Influencers gather here to play, compete, and relive their favorite childhood memories. The room is a fun and lively space, perfect for gaming enthusiasts and fans of vintage entertainment.",
    },
    (8, 0): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "Markiplier",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Markiplier Maze",
        "desc": "|YThis room is a labyrinth of dark corridors and eerie red lighting, echoing the horror games that Markiplier is known for. At the center, Markiplier himself stands, ready to guide or challenge those who enter. His deep voice resonates through the maze, adding to the suspenseful atmosphere.",
    },
    # second row
    (1, 1): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Creator Corner",
        "desc": "|YA cozy corner filled with bean bags, fairy lights, and inspirational quotes. Creators gather here to brainstorm ideas, collaborate on projects, and share their passions. The room is a warm and inviting space, fostering creativity and community among like-minded individuals.",
    },
    (2, 1): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "MrBeast",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "MrBeast's Vault",
        "desc": "|YThis room resembles a massive vault filled with gold, cash, and extravagant prizes. MrBeast stands at the entrance, offering challenges and rewards to those brave enough to participate. The room is a testament to his philanthropic and adventurous spirit, with hidden surprises at every turn.",
    },
    (4, 1): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Content Creator Cafe",
        "desc": "|YA cozy cafe filled with the aroma of freshly brewed coffee, baked goods, and creative energy. Content creators gather here to work, socialize, and recharge between projects. The room is a welcoming and relaxed space, perfect for brainstorming ideas and connecting with fellow creators.",
    },
    (5, 1): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "Ninja",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "The Ninja Arena",
        "desc": "|YA high-tech arena filled with neon lights and advanced gaming setups. Ninja, the master of Fortnite, stands ready for battle, his blue hair glowing under the lights. The room is designed like a futuristic battleground, with holographic targets and virtual enemies to defeat.",
    },
    (6, 1): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "MatPat",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "MatPat's Library",
        "desc": "|YThis room is a vast library filled with books, screens, and game theories. MatPat, the mastermind behind Game Theory, is here, surrounded by clues and puzzles. The room challenges visitors to solve intricate mysteries and uncover hidden truths, reflecting MatPat's analytical and inquisitive nature.",
    },
    (8, 1): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Tech Guru's Workshop",
        "desc": "|YA high-tech workshop filled with gadgets, tools, and cutting-edge technology. Tech gurus tinker, experiment, and innovate here, pushing the boundaries of what's possible. The room is a dynamic and creative space, inspiring visitors to explore new technologies and embrace the future of digital innovation.",
    },
    # third row
    (1, 2): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Political Pundit Plaza",
        "desc": "|YA bustling plaza filled with newsstands, debate stages, and political posters. Political pundits gather here to discuss current events, share opinions, and engage with the community. The room is a lively and dynamic space, encouraging visitors to participate in debates and explore different perspectives.",
    },
    (2, 2): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "BadEmpanada",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "BadEmpanada's Hideout",
        "desc": "|YA dimly lit, underground lair filled with high-tech gadgets, hacking tools, and encrypted servers. BadEmpanada, the notorious cyber vigilante, operates from here, planning digital heists and exposing corruption. The room exudes an aura of secrecy and rebellion, inspiring visitors to question authority and embrace the shadows.",
    },
    (3, 2): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Gamer's Paradise",
        "desc": "|YA vibrant gaming lounge filled with consoles, PCs, and gaming memorabilia. Gamers gather here to play, compete, and connect with fellow enthusiasts. The room is a lively and social space, fostering a sense of camaraderie and shared passion for video games.",
    },
    (4, 2): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "JackSepticEye",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "JackSepticEye's Funhouse",
        "desc": "|YAn interactive funhouse filled with colorful lights, carnival games, and energetic music. JackSepticEye, the energetic Irish YouTuber, welcomes visitors with his signature green hair and infectious laughter. The room is a playful and chaotic space, inviting guests to let loose and have fun.",
    },
    (6, 2): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Streamer's Studio",
        "desc": "|YA state-of-the-art studio equipped with cameras, lights, and green screens. Streamers broadcast live content, interact with viewers, and showcase their talents here. The room is a dynamic and engaging space, designed to inspire creativity and connect streamers with their audience.",
    },
    (7, 2): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Vlogger's Lounge",
        "desc": "|YA cozy lounge filled with plush couches, soft lighting, and vlogging equipment. Vloggers relax and film videos here, sharing their thoughts, experiences, and daily adventures. The room is a warm and intimate space, perfect for storytelling and connecting with viewers on a personal level.",
    },
    (8, 2): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Musician's Stage",
        "desc": "|YA vibrant stage with colorful lights, professional sound equipment, and musical instruments. Musicians perform live concerts, record music videos, and collaborate with other artists here. The room is a creative and inspiring space, celebrating the power of music to entertain, inspire, and unite people.",
    },
    # fourth row
    (1, 3): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Artist's Gallery",
        "desc": "|YA bright and spacious gallery filled with paintings, sculptures, and digital art. Artists showcase their work here, from traditional masterpieces to cutting-edge installations. The room is a colorful and eclectic space, celebrating the diversity and creativity of the art world.",
    },
    (2, 3): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "Dream",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Dream's Challenge",
        "desc": "|YA challenging obstacle course filled with traps, puzzles, and parkour challenges. Dream, the Minecraft speedrunner, watches from above, ready to offer hints or obstacles. The room is a test of skill and strategy, designed to push visitors to their limits and beyond.",
    },
    (4, 3): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Educator's Classroom",
        "desc": "|YA traditional classroom filled with desks, whiteboards, and educational resources. Educators teach lessons, host workshops, and engage with students here, sharing knowledge and inspiring learning. The room is a welcoming and supportive space, designed to empower visitors to explore new ideas and expand their horizons.",
    },
    (5, 3): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Chef's Kitchen",
        "desc": "|YA spacious kitchen filled with cooking utensils, fresh ingredients, and mouth-watering aromas. Chefs prepare delicious meals, share recipes, and host cooking classes here, showcasing their culinary skills and creativity. The room is a warm and inviting space, perfect for food enthusiasts and aspiring chefs.",
    },
    (6, 3): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "Wendigoon",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Wendigoon's Crptid Lair",
        "desc": "|YA dark and mysterious cave filled with eerie whispers and shadowy figures. Wendigoon, the horror narrator, lurks in the shadows, ready to tell chilling tales and test visitors' courage. The room is a haunting and atmospheric space, perfect for those who seek thrills and scares.",
    },
    (8, 3): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Animator's Studio",
        "desc": "|YA cozy studio filled with drawing tablets, animation software, and creative inspiration. Animators work here, bringing characters and stories to life through the magic of animation. The room is a peaceful and imaginative space, perfect for exploring new ideas and expressing creativity through art.",
    },
    (1, 4): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "MeiMei",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Boba Bar",
        "desc": "|YFeed me Mei Mei's boba bar, where the boba influencer is here, pounding bubble tea. Ready to chat, she's surrounded by a rainbow of flavors and toppings, and the room is filled with the sweet aroma of freshly brewed tea.",
    },
    (2, 4): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Traveler's Lounge",
        "desc": "|YA cozy lounge filled with travel guides, maps, and souvenirs from around the world. Travelers share stories, plan adventures, and connect with fellow explorers here, inspiring wanderlust and cultural exchange. The room is a warm and welcoming space, perfect for those who seek new experiences and global connections.",
    },
    (3, 4): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Photographer's Studio",
        "desc": "|YA professional studio with high-quality cameras, lighting equipment, and backdrops. Photographers capture stunning images, host photo shoots, and showcase their portfolios here, highlighting the beauty and artistry of photography. The room is a creative and inspiring space, inviting visitors to explore the world through a lens.",
    },
    (4, 4): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "LoganPaul",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Fitness Guru's Gym",
        "desc": "|YA state-of-the-art gym filled with exercise equipment, motivational quotes, and energetic music. Fitness gurus lead workouts, share tips, and inspire visitors to live a healthy lifestyle. The room is a dynamic and empowering space, designed to motivate and support individuals on their fitness journey.",
    },
    (5, 4): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Meditation Garden",
        "desc": "|YA peaceful garden filled with lush greenery, tranquil ponds, and soothing music. Visitors come here to relax, meditate, and find inner peace amidst the chaos of daily life. The room is a serene and harmonious space, inviting guests to connect with nature and nurture their mind, body, and spirit.",
    },
    (6, 4): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Tech Support Center",
        "desc": "|YA bustling center filled with computers, gadgets, and tech experts. Visitors come here for advice, repairs, and troubleshooting tips, solving technical problems and learning new skills. The room is a helpful and informative space, designed to empower individuals to navigate the digital world with confidence.",
    },
    (7, 4): {
        "prototype_parent": "xyz_room",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Pet Lover's Park",
        "desc": "|YA vibrant park filled with playful animals, pet owners, and pet care resources. Pet lovers gather here to socialize, play, and learn about responsible pet ownership. The room is a joyful and interactive space, celebrating the bond between humans and animals and promoting animal welfare and happiness.",
    },
    (8, 4): {
        "prototype_parent": "xyz_room",
        "spawn_proto": "Caseoh",
        "typeclass": "typeclasses.rooms.MobRoom",
        "tags": [("youtube", "zone")],
        "key": "Caseoh's Meme Zone",
        "desc": "|YA cozy den filled with plush pillows, warm blankets, and soothing candles. Caseoh, the meme master, shares viral videos, funny memes, and internet humor here, spreading joy and laughter to all who enter. The room is a lighthearted and entertaining space, perfect for relaxing and enjoying the lighter side of the internet.",
    },
}


class MobNode(xymap_legend.MapNode):
    prototype = {
        "prototype_parent": "xyz_room",
        "key": "Inside",
        "desc": "A mob in Mobland.",
    }


LEGEND = {
    "M": MobNode,
}

XYMAP_DATA = {
    "zcoord": "youtube",
    "map": MAP,
    "prototypes": PROTOTYPES,
    "legend": LEGEND,
}
