class Inventory:
    def __init__(self):
        # Player Money
        self.wallet = 0

        # Current player weapon
        self.weapon_name = None
        self.weapon_damage = 0

        # Current player armor
        self.armor_name = None
        self.armor_value = 0

    def hasEnoughMoney(self, amount):
        return self.wallet >= amount

    def equipWeapon(self, weapon_name, weapon_damage):
        if self.weapon_name is None:
            self.weapon_name = weapon_name
            self.weapon_damage = weapon_damage
            return [0, weapon_name]
        else:
            self.weapon_name = weapon_name
            old_weapon_damage = self.weapon_damage
            self.weapon_damage = weapon_damage
            return [old_weapon_damage, weapon_damage]

    def equipArmor(self, armor_name, armor_value):
        if self.armor_name is None:
            self.armor_name = armor_name
            self.armor_value = armor_value
            return [0, armor_value]
        else:
            self.armor_name = armor_name
            old_armor_value = self.armor_value
            self.armor_value = armor_value
            return [old_armor_value, armor_value]
