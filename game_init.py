import random

from combat import Combat
from enemy import Enemy


class GameInit:
    def __init__(self, player):
        self.player = player
        self.enemy = Enemy(10, 10, 5, "Tutorial", 5, 5)
        self.names = [
            "Albert", "Gideon", "Felix", "Ronan", "Cedric", "Dorian", "Lucian",
            "Malcolm", "Victor", "Elias", "Benedict", "Thaddeus", "Sebastian",
            "Ignatius", "Alaric", "Cassius", "Evander", "Leander", "Magnus",
            "Quentin", "Raphael", "Silas", "Tobias", "Valerian", "Xander",
            "Zachary", "Darius", "Ezekiel", "Gareth", "Hadrian", "Isidore",
            "Jasper", "Kieran", "Lysander", "Marius", "Nolan", "Orion",
            "Phineas", "Rafferty", "Soren"
        ]
        self.nicknames = [
            "the Cruel", "the Vicious", "the Cunning", "the Ruthless",
            "the Wicked", "the Fearless", "the Savage", "the Devious",
            "the Merciless", "the Brave", "the Silent", "the Fierce",
            "the Bold", "the Grim", "the Deadly", "the Fierce", "the Shadow",
            "the Vengeful", "the Dark", "the Thunderous", "the Iron",
            "the Swift", "the Fierce", "the Savage", "the Mighty",
            "the Unyielding", "the Phantom", "the Grim", "the Bloodied",
            "the Ferocious", "the Silent", "the Obsidian", "the Blade",
            "the Storm", "the Wolf", "the Lionheart", "the Serpent",
            "the Titan", "the Berserker", "the Wraith"
        ]

    def firstFight(self):
        fight = Combat(self.player, self.enemy)
        fight.startBattle()

    @staticmethod
    def randomize_stat(stat):
        LOWER_STAT_PERCENTAGE = 0.85
        UPPER_STAT_PERCENTAGE = 1.05
        lower_stat = int(stat * LOWER_STAT_PERCENTAGE)
        upper_stat = int(stat * UPPER_STAT_PERCENTAGE)
        return random.randint(lower_stat, upper_stat)

    def generateEnemy(self):
        randomized_hp = self.randomize_stat(self.player.hp)

        randomized_armor = self.randomize_stat(self.player.armor)

        randomized_damage = self.randomize_stat(self.player.damage)

        randomized_gold = self.randomize_stat(randomized_hp)

        randomized_xp = self.randomize_stat(randomized_hp)

        randomized_name = f"{random.choice(self.names)} {random.choice(self.nicknames)}"

        return Enemy(randomized_hp, randomized_armor, randomized_damage, randomized_name, randomized_gold, randomized_xp)
