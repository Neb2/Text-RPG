import os
from data.art import Colours
from data.game_map import print_location


def teleport(character, en1):
    from data.menu import game_menu
    os.system("cls")
    if Colours.BOLD + Colours.ORANGE + "[Teleportation Stone]" + Colours.END in character.misc_items:
        print('''Where do you want to teleport to? Input coordinates e.g "d5".''')
        choice = input("> ")
        if choice.lower() in ["b6", "c2", "c5", "c6", "c7", "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "e2", "e5",
                              "e6", "e7", "f5", "f6", "g6", "h6", "i6", "j6", "k5", "k6", "k7", "l5", "l6", "m6", "m7",
                              "n6", "n7", "o7", "o8", "o9", "o10", "p10", "q10"]:
            character.location = choice
            print("You have gone to {}.".format(choice))
            input(">...")
            print_location(character, en1)
        elif choice.lower() in ["r10"]:
            print("It's probably not a good idea to teleport directly into the Baron's lair.")
            input(">...")
        else:
            print("Not a valid location.")
    else:
        print("You haven't unlocked teleportation yet.")
        input(">...")
    game_menu(character, en1)
