
# GENRES = [
#     "Action", "Adventure", "RPG", "Strategy",
#     "Shooter", "Sports", "Racing", "Simulation",
#     "Puzzle",  "Fighting",  "Horror", "Survival"
# ]
# '''
# "Open World"
# "Fantasy"
# "Crime"
# "Sci-Fi"
# "Western"
# "Dark Fantasy", "Challenging""Historical"
# "Sandbox", "Survival", "Creative"
# "Team-Based", "Multiplayer"
# '''

GAMES = [
    {
        "title": "The Elder Scrolls V: Skyrim",
        "genres": ["RPG", "Open World", "Fantasy"],
        "release_date": "2011-11-11",
        "developer": "Bethesda Game Studios",
        "publisher": "Bethesda Softworks",
        "platform": "PC, PlayStation, Xbox",
        "rating": 9.5,
        "description": "Open-world RPG set in a fantasy universe where players can explore, fight dragons, and shape their character's destiny.",
        "price": 39.99,
        "multiplayer": False,
        "no_of_downloads": 30000000
    },
    {
        "title": "Grand Theft Auto V",
        "genres": ["Action", "Open World", "Crime"],
        "release_date": "2013-09-17",
        "developer": "Rockstar North",
        "publisher": "Rockstar Games",
        "platform": "PC, PlayStation, Xbox",
        "rating": 9.7,
        "description": "Action-adventure game with a vast open world, allowing players to commit crimes and complete missions in the fictional state of San Andreas.",
        "price": 29.99,
        "multiplayer": True,
        "no_of_downloads": 145000000
    },
    {
        "title": "The Witcher 3: Wild Hunt",
        "genres": ["RPG", "Fantasy", "Open World"],
        "release_date": "2015-05-19",
        "developer": "CD Projekt Red",
        "publisher": "CD Projekt",
        "platform": "PC, PlayStation, Xbox",
        "rating": 9.8,
        "description": "Open-world RPG set in a dark fantasy universe where players control a monster hunter, Geralt of Rivia, on his quest to find his adopted daughter.",
        "price": 49.99,
        "multiplayer": False,
        "no_of_downloads": 40000000
    },
    {
        "title": "Cyberpunk 2077",
        "genres": ["RPG", "Sci-Fi", "Open World"],
        "release_date": "2020-12-10",
        "developer": "CD Projekt Red",
        "publisher": "CD Projekt",
        "platform": "PC, PlayStation, Xbox",
        "rating": 8.0,
        "description": "Futuristic RPG where players take control of V, a mercenary in the dystopian Night City, navigating through a world of cybernetics and power struggles.",
        "price": 59.99,
        "multiplayer": False,
        "no_of_downloads": 20000000
    },
    {
        "title": "Red Dead Redemption 2",
        "genres": ["Action", "Adventure", "Western", "Open World"],
        "release_date": "2018-10-26",
        "developer": "Rockstar Studios",
        "publisher": "Rockstar Games",
        "platform": "PC, PlayStation, Xbox",
        "rating": 9.6,
        "description": "Set in the American Old West, players control Arthur Morgan, an outlaw, as he navigates a rapidly changing world while maintaining loyalty to his gang.",
        "price": 59.99,
        "multiplayer": True,
        "no_of_downloads": 50000000
    },
    {
        "title": "Horizon Zero Dawn",
        "genres": ["Action", "RPG", "Open World", "Sci-Fi"],
        "release_date": "2017-02-28",
        "developer": "Guerrilla Games",
        "publisher": "Sony Interactive Entertainment",
        "platform": "PC, PlayStation",
        "rating": 9.0,
        "description": "In a post-apocalyptic world overrun by robotic creatures, players control Aloy as she hunts machines and uncovers the mysteries of the world.",
        "price": 49.99,
        "multiplayer": False,
        "no_of_downloads": 10000000
    },
    {
        "title": "Dark Souls III",
        "genres": ["Action", "RPG", "Dark Fantasy", "Challenging"],
        "release_date": "2016-04-12",
        "developer": "FromSoftware",
        "publisher": "Bandai Namco Entertainment",
        "platform": "PC, PlayStation, Xbox",
        "rating": 9.4,
        "description": "Challenging action RPG that tests players' patience and skills as they face numerous enemies in a grim, dark fantasy world.",
        "price": 59.99,
        "multiplayer": True,
        "no_of_downloads": 10000000
    },
    {
        "title": "Assassin's Creed Valhalla",
        "genres": ["Action", "RPG", "Open World", "Historical"],
        "release_date": "2020-11-10",
        "developer": "Ubisoft Montreal",
        "publisher": "Ubisoft",
        "platform": "PC, PlayStation, Xbox",
        "rating": 8.5,
        "description": "Players take on the role of Eivor, a Viking raider, and explore an open world in 9th-century England filled with quests, combat, and settlements.",
        "price": 59.99,
        "multiplayer": False,
        "no_of_downloads": 15000000
    },
    {
        "title": "Minecraft",
        "genres": ["Sandbox", "Survival", "Creative"],
        "release_date": "2011-11-18",
        "developer": "Mojang",
        "publisher": "Mojang",
        "platform": "PC, PlayStation, Xbox, Switch",
        "rating": 9.3,
        "description": "A sandbox game where players can explore procedurally generated worlds, craft items, and build structures while surviving against enemies.",
        "price": 26.95,
        "multiplayer": True,
        "no_of_downloads": 238000000
    },
    {
        "title": "Overwatch",
        "genres": ["Shooter", "Team-Based", "Multiplayer"],
        "release_date": "2016-05-24",
        "developer": "Blizzard Entertainment",
        "publisher": "Blizzard Entertainment",
        "platform": "PC, PlayStation, Xbox",
        "rating": 8.9,
        "description": "Team-based multiplayer first-person shooter where players choose heroes with unique abilities and work together to complete objectives.",
        "price": 39.99,
        "multiplayer": True,
        "no_of_downloads": 50000000
    },
    {
        "title": "Fortnite",
        "genres": ["Action", "Shooter", "Survival"],
        "release_date": "2017-07-25",
        "developer": "Epic Games",
        "publisher": "Epic Games",
        "platform": "PC, PlayStation, Xbox, Switch",
        "rating": 8.0,
        "description": "Battle Royale game where 100 players fight to be the last one standing, featuring building mechanics and a vibrant art style.",
        "price": 0.00,
        "multiplayer": True,
        "no_of_downloads": 400000000
    },
    {
        "title": "Valorant",
        "genres": ["Action", "Shooter", "Strategy"],
        "release_date": "2020-06-02",
        "developer": "Riot Games",
        "publisher": "Riot Games",
        "platform": "PC",
        "rating": 8.5,
        "description": "Tactical first-person shooter where players compete in 5v5 matches, utilizing unique agents with distinct abilities.",
        "price": 0.00,
        "multiplayer": True,
        "no_of_downloads": 35000000
    },
    {
        "title": "Animal Crossing: New Horizons",
        "genres": ["Simulation"],
        "release_date": "2020-03-20",
        "developer": "Nintendo",
        "publisher": "Nintendo",
        "platform": "Nintendo Switch",
        "rating": 9.1,
        "description": "Life simulation game where players create and manage their own island, interacting with animal villagers and customizing the environment.",
        "price": 59.99,
        "multiplayer": True,
        "no_of_downloads": 42000000
    },
    {
        "title": "God of War",
        "genres": ["Action", "Adventure"],
        "release_date": "2018-04-20",
        "developer": "Santa Monica Studio",
        "publisher": "Sony Interactive Entertainment",
        "platform": "PlayStation",
        "rating": 9.8,
        "description": "Kratos embarks on a journey with his son Atreus, battling mythological creatures in the Norse realm while struggling with his own past.",
        "price": 49.99,
        "multiplayer": False,
        "no_of_downloads": 19000000
    },
    {
        "title": "The Last of Us Part II",
        "genres": ["Action", "Adventure", "Survival"],
        "release_date": "2020-06-19",
        "developer": "Naughty Dog",
        "publisher": "Sony Interactive Entertainment",
        "platform": "PlayStation",
        "rating": 9.0,
        "description": "Set in a post-apocalyptic world, players control Ellie as she seeks revenge, confronting tough moral decisions in a brutal and emotional journey.",
        "price": 59.99,
        "multiplayer": False,
        "no_of_downloads": 10000000
    },
    {
        "title": "Sekiro: Shadows Die Twice",
        "genres": ["Action", "Adventure"],
        "release_date": "2019-03-22",
        "developer": "FromSoftware",
        "publisher": "Activision",
        "platform": "PC, PlayStation, Xbox",
        "rating": 9.2,
        "description": "Players take on the role of a shinobi in a fictionalized version of Japan, facing challenging combat against enemies and bosses in a quest for revenge.",
        "price": 59.99,
        "multiplayer": False,
        "no_of_downloads": 5000000
    }

]
GENRES = [
    {"title": "Action", "description": "Games that emphasize physical challenges and hand-eye coordination."},
    {"title": "Adventure", "description": "Games focused on exploration and puzzle-solving."},
    {"title": "RPG", "description": "Role-playing games where players control a character in a fictional world."},
    {"title": "Strategy", "description": "Games that emphasize planning and tactics."},
    {"title": "Shooter", "description": "Games that focus on ranged weapon combat."},
    {"title": "Sports", "description": "Games that simulate real-world or fantasy sports."},
    {"title": "Racing", "description": "Games that involve racing vehicles or characters."},
    {"title": "Simulation", "description": "Games that simulate real-world activities."},
    {"title": "Puzzle", "description": "Games that require problem-solving."},
    {"title": "Fighting", "description": "Games that involve hand-to-hand combat."},
    {"title": "Horror", "description": "Games that aim to scare the player."},
    {"title": "Survival",
        "description": "Games that focus on surviving in a hostile environment."},
    {"title": "Open World",
        "description": "Games set in expansive worlds that players can explore freely."},
    {"title": "Fantasy",
        "description": "Games set in imaginative, magical, or mythical settings."},
    {"title": "Crime", "description": "Games centered around criminal activities or investigations."},
    {"title": "Sci-Fi", "description": "Games set in futuristic or science-based settings."},
    {"title": "Western", "description": "Games themed around the American Old West."},
    {"title": "Dark Fantasy", "description": "Fantasy games with horror or grim elements."},
    {"title": "Challenging",
        "description": "Games known for high difficulty and skill-based gameplay."},
    {"title": "Historical",
        "description": "Games based on real historical events or settings."},
    {"title": "Sandbox",
        "description": "Games that offer open-ended gameplay with creative freedom."},
    {"title": "Creative",
        "description": "Games focused on building, designing, or imaginative tasks."},
    {"title": "Team-Based",
        "description": "Games where cooperative team play is a core mechanic."},
    {"title": "Multiplayer",
        "description": "Games that allow multiple players to play together or against each other."}
]


