import math

winCombos = [
                            [0, 1, 2],
                            [3, 4, 5],
                            [6, 7, 8],
                            [0, 3, 6],
                            [1, 4, 7],
                            [2, 5, 8],
                            [0, 4, 8],
                            [6, 4, 2]
                            ]

def winningPos(board):
        tri:list[int] = []

        ls = []
        for win in winCombos:
            for num in win:
                tri.append(board[math.floor(num/3)][num%3])


            for i in tri:
                if i not in ls:
                    ls.append(i)
            if len(ls) == 1 and ls[0] != 0:
                return True
            ls.clear()
            num =0
            tri.clear()
        return False


def checkdraw(board):
    for row in board:    
        for i in row:
            if i == 0:
                return False
                
    return True