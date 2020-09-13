import random
import os
from data.art import Colours
from data.item_rarity import Item_Rarity


class Loot:
    def __init__(self, gold, item):
        self.forest_mob_drops = {}
        self.gold = gold
        self.item = item


# loot1
Loot.forest_mob_drops = {"[Wooden Sword] + (10 ATK)": 50,
                         "[Leather Armour Set] + (20 HP/2 DF)": 30}
# loot2
Loot.water_mob_drops = {"[Bronze Sword] + (15 ATK)": 100,
                        "[Bronze Armour] + (20 HP/4 DF)": 60}

# loot3
Loot.desert_mob_drops1 = {"[Steel Sword] + (30 ATK)": 300,
                          "[Steel Armour Set] + (50 HP/6 DF)": 200}
Loot.desert_mob_drops2 = {"[Rune Sword] + (40 ATK)": 750, "[Rune Armour Set] + (60 HP/8 DF)": 500}

# loot4
Loot.cave_mob_drops1 = {"[Rune Sword] + (40 ATK)": 750, "[Rune Armour Set] + (60 HP/8 DF)": 500}
Loot.cave_mob_drops2 = {"[Dragon Sword] + (60 ATK)": 1500, "[Dragon Armour Set] + (80 HP/10 DF)": 1000}

# boss
Loot.baron_of_hell1 = {"[Dragon Sword] + (60 ATK)": 1500, "[Dragon Armour Set] + (80 HP/10 DF)": 1000}
Loot.baron_of_hell2 = {"[Sunfury, Cursed Axe of the Breezeseeker] + (100 ATK)": 0, "[The Baron's Armour] + (100/15 DF)": 0}

# boss
Loot.misc_loot = {Colours.BOLD + Colours.ORANGE + "[Baron of Hell Head]" + Colours.END: 0}

# current loot
Loot.drop = {}


def loot1(character, en1):
    gold_drop = random.randint(1, 3)
    print("You gained {} Gold.\n".format(gold_drop))
    character.gold += gold_drop

    loot_chance = random.randint(1, 101)
    if loot_chance in range(71, 101):

        Loot.item = random.choice(list(Loot.forest_mob_drops.items()))

        Loot.drop.update({Loot.item})

        for x in list(Loot.drop):
            remove = x
            print("{} dropped {}.".format(en1.name, Colours.BOLD + Colours.GREEN + x + Colours.END))
            print("Would you like to pick up {}? Y/N".format(Colours.BOLD + Colours.GREEN + x + Colours.END))
            choice = input("> ")
            if choice.lower() == "y":
                if x in character.player_weapons or x in character.player_armour:
                    print("You already have {}, you should leave it for someone else.".format(Colours.BOLD + Colours.GREEN + x + Colours.END))
                else:
                    print("You picked up {}.".format(Colours.BOLD + Colours.GREEN + x + Colours.END))
                    if x in Item_Rarity.uncommon_weapons:
                        character.player_weapons.update({Loot.item})
                    elif x in Item_Rarity.uncommon_armour:
                        character.player_armour.update({Loot.item})
            elif choice.lower() == "n":
                print("You didn't pick up {}.".format(Colours.BOLD + Colours.GREEN + x + Colours.END))
            options = ["y", "n"]
            while choice.lower() not in options:
                print("You must enter Y or N.")
                choice = input("> ")
                if choice.lower() == "y":
                    if x in character.player_weapons or x in character.player_armour:
                        print("You already have {}, you should leave it for someone else.".format(Colours.BOLD + Colours.GREEN + x + Colours.END))
                    else:
                        print("You picked up {}.".format(Colours.BOLD + Colours.GREEN + x + Colours.END))
                        if x in Item_Rarity.uncommon_weapons:
                            character.player_weapons.update({Loot.item})
                        elif x in Item_Rarity.uncommon_armour:
                            character.player_armour.update({Loot.item})
                elif choice.lower() == "n":
                    print("You didn't pick up {}.".format(Colours.BOLD + Colours.GREEN + x + Colours.END))
            del Loot.drop[remove]
    input(">...")


def loot2(character, en1):
    gold_drop = random.randint(3, 6)
    print("You gained {} Gold.\n".format(gold_drop))
    character.gold += gold_drop

    loot_chance = random.randint(1, 101)
    if loot_chance in range(81, 101):

        Loot.item = random.choice(list(Loot.water_mob_drops.items()))

        Loot.drop.update({Loot.item})

        for x in list(Loot.drop):
            remove = x
            print("{} dropped {}.".format(en1.name, Colours.BOLD + Colours.GREEN + x + Colours.END))
            print("Would you like to pick up {}? Y/N".format(Colours.BOLD + Colours.GREEN + x + Colours.END))
            choice = input("> ")
            options = ["y", "n"]
            while choice.lower() not in options:
                print("You must enter Y or N.")
                choice = input("> ")
                if choice.lower() == "y":
                    if x in character.player_weapons or x in character.player_armour:
                        print("You already have {}, you should leave it for someone else.".format(Colours.BOLD + Colours.GREEN + x + Colours.END))
                    else:
                        print("You picked up {}.".format(Colours.BOLD + Colours.GREEN + x + Colours.END))
                        if x in Item_Rarity.uncommon_weapons:
                            character.player_weapons.update({Loot.item})
                        elif x in Item_Rarity.uncommon_armour:
                            character.player_armour.update({Loot.item})
                elif choice.lower() == "n":
                    print("You didn't pick up {}.".format(Colours.BOLD + Colours.GREEN + x + Colours.END))
            del Loot.drop[remove]
    input(">...")


