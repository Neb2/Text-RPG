import os
import sys
from data.item_rarity import Item_Rarity
from data.art import Colours

sys.setrecursionlimit(10**6)  # test


class Shop:
    def __init__(self):
        self.sell_weapons = {}
        self.sell_armour = {}


class Items:
    def __init__(self, name, prop, description, price):
        self.name = name
        self.prop = prop
        self.description = description
        self.price = price


# shop items
class Potions:
    l_health_pot = Items(Colours.BOLD + Colours.GREEN + "[Light Health Potion]" + Colours.END, 50, "+ 50 HP  ", 4)
    health_pot = Items(Colours.BOLD + Colours.BLUE + "[Health Potion]" + Colours.END, 150, "+ 150 HP       ", 10)
    max_pot = Items(Colours.BOLD + Colours.PURPLE + "[Max Health Potion]" + Colours.END, 100000, "+ MAX HP   ", 50)
    plus_hp = Items(Colours.BOLD + Colours.ORANGE + "[Hit Point Potion]" + Colours.END, 1, "+ 1 HP      ", 1000)
    plus_atk = Items(Colours.BOLD + Colours.ORANGE + "[Attack Potion]" + Colours.END, 1, "+ 1 ATK        ", 1000)
    plus_def = Items(Colours.BOLD + Colours.ORANGE + "[Defence Potion]" + Colours.END, 1, "+ 1 DEF       ", 1000)


Shop.sell_weapons = {"[Wooden Sword] + (10 ATK)": 50,
                     "[Bronze Sword] + (15 ATK)": 100,
                     "[Iron Sword] + (20 ATK)": 200,
                     "[Rune Sword] + (40 ATK)": 750,
                     "[General Store Sword] + (80 ATK)": 3000}

Shop.sell_armour = {"[Leather Armour Set] + (20 HP/2 DF)": 30,
                    "[Bronze Armour] + (20 HP/4 DF)": 60,
                    "[Iron Armour Set] + (40 HP/5 DF)": 100,
                    "[Rune Armour Set] + (50 HP/8 DF)": 500,
                    "[General Store Armour Set] (90 HP/12 DF)": 2000}


def shop(character, en1):
    from data.menu import game_menu
    os.system("cls")
    print("Hello {}! Welcome to the General Store, how may I help you today?".format(character.name))
    print("1.) Buy")
    print("2.) Sell")
    print("Press [Enter] to exit the shop.")
    choice = input("> ")
    if choice == "1":
        print("1.) Weapons")
        print("2.) Armour")
        print("3.) Items")
        print("B.) Back")
        choice = input("> ")
        if choice == "1":
            buy_weapons(character, en1)
        if choice == "2":
            buy_armour(character, en1)
        if choice == "3":
            buy_items(character, en1)
        if choice.lower() == "b":
            shop(character, en1)
    elif choice == "2":
        print("1.) Weapons")
        print("2.) Armour")
        print("B.) Back")
        choice = input("> ")
        if choice == "1":
            sell_weapons(character, en1)
        if choice == "2":
            sell_armour(character, en1)
        if choice.lower() == "b":
            shop(character, en1)
    else:
        game_menu(character, en1)


