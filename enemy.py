class Enemy:
    """
    Klasa reprezentująca wroga w grze.

    Parameters
    ----------
    hp: int
        Maksymalne i początkowe punkty życia wroga.
    armor: int
        Ilość pancerza wroga, który pochłania obrażenia przed HP.
    damage: int
        Obrażenia zadawane przez wroga.
    name: str
        Nazwa wroga.
    gold: int
        Ilość złota, którą wróg upuszcza po śmierci.
    xp: int
        Ilość doświadczenia (XP) przyznawanego za pokonanie wroga.
    """

    def __init__(self, hp, armor, damage, name, gold, xp):
        self.enemy_name = name
        self.hp = hp
        self.max_hp = hp
        self.armor = armor
        self.damage = damage
        self.is_alive = True

        self.gold_drop = gold
        self.xp_drop = xp

    def takeDamage(self, amount):
        """
        Zadaje obrażenia wrogowi, uwzględniając pancerz.

        Parameters
        ----------
        amount: int
            Ilość obrażeń do zadania.

        Notes
        -----
        - Obrażenia najpierw są odejmowane od pancerza.
        - Jeśli pancerz zostanie przebity, reszta obrażeń idzie na HP.
        - Jeśli suma pancerza i HP spadnie do 0 lub mniej, wróg zostaje zabity.
        """
        if (self.hp + self.armor) - amount <= 0:
            self.killEnemy()
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

    def killEnemy(self):
        """
        Ustawia stan wroga jako martwy.
        """
        self.hp = 0
        self.armor = 0
        self.is_alive = False
