import os
import random
import sys
from data.art import Colours
from data.game_map import Map
from data.quests import Quest_0
from data.shop_items import shop
from data.level import level
from data.art import wanted_poster
from data.battle import enemy_gen
from data.battle import end_fight_lose

sys.setrecursionlimit(10**6)  # test


def examine(character, en1):
    from data.menu import game_menu
    if character.location == "b6":
        if character.b6_event_1:
            print("You see something shiny behind a tree.")
            input(">...")
            character.gold += 20
            character.b6_event_1 = False
            print("You gain 20 gold.")
            input(">...")
        elif not character.b6_event_1:
            print(Map.zone_map[character.location][Map.EXAMINE])
            input(">...")
    elif character.location == 'c2':
        print(Map.zone_map[character.location][Map.EXAMINE])
        input(">...")
        shop(character, en1)
    elif character.location in ["d2", "d4", "f6", "g6", "k6", "n7", "o7", "q10"]:
        print(Map.zone_map[character.location][Map.EXAMINE])
        input(">...")
    elif character.location == 'd1':
        print(Map.zone_map[character.location][Map.EXAMINE])
        print("Do you want to rest? Y/N")
        choice = input("> ")
        if choice.lower() == "y":
            print("You sleep to regain your strength.")
            print("Your health has been restored to full.")
            character.hp = character.max_hp
        input(">...")
    elif character.location == 'd3':
        if character.d3_event_1:
            print("Do you want to talk to the man sitting in the grass? Y/N")
            choice = input("> ")
            if choice.lower() == "y":
                print("You walk up to the man, and he begins to spew unintelligible words from his mouth. You don't\n"
                      "quite understand what he's saying but nod along anyway. Once he stops talking there's a bit of an\n"
                      "awkward pause as you don't really know what to say, but after a moment he hands you a note that reads...")
                input(">...")
                print('''"KILL 5 BEARS".''')
                input(">...")
                print("Do you wish to take quest to kill 5 bears? Y/N")
                choice = input("> ")
                if choice.lower() == "y":
                    print("You give the strange man a thumbs up and a forced smile as you walk away with the note in\n"
                          "your hand.\n")
                    print("QUEST ACCEPTED: Generic RPG Kill Quest")
                    input(">...")
                    character.active_quests.append({"name": Quest_0.slay_monsters, "test": 0})
                    character.d3_event_1 = False
                    character.d3_event_2 = True
                elif choice.lower() == "n":
                    print(
                        "You decide not to take the quest to kill the innocent bears, probably for the best as it doesn't\n"
                        "look like this man would give you a quest reward anyway. ")
                    input(">...")
                else:
                    print("Not a valid input, enter Y or N.")
            elif choice.lower() == "n":
                print(
                    "You speedily walk past the man in the grass as he begins shouting at you, but you don't understand\n"
                    "what he's saying. Probably for the best you avoided him.")
                input(">...")
            else:
                print("Not a valid input, enter Y or N.")
        elif character.d3_event_2:
            for quest in character.active_quests:
                if "Generic RPG Kill Quest" in quest["name"].name:
                    if quest["test"] <= 4:
                        print("No reason to talk to the strange man again until you've completed the quest.")
                        input(">...")
                    elif quest["test"] == 5:
                        print("You walk up to the man, then as you greet him you pass back the note, covered in bear blood,\n"
                              "and let him know that you've killed the 5 bears as requested.")
                        input(">...")
                        print(
                            "The man takes your note, glances at it for a moment, then stands up from the grass and begins to\n"
                            "shout at you. Unable to understand what he's saying you just ask for your reward but before you get\n"
                            "a chance to finish he pushes into you, knocking you down to the ground and as you fall some gold\n"
                            "drops out of your pocket which he takes and runs into the forest.")
                        input(">...")
                        print("You lose gold but gain valuable life experience.")
                        input(">...")
                        print("You gain 60 XP.")
                        if character.gold >= 10:
                            print("You lose 10 gold.")
                        else:
                            print("You lose all your gold.")
                        input(">...")
                        character.xp1 += 60
                        character.gold -= 10
                        if character.gold <= 0:
                            character.gold = 0
                        # character.active_quests.remove({"name": Quest_0.slay_monsters, "test": 5}) - FIX?
                        for i in range(len(character.active_quests)):
                            if character.active_quests[i]["test"] == 5:
                                del character.active_quests[i]
                                break
                        character.completed_quests.append({"name": Quest_0.slay_monsters})
                        character.d3_event_2 = False
                        character.d3_event_3 = True
                        character.d5_event_1 = True
                        character.d5_event_2 = True
                        if character.xp1 >= character.xp2:
                            level(character)
                            input(">...")
        elif character.d3_event_3:
            print(Map.zone_map[character.location][Map.EXAMINE])
            input(">...")
    elif character.location == "d5":
        if character.d5_event_2:
            print("Do you wish to confront the strange man about your stolen gold? Y/N")
            player_input = input("> ")
            if player_input.lower() == "y":
                print("You walk up to the strange man, but he looks angry, seems like the only way to get your gold\n"
                      "back is to fight him.")
                input(">...")
                enemy_gen(character)
            elif player_input.lower() == "n":
                print("You decide to leave the strange man alone as it's not worth the effort to get your gold back.")
        else:
            print(Map.zone_map[character.location][Map.EXAMINE])
            input(">...")
    elif character.location == 'e2':
        print(Map.zone_map[character.location][Map.EXAMINE])
        if character.e2_event_1:
            print("Everyone is gathered around a poster on the wall, do you want to get a closer look? Y/N")
            option = input("> ")
            if option.lower() == "n":
                print("You decide that you're not interested in the poster at the moment.")
                input(">...")
            elif option.lower() == "y":
                print("To the annoyance of others, you push through to see what everyone's looking at. As you quickly\n"
                      "glance at the poster you soon see what all the fuss is about.")
                input(">...")
                os.system('cls')
                wanted_poster()
                print("Do you wish to take on this quest to kill the Baron of Hell and save the Hyfield Village from\n"
                      "utter doom? Y/N")
                option = input("> ")
                if option.lower() == "n":
                    print("This might a dream, with no real consequences, but you've decided you're not prepared for\n"
                          "this quest.")
                    input(">...")
                elif option.lower() == "y":
                    print("Without hesitation or concern for your own life, you accept the quest.\n")
                    print("QUEST ACCEPTED: WANTED: Baron of Hell")
                    character.active_quests.append({"name": Quest_0.baron_of_hell, "test": 0})
                    character.e2_event_1 = False
                    character.e2_event_2 = True
                    input(">...")
            else:
                print("Not a valid input, enter Y or N.")
        elif character.e2_event_2:
            for quest in character.active_quests:
                if "WANTED: Baron of Hell" in quest["name"].name:
                    if quest["test"] <= 0:
                        print("You should return here once you have completed your quest to slay the Baron of Hell.")
                        input(">...")
                    elif quest["test"] == 1:
                        print("You walk up to the head desk in the Town Hall and slam a bloody bag with the Baron of Hell's head\n"
                              "inside.")
                        input(">...")
                        print("The Quest Masters looks as you in shock, he can't quite believe that you managed to kill the\n"
                              "Baron of Hell. He walks over to his chest, unlocks it, and takes out\nthe " + Colours.BOLD + Colours.ORANGE +
                              "[Teleportation Stone]" + Colours.END + " and a bag of gold.")
                        input(">...")
                        print("The quest master congratulates you, and hands you your rewards.")
                        input(">...")
                        print("You gain 500 gold.")
                        print("You gain 200 XP.")
                        print("You obtain " + Colours.BOLD + Colours.ORANGE + "[Teleportation Stone]" + Colours.END + ".")
                        input(">...")
                        character.misc_items.clear()
                        item = {Colours.BOLD + Colours.ORANGE + "[Teleportation Stone]" + Colours.END: 0}
                        character.misc_items.update(item)
                        character.gold += 500
                        character.e2_event_2 = False
                        character.e2_event_3 = True
                        for i in range(len(character.active_quests)):
                            if character.active_quests[i]["test"] == 1:
                                del character.active_quests[i]
                                break
                        character.completed_quests.append({"name": Quest_0.baron_of_hell})
                        character.xp1 += 200
                        if character.xp1 >= character.xp2:
                            level(character)
                            input(">...")
        elif character.e2_event_3:
            print("Nothing left for you to do now, the Baron of Hell will no longer trouble the people of Hyfield\n"
                  "Village thanks to you.")
            input(">...")
    elif character.location == "f5":
        if character.f5_event_1:
            print("You see a bag next to a bush, do you want to take what's inside? Y/N")
            choice = input("> ")
            if choice.lower() == "y":
                print("You walk up to the bag and grab it, but as you do a plank of wood falls from the tree.\n"
                      "Looks like it was booby-trapped.")
                character.f5_event_1 = False
                input(">...")
                print("You lose HP but at least you found x 2 " + Colours.BOLD + Colours.BLUE + "[Health Potion]" + Colours.END + ".")
                d = dict((i['name'], i["quantity"]) for i in character.items)
                if Colours.BOLD + Colours.BLUE + "[Health Potion]" + Colours.END in d:
                    for i in character.items:
                        if i["name"] == Colours.BOLD + Colours.BLUE + "[Health Potion]" + Colours.END:
                            i["quantity"] += 2
                else:
                    character.items.append({'name': Colours.BOLD + Colours.BLUE + "[Health Potion]" + Colours.END,
                                            'property': 150, 'des': "+ 150 HP       ",  'quantity': 2})
                print("+ 2 " + Colours.BOLD + Colours.BLUE + "[Health Potion]" + Colours.END + ".")
                input(">...")
                character.hp -= 50
                if character.base_hp <= 0:
                    end_fight_lose(character, en1)
            elif choice.lower() == "n":
                print("You leave the bag where it is, probably for the best as it might've been booby-trapped.")
                input(">...")
            else:
                print("Not a valid input, enter Y or N.")
        else:
            print(Map.zone_map[character.location][Map.EXAMINE])
            input(">...")
    elif character.location == 'i6':
        if character.i6_event_1:
            print("You see something shiny at the bottom of the river and swim down to pick it up.")
            input(">...")
            character.gold += 30
            print("You gain 30 gold.")
            input(">...")
            character.i6_event_1 = False
        elif not character.b6_event_1:
            print(Map.zone_map[character.location][Map.EXAMINE])
            input(">...")
    elif character.location == 'l5':
        if character.l5_event_1:
            character.l5_event_1 = False
            print("You've found something in the sand.")
            input(">...")
            d = dict((i['name'], i["quantity"]) for i in character.items)
            if Colours.BOLD + Colours.BLUE + "[Health Potion]" + Colours.END in d:
                for i in character.items:
                    if i["name"] == Colours.BOLD + Colours.BLUE + "[Health Potion]" + Colours.END:
                        i["quantity"] += 5
            else:
                character.items.append({'name': Colours.BOLD + Colours.BLUE + "[Health Potion]" + Colours.END,
                                        'property': 150, 'des': "+ 150 HP       ", 'quantity': 1})
            print("+ 5 " + Colours.BOLD + Colours.BLUE + "[Health Potion]" + Colours.END + ".")
            input(">...")
            game_menu(character, en1)
        else:
            print(Map.zone_map[character.location][Map.EXAMINE])
            input(">...")
            encounter = random.randint(1, 10)
            if encounter in range(1, 10):
                enemy_gen(character)
            else:
                game_menu(character, en1)
    elif character.location == 'n6':
        if character.n6_event_2:
            character.n6_event_2 = False
            print(
                "You open the creaky front door of the cabin, explore inside and find a note on the table which reads...")
            input(">...")
            print('''"Good luck hero, there are supplies are under the table."''')
            input(">...")
            print("You look under the table and find a bag full of supplies, this should come in handy.")
            d = dict((i['name'], i["quantity"]) for i in character.items)
            if Colours.BOLD + Colours.PURPLE + "[Max Health Potion]" + Colours.END in d:
                for i in character.items:
                    if i["name"] == Colours.BOLD + Colours.PURPLE + "[Max Health Potion]" + Colours.END:
                        i["quantity"] += 2
            else:
                character.items.append({'name': Colours.BOLD + Colours.PURPLE + "[Max Health Potion]" + Colours.END,
                                        'property': 100000, 'des': "+ MAX HP   ", 'quantity': 2})
            print("+ 2 " + Colours.BOLD + Colours.PURPLE + "[Max Health Potion]" + Colours.END)
            input(">...")
        else:
            print(Map.zone_map[character.location][Map.EXAMINE])
            input(">...")
            encounter = random.randint(1, 10)
            if encounter in range(1, 10):
                enemy_gen(character)
            else:
                game_menu(character, en1)
    elif character.location in ["c7", "c5", "c6", "d6", "d7", "d8", "e5", "e6", "e7", "f5", "h6", "j6", "k5", "k7", "l6",
                                "m6", "m7", "o8", "o9", "o10", "p10"]:
        print(Map.zone_map[character.location][Map.EXAMINE])
        input(">...")
        encounter = random.randint(1, 10)
        if encounter in range(1, 10):
            enemy_gen(character)
        else:
            game_menu(character, en1)
    elif character.location == 'r10':
        print(Map.zone_map[character.location][Map.EXAMINE])
        input(">...")
        enemy_gen(character)
    game_menu(character, en1)