def buy_weapons(character, en1):
    os.system("cls")
    print("What weapon would you like to buy?")
    print("TIP: Copy and paste the item into the input to buy, e.g. '"
          + Colours.BOLD + Colours.GREEN + "[Bronze Sword] + (15 ATK)" + Colours.END + "'")
    print("Your gold - {}.".format(character.gold))
    for Shop.x, Shop.y in Shop.sell_weapons.items():
        if Shop.x in Item_Rarity.uncommon_weapons:
            print("#", Colours.BOLD + Colours.GREEN + Shop.x + Colours.END, "-", Shop.y, "Gold.")
        if Shop.x in Item_Rarity.rare_weapons:
            print("#", Colours.BOLD + Colours.BLUE + Shop.x + Colours.END, "-", Shop.y, "Gold.")
        if Shop.x in Item_Rarity.epic_weapons:
            print("#", Colours.BOLD + Colours.PURPLE + Shop.x + Colours.END, "-", Shop.y, "Gold.")
    option = input("> ")
    if option in character.player_weapons:
        if option in Item_Rarity.uncommon_weapons:
            print("You already have a " + Colours.BOLD + Colours.GREEN + "{}".format(option) + Colours.END + ", what's wrong with the one you already have?")
        if option in Item_Rarity.rare_weapons:
            print("You already have a " + Colours.BOLD + Colours.BLUE + "{}".format(option) + Colours.END + ", what's wrong with the one you already have?")
        if option in Item_Rarity.epic_weapons:
            print("You already have a " + Colours.BOLD + Colours.PURPLE + "{}".format(option) + Colours.END + ", what's wrong with the one you already have?")
        input(">...")
        buy_weapons(character, en1)
    if option in Shop.sell_weapons:
        price = Shop.sell_weapons[option]
        if character.gold >= Shop.sell_weapons[option]:
            if option in Item_Rarity.uncommon_weapons:
                print("Are you sure you want to buy " + Colours.BOLD + Colours.GREEN + option + Colours.END + " for {} gold? Y/N".format(price))
            if option in Item_Rarity.rare_weapons:
                print("Are you sure you want to buy " + Colours.BOLD + Colours.BLUE + option + Colours.END + " for {} gold? Y/N".format(price))
            if option in Item_Rarity.epic_weapons:
                print("Are you sure you want to buy " + Colours.BOLD + Colours.PURPLE + option + Colours.END + " for {} gold? Y/N".format(price))
            option1 = input("> ")
            if option1.lower() == "y":
                character.player_weapons[option] = price
                character.gold -= price
                if option in Item_Rarity.uncommon_weapons:
                    print("You bought " + Colours.BOLD + Colours.GREEN + option + Colours.END + ".")
                if option in Item_Rarity.rare_weapons:
                    print("You bought " + Colours.BOLD + Colours.BLUE + option + Colours.END + ".")
                if option in Item_Rarity.epic_weapons:
                    print("You bought " + Colours.BOLD + Colours.PURPLE + option + Colours.END + ".")
                input(">...")
                shop(character, en1)
            elif option1.lower() == "n":
                shop(character, en1)
            elif option1 not in ["Y, N, y, n"]:
                print("Input has to be Y/N.")
                shop(character, en1)
        else:
            print("\nYou are too poor to buy this item.")
            input(">...")
            shop(character, en1)
    else:
        print("\nNot a valid item choice.")
        input(">...")
        shop(character, en1)


def buy_armour(character, en1):
    print("What armour would you like to buy?")
    print("TIP: Copy and paste the item into the input to buy, e.g. '"
          + Colours.BOLD + Colours.GREEN + "[Bronze Armour] + (20 HP/4 DF)" + Colours.END + "'")
    print("Your gold - {}.".format(character.gold))
    for Shop.x, Shop.y in Shop.sell_armour.items():
        if Shop.x in Item_Rarity.uncommon_armour:
            print("#", Colours.BOLD + Colours.GREEN + Shop.x + Colours.END, "-", Shop.y, "Gold.")
        if Shop.x in Item_Rarity.rare_armour:
            print("#", Colours.BOLD + Colours.BLUE + Shop.x + Colours.END, "-", Shop.y, "Gold.")
        if Shop.x in Item_Rarity.epic_armour:
            print("#", Colours.BOLD + Colours.PURPLE + Shop.x + Colours.END, "-", Shop.y, "Gold.")
    option = input("> ")
    if option in character.player_armour:
        if option in Item_Rarity.uncommon_armour:
            print("You already have a " + Colours.BOLD + Colours.GREEN + "{}".format(option) + Colours.END +
                  ", what is wrong with the one you already have?")
        if option in Item_Rarity.rare_armour:
            print("You already have a " + Colours.BOLD + Colours.BLUE + "{}".format(option) + Colours.END +
                  ", what is wrong with the one you already have?")
        if option in Item_Rarity.epic_armour:
            print("You already have a " + Colours.BOLD + Colours.PURPLE + "{}".format(option) + Colours.END +
                  ", what is wrong with the one you already have?")
        input(">...")
        buy_armour(character, en1)
    if option in Shop.sell_armour:
        price = Shop.sell_armour[option]
        if character.gold >= Shop.sell_armour[option]:
            if option in Item_Rarity.uncommon_armour:
                print("Are you sure you want to buy " + Colours.BOLD + Colours.GREEN + option + Colours.END + " for {} gold? Y/N".format(price))
            if option in Item_Rarity.rare_armour:
                print("Are you sure you want to buy " + Colours.BOLD + Colours.BLUE + option + Colours.END + " for {} gold? Y/N".format(price))
            if option in Item_Rarity.epic_armour:
                print("Are you sure you want to buy " + Colours.BOLD + Colours.PURPLE + option + Colours.END + " for {} gold? Y/N".format(price))
            option1 = input("> ")
            if option1.lower() == "y":
                character.player_armour[option] = price
                character.gold -= price
                if option in Item_Rarity.uncommon_armour:
                    print("You bought " + Colours.BOLD + Colours.GREEN + option + Colours.END + ".")
                if option in Item_Rarity.rare_armour:
                    print("You bought " + Colours.BOLD + Colours.BLUE + option + Colours.END + ".")
                if option in Item_Rarity.epic_armour:
                    print("You bought " + Colours.BOLD + Colours.PURPLE + option + Colours.END + ".")
                input(">...")
                shop(character, en1)
            elif option1.lower() == "n":
                shop(character, en1)
            elif option1 not in ["Y, N, y, n"]:
                print("Input has to be Y/N.")
                shop(character, en1)
        else:
            print("\nYou are too poor to buy this item.")
            input(">...")
            shop(character, en1)
    else:
        print("\nNot a valid item choice.")
        input(">...")
        shop(character, en1)


