import winsound
from data.game_map import Map


def game_menu_music(character):
    if character.town_zone:
        if Map.zone_map[character.location][Map.ZONE_NAME] in "town":
            winsound.PlaySound("music\\town_theme.wav", winsound.SND_ASYNC + winsound.SND_LOOP)
            character.town_zone = False
            character.forest_zone = True
            character.water_zone = True
            character.desert_zone = True
            character.dungeon_zone = True
    if character.forest_zone:
        if Map.zone_map[character.location][Map.ZONE_NAME] in "forest":
            winsound.PlaySound("music\\forest_theme.wav", winsound.SND_ASYNC + winsound.SND_LOOP)
            character.town_zone = True
            character.forest_zone = False
            character.water_zone = True
            character.desert_zone = True
            character.dungeon_zone = True
    if character.water_zone:
        if Map.zone_map[character.location][Map.ZONE_NAME] in "water":
            winsound.PlaySound("music\\water_theme.wav", winsound.SND_ASYNC + winsound.SND_LOOP)
            character.town_zone = True
            character.forest_zone = True
            character.water_zone = False
            character.desert_zone = True
            character.dungeon_zone = True
    if character.desert_zone:
        if Map.zone_map[character.location][Map.ZONE_NAME] in "desert":
            winsound.PlaySound("music\\desert_theme.wav", winsound.SND_ASYNC + winsound.SND_LOOP)
            character.town_zone = True
            character.forest_zone = True
            character.water_zone = True
            character.desert_zone = False
            character.dungeon_zone = True
    if character.dungeon_zone:
        if Map.zone_map[character.location][Map.ZONE_NAME] in "dungeon":
            winsound.PlaySound("music\\dungeon_theme.wav", winsound.SND_ASYNC + winsound.SND_LOOP)
            character.town_zone = True
            character.forest_zone = True
            character.water_zone = True
            character.desert_zone = True
            character.dungeon_zone = False


def fight_music(character, en1):
    if en1.name == "Baron of Hell":
        if character.boss_music_1:
            winsound.PlaySound("music\\boss_battle.wav", winsound.SND_ASYNC + winsound.SND_LOOP)
            character.boss_music_1 = False
    else:
        if character.battle_music_1:
            character.battle_music_1 = False
            character.battle_music_2 = True
        if character.battle_music_2:
            winsound.PlaySound("music\\battle_theme.wav", winsound.SND_ASYNC + winsound.SND_LOOP)
            character.battle_music_2 = False


def win_music(character):
    character.win_music_2 = True
    if character.win_music_2:
        winsound.PlaySound("music\\battle_victory.wav", winsound.SND_ASYNC + winsound.SND_LOOP)
        character.defeat_music_1 = True
        character.win_music_1 = True
        character.win_music_2 = False
        character.boss_music_1 = True
        character.town_zone = True
        character.forest_zone = True
        character.water_zone = True
        character.desert_zone = True
        character.dungeon_zone = True


def defeat_music(character):
    character.defeat_music_1 = True
    if character.defeat_music_1:
        winsound.PlaySound("music\\you_died.wav", winsound.SND_ASYNC)
        character.defeat_music_1 = False
        character.win_music_1 = True
        character.win_music_2 = True
        character.boss_music_1 = True
        character.town_zone = True
        character.forest_zone = True
        character.water_zone = True
        character.desert_zone = True
        character.dungeon_zone = True
