import os
import pickle
import sys


def save(character, en1):
    from data.menu import game_menu
    if os.path.exists("save_file"):
        print("Are you sure you want to overwrite your current save? Y/N")
        option = input("> ")
        if option.lower() == "y":
            with open('save_file', 'wb') as f:
                pickle.dump(character, f)
                print("Game has been saved.")
        else:
            print("Game hasn't been saved.")
    else:
        with open('save_file', 'wb') as f:
            pickle.dump(character, f)
            print("Game has been saved.")
    input(">...")
    game_menu(character, en1)


def auto_save(character):
    with open('save_file', 'wb') as f:
        pickle.dump(character, f)


def exit_check(character, en1):
    from data.menu import game_menu
    os.system("cls")
    print("Are you sure you want to exit? Make sure you have saved first. Y/N")
    choice = input("> ")
    if choice.lower() == "y":
        sys.exit()
    else:
        game_menu(character, en1)
