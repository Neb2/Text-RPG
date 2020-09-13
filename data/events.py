import sys
from data.battle import enemy_gen

sys.setrecursionlimit(10**6)  # test


def events(character):
    if character.location == "d3":
        if character.d3_event_4:
            print("In the distance you see a man sitting down in the grass staring at you, maybe you should\n"
                  "go talk to him.")
            input(">...")
            event_check(character)
    if character.location == "d4":
        if character.d4_event_1:
            print("As you enter the forest, you feel as if you are being watched by something.")
            input(">...")
            enemy_gen(character)
    if character.location == "f6":
        if character.f6_event_2:
            print("As you walk towards the river you hear something run up from behind you.")
            input(">...")
            enemy_gen(character)
    if character.location == "g6":
        if character.g6_event_2:
            print("You start to swim across the river, but suddenly feel your leg being pulled from beneath you.")
            input(">...")
            enemy_gen(character)
    if character.location == "k6":
        if character.k6_event_2:
            print("You arrive onto dry land again, but it's not long before you are interrupted again.")
            input(">...")
            enemy_gen(character)
    if character.location == "o7":
        if character.o7_event_2:
            print("You find a torch on the wall and decide to light it so you can see what's in the dungeon, but now what's\n"
                  "in the dungeon can see you as well!")
            input(">...")
            enemy_gen(character)
    if character.location == "q10":
        if character.q10_event_1:
            print("Close to the end now, you prepare yourself for your battle against the Baron of Hell, but you are\n"
                  "ambushed when doing so.")
            input(">...")
            enemy_gen(character)
    # if character.location == "d7":
    #     if character.d7_event_1:
    #         print("testtesttest")
    #         input(">...")
    #         event_check(character)


def event_check(character):
    if character.location == "d3":
        if character.d3_event_4:
            character.d3_event_4 = False
    if character.location == "d4":
        if character.d4_event_1:
            character.d4_event_1 = False
    if character.location == "f6":
        if character.f6_event_2:
            character.f6_event_2 = False
    if character.location == "g6":
        if character.g6_event_2:
            character.g6_event_2 = False
    if character.location == "k6":
        if character.k6_event_2:
            character.k6_event_2 = False
    if character.location == "o7":
        if character.o7_event_2:
            character.o7_event_2 = False
    if character.location == "q10":
        if character.q10_event_1:
            character.q10_event_1 = False
    # if character.location == "d7":
    #     if character.d7_event_1:
    #         character.d7_event_1 = False
