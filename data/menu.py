import os
import sys
from data.art import Colours
from data.display_map import print_map_town
from data.music import game_menu_music
from data.item_rarity import Item_Rarity
from data.events import events
from data.game_map import move
from data.inventory import inventory
from data.quests import quests
from data.examine import examine
from data.teleport import teleport
from data.save_exit import save, exit_check

sys.setrecursionlimit(10**6)  # test


def game_menu(character, en1):
    events(character)
    game_menu_music(character)
    os.system("cls")
    print_map_town(character)
    print("")
    character.bleed_check = False
    character.burn_check = False
    character.b_atk_p = 0
    print(Colours.BOLD + "Character Stats" + Colours.END)
    print("Name: {}".format(character.name))
    print("Gold: {}".format(character.gold))
    if character.level == 10:
        print("XP: 777/777")
    else:
        print("XP: {}/{}".format(character.xp1, character.xp2))
    print("Level: {}\n".format(character.level))
    print("Health: {}/{}".format(character.base_hp, character.hp_max))
    print("Attack: {}".format(character.current_atk))
    print("Defence: {}\n".format(character.current_defence))
    print("Current Location - {}\n".format(character.location))
    if character.current_weapon == "":
        print("Current Weapon - " + Colours.WHITE + "[Fists] + (0 ATK)" + Colours.END)
    if character.current_weapon in Item_Rarity.uncommon_weapons:
        print("Current Weapon -" + Colours.GREEN + Colours.BOLD + " {}".format(character.current_weapon) + Colours.END)
    if character.current_weapon in Item_Rarity.rare_weapons:
        print("Current Weapon -" + Colours.BLUE + Colours.BOLD + " {}".format(character.current_weapon) + Colours.END)
    if character.current_weapon in Item_Rarity.epic_weapons:
        print("Current Weapon -" + Colours.PURPLE + Colours.BOLD + " {}".format(character.current_weapon) + Colours.END)
    if character.current_weapon in Item_Rarity.legendary_weapons:
        print("Current Weapon -" + Colours.ORANGE + Colours.BOLD + " {}".format(character.current_weapon) + Colours.END)
    if character.current_armour == "":
        print("Current Armour - " + Colours.WHITE + "[Naked] + (0 HP/0 DF)\n" + Colours.END)
    if character.current_armour in Item_Rarity.uncommon_armour:
        print("Current Armour -" + Colours.GREEN + Colours.BOLD + " {}\n".format(character.current_armour) + Colours.END)
    if character.current_armour in Item_Rarity.rare_armour:
        print("Current Armour -" + Colours.BLUE + Colours.BOLD + " {}\n".format(character.current_armour) + Colours.END)
    if character.current_armour in Item_Rarity.epic_armour:
        print("Current Armour -" + Colours.PURPLE + Colours.BOLD + " {}\n".format(character.current_armour) + Colours.END)
    if character.current_armour in Item_Rarity.legendary_armour:
        print("Current Armour -" + Colours.ORANGE + Colours.BOLD + " {}\n".format(character.current_armour) + Colours.END)
    print(Colours.BOLD + "Menu" + Colours.END)
    print("1.) Move")
    print("2.) Inventory")
    print("3.) Info")
    print("4.) Examine")
    print("5.) Teleport")
    print("6.) Save")
    print("7.) Exit\n")
    option = input("> ")
    os.system('cls')
    if option == "1":
        move(character, en1)
    if option == "2":
        inventory(character, en1)
    if option == "3":
        quests(character, en1)
    if option == "4":
        examine(character, en1)
    if option == "5":
        teleport(character, en1)
    if option == "6":
        save(character, en1)
    if option == "7":
        exit_check(character, en1)
    else:
        game_menu(character, en1)
