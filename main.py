# Text RPG
# Neb2
#
# VERSIONS
# 0.0 - 20/06/2020
# 1.0 - 10/09/2020
# 1.1 - xx/xx/2020

import sys
import os
import pickle
import winsound
from data.menu import game_menu
from data.intro import intro
from data.full_screen import maximize_console
from data.art import title_art, Colours
from data.loading import loading_1

sys.setrecursionlimit(10**6)  # test

winsound.PlaySound("music\\title_screen_delay.wav", winsound.SND_ASYNC + winsound.SND_FILENAME)


# game title screen
def main(character, en1):
    loading_1()
    maximize_console()
    os.system("cls")
    title_art()
    title_screen_selection(character, en1)


def title_screen_selection(character, en1):
    maximize_console()
    os.system("cls")
    title_art()
    option = input("> ")
    if option == "1":
        intro(en1)
    elif option == "2":
        if os.path.exists("save_file"):
            with open('save_file', 'rb') as f:
                character = pickle.load(f)
            os.system("cls")
            print("Save file loaded.")
            input(">...")
            character.town_zone = True
            character.forest_zone = True
            character.water_zone = True
            character.desert_zone = True
            character.dungeon_zone = True
            character.battle_music_1 = True
            character.battle_music_2 = True
            character.boss_music_1 = True
            character.win_music_1 = True
            character.win_music_2 = True
            character.defeat_music_1 = True
            game_menu(character, en1)
        else:
            os.system("cls")
            print("You have no save file.")
            input(">...")
            title_screen_selection(character, en1)
    elif option == "3":
        help_menu(character, en1)
    elif option == "4":
        sys.exit()
    else:
        title_screen_selection(character, en1)


def help_menu(character, en1):
    os.system("cls")
    print(Colours.BOLD + "CONTROLS\n" + Colours.END)
    print(
        "Most actions in the game can be done using your numpad, you enter the number next to the selection you want\n"
        "and press enter to complete the action.\n")
    print(
        "For equipping Weapons and Armour make sure you copy and paste the name in full of the Weapon/Armour you want\n"
        "to equip. For example: [Bronze Sword] + (15 ATK)")
    print(
        "The easiest way to do this in CLI is to highlight the Weapon/Armour name then press Ctrl + C to copy,\n"
        "and right click the mouse to paste, or Ctrl + V.\n")
    print("Some inputs require a Yes or No input, which can be done by simply inputting Y for yes, and N for no.\n")
    print("For returning back to the main menu you can usually press ENTER to do so.\n")
    input(">...")
    os.system("cls")
    title_art()
    title_screen_selection(character, en1)


title_screen_selection(sys.argv, sys.argv[0])
# main(sys.argv, sys.argv[0])
