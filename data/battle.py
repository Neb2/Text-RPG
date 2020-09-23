import os
import random
import sys
from data.player import Spells
from data.level import level
from data.quests import quest_tracker
from data.enemies import Enemy, Mobs
from data.music import fight_music, win_music, defeat_music
from data.loot import loot1, loot2, loot3, loot4, baron_loot, alien_loot
from data.art import F_Mobs, W_Mobs, D_Mobs, C_Mobs, Colours, player_health_bar, enemy_health_bar, player_attack_bar, easter_egg_mob

sys.setrecursionlimit(10**6)  # test

# character spells
great_strike = Spells("Great Strike", 40, 50)
bleed = Spells("Bleed", 20, 5)
regen = Spells("Regenerate", 50, 50)

# enemy spells
heal = Spells("Heal", 0, 80)
burn = Spells("Burn", 0, 40)


def enemy_gen(character):
    character.battle_music_1 = True
    en1 = Mobs.enemy_gen(Enemy, character)
    if en1.name == "Baron of Hell":
        print("You have encountered the {}.".format(en1.name))
    elif en1.name == "Alien":
        print("You have encountered an Alien, he must be in the wrong game...")
    else:
        print("You have encountered a {}.".format(en1.name))
    enemy_print(en1, character)
    input(">...")
    fight(character, en1)


def enemy_print(en1, character):
    if en1.name == "Giant Frog":
        print(F_Mobs.frog)
    elif en1.name == "Spider":
        print(F_Mobs.spider)
    elif en1.name == "Bear":
        print(F_Mobs.bear)
    elif en1.name == "Goblin":
        print(F_Mobs.goblin)
    elif en1.name == "Strange Man":
        print(F_Mobs.strange_man)
    elif en1.name == "Shark":
        print(W_Mobs.shark)
    elif en1.name == "Giant Blowfish":
        print(W_Mobs.blowfish)
    elif en1.name == "Octopus":
        print(W_Mobs.octopus)
    elif en1.name == "Scorpion":
        print(D_Mobs.scorpion)
    elif en1.name == "Lizard":
        print(D_Mobs.lizard)
    elif en1.name == "Snake":
        print(D_Mobs.snake)
    elif en1.name == "Sand Crab":
        print(D_Mobs.sand_crab)
    elif en1.name == "Dragon":
        print(C_Mobs.dragon)
    elif en1.name == "Demon":
        print(C_Mobs.demon)
    elif en1.name == "Baron of Hell":
        print(C_Mobs.baron_of_hell)
    elif en1.name == "Alien":
        easter_egg_mob()
    fight_music(character, en1)


def fight(character, en1):
    os.system("cls")
    enemy_print(en1, character)
    print(Colours.BOLD + en1.name + Colours.END)
    print("HP: {}/{}".format(en1.hp, en1.max_hp))
    enemy_health_bar(en1)
    print("Attack: {} | Defence: {}\n".format(en1.atk, en1.defence))
    print(Colours.BOLD + character.name + Colours.END)
    print("HP: {}/{}".format(character.base_hp, character.hp_max))
    player_health_bar(character)
    print("Attack Power: {}/{}".format(character.b_atk_p, character.m_atk_p))
    player_attack_bar(character)
    print("Attack: {} | Defence: {}\n".format(character.current_atk, character.current_defence))
    print("1.) Attack")
    print("2.) Run\n")
    option = input("> ")
    if option == "1":
        spell_choice(character, en1)
    if option == "2":
        run(character, en1)
    else:
        fight(character, en1)


def run(character, en1):
    from data.menu import game_menu
    run_chance = random.randint(1, 10)
    if character.location == "d4":
        if character.d4_event_1:
            print("You can't run!")
            input(">...")
    if character.location == "f6":
        if character.f6_event_2:
            print("You can't run!")
            input(">...")
    if character.location == "g6":
        if character.g6_event_2:
            print("You can't run!")
            input(">...")
    if character.location == "k6":
        if character.k6_event_2:
            print("You can't run!")
            input(">...")
    if character.location == "o7":
        if character.o7_event_2:
            print("You can't run!")
            input(">...")
    if character.location == "q10":
        if character.q10_event_1:
            print("You can't run!")
            input(">...")
    if en1.name == "Baron of Hell":
        print("You can't run from the Baron of Hell!")
        input(">...")
    if character.location not in ["d4", "f6", "g6", "k6", "o7", "q10", "r10"]:
        if run_chance >= 6:
            print("You ran away successfully.")
            input(">...")
            character.town_zone = True
            character.forest_zone = True
            character.water_zone = True
            character.desert_zone = True
            character.dungeon_zone = True
            game_menu(character, en1)
        else:
            print("You tried to run away but were hit by {}.".format(en1.name))
            input(">...")
    character.player_atk_turn = False
    if not character.player_atk_turn:
        if en1.name == "Baron of Hell":
            baron_of_hell_atk(character, en1)
        else:
            enemy_atk(character, en1)