feedbacks = [
    "Amazing gameplay with stunning graphics. The story kept me hooked from start to finish. Definitely worth a play!",
    "The multiplayer mode is fun, but the single-player campaign feels too short. Needs more content for long-term enjoyment.",
    "I enjoyed the puzzles and challenges. However, the controls were a bit clunky at times. Overall, a solid game experience.",
    "Great concept but poorly executed. There were too many bugs, and the AI felt really unresponsive.",
    "This game has fantastic potential. The art style is unique, and the soundtrack is superb. Looking forward to future updates.",
    "Too many microtransactions ruined the experience for me. It could have been a great game, but it feels more like a cash grab.",
    "The open-world exploration was great, but the missions felt repetitive after a while. Needs more variety in objectives.",
    "An excellent RPG with deep character customization and an engaging story. I spent hours crafting my perfect hero!",
    "This game is a masterpiece. The attention to detail in the environment and character design is truly impressive.",
    "Enjoyable for a casual gamer. Easy to pick up, but doesnt have much replay value. Perfect for short bursts of fun.",
    "Loved the fast-paced action! The combat mechanics are smooth, and the variety of weapons kept things fresh throughout.",
    "The game is alright, but the loading times are unbearable. It really takes away from the immersion.",
    "Solid multiplayer experience. Had a blast playing with friends, but the solo mode needs more depth.",
    "I found the boss fights to be incredibly challenging, but that made the victories so much sweeter!",
    "The graphics are absolutely stunning, but the story lacks depth. It's visually impressive but doesn't leave a lasting impression.",
    "I couldn't put it down! The plot twists were incredible, and the character development was top-notch. Highly recommended!",
    "The game was fun, but it felt a bit too short. I was left wanting more content and better post-launch support.",
    "This game has a great atmosphere. The soundtrack and visual design create a hauntingly beautiful world.",
    "The level design is very creative, but the difficulty spikes in some areas made it frustrating to play at times.",
    "Decent enough game, but the controls take a while to get used to. Once you do, it's an enjoyable experience.",
    "The story started off strong but became predictable toward the end. Still, the characters were engaging and fun to follow.",
    "Amazing combat mechanics but lacking in story development. The gameplay is smooth, but the narrative didn't draw me in.",
    "An emotional rollercoaster! The story and characters really made me feel invested. One of the best narrative-driven games I've played.",
    "The soundtrack is absolutely phenomenal. It complements the gameplay perfectly and really adds to the overall experience.",
    "The online community is toxic, which really brings down the enjoyment of multiplayer. Needs better moderation tools.",
    "Good game with a few minor bugs. Nothing game-breaking, but they can be annoying during certain missions.",
    "It's a decent game, but nothing really stands out. Feels like it could have used more innovation in its gameplay mechanics.",
    "The variety of characters you can play as is awesome! Each one feels unique and has a distinct style.",
    "I liked the overall concept, but it felt unfinished. With more polish, this could be a top-tier game.",
    "The game had so much potential, but it was ruined by poor balancing. Some parts were just way too easy.",
    "Beautifully crafted environments with an immersive world. I just wish the story was as engaging as the setting.",
    "Not my type of game. The combat felt slow, and the narrative wasn't compelling enough to keep me playing."
]


