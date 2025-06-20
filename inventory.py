class Inventory:
    """
    Klasa reprezentująca ekwipunek gracza.

    Attributes
    ----------
    wallet : int
        Ilość pieniędzy posiadanych przez gracza.
    weapon_name : str or None
        Nazwa aktualnie wyposażonej broni.
    weapon_damage : int
        Obrażenia zadawane przez aktualnie wyposażoną broń.
    armor_name : str or None
        Nazwa aktualnie wyposażonej zbroi.
    armor_value : int
        Wartość pancerza aktualnie wyposażonej zbroi.
    """

    def __init__(self):
        self.wallet = 0
        self.weapon_name = None
        self.weapon_damage = 0
        self.armor_name = None
        self.armor_value = 0

    def hasEnoughMoney(self, amount):
        """
        Sprawdza, czy gracz ma wystarczającą ilość pieniędzy.

        Parameters
        ----------
        amount : int
            Wymagana ilość pieniędzy.

        Returns
        -------
        bool
            True jeśli ilość pieniędzy w portfelu jest większa lub równa amount, False w przeciwnym razie.
        """
        return self.wallet >= amount

    def equipWeapon(self, weapon_name, weapon_damage):
        """
        Wyposaż gracza w nową broń.

        Parameters
        ----------
        weapon_name : str
            Nazwa nowej broni.
        weapon_damage : int
            Obrażenia zadawane przez nową broń.

        Returns
        -------
        list of int and str
            [stare obrażenia broni (lub 0 jeśli brak broni), nowe obrażenia broni]
        """
        if self.weapon_name is None:
            self.weapon_name = weapon_name
            self.weapon_damage = weapon_damage
            return [0, weapon_damage]
        else:
            old_weapon_damage = self.weapon_damage
            self.weapon_name = weapon_name
            self.weapon_damage = weapon_damage
            return [old_weapon_damage, weapon_damage]

    def equipArmor(self, armor_name, armor_value):
        """
        Wyposaż gracza w nową zbroję.

        Parameters
        ----------
        armor_name : str
            Nazwa nowej zbroi.
        armor_value : int
            Wartość pancerza nowej zbroi.

        Returns
        -------
        list of int
            [stara wartość pancerza (lub 0 jeśli brak zbroi), nowa wartość pancerza]
        """
        if self.armor_name is None:
            self.armor_name = armor_name
            self.armor_value = armor_value
            return [0, armor_value]
        else:
            old_armor_value = self.armor_value
            self.armor_name = armor_name
            self.armor_value = armor_value
            return [old_armor_value, armor_value]