def spell_choice(character, en1):
    character.player_atk_turn = True
    print("Select Spell\n")
    print("1.) [Strike]       ({} - {}) DMG [Generates 10 - 20 Atk Power]".format(character.current_atk + character.atk_l,
                                                                                  character.current_atk + character.atk_h))
    print("2.) [Great Strike] ({} - {}) DMG [Cost 40]".format(character.current_atk + great_strike.dmg + character.atk_l,
                                                              character.current_atk + great_strike.dmg + character.atk_h))
    print("3.) [Bleed]        ({} - {}) DMG [Cost 20] - [DoT for 5 Turns]".format(character.current_atk // 2 + bleed.dmg + character.atk_l,
                                                                                  character.current_atk // 2 + bleed.dmg + character.atk_h))
    print("4.) [Regenerate]   ({} - {}) HP  [Cost 50]".format(character.current_atk + regen.dmg + character.atk_l,
                                                              character.current_atk + regen.dmg + character.atk_h))
    option = input("> ")
    if option == "1":
        character_range = random.randint(character.atk_l, character.atk_h)
        character_attack = character_range + character.current_atk
        if character_attack < en1.defence:
            print("The enemy is too strong for you and blocked all your damage.\n")
            character.player_atk_turn = False
        else:
            en1.hp -= character_attack - en1.defence
            print("Your [Strike] attack hits for {} damage.".format(character_attack - en1.defence))
            character.player_atk_turn = False
            character.b_atk_p += random.randint(15, 25)
            if character.b_atk_p >= character.m_atk_p:
                character.b_atk_p = character.m_atk_p
        input(">...")
    elif option == "2":
        if character.b_atk_p >= great_strike.cost:
            character.b_atk_p -= great_strike.cost
            character_range = random.randint(character.atk_l, character.atk_h)
            character_attack = character_range + character.current_atk + great_strike.dmg
            if character_attack < en1.defence:
                print("The enemy is too strong for you and blocked all your damage.\n")
                character.player_atk_turn = False
            else:
                en1.hp -= character_attack - en1.defence
                print("Your [Great Strike] attack hits for {} damage.".format(character_attack - en1.defence))
                character.player_atk_turn = False
            input(">...")
        else:
            print("You don't have enough Attack Power for that spell.")
            input(">...")
            fight(character, en1)
    elif option == "3":
        if character.b_atk_p >= bleed.cost:
            character.b_atk_p -= bleed.cost
            character_range = random.randint(character.atk_l, character.atk_h)
            character_attack = character.current_atk // 2
            character.bleed_dot_dmg = character_range + bleed.dmg + character_attack
            en1.hp -= character.bleed_dot_dmg
            character.bleed_dot_count = 0
            character.bleed_check = True
        else:
            print("You don't have enough Attack Power for that spell.")
            input(">...")
            fight(character, en1)
        # input(">...")
    elif option == "4":
        if character.b_atk_p >= regen.cost:
            character.b_atk_p -= regen.cost
            character_range = random.randint(character.atk_l, character.atk_h)
            character_heal = character_range + regen.dmg + character.current_atk
            if character_heal + character.hp >= character.max_hp:
                print("Your [Regenerate] heals for {} HP.".format(character.max_hp - character.hp))
                character.hp += character_heal
                character.hp = character.max_hp
                character.player_atk_turn = False
            else:
                print("You [Regenerate] heals for {} HP.".format(character_heal))
                character.hp += character_heal
                character.player_atk_turn = False
        else:
            print("You don't have enough Attack Power for that spell.")
            input(">...")
            fight(character, en1)
        input(">...")
    else:
        fight(character, en1)
    if character.bleed_check:
        bleed_check(character, en1)
    if en1.hp <= 0:
        end_fight_win(character, en1)
        character.win_music_1 = True
    if character.bleed_check:
        bleed_check(character, en1)
    if not character.player_atk_turn:
        if en1.name == "Baron of Hell":
            baron_of_hell_atk(character, en1)
        else:
            enemy_atk(character, en1)
    os.system("cls")


def enemy_atk(character, en1):
    enemy_range = random.randint(en1.atk_l, en1.atk_h)
    enemy_attack = enemy_range + en1.atk
    print("{} uses [Melee] for {} damage.".format(en1.name, enemy_attack - character.current_defence))
    if enemy_attack < character.current_defence:
        print("You blocked all of the damage.\n")
    else:
        character.hp -= enemy_attack - character.current_defence
        input(">...")
    if character.base_hp <= 0:
        end_fight_lose(character, en1)
    fight(character, en1)


def baron_of_hell_atk(character, en1):
    if not character.burn_check:
        print("{} uses [Burn].".format(en1.name))
        input(">...")
        enemy_range = random.randint(en1.atk_l, en1.atk_h)
        character.burn_dot_dmg = enemy_range + burn.dmg
        character.hp -= character.burn_dot_dmg
        character.burn_dot_count = 0
        character.burn_check = True
    elif en1.hp <= 200:
        chance = random.randint(1, 6)
        if chance <= 3:
            heal_range = random.randint(en1.atk_l, en1.atk_h)
            enemy_heal = heal_range + heal.dmg
            print("{} uses [Heal] for {} HP.".format(en1.name, enemy_heal))
            en1.hp += enemy_heal
            input(">...")
        elif chance > 3:
            enemy_range = random.randint(en1.atk_l, en1.atk_h)
            enemy_attack = enemy_range + en1.atk
            print("{} uses [Melee] for {} damage.".format(en1.name, enemy_attack - character.current_defence))
            character.hp -= enemy_attack - character.current_defence
            input(">...")
    else:
        enemy_range = random.randint(en1.atk_l, en1.atk_h)
        enemy_attack = enemy_range + en1.atk
        print("{} uses [Melee] for {} damage.".format(en1.name, enemy_attack - character.current_defence))
        character.hp -= enemy_attack - character.current_defence
        input(">...")
    if character.base_hp <= 0:
        end_fight_lose(character, en1)
    burn_check(character, en1)


def end_fight_win(character, en1):
    from data.menu import game_menu
    from data.events import event_check
    os.system("cls")
    event_check(character)
    win_music(character)
    print("You defeated {}.\n".format(en1.name))
    en1.hp = en1.max_hp
    if en1.name in ["Strange Man"]:
        input(">...")
        print("You murder the strange man, search his corpse, and find ....5 gold.")
        input(">...")
        character.gold += 5
    if en1.name in ["Spider", "Bear", "Giant Frog", "Goblin"]:
        if character.d4_event_2:
            print(en1.name + " dropped x 5 " + Colours.BOLD + Colours.GREEN + "[Light Health Potion]" + Colours.END + ".")
            print("+ 5 " + Colours.BOLD + Colours.GREEN + "[Light Health Potion]" + Colours.END + ".\n")
            character.items.append({'name': Colours.BOLD + Colours.GREEN + "[Light Health Potion]" + Colours.END,
                                    'property': 50, 'des': "+ 50 HP  ", 'quantity': 5})
            character.d4_event_2 = False
        if character.level == 10:
            character.xp1 += 0
        else:
            character.xp1 += 5
            print("You gained 5 XP.")
        if character.xp1 >= character.xp2:
            level(character)
        loot1(character, en1)
    elif en1.name in ["Shark", "Octopus", "Giant Blowfish"]:
        if character.level == 10:
            character.xp1 += 0
        else:
            character.xp1 += 10
            print("You gained 10 XP.")
        if character.xp1 >= character.xp2:
            level(character)
        loot2(character, en1)
    elif en1.name in ["Scorpion", "Lizard", "Snake", "Sand Crab"]:
        if character.level == 10:
            character.xp1 += 0
        else:
            character.xp1 += 20
            print("You gained 20 XP.")
        if character.xp1 >= character.xp2:
            level(character)
        loot3(character, en1)
    elif en1.name in ["Dragon", "Demon"]:
        if character.level == 10:
            character.xp1 += 0
        else:
            character.xp1 += 30
            print("You gained 30 XP.")
        if character.xp1 >= character.xp2:
            level(character)
        loot4(character, en1)
    elif en1.name in ["Alien"]:
        if character.level == 10:
            character.xp1 += 0
        else:
            character.xp1 += 50
            print("You gained 50 XP.")
        if character.xp1 >= character.xp2:
            level(character)
        alien_loot(character, en1)
    elif en1.name in ["Baron of Hell"]:
        if character.level == 10:
            character.xp1 += 0
        else:
            character.xp1 += 50
            print("You gained 50 XP.")
        if character.xp1 >= character.xp2:
            level(character)
        baron_loot(character, en1)
    quest_tracker(character, en1)
    game_menu(character, en1)


def end_fight_lose(character, en1):
    from data.menu import game_menu
    os.system("cls")
    defeat_music(character)
    character.hp = character.max_hp
    en1.hp = en1.max_hp
    character.location = "d1"
    print("You died!")
    if character.gold <= 20:
        print("You've lost {} gold.".format(character.gold))
        character.gold -= 20
        character.gold = 0
    else:
        print("You've lost 20 gold.")
        character.gold -= 20
    input(">...")
    game_menu(character, en1)


def bleed_check(character, en1):
    character.bleed_dot_count += 1
    if character.bleed_dot_count >= 2:
        en1.hp -= character.bleed_dot_dmg
    print("Your [Bleed] does {} DMG.".format(character.bleed_dot_dmg))
    input(">...")
    if en1.hp <= 0:
        character.win_music_1 = True
        end_fight_win(character, en1)
    if character.bleed_dot_count == 5:
        character.bleed_check = False
        character.bleed_dot_count = 0
    if en1.name == "Baron of Hell":
        baron_of_hell_atk(character, en1)
    else:
        enemy_atk(character, en1)


def burn_check(character, en1):
    character.burn_dot_count += 1
    if character.burn_dot_count >= 2:
        character.hp -= character.burn_dot_dmg
    print("[Burn] does {} DMG.".format(character.burn_dot_dmg))
    input(">...")
    if character.base_hp <= 0:
        end_fight_lose(character, en1)
    if character.burn_dot_count == 5:
        character.burn_check = False
        character.burn_dot_count = 0
    fight(character, en1)
