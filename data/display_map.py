from data.art import Colours


def print_map_town(character):
    print(Colours.BOLD + "Minimap\n" + Colours.END)
    location = Colours.GREEN + "@" + Colours.END
    home = Colours.GREEN + "▀" + Colours.END
    store = Colours.WHITE + "▀" + Colours.END
    hall = Colours.BROWN + "▀" + Colours.END
    street = Colours.WHITE + "=" + Colours.END
    forest = Colours.GREEN2 + "♣" + Colours.END
    water = Colours.BLUE + "~" + Colours.END
    desert = Colours.YELLOW + "░" + Colours.END
    cave = Colours.BROWN + "▀" + Colours.END
    boss = Colours.RED + "@" + Colours.END
    if character.location in ["c2", "d1", "d2", "d3", "e2"]:
        print("    B   C   D   E   F  ")
        print("  ---------------------")
        if character.location == 'd1':
            print("1 |   |   | " + location + " |   |   |")
        else:
            print("1 |   |   | " + home + " |   |   |")
        print("  ---------------------")
        if character.location == 'c2':
            print("2 |   | " + location + " | " + street + " | " + hall + " |   |")
        elif character.location == 'd2':
            print("2 |   | " + store + " | " + location + " | " + hall + " |   |")
        elif character.location == "e2":
            print("2 |   | " + store + " | " + street + " | " + location + " |   |")
        else:
            print("2 |   | " + store + " | " + street + " | " + hall + " |   |")
        print("  ---------------------")
        if character.location == 'd3':
            print("3 |   |   | " + location + " |   |   |")
        else:
            print("3 |   |   | " + street + " |   |   |")
        print("  ---------------------")
    if character.location in ["b6", "c5", "c6", "c7", "d4", "d5", "d6", "d7", "d8", "e5", "e6", "e7", "f5", "f6"]:
        print("    A   B   C   D   E   F   G  ")
        print("  -----------------------------")
        if character.location == "d4":
            print("4 |   |   |   | " + location + " |   |   |   |")
        else:
            print("4 |   |   |   | " + forest + " |   |   |   |")
        print("  -----------------------------")
        if character.location == "c5":
            print("5 |   |   | " + location + " | " + forest + " | " + forest + " | " + forest + " |   |")
        elif character.location == "d5":
            print("5 |   |   | " + forest + " | " + location + " | " + forest + " | " + forest + " |   |")
        elif character.location == "e5":
            print("5 |   |   | " + forest + " | " + forest + " | " + location + " | " + forest + " |   |")
        elif character.location == "f5":
            print("5 |   |   | " + forest + " | " + forest + " | " + forest + " | " + location + " |   |")
        else:
            print("5 |   |   | " + forest + " | " + forest + " | " + forest + " | " + forest + " |   |")
        print("  -----------------------------")
        if character.location == "b6":
            print("6 |   | " + location + " | " + forest + " | " + forest + " | " + forest + " | " + forest + " |   |")
        elif character.location == "c6":
            print("6 |   | " + forest + " | " + location + " | " + forest + " | " + forest + " | " + forest + " |   |")
        elif character.location == "d6":
            print("6 |   | " + forest + " | " + forest + " | " + location + " | " + forest + " | " + forest + " |   |")
        elif character.location == "e6":
            print("6 |   | " + forest + " | " + forest + " | " + forest + " | " + location + " | " + forest + " |   |")
        elif character.location == "f6":
            print("6 |   | " + forest + " | " + forest + " | " + forest + " | " + forest + " | " + location + " |   |")
        else:
            print("6 |   | " + forest + " | " + forest + " | " + forest + " | " + forest + " | " + forest + " |   |")
        print("  -----------------------------")
        if character.location == "c7":
            print("7 |   |   | " + location + " | " + forest + " | " + forest + " |   |   |")
        elif character.location == "d7":
            print("7 |   |   | " + forest + " | " + location + " | " + forest + " |   |   |")
        elif character.location == "e7":
            print("7 |   |   | " + forest + " | " + forest + " | " + location + " |   |   |")
        else:
            print("7 |   |   | " + forest + " | " + forest + " | " + forest + " |   |   |")
        print("  -----------------------------")
        if character.location == "d8":
            print("8 |   |   |   | " + location + " |   |   |   |")
        else:
            print("8 |   |   |   | " + forest + " |   |   |   |")
        print("  -----------------------------")
    if character.location in ["g6", "h6", "i6", "j6"]:
        print("    F   G   H   I   J   K")
        print("  -------------------------")
        if character.location == "g6":
            print("6 |   | " + location + " | " + water + " | " + water + " | " + water + " |   |")
        elif character.location == "h6":
            print("6 |   | " + water + " | " + location + " | " + water + " | " + water + " |   |")
        elif character.location == "i6":
            print("6 |   | " + water + " | " + water + " | " + location + " | " + water + " |   |")
        elif character.location == "j6":
            print("6 |   | " + water + " | " + water + " | " + water + " | " + location + " |   |")
        print("  -------------------------")
    if character.location in ["k5", "k6", "k7", "l5", "l6", "m6", "m7", "n6", "n7"]:
        print("    J   K   L   M   N   O")
        print("  -------------------------")
        if character.location == "k5":
            print("5 |   | " + location + " | " + desert + " |   |   |   |")
        elif character.location == "l5":
            print("5 |   | " + desert + " | " + location + " |   |   |   |")
        else:
            print("5 |   | " + desert + " | " + desert + " |   |   |   |")
        print("  -------------------------")
        if character.location == "k6":
            print("6 |   | " + location + " | " + desert + " | " + desert + " | " + desert + " |   |")
        elif character.location == "l6":
            print("6 |   | " + desert + " | " + location + " | " + desert + " | " + desert + " |   |")
        elif character.location == "m6":
            print("6 |   | " + desert + " | " + desert + " | " + location + " | " + desert + " |   |")
        elif character.location == "n6":
            print("6 |   | " + desert + " | " + desert + " | " + desert + " | " + location + " |   |")
        else:
            print("6 |   | " + desert + " | " + desert + " | " + desert + " | " + desert + " |   |")
        print("  -------------------------")
        if character.location == "k7":
            print("7 |   | " + location + " |   | " + desert + " | " + desert + " |   |")
        elif character.location == "m7":
            print("7 |   | " + desert + " |   | " + location + " | " + desert + " |   |")
        elif character.location == "n7":
            print("7 |   | " + desert + " |   | " + desert + " | " + location + " |   |")
        else:
            print("7 |   | " + desert + " |   | " + desert + " | " + desert + " |   |")
        print("  -------------------------")
    if character.location in ["o7", "o8", "o9", "o10", "p10", "q10", "r10"]:
        print("    N   O   P   Q   R   S")
        print("  -------------------------")
        if character.location == "o7":
            print("7 |   | " + location + " |   |   |   |   |")
        else:
            print("7 |   | " + cave + " |   |   |   |   |")
        print("  -------------------------")
        if character.location == "o8":
            print("8 |   | " + location + " |   |   |   |   |")
        else:
            print("8 |   | " + cave + " |   |   |   |   |")
        print("  -------------------------")
        if character.location == "o9":
            print("9 |   | " + location + " |   |   |   |   |")
        else:
            print("9 |   | " + cave + " |   |   |   |   |")
        print("  -------------------------")
        if character.location == "o10":
            print("10|   | " + location + " | " + cave + " | " + cave + " | " + boss + " |   |")
        elif character.location == "p10":
            print("10|   | " + cave + " | " + location + " | " + cave + " | " + boss + " |   |")
        elif character.location == "q10":
            print("10|   | " + cave + " | " + cave + " | " + location + " | " + boss + " |   |")
        elif character.location == "r10":
            print("10|   | " + cave + " | " + cave + " | " + cave + " | " + location + " |   |")
        else:
            print("10|   | " + cave + " | " + cave + " | " + cave + " | " + boss + " |   |")
        print("  -------------------------")




