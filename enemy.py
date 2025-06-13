class Enemy:
    def __init__(self, hp, armor, damage, name, gold, xp):
        self.enemy_name = name
        self.hp = hp
        self.max_hp = hp
        self.armor = armor
        self.damage = damage
        self.is_alive = True

        self.gold_drop = gold
        self.xp_drop = xp

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
