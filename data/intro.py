import os
import winsound
from data.full_screen import maximize_console
from data.menu import game_menu
from data.player import Player
from data.level import Attributes
from data.text import typewriter
from data.art import cut_scene_art


# game intro with character creation to assign base stats and name with the player class variable character
def intro(en1):
    maximize_console()
    winsound.PlaySound("music\\story_intro.wav", winsound.SND_ASYNC + winsound.SND_LOOP)
    os.system("cls")
    print(cut_scene_art.sleeping)
    typewriter(
        "It's 3am, the night is young, you're up late again playing your favourite RPG game - Skyrim.\n"
        "You drift off to sleep in front of your computer, dreaming of what it would be like to live in\n"
        "a world just like that, where you can fight Mudcrabs and shout at Dragons.\n")
    input(">...")
    os.system("cls")
    print(cut_scene_art.bedroom)
    typewriter(
        "The next morning you wake from your chair but nothing in your room is the same, your computer is gone,\n"
        "along with all of your other possessions.\n")
    input(">...")
    os.system("cls")
    print(cut_scene_art.bedroom)
    typewriter("Suddenly you hear a voice coming from behind you.\n")
    input(">...")
    os.system("cls")
    print(cut_scene_art.bedroom)
    typewriter('''“Hey, you. You're finally awake.”\n''')
    input(">...")
    os.system("cls")
    print(cut_scene_art.bedroom)
    typewriter("You quickly spin around, but there's nobody there. It must have just been your imagination.\n")
    input(">...")
    os.system("cls")
    print(cut_scene_art.village)
    typewriter("You walk over to your window to check what's outside, and you see this beautiful village,\n"
               "just like the one you dreamed of.\n")
    input(">...")
    os.system("cls")
    print(cut_scene_art.village)
    typewriter(
        "Then it hits you, suddenly you realise you are in the village you dreamed of, whether it's still a dream\n"
        "or not you are unsure of, but one thing is for certain, you have decided that you are going to be the hero\n"
        "that this village may, or may not need!\n")
    input(">...")
    os.system("cls")
    print(cut_scene_art.village)
    typewriter(
        "Though you think to yourself, if you're going to be a hero, you will need a name worthy to be one that\n"
        "people can write stories about and sing songs in your name.\n")
    input(">...\n")
    player_name = input("Enter Name: ")
    typewriter("\nGood! " + player_name + " is a great name.\n")
    input(">...\n")
    typewriter("So, " + player_name + ", it's now time to venture outside and conquer whatever challenges you\n"
                                      "may face in your adventures.\n")
    # hp 250, atk 15, defence, name, atk_l, atk_h, b_atk_p, m_atk_p, bleed_dot_count, bleed_dot_dmg, burn_dot_count, burn_dot_dmg, gold, level, xp1, xp2, str
    character = Player(250, 15, 0, player_name, - 5, + 5, 0, 100, 0, 0, 0, 0, 0, Attributes.char["xp"],
                       Attributes.char["level_up"], Attributes.char["level"], Attributes.stats["str"])
    input(">...")
    game_menu(character, en1)