def buy_items(character, en1):
    i = 1
    print("TIP: Input the number next to the item you want.")
    print("Your gold - {}.".format(character.gold))
    for item in character.shop_pots:
        print(str(i) + ".)", item["item"].name, item["item"].description,
              "(x" + str(item["quantity"]) + ") " + item["price"])
        i += 1
    while True:
        try:
            item_choice = int(input("> ")) - 1
        except ValueError:
            print("Input must be a number.")
        else:
            if 0 <= item_choice < i - 1:
                break
            else:
                print("That number is out of range.")

    if character.shop_pots[item_choice]["quantity"] == 0:
        print("\n" + "None left...")
        buy_items(character, en1)

    print("How many of {} would you like to buy? MAX {}".format(character.shop_pots[item_choice]["item"].name,
                                                                character.shop_pots[item_choice]["quantity"]))
    while True:
        try:
            quantity_choice = int(input("> "))
        except ValueError:
            print("Input must be a number.")
        else:
            break

    if quantity_choice > character.shop_pots[item_choice]["quantity"]:
        print("There is only {} in stock, you cannot buy {}.".format(character.shop_pots[item_choice]["quantity"],
                                                                     quantity_choice))
        input(">...")
        buy_items(character, en1)
    else:
        total_cost = character.shop_pots[item_choice]["item"].price * quantity_choice

        print("Buy {} x {} for {} gold? Y/N".format(quantity_choice, character.shop_pots[item_choice]["item"].name,
                                                    total_cost))
        choice = input("> ")

        if choice.lower() == "y":
            if character.gold >= total_cost:
                print("You bought {} x {} for {} gold.".format(quantity_choice, character.shop_pots[item_choice]["item"].name,
                                                               total_cost))
                input(">...")
                character.shop_pots[item_choice]["quantity"] -= quantity_choice
                character.gold -= total_cost
                # creates a dict for searching if item already exists in inventory
                d = dict((i['name'], i["quantity"]) for i in character.items)
                if character.shop_pots[item_choice]["item"].name in d:
                    character.items[item_choice]["quantity"] += quantity_choice
                else:
                    bought_item_dict = {'name': character.shop_pots[item_choice]["item"].name,
                                        'property': character.shop_pots[item_choice]["item"].prop,
                                        'des': character.shop_pots[item_choice]["item"].description,
                                        'quantity': quantity_choice}
                    character.items.append(bought_item_dict)
                shop(character, en1)
            else:
                print("You are too poor to buy {} x {}.".format(quantity_choice, character.shop_pots[item_choice]["item"].name))
                input(">...")
                shop(character, en1)
        elif choice.lower() == "n":
            shop(character, en1)
        elif choice not in ["Y, N, y, n"]:
            print("Choice must be Y or N, try again.")
            shop(character, en1)