# game_images = {
#     "Fortnite": [
#         "https://i.ytimg.com/vi/2v9ITWIotWE/maxresdefault.jpg",
#         "https://i.ytimg.com/vi/TDR5MlyOfNE/maxresdefault.jpg",
#         "https://th.bing.com/th/id/OIP.frZNGiDnBSHawYUVl6_qXgHaEK?rs=1&pid=ImgDetMain",
#         "https://preview.redd.it/htc2wntq0ty71.png?width=640&crop=smart&auto=webp&s=b0df7963d1bbd5f96df61ece63121c05988b1121",
#         "https://staticg.sportskeeda.com/editor/2022/01/89b9e-16427605313579-1920.jpg",
#         "https://cdn2.unrealengine.com/fortnite-falcon-scout-gameplay-2-1920x1080-65f8bb6b4dfd.jpg"
#     ],
#     "Overwatch": [
#         "https://i2-prod.dailystar.co.uk/incoming/article20796108.ece/ALTERNATES/s1227b/0_Overwatch-2_Blizzcon_2019_Screenshot_Push_Gameplay_03_png_jpgcopy.jpg",
#         "https://i2-prod.dailystar.co.uk/incoming/article20796102.ece/ALTERNATES/s1227b/0_Overwatch-2_Blizzcon_2019_Screenshot_Rio_Group_3P_Gameplay_03_png_jpgcopy.jpg",
#         "https://i2-prod.dailystar.co.uk/incoming/article20796113.ece/ALTERNATES/s1227b/0_Overwatch-2_Blizzcon_2019_Screenshot_Rio_Reinhardt_1P_Gameplay_01_png_jpgcopy.jpg",
#         "https://d1lss44hh2trtw.cloudfront.net/assets/article/2019/11/01/overwatch-2-announce-cinematic-zero-hour-7-40-screenshot_feature.png"
#     ],
#     "God Of War": [
#         "https://cdn.wccftech.com/wp-content/uploads/2018/03/God-of-War-gameplay.jpg",
#         "https://mp1st.com/wp-content/uploads/2022/09/god-of-war-ragnarok.jpeg",
#         "https://blog.br.playstation.com/tachyon/sites/4/2022/10/44b69a6259e928b3c0aa5839b5255c9972e8ac14-scaled.jpg",
#         "https://www.playstationlifestyle.net/wp-content/uploads/sites/9/2018/10/god-of-war.jpg?w=555"
#     ],
#     "Valorant": [
#         "https://i.ytimg.com/vi/k6YDV9Z0L9w/maxresdefault.jpg",
#         "https://i.ytimg.com/vi/Wrdh5HrOCMc/maxresdefault.jpg",
#         "https://cdn.nichesites.pikoya.com/playmmofps_com/images/games/22929/gallery/63622.jpg",
#         "https://cdn.vox-cdn.com/thumbor/bKd8ax3VdxEJmFvf5k3fEKMU9YA=/0x0:3840x2160/1200x675/filters:focal(1613x773:2227x1387)/cdn.vox-cdn.com/uploads/chorus_image/image/66414726/FirstLook_CreepCreep_VALORANT.0.jpg",
#         "https://www.thetechgame.com/images/news/article/4bb62202ff.jpg"
#     ],
#     "The Last Of Us Part 2": [
#         "https://www.numerama.com/wp-content/uploads/2023/11/lastofus-partii-remastered.jpg",
#         "https://th.bing.com/th/id/OIP.apv9_reUCArqwv3VklLpzgHaEK?rs=1&pid=ImgDetMain",
#         "https://salaodejogos.net/wp-content/uploads/2020/06/the-last-of-us-part-2-sop-sep-screen-03-ps4-en-25sep19_1569406887183.jpg",
#         "https://i.3djuegos.com/juegos/14236/the_last_of_us_2/fotos/ficha/the_last_of_us_2-4978633.jpg",
#         "https://wallpapercrafter.com/desktop2/763054-Ellie-Game-The-Last-of-Us-Naughty-Dog-Some-of-Us.jpg"
#     ],
#     "Sekiro: Shadows Die Twice": [
#         "https://images.gamersyde.com/image_stream-41893-4096_0002.jpg",
#         "https://criticalhits.com.br/wp-content/uploads/2018/08/Sekiro-shadows-die-twice-gameplay-oficial-gamescon-2018.jpg",
#         "https://theaureview.com/wp-content/uploads/2020/01/sekiropic.jpg"
#     ],
#     "Minecraft": [
#         "https://i.ytimg.com/vi/CpYXJ1j46HI/maxresdefault.jpg",
#         "https://th.bing.com/th/id/OIP.ENoIfxI-lDdmlZWen94MgAAAAA?rs=1&pid=ImgDetMain",
#         "https://external-preview.redd.it/8BrJMW2sdU1JZIP82OstTy7kBbPzyg0_OeJ5naXmK6A.png?format=pjpg&auto=webp&s=80859ff09dd6c2451b8009a3b1ecd964ba1a2ad3",
#         "https://media.playstation.com/is/image/SCEA/minecraft-screenshot-05-ps4-05dec19-en-us?$native_nt$",
#         "https://4.bp.blogspot.com/-VnQVhlX3y_4/VCVZPOGKs7I/AAAAAAAAB_8/VWCTX-kVz8I/s1600/minecraft.jpg"
#     ],
#     "Animal Crossing: New Horizons": [
#         "https://sm.ign.com/t/ign_br/screenshot/default/aaaaa_gh6c.1200.jpg",
#         "https://cdn.mos.cms.futurecdn.net/FgNNf5NwsrHfPGFZPX2RyT.jpg",
#         "https://hanoicomputercdn.com/media/lib/20-02-2023/the-game-nintendo-switch-animal-crossing-new-horizons4.jpg"
#     ],
#     "Dark Souls 3": [
#         "https://www.gamereactor.eu/media/38/darksouls3_1723893b.jpg",
#         "https://www.dsogaming.com/wp-content/uploads/2015/09/Dark-Souls-III_2015_09-16-15_002.jpg",
#         "https://images.gamewatcherstatic.com/image/file/5/46/75955/ds3-1.jpg",
#         "https://th.bing.com/th/id/OIP.ph9AjFBSvlMKlfpLeuNKmgAAAA?rs=1&pid=ImgDetMain"
#     ],
#     "Horizon Zero Dawn": [
#         "https://th.bing.com/th/id/R.48a7dab30377763fe2f9a0550ef0adb8?rik=hgvBbTWvNAagkw&riu=http%3a%2f%2fwww.capsulecomputers.com.au%2fwp-content%2fuploads%2f2016%2f09%2fHorizon-Zero-Dawn-screenshot-9.jpg&ehk=cPIhmXnd0d0zvhmII18UkgsWcwWnwlxsuRj9l76ODfM%3d&risl=&pid=ImgRaw&r=0",
#         "https://th.bing.com/th/id/R.89c7d2193202f7133595119e81f97742?rik=OIeO2G50Qa4AEw&riu=http%3a%2f%2fimages.gamersyde.com%2fimage_horizon_zero_dawn-32167-3283_0013.jpg&ehk=wughdxLr4hhVpUr4caFS6A%2fFJJlmx6VAYJCHwzaXaEw%3d&risl=&pid=ImgRaw&r=0",
#         "https://th.bing.com/th/id/R.0100feda076da64940a169008aee49e9?rik=lofDiYl%2fTjIP5A&riu=http%3a%2f%2fwww.godisageek.com%2fwp-content%2fuploads%2fhorizon-zero-dawn-e3-gameplay-anteprima.jpg&ehk=DATRkx9t9oxk8KWB3Ceqp8FGJn79avQTpxl4pvZzqY8%3d&risl=&pid=ImgRaw&r=0",
#         "https://th.bing.com/th/id/OIP.JVkNHKIjEpvF2NN6oPZgqwAAAA?rs=1&pid=ImgDetMain",
#         "https://cdn.vox-cdn.com/thumbor/QyQgxyKMB04yfzlMuQwp7W4Wta8=/8x0:1694x948/1600x900/cdn.vox-cdn.com/uploads/chorus_image/image/49847503/Screen_Shot_2016-06-13_at_6.36.06_PM.0.0.png"
#     ],
#     "Cyberpunk 2077": [
#         "https://reelzap.com/wp-content/uploads/2024/04/cyberpunk-2077-1536x864.jpeg",
#         "https://i.ytimg.com/vi/aUeVLrcsMOA/maxresdefault.jpg",
#         "https://images.pushsquare.com/screenshots/111368/large.jpg"
#     ],
#     "The Witcher 3": [
#         "https://th.bing.com/th/id/R.1eb84e40a44c4e6949b794df35d5ad47?rik=tt8c0vJBgxb84Q&riu=http%3a%2f%2fgamingbolt.com%2fwp-content%2fuploads%2f2015%2f04%2fThe-Witcher-3-3.jpg&ehk=5C66vu3CWDXpn2qkjkTACUHkkJNoXSzPCSm6rhyzVbo%3d&risl=&pid=ImgRaw&r=0",
#         "https://i.ytimg.com/vi/WWqbErjF39Y/maxresdefault.jpg",
#         "https://wallpapers-all.com/uploads/posts/2016-12/21_the_witcher_3.jpg"
#     ],
#     "GTA 5": [
#         "https://image.api.playstation.com/cdn/UP1004/CUSA00419_00/bTNSe7ok8eFVGeQByA5qSzBQoKAAY32R.png",
#         "https://images.ladbible.com/resize?type=webp&quality=70&width=3840&fit=contain&gravity=auto&url=https://images.ladbiblegroup.com/v3/assets/bltcd74acc1d0a99f3a/bltae832dcc465ec622/653a603aa24707040acc65cb/resize.webp",
#         "https://images.squarespace-cdn.com/content/v1/51b3dc8ee4b051b96ceb10de/1373393520594-MG4FG48EUDLRXQTWTNRD/first-grand-theft-auto-v-gameplay-video-released-21.jpg",
#         "https://cdn.wccftech.com/wp-content/uploads/2013/08/gta1.png"
#     ]
# }

