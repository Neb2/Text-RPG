# character stats
class Attributes:
    char = {"level": 1,
            "xp": 0,
            "level_up": 30}

    stats = {"str": 1}


def level(character):
    player_str = 0

    while character.xp1 >= character.xp2:
        character.level += 1
        character.xp1 = character.xp1 - character.xp2
        character.xp2 = round(character.xp2 * 1.5)
        player_str += 1
        character.strength += player_str

    if character.level == 2:
        print("You've reached level 2!\nYour HP has been restored.\n+ 2 ATK\n+ 4 HP")
        character.base_atk += 2
        character.hp += 4
        character.max_hp += 4
        character.hp = character.max_hp
        # - 10, + 12
        character.atk_h += 2
    elif character.level == 3:
        print("You've reached level 3!\nYour HP has been restored.\n+ 2 ATK\n+ 4 HP")
        character.base_atk += 2
        character.hp += 4
        character.max_hp += 4
        character.hp = character.max_hp
        # - 12, + 14
        character.atk_h += 2
        character.atk_l += 2
    elif character.level == 4:
        print("You've reached level 4!\nYour HP has been restored.\n+ 3 ATK\n+ 5 HP")
        character.base_atk += 3
        character.hp += 5
        character.max_hp += 5
        character.hp = character.max_hp
        # -12, + 16
        character.atk_h += 2
    elif character.level == 5:
        print("You've reached level 5!\nYour HP has been restored.\n+ 3 ATK\n+ 5 HP")
        character.base_atk += 3
        character.hp += 5
        character.max_hp += 5
        character.hp = character.max_hp
        # -12, + 18
        character.atk_h += 2
    elif character.level == 6:
        print("You've reached level 6!\nYour HP has been restored.\n+ 4 ATK\n+ 6 HP")
        character.base_atk += 4
        character.hp += 6
        character.max_hp += 6
        character.hp = character.max_hp
        # -14, + 20
        character.atk_h += 2
        character.atk_l += 2
    elif character.level == 6:
        print("You've reached level 6!\nYour HP has been restored.\n+ 4 ATK\n+ 6 HP")
        character.base_atk += 4
        character.hp += 6
        character.max_hp += 6
        character.hp = character.max_hp
        # -14, + 22
        character.atk_h += 2
    elif character.level == 7:
        print("You've reached level 7!\nYour HP has been restored.\n+ 5 ATK\n+ 7 HP")
        character.base_atk += 5
        character.hp += 7
        character.max_hp += 7
        character.hp = character.max_hp
        # -14, + 24
        character.atk_h += 2
    elif character.level == 7:
        print("You've reached level 7!\nYour HP has been restored.\n+ 5 ATK\n+ 7 HP")
        character.base_atk += 5
        character.hp += 7
        character.max_hp += 7
        character.hp = character.max_hp
        # -14, + 22
        character.atk_h += 2
    elif character.level == 8:
        print("You've reached level 8!\nYour HP has been restored.\n+ 5 ATK\n+ 7 HP")
        character.base_atk += 5
        character.hp += 7
        character.max_hp += 7
        character.hp = character.max_hp
        # -16, + 24
        character.atk_h += 2
        character.atk_l += 2
    elif character.level == 9:
        print("You've reached level 9!\nYour HP has been restored.\n+ 6 ATK\n+ 8 HP")
        character.base_atk += 6
        character.hp += 8
        character.max_hp += 8
        character.hp = character.max_hp
        # -16, + 26
        character.atk_h += 2
    elif character.level == 10:
        print("You've reached level 10!\nYour HP has been restored.\n+ 6 ATK\n+ 8 HP")
        character.base_atk += 6
        character.hp += 8
        character.max_hp += 8
        character.hp = character.max_hp
        # -16, + 28
        character.atk_h += 2
