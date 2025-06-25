from inventory import Inventory
from level_manager import LevelManager


class Player:
    """
    Klasa reprezentująca gracza.

    Parameters
    ----------
    hp: int
        Maksymalne i początkowe punkty życia gracza.
    armor: int
        Ilość pancerza gracza, pochłaniającego obrażenia przed HP.
    damage: int
        Obrażenia zadawane przez gracza.
    stamina: int
        Maksymalna i początkowa wartość staminy (energii do ataków).
    name: str
        Nazwa (nick) gracza.
    """

    def __init__(self, hp, armor, damage, stamina, name):
        self.player_name = name
        self.hp = hp
        self.max_hp = hp
        self.armor = armor
        self.max_armor = armor
        self.damage = damage
        self.stamina = stamina
        self.max_stamina = stamina
        self.is_alive = True

        self.player_level_manager = LevelManager()
        self.player_inventory = Inventory()

    def takeDamage(self, amount):
        """
        Zadaje obrażenia graczowi, uwzględniając pancerz.

        Parameters
        ----------
        amount: int
            Ilość obrażeń do zadania.

        Notes
        -----
        Obrażenia najpierw są odejmowane od pancerza.
        Jeśli pancerz zostanie przebity, reszta obrażeń idzie na HP.
        Jeśli suma pancerza i HP spadnie do 0 lub mniej, gracz zostaje zabity.
        """
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
        """
        Ustawia stan gracza jako martwy.
        """
        self.hp = 0
        self.armor = 0
        self.is_alive = False

    def healHP(self, amount):
        """
        Leczy gracza, zwiększając HP.

        Parameters
        ----------
        amount: int
            Ilość punktów życia do przywrócenia.

        Notes
        -----
        HP nie może przekroczyć maksymalnej wartości.
        """
        if self.hp + amount >= self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += amount

    def useStamina(self, amount):
        """
        Zużywa określoną ilość staminy.

        Parameters
        ----------
        amount: int
            Ilość staminy do zużycia.

        Notes
        -----
        Stamina nie spada poniżej zera.
        """
        if self.stamina - amount <= 0:
            self.stamina = 0
        else:
            self.stamina -= amount

    def haveEnoughStamina(self, amount) -> bool:
        """
        Sprawdza, czy gracz ma wystarczająco staminy.

        Parameters
        ----------
        amount: int
            Wymagana ilość staminy.

        Returns
        -------
        bool
            True, jeśli gracz ma co najmniej tyle staminy, False w przeciwnym razie.
        """
        return self.stamina >= amount

    def regenerateStamina(self, amount):
        """
        Regeneruje staminy gracza.

        Parameters
        ----------
        amount: int
            Ilość staminy do odzyskania.

        Notes
        -----
        Stamina nie może przekroczyć maksymalnej wartości.
        """
        if self.stamina + amount >= self.max_stamina:
            self.stamina = self.max_stamina
        else:
            self.stamina += amount
