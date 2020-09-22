import random


# generates a random enemy from a txt file.
class Mobs:
    def enemy_gen(self, character):
        if character.location in ["b6", "c5", "c6", "c7", "d4", "d5", "d6", "d7", "d8", "e5", "e6", "e7", "f5", "f6",
                                  "g6", "h6", "i6", "j6", "k5", "k6", "k7", "l5", "l6", "m6", "m7", "n6", "n7", "o7",
                                  "o8", "o9", "o10", "p10", "q10", "r10"]:
            chance = random.randint(1, 101)
            if chance in range(96, 101):
                name = "Alien"
                hp = 100
                atk = 10
                defence = 10

                return Enemy(hp, atk, defence, name, - 0, + 0)
            else:
                if character.location in ["b6", "c5", "c6", "c7", "d4", "d5", "d6", "d7", "d8", "e5", "e6", "e7", "f5", "f6"]:
                    if character.d5_event_2:
                        name = "Strange Man"
                        hp = 10
                        atk = 0
                        defence = 0
                        character.d5_event_2 = False
                    else:

                        file = open("mobs/forest_mobs.txt", "r")
                        lines = file.readlines()

                        name = lines[random.randint(0, len(lines) - 1)][:-1]
                        file.close()

                        hp = random.randint(80, 110)  # 70, 100
                        atk = random.randint(10, 20)  # 15, 25
                        defence = random.randint(6, 11)  # 5, 10

                    # from enemy class
                    return Enemy(hp, atk, defence, name, - 0, + 0)  # 10, 10
                elif character.location in ["g6", "h6", "i6", "j6"]:
                    file = open("mobs/water_mobs.txt", "r")
                    lines = file.readlines()

                    name = lines[random.randint(0, len(lines) - 1)][:-1]
                    file.close()

                    hp = random.randint(140, 170)  # 110, 140
                    atk = random.randint(40, 50)  # 30, 40
                    defence = random.randint(12, 15)  # 8, 13

                    return Enemy(hp, atk, defence, name, - 6, + 6)  # 10, 10
                elif character.location in ["k5", "k6", "k7", "l5", "l6", "m6", "m7", "n6", "n7"]:
                    file = open("mobs/desert_mobs.txt", "r")
                    lines = file.readlines()

                    name = lines[random.randint(0, len(lines) - 1)][:-1]
                    file.close()

                    hp = random.randint(180, 210)  # 150, 170
                    atk = random.randint(50, 60)  # 45, 55
                    defence = random.randint(15, 18)  # 12, 16

                    return Enemy(hp, atk, defence, name, - 10, + 10)  # 15, 15
                elif character.location in ["o7", "o8", "o9", "o10", "p10", "q10"]:
                    file = open("mobs/cave_mobs.txt", "r")
                    lines = file.readlines()

                    name = lines[random.randint(0, len(lines) - 1)][:-1]
                    file.close()

                    hp = random.randint(220, 250)  # 170, 200
                    atk = random.randint(60, 70)  # 55, 65
                    defence = random.randint(17, 20)  # 14, 17

                    return Enemy(hp, atk, defence, name, - 12, + 15)  # 10, 20
                elif character.location in ["r10"]:

                    name = "Baron of Hell"
                    hp = 750  # 450
                    atk = 35  # 60
                    defence = 25  # 30

                    return Enemy(hp, atk, defence, name, - 10, + 10)  # 30, 30


# enemy class
class Enemy:
    def __init__(self, hp, atk, defence, name, atk_l, atk_h):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.atk = atk
        self.atk_l = atk_l
        self.atk_h = atk_h
        self.defence = defence


