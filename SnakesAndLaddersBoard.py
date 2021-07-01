import JsonOperations

class SnakesAndLaddersBoard():

    def __init__(self,gameJsonPath):
        self.gameData=JsonOperations.JsonToObject(gameJsonPath)
        self.boardSize=int(self.gameData['Size'])
        self.boardSnakes=dict()
        self.boardSnakesEnds=dict()
        self.boardLadders=dict()
        self.boardLaddersEnds=dict()
        snakeCount=1
        for snake in self.gameData['Snakes']:
            if snake[0] not in self.boardSnakes:
                self.boardSnakes[snake[0]]=[0,snakeCount]
                if snake[1] not in self.boardSnakesEnds:
                    self.boardSnakesEnds[snake[1]]=[0,snakeCount]
                snakeCount+=1
            self.boardSnakes[snake[0]][0]=snake[1]
        
        ladderCount=1
        for ladder in self.gameData['Ladders']:
            if ladder[0] not in self.boardLadders:
                self.boardLadders[ladder[0]]=[0,ladderCount]
                if ladder[1] not in self.boardLaddersEnds:
                    self.boardLaddersEnds[ladder[1]]=[0,ladderCount]
                ladderCount+=1
            self.boardLadders[ladder[0]][0]=ladder[1]
        self.playerPosition=1

    def PrintBoard(self):
        temp=self.boardSize*self.boardSize
        maxNumber=len(str(temp))
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if temp==self.playerPosition:
                    print ("P".rjust(maxNumber,'x')+"\t",end ="")
                elif temp in self.boardSnakes:
                    sTemp="S"+str(self.boardSnakes[temp][1])
                    print (sTemp.rjust(maxNumber,'x')+"\t",end ="")
                elif temp in self.boardSnakesEnds:
                    sTemp="S"+str(self.boardSnakesEnds[temp][1])
                    print (sTemp.rjust(maxNumber,'x')+"\t",end ="")
                elif temp in self.boardLadders:
                    lTemp="L"+str(self.boardLadders[temp][1])
                    print (lTemp.rjust(maxNumber,'x')+"\t",end ="")
                elif temp in self.boardLaddersEnds:
                    lTemp="L"+str(self.boardLaddersEnds[temp][1])
                    print (lTemp.rjust(maxNumber,'x')+"\t",end ="")
                else:
                    print (str(temp).rjust(maxNumber,'0')+"\t",end ="")
                temp-=1
            print("\n")
        return 123