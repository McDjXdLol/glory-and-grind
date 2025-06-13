import random


class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def displayBattleStatus(self):
        print(f"""
        {self.player.player_name}
Player HP: {self.player.hp}
Player Armor: {self.player.armor}
Player Damage: {self.player.damage}

        {self.enemy.enemy_name}
Enemy HP: {self.enemy.hp}
Enemy Armor: {self.enemy.armor}
Enemy Damage: {self.enemy.damage}
""")

    # Attack handling functions
    def normalAttack(self):
        self.enemy.takeDamage(self.player.damage)
        print(f"""
{self.player.player_name} dealt {self.player.damage} dmg!
{self.enemy.enemy_name} HP: {self.enemy.hp} / {self.enemy.max_hp} Armor: {self.enemy.armor}
""")

    def strongAttack(self):
        if random.random() < 0.5:
            print("Your attack hit the enemy!")
            self.enemy.takeDamage(self.player.damage * 2)
            print(f"""
{self.player.player_name} dealt {self.player.damage * 2} dmg!
{self.enemy.enemy_name} HP: {self.enemy.hp} / {self.enemy.max_hp} Armor: {self.enemy.armor}
""")
        else:
            print("Your attack missed! You lost your turn!")

    def fastAttack(self):
        if random.random() < 0.3:
            print("Your attack hit the enemy!")
            self.enemy.takeDamage(self.player.damage)
            print(f"""
{self.player.player_name} dealt {self.player.damage} dmg!
{self.enemy.enemy_name} HP: {self.enemy.hp} / {self.enemy.max_hp} Armor: {self.enemy.armor}
""")
            print("Quick strike landed! You get to attack again!")
            return 0
        else:
            print("Your attack missed! You lost your turn!")
            return 1

    def recovery(self):
        self.player.healHP(int(self.player.max_hp * 0.15))
        self.player.regenerateStamina(int(self.player.max_stamina * 0.35))
        print("You catch your breath and recover some stamina!")
        print(f"Player HP: {self.player.hp} / {self.player.max_hp}\nPlayer Stamina: {self.player.stamina}")

    def player_turn(self):
        print("Select attack!")
        attack_selection = None
        try:
            attack_selection = int(input(
                "1. Normal attack (100%) - 20 Stamina\n2. Strong attack (50%) - 35 Stamina\n3. Fast attack (30%) - 15 Stamina\n4. Heal"))
        except ValueError:
            print("You have to enter the number! You lost your turn!")
            return 1
        match attack_selection:
            case 1:
                if self.player.haveEnoughStamina(20):
                    self.player.useStamina(20)
                    self.normalAttack()
                    return 1
                else:
                    print("You don't have enough stamina!")
                    return 0
            case 2:
                if self.player.haveEnoughStamina(35):
                    self.player.useStamina(35)
                    self.strongAttack()
                    return 1
                else:
                    print("You don't have enough stamina!")
                    return 0
            case 3:
                if self.player.haveEnoughStamina(15):
                    self.player.useStamina(15)
                    return self.fastAttack()
                else:
                    return 0
            case 4:
                self.recovery()
                return 1
            case _:
                print("You entered the wrong number! You lost your turn!")
                return 1

    def enemy_turn(self):
        self.player.takeDamage(self.enemy.damage)
        print(f"""
{self.enemy.enemy_name} dealt {self.enemy.damage} dmg!
{self.player.player_name} HP: {self.player.hp} / {self.player.max_hp} Armor: {self.player.armor}
""")

    def fight(self):
        # Who starts
        # - 0 - Player
        # - 1 - Enemy
        turn_owner = random.randint(0, 1)
        while self.player.is_alive and self.enemy.is_alive:
            if turn_owner == 0:
                print(f"{self.player.player_name} turn!")
                turn_owner = self.player_turn()
            else:
                print(f"{self.enemy.enemy_name} turn!")
                self.enemy_turn()
                self.player.regenerateStamina(15)
                turn_owner = 0

    def fight_result(self):
        if not self.player.is_alive and not self.enemy.is_alive:
            print("Tie!")
            return 0
        elif not self.player.is_alive and self.enemy.is_alive:
            print("You lost!")
            return 0
        elif self.player.is_alive and not self.enemy.is_alive:
            print("You won!")
            return 1

    def give_drop(self):
        self.player.player_level_manager.giveXP(self.enemy.xp_drop)
        self.player.player_inventory.wallet += self.enemy.gold_drop
        print(f"Battle won! Gained {self.enemy.gold_drop} gold & {self.enemy.xp_drop} XP!")

    def startBattle(self):
        self.displayBattleStatus()
        self.fight()
        if self.fight_result() == 1:
            self.give_drop()