game_images = {
    "Fortnite": [
        "https://i.ytimg.com/vi/2v9ITWIotWE/maxresdefault.jpg",
        "https://i.ytimg.com/vi/TDR5MlyOfNE/maxresdefault.jpg",
        "https://th.bing.com/th/id/OIP.frZNGiDnBSHawYUVl6_qXgHaEK?rs=1&pid=ImgDetMain",
        "https://preview.redd.it/htc2wntq0ty71.png?width=640&crop=smart&auto=webp&s=b0df7963d1bbd5f96df61ece63121c05988b1121",
        "https://staticg.sportskeeda.com/editor/2022/01/89b9e-16427605313579-1920.jpg",
        "https://cdn2.unrealengine.com/fortnite-falcon-scout-gameplay-2-1920x1080-65f8bb6b4dfd.jpg"
    ],
    "Overwatch": [
        "https://i2-prod.dailystar.co.uk/incoming/article20796108.ece/ALTERNATES/s1227b/0_Overwatch-2_Blizzcon_2019_Screenshot_Push_Gameplay_03_png_jpgcopy.jpg",
        "https://i2-prod.dailystar.co.uk/incoming/article20796102.ece/ALTERNATES/s1227b/0_Overwatch-2_Blizzcon_2019_Screenshot_Rio_Group_3P_Gameplay_03_png_jpgcopy.jpg",
        "https://i2-prod.dailystar.co.uk/incoming/article20796113.ece/ALTERNATES/s1227b/0_Overwatch-2_Blizzcon_2019_Screenshot_Rio_Reinhardt_1P_Gameplay_01_png_jpgcopy.jpg",
        "https://d1lss44hh2trtw.cloudfront.net/assets/article/2019/11/01/overwatch-2-announce-cinematic-zero-hour-7-40-screenshot_feature.png"
    ],
    "God of War": [
        "https://cdn.wccftech.com/wp-content/uploads/2018/03/God-of-War-gameplay.jpg",
        "https://mp1st.com/wp-content/uploads/2022/09/god-of-war-ragnarok.jpeg",
        "https://blog.br.playstation.com/tachyon/sites/4/2022/10/44b69a6259e928b3c0aa5839b5255c9972e8ac14-scaled.jpg",
        "https://www.playstationlifestyle.net/wp-content/uploads/sites/9/2018/10/god-of-war.jpg?w=555"
    ],
    "Valorant": [
        "https://i.ytimg.com/vi/k6YDV9Z0L9w/maxresdefault.jpg",
        "https://i.ytimg.com/vi/Wrdh5HrOCMc/maxresdefault.jpg",
        "https://cdn.nichesites.pikoya.com/playmmofps_com/images/games/22929/gallery/63622.jpg",
        "https://cdn.vox-cdn.com/thumbor/bKd8ax3VdxEJmFvf5k3fEKMU9YA=/0x0:3840x2160/1200x675/filters:focal(1613x773:2227x1387)/cdn.vox-cdn.com/uploads/chorus_image/image/66414726/FirstLook_CreepCreep_VALORANT.0.jpg",
        "https://www.thetechgame.com/images/news/article/4bb62202ff.jpg"
    ],
    "The Last of Us Part II": [
        "https://www.numerama.com/wp-content/uploads/2023/11/lastofus-partii-remastered.jpg",
        "https://th.bing.com/th/id/OIP.apv9_reUCArqwv3VklLpzgHaEK?rs=1&pid=ImgDetMain",
        "https://salaodejogos.net/wp-content/uploads/2020/06/the-last-of-us-part-2-sop-sep-screen-03-ps4-en-25sep19_1569406887183.jpg",
        "https://i.3djuegos.com/juegos/14236/the_last_of_us_2/fotos/ficha/the_last_of_us_2-4978633.jpg",
        "https://wallpapercrafter.com/desktop2/763054-Ellie-Game-The-Last-of-Us-Naughty-Dog-Some-of-Us.jpg"
    ],
    "Sekiro: Shadows Die Twice": [
        "https://images.gamersyde.com/image_stream-41893-4096_0002.jpg",
        "https://criticalhits.com.br/wp-content/uploads/2018/08/Sekiro-shadows-die-twice-gameplay-oficial-gamescon-2018.jpg",
        "https://theaureview.com/wp-content/uploads/2020/01/sekiropic.jpg"
    ],
    "Minecraft": [
        "https://i.ytimg.com/vi/CpYXJ1j46HI/maxresdefault.jpg",
        "https://th.bing.com/th/id/OIP.ENoIfxI-lDdmlZWen94MgAAAAA?rs=1&pid=ImgDetMain",
        "https://external-preview.redd.it/8BrJMW2sdU1JZIP82OstTy7kBbPzyg0_OeJ5naXmK6A.png?format=pjpg&auto=webp&s=80859ff09dd6c2451b8009a3b1ecd964ba1a2ad3",
        "https://media.playstation.com/is/image/SCEA/minecraft-screenshot-05-ps4-05dec19-en-us?$native_nt$",
        "https://4.bp.blogspot.com/-VnQVhlX3y_4/VCVZPOGKs7I/AAAAAAAAB_8/VWCTX-kVz8I/s1600/minecraft.jpg"
    ],
    "Animal Crossing: New Horizons": [
        "https://sm.ign.com/t/ign_br/screenshot/default/aaaaa_gh6c.1200.jpg",
        "https://cdn.mos.cms.futurecdn.net/FgNNf5NwsrHfPGFZPX2RyT.jpg",
        "https://hanoicomputercdn.com/media/lib/20-02-2023/the-game-nintendo-switch-animal-crossing-new-horizons4.jpg"
    ],
    "Dark Souls III": [
        "https://www.gamereactor.eu/media/38/darksouls3_1723893b.jpg",
        "https://www.dsogaming.com/wp-content/uploads/2015/09/Dark-Souls-III_2015_09-16-15_002.jpg",
        "https://images.gamewatcherstatic.com/image/file/5/46/75955/ds3-1.jpg",
        "https://th.bing.com/th/id/OIP.ph9AjFBSvlMKlfpLeuNKmgAAAA?rs=1&pid=ImgDetMain"
    ],
    "Horizon Zero Dawn": [
        "https://th.bing.com/th/id/R.48a7dab30377763fe2f9a0550ef0adb8?rik=hgvBbTWvNAagkw&riu=http%3a%2f%2fwww.capsulecomputers.com.au%2fwp-content%2fuploads%2f2016%2f09%2fHorizon-Zero-Dawn-screenshot-9.jpg&ehk=cPIhmXnd0d0zvhmII18UkgsWcwWnwlxsuRj9l76ODfM%3d&risl=&pid=ImgRaw&r=0",
        "https://th.bing.com/th/id/R.89c7d2193202f7133595119e81f97742?rik=OIeO2G50Qa4AEw&riu=http%3a%2f%2fimages.gamersyde.com%2fimage_horizon_zero_dawn-32167-3283_0013.jpg&ehk=wughdxLr4hhVpUr4caFS6A%2fFJJlmx6VAYJCHwzaXaEw%3d&risl=&pid=ImgRaw&r=0",
        "https://th.bing.com/th/id/R.0100feda076da64940a169008aee49e9?rik=lofDiYl%2fTjIP5A&riu=http%3a%2f%2fwww.godisageek.com%2fwp-content%2fuploads%2fhorizon-zero-dawn-e3-gameplay-anteprima.jpg&ehk=DATRkx9t9oxk8KWB3Ceqp8FGJn79avQTpxl4pvZzqY8%3d&risl=&pid=ImgRaw&r=0",
        "https://th.bing.com/th/id/OIP.JVkNHKIjEpvF2NN6oPZgqwAAAA?rs=1&pid=ImgDetMain",
        "https://cdn.vox-cdn.com/thumbor/QyQgxyKMB04yfzlMuQwp7W4Wta8=/8x0:1694x948/1600x900/cdn.vox-cdn.com/uploads/chorus_image/image/49847503/Screen_Shot_2016-06-13_at_6.36.06_PM.0.0.png"
    ],
    "Cyberpunk 2077": [
        "https://reelzap.com/wp-content/uploads/2024/04/cyberpunk-2077-1536x864.jpeg",
        "https://i.ytimg.com/vi/aUeVLrcsMOA/maxresdefault.jpg",
        "https://images.pushsquare.com/screenshots/111368/large.jpg"
    ],
    "The Witcher 3: Wild Hunt": [
        "https://th.bing.com/th/id/R.1eb84e40a44c4e6949b794df35d5ad47?rik=tt8c0vJBgxb84Q&riu=http%3a%2f%2fgamingbolt.com%2fwp-content%2fuploads%2f2015%2f04%2fThe-Witcher-3-3.jpg&ehk=5C66vu3CWDXpn2qkjkTACUHkkJNoXSzPCSm6rhyzVbo%3d&risl=&pid=ImgRaw&r=0",
        "https://i.ytimg.com/vi/WWqbErjF39Y/maxresdefault.jpg",
        "https://wallpapers-all.com/uploads/posts/2016-12/21_the_witcher_3.jpg"
    ],
    "Grand Theft Auto V": [
        "https://image.api.playstation.com/cdn/UP1004/CUSA00419_00/bTNSe7ok8eFVGeQByA5qSzBQoKAAY32R.png",
        "https://images.ladbible.com/resize?type=webp&quality=70&width=3840&fit=contain&gravity=auto&url=https://images.ladbiblegroup.com/v3/assets/bltcd74acc1d0a99f3a/bltae832dcc465ec622/653a603aa24707040acc65cb/resize.webp",
        "https://images.squarespace-cdn.com/content/v1/51b3dc8ee4b051b96ceb10de/1373393520594-MG4FG48EUDLRXQTWTNRD/first-grand-theft-auto-v-gameplay-video-released-21.jpg",
        "https://cdn.wccftech.com/wp-content/uploads/2013/08/gta1.png"
    ]
}
