import os
from data.art import Colours


class Quests_2:
    def __init__(self, name, description, requirement1, requirement2):
        self.name = name
        self.description = description
        self.requirement1 = requirement1
        self.requirement2 = requirement2


class Quest_0:
    baron_of_hell = Quests_2("WANTED: Baron of Hell",
                             "Your objective is to travel to the far edge of the small world\n"
                             "to find and kill the Baron of Hell.\nOnce killed, return to the Hyfield Town "
                             "Hall with his head to receive your rewards.", 0, "/ 1 [Item] Obtained.")
    slay_monsters = Quests_2("Generic RPG Kill Quest",
                             "Your objective here is to kill 5 bears, the strange man must hate bears.\nReturn to the "
                             "strange man once you have done so.", 0, "/ 5 Bears Killed.")


def quests(character, en1):
    from data.menu import game_menu
    os.system("cls")
    print("Select an Option:")
    print("1.) Spell Information")
    print("2.) Quest Log")
    option = input("> ")
    if option == "1":
        spell_info(character, en1)
    elif option == "2":
        quest_log(character, en1)
    else:
        game_menu(character, en1)


def spell_info(character, en1):
    os.system("cls")
    print(Colours.BOLD + "Character Abilities\n" + Colours.END)
    print(Colours.BOLD + "[Strike]" + Colours.END + ": This ability is your basic melee attack that generates 10 to 20 attack power. The attack range is\n"
          "your current attack power - your hidden attack low stat and your current attack power + your hidden\n"
          "attack high stat. {}/{}\n"
          .format(character.current_atk + character.atk_l,
                  character.current_atk + character.atk_h))
    print(Colours.BOLD + "[Great Strike]" + Colours.END + ": This ability deals a great blow to your opponent which costs 40 attack power to use. The attack\n"
          "range is your current attack + the base damage of [Great Strike] (40) - your hidden attack\n"
          "low stat and your current attack + the base damage of [Great Strike] (40) + your current attack high stat. {}/{}\n"
          .format(character.current_atk + 50 + character.atk_l,
                  character.current_atk + 50 + character.atk_h))
    print(Colours.BOLD + "[Bleed]" + Colours.END + ": This ability causes your opponent to bleed for 5 attack turns and costs 20 attack power. The attack range\n"
          "is your current attack / 2 - your hidden attack low stat and your current attack / 2 + your hidden\n"
          "attack high stat. {}/{}\n"
          .format(character.current_atk // 2 + 5 + character.atk_l,
                  character.current_atk // 2 + 5 + character.atk_h))
    print(Colours.BOLD + "[Regenerate]" + Colours.END + ": This ability allows you to heal with a cost of 30 attack power. The heal range is\n"
          "your current attack + the base heal of [Regenerate] (50) - your hidden attack low stat and your current attack +\n"
          "the base heal of [Regenerate] (50) + your hidden attack high stat. {}/{}"
          .format(character.current_atk + 50 + character.atk_l,
                  character.current_atk + 50 + character.atk_h))
    input(">...")
    quests(character, en1)


def quest_log(character, en1):
    os.system("cls")
    i = 1
    print(Colours.BOLD + "Quests\n" + Colours.END)
    print("ACTIVE QUESTS:")
    for quest in character.active_quests:
        print(str(i) + ".)", Colours.YELLOW2 + quest["name"].name + Colours.END)
        i += 1
    print("\nCOMPLETE QUESTS:")
    for quest in character.completed_quests:
        print("# " + Colours.GREEN3 + quest["name"].name + Colours.END)
    else:
        try:
            item_choice = int(input("\n> ")) - 1
        except ValueError:
            print("Input must be a number.")
        else:
            if 0 <= item_choice < i - 1:
                print(character.active_quests[item_choice]["name"].description,
                      character.active_quests[item_choice]["name"].requirement1,
                      character.active_quests[item_choice]["name"].requirement2)
            else:
                print("That number is out of range.")
    input(">...")
    quests(character, en1)


def quest_tracker(character, en1):
    for quest in character.active_quests:
        if "Generic RPG Kill Quest" in quest["name"].name:
            if en1.name == "Bear":
                quest["name"].requirement1 += 1
                quest["test"] += 1
                if quest["test"] >= 5:
                    quest["test"] = 5
                if quest["name"].requirement1 >= 5:
                    quest["name"].requirement1 = 5
        if "WANTED: Baron of Hell" in quest["name"].name:
            if en1.name == "Baron of Hell":
                quest["name"].requirement1 += 1
                quest["test"] += 1
                if quest["test"] >= 1:
                    quest["test"] = 1
                if quest["name"].requirement1 >= 1:
                    quest["name"].requirement1 = 1
