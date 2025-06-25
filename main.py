import sys
import time

from combat import Combat
from game_init import GameInit
from player import Player
from player_setup import PlayerSetup
from shop import Shop

def main():
    """
    Główna pętla gry
    :return:
    """
    NICKNAME = PlayerSetup.getPlayerName()
    player = Player(100, 100, 20, 100, NICKNAME)
    gi = GameInit(player)
    gi.firstFight()
    shop = Shop(player)
    while True:
        sel = 0
        try:
            sel = int(input("1. Arena\n2. Shop\n3. Spend Points\n4. Exit"))
        except ValueError:
            print("You have to enter the number! Try again")
            continue
        match sel:
            case 1:
                rival = gi.generateEnemy()
                if Combat(player, rival).startBattle():
                    continue
                else:
                    break
            case 2:
                shop.openItemShop()
                continue
            case 3:
                shop.openPointsShop()
                continue
            case 4:
                print("Exiting...")
                time.sleep(2)
                sys.exit()
            case _:
                print("You entered the wrong number! Try again")
                continue

if __name__ == "__main__":
    while True:
        main()
        print("Try again? (y\n)")
        if input().lower() == "y":
            continue
        else:
            break

