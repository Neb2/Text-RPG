import sys
from data.art import cut_scene_art

sys.setrecursionlimit(10**6)  # test


# game map
class Map:
    ZONE_NAME = ''
    EXAMINE = 'info'
    DESCRIPTION = 'description'
    UP = 'north'
    DOWN = 'south'
    LEFT = 'west'
    RIGHT = 'east'

    zone_map = {
        'b6': {
            ZONE_NAME: "forest",
            EXAMINE: "Nothing here but trees...",
            DESCRIPTION: "Hyfield Forest - b6",
            UP: "",
            DOWN: "",
            LEFT: "",
            RIGHT: "c6"
        },
        'c2': {
            ZONE_NAME: "town",
            EXAMINE: "Here you can buy and sell various items.",
            DESCRIPTION: "Welcome to the general store.",
            UP: "",
            DOWN: "",
            LEFT: "",
            RIGHT: "d2"
        },
        'c5': {
            ZONE_NAME: "forest",
            EXAMINE: "Nothing here but trees...",
            DESCRIPTION: "Hyfield Forest - c5",
            UP: "",
            DOWN: "c6",
            LEFT: "",
            RIGHT: "d5"
        },
        'c6': {
            ZONE_NAME: "forest",
            EXAMINE: "Nothing here but trees...",
            DESCRIPTION: "Hyfield Forest - c6",
            UP: "c5",
            DOWN: "c7",
            LEFT: "b6",
            RIGHT: "d6"
        },
        'c7': {
            ZONE_NAME: "forest",
            EXAMINE: "Nothing here but trees...",
            DESCRIPTION: "Hyfield Forest - c7",
            UP: "c6",
            DOWN: "",
            LEFT: "",
            RIGHT: "d7"
        },
        'd1': {
            ZONE_NAME: "town",
            EXAMINE: "Maybe you should leave home, there isn't much to do here...",
            DESCRIPTION: "This is your home, home sweet home.",
            UP: "",
            DOWN: "d2",
            LEFT: "",
            RIGHT: ""
        },
        'd2': {
            ZONE_NAME: "town",
            EXAMINE: "Hyfield Market, famous for its Hats!",
            DESCRIPTION: "The streets of Hyfield Village.",
            UP: "d1",
            DOWN: "d3",
            LEFT: "c2",
            RIGHT: "e2"
        },
        'd3': {
            ZONE_NAME: "town",
            EXAMINE: "The forrest ahead looks daunting.",
            DESCRIPTION: "The way out from Hyfield Village.",
            UP: "d2",
            DOWN: "d4",
            LEFT: "",
            RIGHT: ""
        },
        'd4': {
            ZONE_NAME: "forest",
            EXAMINE: "You should be prepared for the dangers that await in the Hyfield Forest.",
            DESCRIPTION: "Hyfield Forest - d4",
            UP: "d3",
            DOWN: "d5",
            LEFT: "",
            RIGHT: ""
        },
        'd5': {
            ZONE_NAME: "forest",
            EXAMINE: "Nothing here but trees...",
            DESCRIPTION: "Hyfield Forest - d5",
            UP: "d4",
            DOWN: "d6",
            LEFT: "c5",
            RIGHT: "e5"
        },
        'd6': {
            ZONE_NAME: "forest",
            EXAMINE: "Nothing here but trees...",
            DESCRIPTION: "Hyfield Forest - d6",
            UP: "d5",
            DOWN: "d7",
            LEFT: "c6",
            RIGHT: "e6"

        },
        'd7': {
            ZONE_NAME: "forest",
            EXAMINE: "Nothing here but trees...",
            DESCRIPTION: "Hyfield Forest - d7",
            UP: "d6",
            DOWN: "d8",
            LEFT: "c7",
            RIGHT: "e7"

        },
        'd8': {
            ZONE_NAME: "forest",
            EXAMINE: "Nothing here but trees...",
            DESCRIPTION: "Hyfield Forest - d8",
            UP: "d7",
            DOWN: "",
            LEFT: "",
            RIGHT: ""
        },
        'e2': {
            ZONE_NAME: "town",
            EXAMINE: "The Town Hall is full of adventurers like you.",
            DESCRIPTION: "Hyfield Town Hall - e2",
            UP: "",
            DOWN: "",
            LEFT: "d2",
            RIGHT: ""
        },
        'e5': {
            ZONE_NAME: "forest",
            EXAMINE: "Nothing here but trees...",
            DESCRIPTION: "Hyfield Forest - e5",
            UP: "",
            DOWN: "e6",
            LEFT: "d5",
            RIGHT: "f5"
        },
        'e6': {
            ZONE_NAME: "forest",
            EXAMINE: "Nothing here but trees...",
            DESCRIPTION: "Hyfield Forest - e6",
            UP: "e5",
            DOWN: "e7",
            LEFT: "d6",
            RIGHT: "f6"
        },
        'e7': {
            ZONE_NAME: "forest",
            EXAMINE: "Nothing here but trees..",
            DESCRIPTION: "Hyfield Forest - e7",
            UP: "e6",
            DOWN: "",
            LEFT: "d7",
            RIGHT: ""
        },
        'f5': {
            ZONE_NAME: "forest",
            EXAMINE: "Nothing here but trees..",
            DESCRIPTION: "Hyfield Forest - f5",
            UP: "",
            DOWN: "f6",
            LEFT: "e5",
            RIGHT: ""
        },
        'f6': {
            ZONE_NAME: "forest",
            EXAMINE: "The edge of the forest.",
            DESCRIPTION: "Hyfield Forest - f6",
            UP: "f5",
            DOWN: "",
            LEFT: "e6",
            RIGHT: "g6"
        },
        'g6': {
            ZONE_NAME: "water",
            EXAMINE: "The cold waters of Stonemis River.",
            DESCRIPTION: "Stonemis River - g6",
            UP: "",
            DOWN: "",
            LEFT: "f6",
            RIGHT: "h6"
        },
        'h6': {
            ZONE_NAME: "water",
            EXAMINE: "The cold waters of Stonemis River.",
            DESCRIPTION: "Stonemis River - n6",
            UP: "",
            DOWN: "",
            LEFT: "g6",
            RIGHT: "i6"
        },
        'i6': {
            ZONE_NAME: "water",
            EXAMINE: "The cold waters of Stonemis River.",
            DESCRIPTION: "Stonemis River - i6",
            UP: "",
            DOWN: "",
            LEFT: "h6",
            RIGHT: "j6"
        },
        'j6': {
            ZONE_NAME: "water",
            EXAMINE: "The warmer waters of Stonemis River.",
            DESCRIPTION: "Stonemis River - j6",
            UP: "",
            DOWN: "",
            LEFT: "i6",
            RIGHT: "k6"
        },
        'k5': {
            ZONE_NAME: "desert",
            EXAMINE: "Nothing but sand here...",
            DESCRIPTION: "The Virwaki Desert - k5",
            UP: "",
            DOWN: "k6",
            LEFT: "",
            RIGHT: "l5"
        },
        'k6': {
            ZONE_NAME: "desert",
            EXAMINE: "Nothing but sand here...",
            DESCRIPTION: "The Virwaki Desert - k6",
            UP: "k5",
            DOWN: "k7",
            LEFT: "j6",
            RIGHT: "l6"
        },
        'k7': {
            ZONE_NAME: "desert",
            EXAMINE: "Nothing but sand here...",
            DESCRIPTION: "The Virwaki Desert - k7",
            UP: "k6",
            DOWN: "",
            LEFT: "",
            RIGHT: ""
        },
        'l5': {
            ZONE_NAME: "desert",
            EXAMINE: "Nothing but sand here...",
            DESCRIPTION: "The Virwaki Desert - l5",
            UP: "",
            DOWN: "l6",
            LEFT: "k5",
            RIGHT: ""
        },
        'l6': {
            ZONE_NAME: "desert",
            EXAMINE: "Nothing but sand here...",
            DESCRIPTION: "The Virwaki Desert - l6",
            UP: "l5",
            DOWN: "",
            LEFT: "k6",
            RIGHT: "m6"
        },
        'm6': {
            ZONE_NAME: "desert",
            EXAMINE: "Nothing but sand here...",
            DESCRIPTION: "The Virwaki Desert - m6",
            UP: "",
            DOWN: "m7",
            LEFT: "l6",
            RIGHT: "n6"
        },
        'm7': {
            ZONE_NAME: "desert",
            EXAMINE: "Nothing but sand here..",
            DESCRIPTION: "The Virwaki Desert - m7",
            UP: "m6",
            DOWN: "",
            LEFT: "",
            RIGHT: "n7"
        },
        'n6': {
            ZONE_NAME: "desert",
            EXAMINE: "You don't find anything else of use in here.",
            DESCRIPTION: "The Virwaki Desert - n6",
            UP: "",
            DOWN: "n7",
            LEFT: "m6",
            RIGHT: ""
        },
        'n7': {
            ZONE_NAME: "desert",
            EXAMINE: "Up ahead is the entrance to the Virwaki Dungeon.",
            DESCRIPTION: "The Virwaki Desert - n7\n",
            UP: "n6",
            DOWN: "",
            LEFT: "m7",
            RIGHT: "o7"
        },
        'o7': {
            ZONE_NAME: "dungeon",
            EXAMINE: "No turning back now.",
            DESCRIPTION: "Virwaki Dungeon - o7",
            UP: "",
            DOWN: "o8",
            LEFT: "n7",
            RIGHT: ""
        },
        'o8': {
            ZONE_NAME: "dungeon",
            EXAMINE: "Sure is dark in here...",
            DESCRIPTION: "Virwaki Dungeon - o8",
            UP: "o7",
            DOWN: "o9",
            LEFT: "",
            RIGHT: ""
        },
        'o9': {
            ZONE_NAME: "dungeon",
            EXAMINE: "Sure is dark in here...",
            DESCRIPTION: "Virwaki Dungeon - o9",
            UP: "o8",
            DOWN: "o10",
            LEFT: "",
            RIGHT: ""
        },
        'o10': {
            ZONE_NAME: "dungeon",
            EXAMINE: "Sure is dark in here...",
            DESCRIPTION: "Virwaki Dungeon - o10",
            UP: "o9",
            DOWN: "",
            LEFT: "",
            RIGHT: "p10"
        },
        'p10': {
            ZONE_NAME: "dungeon",
            EXAMINE: "You sense you are getting closer to the end of the Dungeon now.",
            DESCRIPTION: "Virwaki Dungeon - p10",
            UP: "",
            DOWN: "",
            LEFT: "o10",
            RIGHT: "q10"
        },
        'q10': {
            ZONE_NAME: "dungeon",
            EXAMINE: "From here you can see the Baron of Hell.",
            DESCRIPTION: "Virwaki Dungeon - q10",
            UP: "",
            DOWN: "",
            LEFT: "p10",
            RIGHT: "r10"
        },
        'r10': {
            ZONE_NAME: "dungeon",
            EXAMINE: "Hope you are prepared...",
            DESCRIPTION: "The Baron of Hell Pit - r10",
            UP: "",
            DOWN: "",
            LEFT: "q10",
            RIGHT: ""
        },
    }