def loot3(character, en1):
    gold_drop = random.randint(6, 10)
    print("You gained {} Gold.\n".format(gold_drop))
    character.gold += gold_drop

    loot_chance = random.randint(1, 101)

    if loot_chance in range(71, 95):
        Loot.item = random.choice(list(Loot.desert_mob_drops1.items()))

        Loot.drop.update({Loot.item})

        for x in list(Loot.drop):
            remove = x
            print("{} dropped {}.".format(en1.name, Colours.BOLD + Colours.GREEN + x + Colours.END))
            print("Would you like to pick up {}? Y/N".format(Colours.BOLD + Colours.GREEN + x + Colours.END))
            choice = input("> ")
            options = ["y", "n"]
            while choice.lower() not in options:
                print("You must enter Y or N.")
                choice = input("> ")
                if choice.lower() == "y":
                    if x in character.player_weapons or x in character.player_armour:
                        print("You already have {}, you should leave it for someone else.".format(Colours.BOLD + Colours.GREEN + x + Colours.END))
                    else:
                        print("You picked up {}.".format(Colours.BOLD + Colours.GREEN + x + Colours.END))
                        if x in Item_Rarity.uncommon_weapons:
                            character.player_weapons.update({Loot.item})
                        elif x in Item_Rarity.uncommon_armour:
                            character.player_armour.update({Loot.item})
                elif choice.lower() == "n":
                    print("You didn't pick up {}.".format(Colours.BOLD + Colours.GREEN + x + Colours.END))
            del Loot.drop[remove]

    elif loot_chance in range(96, 101):
        Loot.item = random.choice(list(Loot.desert_mob_drops2.items()))

        Loot.drop.update({Loot.item})

        for x in list(Loot.drop):
            remove = x
            print("{} dropped {}.".format(en1.name, Colours.BOLD + Colours.BLUE + x + Colours.END))
            print("Would you like to pick up {}? Y/N".format(Colours.BOLD + Colours.BLUE + x + Colours.END))
            choice = input("> ")
            options = ["y", "n"]
            while choice.lower() not in options:
                print("You must enter Y or N.")
                choice = input("> ")
                if choice.lower() == "y":
                    if x in character.player_weapons or x in character.player_armour:
                        print("You already have {}, you should leave it for someone else.".format(Colours.BOLD + Colours.BLUE + x + Colours.END))
                    else:
                        print("You picked up {}.".format(Colours.BOLD + Colours.BLUE + x + Colours.END))
                        if x in Item_Rarity.rare_weapons:
                            character.player_weapons.update({Loot.item})
                        elif x in Item_Rarity.rare_armour:
                            character.player_armour.update({Loot.item})
                elif choice.lower() == "n":
                    print("You didn't pick up {}.".format(Colours.BOLD + Colours.BLUE + x + Colours.END))
            del Loot.drop[remove]
    input(">...")


def loot4(character, en1):
    gold_drop = random.randint(8, 13)
    print("You gained {} Gold.\n".format(gold_drop))
    character.gold += gold_drop

    loot_chance = random.randint(1, 101)
    if loot_chance in range(81, 95):

        Loot.item = random.choice(list(Loot.cave_mob_drops1.items()))

        Loot.drop.update({Loot.item})

        for x in list(Loot.drop):
            remove = x
            print("{} dropped {}.".format(en1.name, Colours.BOLD + Colours.BLUE + x + Colours.END))
            print("Would you like to pick up {}? Y/N".format(Colours.BOLD + Colours.BLUE + x + Colours.END))
            choice = input("> ")
            options = ["y", "n"]
            while choice.lower() not in options:
                print("You must enter Y or N.")
                choice = input("> ")
                if choice.lower() == "y":
                    if x in character.player_weapons or x in character.player_armour:
                        print("You already have {}, you should leave it for someone else.".format(
                            Colours.BLUE + x + Colours.END))
                    else:
                        print("You picked up {}.".format(Colours.BOLD + Colours.BLUE + x + Colours.END))
                        if x in Item_Rarity.rare_weapons:
                            character.player_weapons.update({Loot.item})
                        elif x in Item_Rarity.rare_armour:
                            character.player_armour.update({Loot.item})
                elif choice.lower() == "n":
                    print("You didn't pick up {}.".format(Colours.BOLD + Colours.BLUE + x + Colours.END))
            del Loot.drop[remove]

    elif loot_chance in range(96, 101):

        Loot.item = random.choice(list(Loot.cave_mob_drops2.items()))

        Loot.drop.update({Loot.item})

        for x in list(Loot.drop):
            remove = x
            print("{} dropped {}.".format(en1.name, Colours.BOLD + Colours.PURPLE + x + Colours.END))
            print("Would you like to pick up {}? Y/N".format(Colours.BOLD + Colours.PURPLE + x + Colours.END))
            choice = input("> ")
            options = ["y", "n"]
            while choice.lower() not in options:
                print("You must enter Y or N.")
                choice = input("> ")
                if choice.lower() == "y":
                    if x in character.player_weapons or x in character.player_armour:
                        print("You already have {}, you should leave it for someone else.".format(Colours.BOLD + Colours.PURPLE + x + Colours.END))
                    else:
                        print("You picked up {}.".format(Colours.BOLD + Colours.PURPLE + x + Colours.END))
                        if x in Item_Rarity.epic_weapons:
                            character.player_weapons.update({Loot.item})
                        elif x in Item_Rarity.epic_armour:
                            character.player_armour.update({Loot.item})
                elif choice.lower() == "n":
                    print("You didn't pick up {}.".format(Colours.BOLD + Colours.PURPLE + x + Colours.END))
            del Loot.drop[remove]
    input(">...")


