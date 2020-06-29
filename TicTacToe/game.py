
from Player import Player
from Grid import Grid

def main():

    print(" _______ _          _______             _______         ")
    print("|__   __(_)        |__   __|           |__   __|  ")
    print("   | |   _  ___ ______| | __ _  ___ ______| | ___   ___ ")
    print("   | |  | |/ __|______| |/ _` |/ __|______| |/ _ \ / _ \\")
    print("   | |  | | (__       | | (_| | (__       | | (_) |  __/")
    print("   |_|  |_|\___|      |_|\__,_|\___|      |_|\___/ \___|")

    playerOne = Player(input("Enter player 1 name: "), 1)
    playerTwo = Player(input("Enter player 2 name: "), 2)

    print(playerOne.getName())
    print(playerTwo.getName())

    grid = Grid(10)
    grid.printGrid()

    pass

main()