import math
from copy import deepcopy

from utils import checkdraw, winningPos
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
def evaluate(player:int,board):
        x1 = 0
        x2 = 0
        o1 = 0
        o2 = 0
        for win in winCombos:
            res =[]
            for ind in win:
                res.append(board[math.floor(ind/3)][ind%3])
            op = (1- (player-1))+1
            if op not in res:
                ones = res.count(player)
                zeros = res.count(0)
                
                if ones == 2 and zeros == 1:
                    x2+=1
                elif ones ==1 and zeros ==2:
                    x1+=1
            elif player not in res:
                ones = res.count(op)
                zeros = res.count(0)
                if ones == 2 and zeros == 1:
                    o2+=1
                elif ones ==1 and zeros ==2:
                    o1+=1
        return ((3*o2) +o1) -((3*x2)+x1)


def minimax(position,depth:"int",maximizingPlayer:bool ):
    if depth == 0 or winningPos(position) or checkdraw(position):
        return evaluate(2 if maximizingPlayer else 1,position)
    
    if maximizingPlayer:
        maxEval = -1000000
        for child in children(position):
            eval = minimax(child,depth-1,False)
            maxEval = max(eval,maxEval)
        return maxEval
    else:
        minEval = 1000000
        for child in children(position):
            eval = minimax(child, depth-1,True)

            minEval = min(minEval,eval)
        return minEval

def children(position:"list[list[int]]")->"list[list[list[int]]]":
    main = []
    other = deepcopy(position)
    for ind,row in enumerate(position):
        for inder,col in enumerate(row):
            ls = deepcopy(other)

            if col == 0:
                ls[ind][inder] = 2

                main.append(ls)


    return main
                

            




class Tic:
    def __init__(self, constructFromParent:bool= False,parent:"Tic"= None) -> None:
        self.board:list[list[int]] = []
        if constructFromParent:
            self.board = parent.board
        else:
            for i in range(3):
                self.board.append([0,0,0])
        self.current_player: int = 1
        self.winCombos = [
                            [0, 1, 2],
                            [3, 4, 5],
                            [6, 7, 8],
                            [0, 3, 6],
                            [1, 4, 7],
                            [2, 5, 8],
                            [0, 4, 8],
                            [6, 4, 2]
                            ]
       
    def winningPos(self):
        tri:list[int] = []

        ls = []
        for win in self.winCombos:
            for num in win:
                tri.append(self.board[math.floor(num/3)][num%3])


            for i in tri:
                if i not in ls:
                    ls.append(i)
            if len(ls) == 1 and ls[0] != 0:
                return True
            ls.clear()
            num =0
            tri.clear()
        return False
    


        
    def makeMove(self,one, two):
        if one < 3 and two< 3:
            if not self.checkTaken(one,two):
                self.board[one][two] = self.current_player
                if self.winningPos():
                    return 1
                elif self.checkdraw():
                    return 2
                else:
                    self.current_player = 1 if self.current_player == 2 else 2
                    return 0
            return -2
        else:
            return -1

    def __str__(self) -> str:
        res = ""
        for row in self.board:
            res+="["
            for ind, i in enumerate(row):
                res+=str(i)
                if ind<2:
                    res+=","
            res+="]\n"
        return res

    def checkdraw(self):
        for row in self.board:    
            for i in row:
                if i == 0:
                    return False
                    
        return True
    def checkTaken(self, x, y):
        return self.board[x][y] != 0
    
    
    def reset(self,board:"list[list[int]]"):
        self.board = board


        
    
    def automatedMove(self):
        get = children(self.board)
        les = []
        for tic in get:
            eval = minimax(position=tic,depth=10,maximizingPlayer=True)
            les.append(eval)
        
        res = les.index(max(les))
        self.board = get[res]
        self.current_player = 1 if self.current_player == 2 else 2
        if self.winningPos():
            return 1
        return 0

                

                


        



