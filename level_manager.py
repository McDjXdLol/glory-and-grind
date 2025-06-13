class LevelManager:
    def __init__(self):
        self.xp = 0
        self.lvl = 1
        self.xp_needed_for_level = [100, 200, 350, 550, 800, 1100, 1500, 2000, 2600, 3300]

    def giveXP(self, amount):
        self.xp += amount
        if self.lvl < len(self.xp_needed_for_level):
            if self.xp >= self.xp_needed_for_level[self.lvl - 1]:
                self.xp = self.xp - self.xp_needed_for_level[self.lvl - 1]
                self.lvl += 1
                print("You got another level!")
            else:
                print(f"You need {self.xp_needed_for_level[self.lvl] - self.xp} to get {self.lvl + 1} lvl!")
        else:
            xp_needed = int(self.xp_needed_for_level[9] + (1000 * (self.lvl / 10)))
            if self.xp >= xp_needed:
                self.xp = self.xp - xp_needed
                self.lvl += 1
                print("You got another level!")
            else:
                print(f"You need {xp_needed - self.xp} to get {self.lvl + 1} lvl!")
