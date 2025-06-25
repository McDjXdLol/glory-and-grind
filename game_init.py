from combat import Combat
from enemy import Enemy

class GameInit:
    def __init__(self, player):
        self.player = player
        self.enemy = Enemy(10, 10, 5, "Tutorial", 5, 5)

    def firstFight(self):
        fight = Combat(self.player, self.enemy)
        fight.startBattle()