def baron_loot(character, en1):
    gold_drop = random.randint(12, 17)
    print("You gained {} Gold.\n".format(gold_drop))
    character.gold += gold_drop
    if character.r10_event_1:
        for x in list(Loot.misc_loot):
            print("You obtained {}.".format(x))
            character.r10_event_1 = False
            character.r10_event_2 = True
            character.misc_items.update(Loot.misc_loot)
    loot_chance = random.randint(1, 101)
    if loot_chance in range(81, 95):

        Loot.item = random.choice(list(Loot.baron_of_hell1.items()))

        Loot.drop.update({Loot.item})

        for x in list(Loot.drop):
            remove = x
            print("{} dropped {}.".format(en1.name, Colours.BOLD + Colours.PURPLE + x + Colours.END))
            print("Would you like to pick up {}? Y/N".format(Colours.BOLD + Colours.PURPLE + x + Colours.END))
            choice = input("> ")
            options = ["y", "n"]
            while choice.lower() not in options:
                print("You must enter Y or N.")
                choice = input("> ")
                if choice.lower() == "y":
                    if x in character.player_weapons or x in character.player_armour:
                        print("You already have {}, you should leave it for someone else.".format(Colours.BOLD + Colours.PURPLE + x + Colours.END))
                    else:
                        print("You picked up {}.".format(Colours.BOLD + Colours.PURPLE + x + Colours.END))
                        if x in Item_Rarity.epic_weapons:
                            character.player_weapons.update({Loot.item})
                        elif x in Item_Rarity.epic_armour:
                            character.player_armour.update({Loot.item})
                elif choice.lower() == "n":
                    print("You didn't pick up {}.".format(Colours.BOLD + Colours.PURPLE + x + Colours.END))
            del Loot.drop[remove]
    elif loot_chance in range(96, 101):

        Loot.item = random.choice(list(Loot.baron_of_hell2.items()))

        Loot.drop.update({Loot.item})

        for x in list(Loot.drop):
            remove = x
            print("{} dropped {}.".format(en1.name, Colours.BOLD + Colours.ORANGE + x + Colours.END))
            print("Would you like to pick up {}? Y/N".format(Colours.BOLD + Colours.ORANGE + x + Colours.END))
            choice = input("> ")
            options = ["y", "n"]
            while choice.lower() not in options:
                print("You must enter Y or N.")
                choice = input("> ")
                if choice.lower() == "y":
                    if x in character.player_weapons or x in character.player_armour:
                        print("You already have {}, you should leave it for someone else.".format(Colours.BOLD + Colours.ORANGE + x + Colours.END))
                    else:
                        print("You picked up {}.".format(Colours.BOLD + Colours.ORANGE + x + Colours.END))
                        if x in Item_Rarity.legendary_weapons:
                            character.player_weapons.update({Loot.item})
                        elif x in Item_Rarity.legendary_armour:
                            character.player_armour.update({Loot.item})
                elif choice.lower() == "n":
                    print("You didn't pick up {}.".format(Colours.BOLD + Colours.ORANGE + x + Colours.END))
            del Loot.drop[remove]
    input(">...")
    if character.r10_event_2:
        print("Congratulations on defeating the Baron of Hell, would you like to go home and claim your rewards? Y/N")
        choice = input("> ")
        if choice.lower() == "y":
            character.location = "d1"
        else:
            print("It will be a long walk back...")
            input(">...")
        character.r10_event_2 = False


def gold_cheat(character, en1):
    from data.menu import game_menu
    os.system("cls")
    print("Cheat Activated: + 1000 Gold")
    input(">...")
    character.gold += 1000
    game_menu(character, en1)
