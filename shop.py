class Shop:
    """
    Sklep, w którym gracz może kupować bronie i zbroje.

    Attributes
    ----------
    player : Player
        Obiekt gracza, który dokonuje zakupów.
    weapons : dict
        Słownik dostępnych broni, z ich obrażeniami i cenami.
    armors : dict
        Słownik dostępnych zbroi, z ich wartością pancerza i cenami.
    """

    def __init__(self, player):
        """
        Inicjalizuje sklep z listą broni i zbroi oraz przypisuje gracza.

        Parameters
        ----------
        player : Player
            Gracz, który będzie kupował przedmioty.
        """
        self.player = player
        self.weapons = {
            "Wooden Stick": {"damage": 5, "price": 10},
            "Iron Sword": {"damage": 15, "price": 50},
            "Steel Axe": {"damage": 25, "price": 120},
            "Dark Bow": {"damage": 30, "price": 180},
            "Dragon Sword": {"damage": 50, "price": 500},
        }
        self.armors = {
            "Leather Jacket": {"armor": 5, "price": 20},
            "Chainmail": {"armor": 15, "price": 60},
            "Plate Armor": {"armor": 30, "price": 150},
            "Shadow Armor": {"armor": 40, "price": 300},
            "Dragon Armor": {"armor": 60, "price": 600},
        }

    def showItemsToBuy(self):
        """
        Wyświetla menu sklepu i obsługuje proces zakupu broni i zbroi.

        Funkcja pyta gracza co chce kupić (broń, zbroję lub wyjść),
        wyświetla dostępne przedmioty, sprawdza stan portfela,
        dokonuje zakupu i aktualizuje statystyki gracza.
        """
        bad_answer = True
        player_choice = None
        while bad_answer:
            try:
                player_choice = int(input("What do you want to buy?\n1. Weapon\n2. Armor\n3. Exit\n"))
                if 3 >= player_choice >= 1:
                    bad_answer = False
            except ValueError:
                print("You have to enter the number!")

        if player_choice == 1:
            weapon_list = []
            print("These are the weapons that I sell:")
            for nr, weapon_name in enumerate(self.weapons):
                print(
                    f"{nr + 1}. {weapon_name} {self.weapons[weapon_name]['damage']} dmg - {self.weapons[weapon_name]['price']} gold")
                weapon_list.append(weapon_name)

            bad_answer = True
            weapon_choice = None
            while bad_answer:
                try:
                    weapon_choice = int(input(f"Which one do you want to buy?\nYour gold: {self.player.player_inventory.wallet}\n"))
                    if len(weapon_list) >= weapon_choice >= 1:
                        bad_answer = False
                except ValueError:
                    print("You have to enter the number!")

            weapon_choice -= 1
            if self.player.player_inventory.hasEnoughMoney(self.weapons[weapon_list[weapon_choice]]['price']):
                self.player.player_inventory.wallet -= self.weapons[weapon_list[weapon_choice]]['price']
                weapon = self.player.player_inventory.equipWeapon(weapon_list[weapon_choice], self.weapons[weapon_list[weapon_choice]]['damage'])
                self.player.damage -= weapon[0]
                self.player.damage += weapon[1]
                print(f"You bought {weapon_list[weapon_choice]}! Your damage: {self.player.damage}")
            else:
                print("Not enough gold!")

        elif player_choice == 2:
            armor_list = []
            print("These are the armors that I sell:")
            for nr, armor in enumerate(self.armors):
                print(f"{nr + 1}. {armor} {self.armors[armor]['armor']} armor - {self.armors[armor]['price']} gold")
                armor_list.append(armor)

            bad_answer = True
            armor_choice = None
            while bad_answer:
                try:
                    armor_choice = int(input(f"Which one do you want to buy?\nYour gold: {self.player.player_inventory.wallet}\n"))
                    if len(armor_list) >= armor_choice >= 1:
                        bad_answer = False
                except ValueError:
                    print("You have to enter the number!")
            armor_choice -= 1
            if self.player.player_inventory.hasEnoughMoney(self.armors[armor_list[armor_choice]]['price']):
                self.player.player_inventory.wallet -= self.armors[armor_list[armor_choice]]['price']
                armor = self.player.player_inventory.equipArmor(armor_list[armor_choice], self.armors[armor_list[armor_choice]]['armor'])
                self.player.armor -= armor[0]
                self.player.armor += armor[1]
                print(f"You bought {armor_list[armor_choice]}! Your armor: {self.player.armor}")
            else:
                print("Not enough gold!")

        elif player_choice == 3:
            return
