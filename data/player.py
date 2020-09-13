from data.shop_items import Potions


# player class
class Player:
    def __init__(self, hp, atk, defence, name, atk_l, atk_h, b_atk_p, m_atk_p, bleed_dot_count, bleed_dot_dmg, burn_dot_count,
                 burn_dot_dmg, gold, xp1, xp2, level, strength):
        self.name = name
        self.hp = hp
        self.max_hp = self.hp
        self.base_atk = atk
        self.defence = defence
        self.atk_l = atk_l
        self.atk_h = atk_h
        self.b_atk_p = b_atk_p
        self.m_atk_p = m_atk_p
        self.bleed_check = False
        self.bleed_dot_count = bleed_dot_count
        self.bleed_dot_dmg = bleed_dot_dmg
        self.gold = gold
        self.burn_check = False
        self.burn_dot_count = burn_dot_count
        self.burn_dot_dmg = burn_dot_dmg
        self.xp1 = xp1
        self.xp2 = xp2
        self.level = level
        self.strength = strength
        self.player_armour = {}
        self.player_weapons = {}
        self.shop_items = [""]
        self.items = []
        self.misc_items = {}
        self.current_armour = ""
        self.current_weapon = ""
        self.location = "d1"
        self.shop_pots = [{"item": Potions.l_health_pot, "quantity": 500, "price": " 4G Each"},
                          {"item": Potions.health_pot, "quantity": 500, "price": " 10G Each"},
                          {"item": Potions.max_pot, "quantity": 1000, "price": "50G Each"},
                          {"item": Potions.plus_hp, "quantity": 20, "price": "  1000G Each"},
                          {"item": Potions.plus_atk, "quantity": 20, "price": "  1000G Each"},
                          {"item": Potions.plus_def, "quantity": 20, "price": "  1000G Each"}]
        self.active_quests = []
        self.completed_quests = []
        self.player_atk_turn = True
        self.b6_event_1 = True
        self.d3_event_1 = True
        self.d3_event_2 = False
        self.d3_event_3 = False
        self.d3_event_4 = True
        self.d4_event_1 = True
        self.d4_event_2 = True
        self.e2_event_1 = True
        self.e2_event_2 = False
        self.e2_event_3 = False
        self.f5_event_1 = True
        self.f6_event_1 = True
        self.f6_event_2 = True
        self.g6_event_1 = True
        self.g6_event_2 = True
        self.i6_event_1 = True
        self.j6_event_1 = True
        self.k6_event_1 = True
        self.k6_event_2 = True
        self.l5_event_1 = True
        self.n6_event_1 = True
        self.n6_event_2 = True
        self.n7_event_1 = True
        self.o7_event_1 = True
        self.o7_event_2 = True
        self.q10_event_1 = True
        self.r10_event_1 = True
        self.r10_event_2 = False
        self.d3_d4_map = False
        self.f6_g6_map = False
        self.j6_k6_map = False
        self.n6_o7_map = False
        self.title_screen = True
        self.story_intro = True
        self.town_zone = True
        self.forest_zone = True
        self.water_zone = True
        self.desert_zone = True
        self.dungeon_zone = True
        self.battle_music_1 = True
        self.battle_music_2 = True
        self.boss_music_1 = True
        self.win_music_1 = True
        self.win_music_2 = True
        self.defeat_music_1 = True

    # modifiers for the current_atk
    @property
    def current_atk(self):
        current_atk = self.base_atk
        if self.current_weapon == "[Wooden Sword] + (10 ATK)":
            current_atk += 10
        if self.current_weapon == "[Bronze Sword] + (15 ATK)":
            current_atk += 15
        if self.current_weapon == "[Iron Sword] + (20 ATK)":
            current_atk += 20
        if self.current_weapon == "[Steel Sword] + (30 ATK)":
            current_atk += 30
        if self.current_weapon == "[Rune Sword] + (40 ATK)":
            current_atk += 40
        if self.current_weapon == "[Dragon Sword] + (60 ATK)":
            current_atk += 60
        if self.current_weapon == "[General Store Sword] + (80 ATK)":
            current_atk += 80
        if self.current_weapon == "[Sunfury, Cursed Axe of the Breezeseeker] + (100 ATK)":
            current_atk += 100
        return current_atk

    # modifiers for base_hp
    @property
    def base_hp(self):
        base_hp = self.hp
        if self.current_armour == "[Leather Armour Set] + (20 HP/2 DF)":
            base_hp += 20
        if self.current_armour == "[Bronze Armour] + (20 HP/4 DF)":
            base_hp += 20
        if self.current_armour == "[Iron Armour Set] + (40 HP/5 DF)":
            base_hp += 40
        if self.current_armour == "[Steel Armour Set] + (50 HP/6 DF)":
            base_hp += 50
        if self.current_armour == "[Rune Armour Set] + (60 HP/8 DF)":
            base_hp += 60
        if self.current_armour == "[Dragon Armour Set] + (80 HP/10 DF)":
            base_hp += 80
        if self.current_armour == "[General Store Armour Set] (90 HP/12 DF)":
            base_hp += 90
        if self.current_armour == "[The Baron's Armour] + (100/15 DF)":
            base_hp += 100
        return base_hp

    # modifiers for max_hp
    @property
    def hp_max(self):
        hp_max = self.max_hp
        if self.current_armour == "[Leather Armour Set] + (20 HP/2 DF)":
            hp_max += 20
        if self.current_armour == "[Bronze Armour] + (20 HP/4 DF)":
            hp_max += 20
        if self.current_armour == "[Iron Armour Set] + (40 HP/5 DF)":
            hp_max += 40
        if self.current_armour == "[Steel Armour Set] + (50 HP/6 DF)":
            hp_max += 50
        if self.current_armour == "[Rune Armour Set] + (60 HP/8 DF)":
            hp_max += 60
        if self.current_armour == "[Dragon Armour Set] + (80 HP/10 DF)":
            hp_max += 80
        if self.current_armour == "[General Store Armour Set] (90 HP/12 DF)":
            hp_max += 90
        if self.current_armour == "[The Baron's Armour] + (100/15 DF)":
            hp_max += 100
        return hp_max

    # modifiers for current_defence
    @property
    def current_defence(self):
        current_defence = self.defence
        if self.current_armour == "[Leather Armour Set] + (20 HP/2 DF)":
            current_defence += 2
        if self.current_armour == "[Bronze Armour] + (20 HP/4 DF)":
            current_defence += 4
        if self.current_armour == "[Iron Armour Set] + (40 HP/5 DF)":
            current_defence += 5
        if self.current_armour == "[Steel Armour Set] + (50 HP/6 DF)":
            current_defence += 6
        if self.current_armour == "[Rune Armour Set] + (60 HP/8 DF)":
            current_defence += 8
        if self.current_armour == "[Dragon Armour Set] + (80 HP/10 DF)":
            current_defence += 10
        if self.current_armour == "[General Store Armour Set] (90 HP/12 DF)":
            current_defence += 12
        if self.current_armour == "[The Baron's Armour] + (100/15 DF)":
            current_defence += 15
        return current_defence


# class for creating spells
class Spells:
    def __init__(self, name, cost, dmg):
        self.name = name
        self.cost = cost
        self.dmg = dmg