def sell_weapons(character, en1):
    print("What weapon would you like to sell?")
    print('''TIP: Copy and paste the item into the input to sell, e.g. "[Bronze Sword] + (15 ATK)"''')
    for character.x, character.y, in character.player_weapons.items():
        if character.x in Item_Rarity.uncommon_weapons:
            print("#", Colours.BOLD + Colours.GREEN + character.x + Colours.END, "-", character.y, "Gold.")
        elif character.x in Item_Rarity.rare_weapons:
            print("#", Colours.BOLD + Colours.BLUE + character.x + Colours.END, "-", character.y, "Gold.")
        elif character.x in Item_Rarity.epic_weapons:
            print("#", Colours.BOLD + Colours.PURPLE + character.x + Colours.END, "-", character.y, "Gold.")
        elif character.x in Item_Rarity.legendary_weapons:
            print("#", Colours.BOLD + Colours.ORANGE + character.x + Colours.END, "-", character.y, "Gold.")
    print("B). Back")
    wep = input("> ")
    if wep.lower() == "b":
        shop(character, en1)
    elif wep in character.player_weapons:
        price = character.player_weapons[wep]
        if wep in Item_Rarity.uncommon_weapons:
            print("Are you sure you want to sell " + Colours.BOLD + Colours.GREEN + wep + Colours.END + " for {} gold? Y/N".format(price))
        elif wep in Item_Rarity.rare_weapons:
            print("Are you sure you want to sell " + Colours.BOLD + Colours.BLUE + wep + Colours.END + " for {} gold? Y/N".format(price))
        elif wep in Item_Rarity.epic_weapons:
            print("Are you sure you want to sell " + Colours.BOLD + Colours.PURPLE + wep + Colours.END + " for {} gold? Y/N".format(price))
        elif wep in Item_Rarity.legendary_weapons:
            print("Are you sure you want to sell " + Colours.BOLD + Colours.ORANGE + wep + Colours.END + " for {} gold? Y/N".format(price))
        choice = input("> ")
        if choice.lower() == "y":
            if wep in Item_Rarity.uncommon_weapons:
                print("You sold " + Colours.BOLD + Colours.GREEN + wep + Colours.END + " for {} gold.".format(price))
            elif wep in Item_Rarity.rare_weapons:
                print("You sold " + Colours.BOLD + Colours.BLUE + wep + Colours.END + " for {} gold.".format(price))
            elif wep in Item_Rarity.epic_weapons:
                print("You sold " + Colours.BOLD + Colours.PURPLE + wep + Colours.END + " for {} gold.".format(price))
            elif wep in Item_Rarity.legendary_weapons:
                print("You sold " + Colours.BOLD + Colours.ORANGE + wep + Colours.END + " for {} gold.".format(price))
            character.gold += price
            if character.current_weapon in [wep]:
                character.current_weapon = ""
            del character.player_weapons[wep]
            input(">...")
            shop(character, en1)
    elif wep not in character.player_weapons:
        print("You don't have that item.")
        input(">...")
        shop(character, en1)


def sell_armour(character, en1):
    print("What armour would you like to sell?")
    print('''TIP: Copy and paste the item into the input to buy, e.g. "[Bronze Armour] + (20 HP/2 DF)"''')
    for character.x, character.y, in character.player_armour.items():
        if character.x in Item_Rarity.uncommon_armour:
            print("#", Colours.BOLD + Colours.GREEN + character.x + Colours.END, "-", character.y, "Gold.")
        if character.x in Item_Rarity.rare_armour:
            print("#", Colours.BOLD + Colours.BLUE + character.x + Colours.END, "-", character.y, "Gold.")
        if character.x in Item_Rarity.epic_armour:
            print("#", Colours.BOLD + Colours.PURPLE + character.x + Colours.END, "-", character.y, "Gold.")
        if character.x in Item_Rarity.legendary_armour:
            print("#", Colours.BOLD + Colours.ORANGE + character.x + Colours.END, "-", character.y, "Gold.")
    print("B). Back")
    armour = input("> ")
    if armour.lower() == "b":
        shop(character, en1)
    elif armour in character.player_armour:
        price = character.player_armour[armour]
        if armour in Item_Rarity.uncommon_armour:
            print("Are you sure you want to sell " + Colours.BOLD + Colours.GREEN + armour + Colours.END + " for {} gold? Y/N".format(price))
        if armour in Item_Rarity.rare_armour:
            print("Are you sure you want to sell " + Colours.BOLD + Colours.BLUE + armour + Colours.END + " for {} gold? Y/N".format(price))
        if armour in Item_Rarity.epic_armour:
            print("Are you sure you want to sell " + Colours.BOLD + Colours.PURPLE + armour + Colours.END + " for {} gold? Y/N".format(price))
        if armour in Item_Rarity.legendary_armour:
            print("Are you sure you want to sell " + Colours.BOLD + Colours.ORANGE + armour + Colours.END + " for {} gold? Y/N".format(price))
        choice = input("> ")
        if choice.lower() == "y":
            if armour in Item_Rarity.uncommon_armour:
                print("You sold " + Colours.BOLD + Colours.GREEN + armour + Colours.END + " for {} gold.".format(price))
            elif armour in Item_Rarity.rare_armour:
                print("You sold " + Colours.BOLD + Colours.BLUE + armour + Colours.END + " for {} gold.".format(price))
            elif armour in Item_Rarity.epic_armour:
                print("You sold " + Colours.BOLD + Colours.PURPLE + armour + Colours.END + " for {} gold.".format(price))
            elif armour in Item_Rarity.legendary_armour:
                print("You sold " + Colours.BOLD + Colours.ORANGE + armour + Colours.END + " for {} gold.".format(price))
            character.gold += price
            if character.current_armour in [armour]:
                character.current_armour = ""
            del character.player_armour[armour]
            input(">...")
            shop(character, en1)
    elif armour not in character.player_armour:
        print("You don't have that item.")
        input(">...")
        shop(character, en1)
