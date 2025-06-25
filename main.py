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
    gracz = Player(100, 100, 20, 100, NICKNAME)
    GameInit(gracz).firstFight()
    shop = Shop(gracz)
    while True:
        wybor = 0
        try:
            wybor = int(input("1. Arena\n2. Shop\n3. Spend Points"))
        except ValueError:
            print("You have to enter the number! Try again")
            continue
        match wybor:
            case 1:
                # Fight
                pass
            case 2:
                shop.openItemShop()
            case 3:
                # Spend points
                pass


    # TODO:
    #  - [x] Dodać wpisywanie nazwy użytkownika
    #  - [-] Zrobić wybór klasy
    #  - [+] Pierwsza walka/tutorial
    #  - [ ] Rozpisać "tworzenie przeciwników" / napisać "przeciwników"
    #  - [ ] Reszta gry:
    #   - [ ] Dostęp do areny (tam walka z następnym przeciwnikiem)
    #   - [x] Dostęp do sklepu z broniami i zbrojami
    #   - [ ] Dostęp do "sklepu z punktami" (gracz może wydawać swoje punkty doświadczenia)

if __name__ == "__main__":
    main()
