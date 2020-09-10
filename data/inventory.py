import os
import sys
from data.art import Colours
from data.item_rarity import Item_Rarity

sys.setrecursionlimit(10**6)  # test


def inventory(character, en1):
    from data.menu import game_menu
    os.system("cls")
    print("Select an Option:")
    print("1.) Equip")
    print("2.) Potions")
    print("3.) Misc")
    print("B.) Back")
    option = input("> ")
    if option == "1":
        item_type(character, en1)
    if option == "2":
        potion_items(character, en1)
    if option == "3":
        misc_items(character, en1)
    if option.lower() == "b":
        game_menu(character, en1)


def item_type(character, en1):
    print("Select an Option:")
    print("1.) Weapons")
    print("2.) Armour")
    print("B.) Back")
    option = input("> ")
    if option == "1":
        equip_weapons(character, en1)
    if option == "2":
        equip_armour(character, en1)
    if option.lower() == "b":
        os.system("cls")
        inventory(character, en1)


def equip_weapons(character, en1):
    print("What weapon do you want to equip?")
    print("TIP: Copy and paste the weapon into the input to equip, e.g." + Colours.BOLD + Colours.GREEN +
          ''' "[Wooden Sword] + (10 ATK)"''' + Colours.END)
    for character.x, character.y in character.player_weapons.items():
        if character.x in Item_Rarity.uncommon_weapons:
            print("# " + Colours.BOLD + Colours.GREEN + character.x + Colours.END)
        if character.x in Item_Rarity.rare_weapons:
            print("# " + Colours.BOLD + Colours.BLUE + character.x + Colours.END)
        if character.x in Item_Rarity.epic_weapons:
            print("# " + Colours.BOLD + Colours.PURPLE + character.x + Colours.END)
        if character.x in Item_Rarity.legendary_weapons:
            print("# " + Colours.BOLD + Colours.ORANGE + character.x + Colours.END)
    if not character.player_weapons:
        print("Nothing here...")
    print("B.) Back")
    choice = input("> ")
    if choice in character.player_weapons:
        character.current_weapon = choice
        if choice in Item_Rarity.uncommon_weapons:
            print("\nYou equipped " + Colours.BOLD + Colours.GREEN + choice + Colours.END + ".")
        elif choice in Item_Rarity.rare_weapons:
            print("\nYou equipped " + Colours.BOLD + Colours.BLUE + choice + Colours.END + ".")
        elif choice in Item_Rarity.epic_weapons:
            print("\nYou equipped " + Colours.BOLD + Colours.PURPLE + choice + Colours.END + ".")
        elif choice in Item_Rarity.legendary_weapons:
            print("\nYou equipped " + Colours.BOLD + Colours.ORANGE + choice + Colours.END + ".")
    elif choice.lower() == "b":
        os.system("cls")
        item_type(character, en1)
    else:
        print("Not a valid item.")
        input(">...")
        inventory(character, en1)
    input(">...")


def equip_armour(character, en1):
    print("What armour do you want to equip?")
    print("TIP: Copy and paste the armour into the input to equip, e.g." + Colours.BOLD + Colours.GREEN +
          ''' "[Leather Armour Set] + (20 HP/2 DF)"''' + Colours.END)
    for character.x, character.y in character.player_armour.items():
        if character.x in Item_Rarity.uncommon_armour:
            print("# " + Colours.BOLD + Colours.GREEN + character.x + Colours.END)
        if character.x in Item_Rarity.rare_armour:
            print("# " + Colours.BOLD + Colours.BLUE + character.x + Colours.END)
        if character.x in Item_Rarity.epic_armour:
            print("# " + Colours.BOLD + Colours.PURPLE + character.x + Colours.END)
        if character.x in Item_Rarity.legendary_armour:
            print("# " + Colours.BOLD + Colours.ORANGE + character.x + Colours.END)
    if not character.player_armour:
        print("Nothing here...")
    print("B.) Back")
    choice = input("> ")
    if choice in character.player_armour:
        character.current_armour = choice
        if choice in Item_Rarity.uncommon_armour:
            print("\nYou equipped " + Colours.BOLD + Colours.GREEN + choice + Colours.END + ".")
        if choice in Item_Rarity.rare_armour:
            print("\nYou equipped " + Colours.BOLD + Colours.BLUE + choice + Colours.END + ".")
        if choice in Item_Rarity.epic_armour:
            print("\nYou equipped " + Colours.BOLD + Colours.PURPLE + choice + Colours.END + ".")
        if choice in Item_Rarity.legendary_armour:
            print("\nYou equipped " + Colours.BOLD + Colours.ORANGE + choice + Colours.END + ".")
    elif choice.lower() == "b":
        os.system("cls")
        item_type(character, en1)
    else:
        print("Not a valid item.")
        input(">...")
        inventory(character, en1)
    input(">...")


def potion_items(character, en1):
    print("What potion do you want to use?")
    i = 1
    for item in character.items:
        print(str(i) + ".)", item['name'],  item['des'], "(x" + str(item['quantity']) + ")")
        i += 1
    try:
        item_choice = int(input("> ")) - 1
    except ValueError:
        print("Input must be a number.")
    else:
        if 0 <= item_choice < i - 1:
            if character.items[item_choice]['name'] in [Colours.BOLD + Colours.GREEN + "[Light Health Potion]" + Colours.END,
                                                        Colours.BOLD + Colours.BLUE + "[Health Potion]" + Colours.END,
                                                        Colours.BOLD + Colours.PURPLE + "[Max Health Potion]" + Colours.END]:
                if character.items[item_choice]['quantity'] == 0:
                    print("None left.")
                elif character.items[item_choice]['property'] + character.hp >= character.max_hp:
                    print("You healed for {} HP.".format(character.max_hp - character.hp))
                    character.items[item_choice]['quantity'] -= 1
                    character.hp += character.items[item_choice]['property']
                    character.hp = character.max_hp
                else:
                    print("You healed for {} HP.".format(character.items[item_choice]['property']))
                    character.items[item_choice]['quantity'] -= 1
                    character.hp += character.items[item_choice]['property']
            elif character.items[item_choice]['name'] in [Colours.BOLD + Colours.ORANGE + "[Hit Point Potion]" + Colours.END]:
                if character.items[item_choice]['quantity'] == 0:
                    print("None left.")
                else:
                    print("You gain 1 permanent health point.")
                    character.hp += character.items[item_choice]['property']
                    character.max_hp += character.items[item_choice]['property']
                    character.items[item_choice]['quantity'] -= 1
            elif character.items[item_choice]['name'] in [Colours.BOLD + Colours.ORANGE + "[Attack Potion]" + Colours.END]:
                if character.items[item_choice]['quantity'] == 0:
                    print("None left.")
                else:
                    print("You gain 1 permanent attack point.")
                    character.base_atk += character.items[item_choice]['property']
                    character.items[item_choice]['quantity'] -= 1
            elif character.items[item_choice]['name'] in [Colours.BOLD + Colours.ORANGE + "[Defence Potion]" + Colours.END]:
                if character.items[item_choice]['quantity'] == 0:
                    print("None left.")
                else:
                    print("You gain 1 permanent defence point.")
                    character.defence += character.items[item_choice]['property']
                    character.items[item_choice]['quantity'] -= 1
        else:
            print("That number is out of range.")
    input(">...")
    inventory(character, en1)


def misc_items(character, en1):
    print("Miscellaneous Items")
    for character.x, character.y in character.misc_items.items():
        print("# " + character.x)
    print("B.) Back")
    choice = input("> ")
    if choice.lower() == "b":
        inventory(character, en1)
