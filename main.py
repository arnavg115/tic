import math
from Tic import Tic

running = True
game = Tic()
result = 0
while running:
    player = game.current_player
    print(f"{str(player)}'s turn")

    if player == 1:
        one = int(input("> "))
        res = game.makeMove(math.floor(one/3),one%3)
    else:
        res = game.automatedMove()
    print(game)
    if res > 0:
        result = res
        running = False
    elif res<0:
        print("Invalid index try again" if res == -1 else "Position taken try again")


# print(result)

