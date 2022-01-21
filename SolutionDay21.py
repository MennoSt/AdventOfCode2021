from utils.AocUtils import *
from utils.FileReader import FileReader

# %%

class DiceRoller:
    
    def __init__(self):
        self.rollCycles = 0
        self.playerInfo = []
        self.diceOne = -2
        self.diceTwo = -1
        self.diceThree = 0
        self.totalScore = 0
        
    def loadStartPositions(self, fileString):
        for player in fileString:
            player = player.replace("Player ", "")
            player = player.split(" starting position: ")
            playerInfo = {"player":0, "position":0, "score": 0}
            playerNumber = player[0]
            position = player[1]
            playerInfo["player"] = int(playerNumber)
            playerInfo["position"] = int(position)
            self.playerInfo.append(playerInfo)
    
    def __throwDices(self):

        self.diceOne = self.updateDice(self.diceOne)
        self.diceTwo = self.updateDice(self.diceTwo)
        self.diceThree = self.updateDice(self.diceThree)
            
        self.totalScore = self.diceOne + self.diceTwo + self.diceThree

    def updateDice(self, dice):
        dice += 3
        modulus = dice%100
        if modulus == 0:
            dice = 100
        else:
            dice = modulus
        
        return dice
    
    def performNextRound(self):
        highestPlayerScore = max(self.playerInfo[0]["score"], self.playerInfo[1]["score"])
        if highestPlayerScore <1000:
            self.playerThrowsDice(1)
            
        highestPlayerScore = max(self.playerInfo[0]["score"], self.playerInfo[1]["score"])
        if highestPlayerScore <1000:   
            self.playerThrowsDice(2)

    def playerThrowsDice(self, playerNumber):
        self.rollCycles += 3
        self.__throwDices()
        for player in self.playerInfo:
            if player["player"] == playerNumber:
                player["position"] += self.totalScore
                if player["position"] > 10:
                    modulus = player["position"] % 10
                    if modulus == 0:
                        player["position"] = 10
                    else:
                        player["position"] = modulus
                player["score"] += player["position"]
    
    def playGame(self):
        highestPlayerScore = 0
        self.rollCycles = 0
        
        while highestPlayerScore < 1000:
            self.performNextRound()
            highestPlayerScore = max(self.playerInfo[0]["score"], self.playerInfo[1]["score"])
    
    def determineGameScore(self):
        self.playGame()
        lowestScore = min(self.playerInfo[0]["score"], self.playerInfo[1]["score"])
        gameScore = lowestScore * self.rollCycles
        
        return gameScore
        
            
def solutionDay21():
    fileReader = FileReader()
    diceRoller = DiceRoller()
    fileString = fileReader.readLinesToStringArray("input/inputday21")
    diceRoller.loadStartPositions(fileString)
    
    answerPart1 = diceRoller.determineGameScore()
    answerPart2 = 0
    printAnswer(20, answerPart1, answerPart2)
    

# %%