# allows the player to move direction
def move(character, en1):
    print("Where do you want to move to?\n")
    print("Options = (W, A, S, D)")
    direction = input("> ")
    if direction in ['W', "w"]:
        destination = Map.zone_map[character.location][Map.UP]
        if destination == "":
            print("You can't go that way.")
            move(character, en1)
        else:
            movement_handler(destination, character, en1)
    elif direction in ['A', "a"]:
        destination = Map.zone_map[character.location][Map.LEFT]
        if destination == "":
            print("You can't go that way.")
            move(character, en1)
        else:
            movement_handler(destination, character, en1)
    elif direction in ['D', "d"]:
        destination = Map.zone_map[character.location][Map.RIGHT]
        if destination == "":
            print("You can't go that way.")
            move(character, en1)
        else:
            movement_handler(destination, character, en1)
    elif direction in ['S', "s"]:
        destination = Map.zone_map[character.location][Map.DOWN]
        if destination == "":
            print("You can't go that way.")
            move(character, en1)
        else:
            movement_handler(destination, character, en1)


# handles player movement
def movement_handler(destination, character, en1):
    character.location = destination
    print("\n" "You have gone to " + character.location + ".\n")
    if Map.zone_map[character.location][Map.ZONE_NAME] in "town":
        print(cut_scene_art.village)
    elif Map.zone_map[character.location][Map.ZONE_NAME] in "forest":
        print(cut_scene_art.forest)
    elif Map.zone_map[character.location][Map.ZONE_NAME] in "water":
        print(cut_scene_art.water)
    elif Map.zone_map[character.location][Map.ZONE_NAME] in "desert":
        print(cut_scene_art.desert)
    elif Map.zone_map[character.location][Map.ZONE_NAME] in "dungeon":
        print(cut_scene_art.dungeon)
    print_location(character, en1)


