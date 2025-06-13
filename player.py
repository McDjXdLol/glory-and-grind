from inventory import Inventory
from level_manager import LevelManager


class Player:
    def __init__(self, hp, armor, damage, stamina, name):
        self.player_name = name
        self.hp = hp
        self.max_hp = hp
        self.armor = armor
        self.damage = damage
        self.stamina = stamina
        self.max_stamina = stamina
        self.is_alive = True

        self.player_level_manager = LevelManager()
        self.player_inventory = Inventory()

    # Deal damage function
    def takeDamage(self, amount):
        if (self.hp + self.armor) - amount <= 0:
            self.killPlayer()
        else:
            if self.armor > 0:
                if self.armor - amount <= 0:
                    amount -= self.armor
                    self.armor = 0
                    self.hp -= amount
                else:
                    self.armor -= amount
            else:
                self.hp -= amount

    def killPlayer(self):
        self.hp = 0
        self.armor = 0
        self.is_alive = False

    # Healing HP
    def healHP(self, amount):
        if self.hp + amount >= self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += amount

    # Stamina functions
    def useStamina(self, amount):
        if self.stamina - amount <= 0:
            self.stamina = 0
        else:
            self.stamina -= amount

    def haveEnoughStamina(self, amount) -> bool:
        return self.stamina >= amount

    def regenerateStamina(self, amount):
        if self.stamina + amount >= self.max_stamina:
            self.stamina = self.max_stamina
        else:
            self.stamina += amount
