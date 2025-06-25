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

    def generateEnemy(self):
        LOWER_STAT_PERCENTAGE = 0.85
        UPPER_STAT_PERCENTAGE = 1.05
        lower_stat_hp = int(self.player.max_hp * LOWER_STAT_PERCENTAGE)  # 90%
        upper_stat_hp = int(self.player.max_hp * UPPER_STAT_PERCENTAGE)  # 105%
        randomized_hp = random.randint(lower_stat_hp, upper_stat_hp)

        lower_stat_armor = int(self.player.armor * LOWER_STAT_PERCENTAGE)  # 90%
        upper_stat_armor = int(self.player.armor * UPPER_STAT_PERCENTAGE)  # 105%
        randomized_armor = random.randint(lower_stat_armor, upper_stat_armor)

        lower_stat_damage = int(self.player.damage * LOWER_STAT_PERCENTAGE)  # 90%
        upper_stat_damage = int(self.player.damage * UPPER_STAT_PERCENTAGE)  # 105%
        randomized_damage = random.randint(lower_stat_damage, upper_stat_damage)

        lower_stat_gold = int(randomized_hp * LOWER_STAT_PERCENTAGE)  # 90%
        upper_stat_gold = int(randomized_hp * UPPER_STAT_PERCENTAGE)  # 105%
        randomized_gold = random.randint(lower_stat_gold, upper_stat_gold)

        lower_stat_xp = int(randomized_hp * LOWER_STAT_PERCENTAGE)  # 90%
        upper_stat_xp = int(randomized_hp * UPPER_STAT_PERCENTAGE)  # 105%
        randomized_xp = random.randint(lower_stat_xp, upper_stat_xp)

        randomized_name = f"{random.choice(self.names)} {random.choice(self.nicknames)}"

        return Enemy(randomized_hp, randomized_armor, randomized_damage, randomized_name, randomized_gold, randomized_xp)