# description of player location & events
def print_location(character, en1):
    from data.menu import game_menu
    print(Map.zone_map[character.location][Map.DESCRIPTION])
    if character.location == 'f6':
        if character.f6_event_1:
            input(">...")
            print("You finally see a way out of the forest, on the edge of the forest is a river.")
            character.f6_event_1 = False
    elif character.location == 'g6':
        if character.g6_event_1:
            input(">...")
            print("You look around but there's no bridge in sight, it seems the only way to cross the river is to swim.\n"
                  "Good thing you took all of those swimming classes.")
            character.g6_event_1 = False
    elif character.location == 'j6':
        if character.j6_event_1:
            input(">...")
            print("You're almost onto the other side of the river now, you can see the sand in the distance.")
            character.j6_event_1 = False
    elif character.location == "k6":
        if character.k6_event_1:
            input(">...")
            print("At last, dry land.")
            character.k6_event_1 = False
    elif character.location == "n6":
        if character.n6_event_1:
            input(">...")
            print("There's a small cabin up ahead, maybe you should take a look inside.")
            character.n6_event_1 = False
    elif character.location == "n7":
        if character.n7_event_1:
            input(">...")
            print("In the distance you see a small opening in the ground, that must be the entrance to Virwaki Dungeon.")
            character.n7_event_1 = False
    elif character.location == "o7":
        if character.n7_event_1:
            input(">...")
            print("You descend down the stairs into Virwaki Dungeon, which is dark, smelly, and has a lot of unnerving\n"
                  "sounds coming from the depths of the Dungeon.")
            character.n7_event_1 = False
    input(">...")
    game_menu(character, en1)
