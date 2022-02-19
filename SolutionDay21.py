from utils.AocUtils import *
from utils.FileReader import FileReader
import copy

# %%

class DiceRoller:
    
    def __init__(self):
        self.rollCycles = 0
        self.playerInfo = []
        self.diceOne = -2
        self.diceTwo = -1
        self.diceThree = 0
        self.totalScore = 0
        
        self.universWinsPlayer1 = 0
        self.universWinsPlayer2 = 0
        
    def loadStartPositions(self, fileString):
        self.playerInfo = []
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
            
        score = self.diceOne + self.diceTwo + self.diceThree
        return score

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
            self.playerThrowsDeterDice(1)
            
        highestPlayerScore = max(self.playerInfo[0]["score"], self.playerInfo[1]["score"])
        if highestPlayerScore <1000:   
            self.playerThrowsDeterDice(2)

    def playerThrowsDeterDice(self, playerNumber):
        self.rollCycles += 3
        score = self.__throwDices()
        self.updateScore(playerNumber,score)

    def playDeterDiceGame(self):
        highestPlayerScore = 0
        self.rollCycles = 0
        
        while highestPlayerScore < 1000:
            self.performNextRound()
            highestPlayerScore = max(self.playerInfo[0]["score"], self.playerInfo[1]["score"])
    
    def determineGameScore(self):
        self.playDeterDiceGame()
        lowestScore = min(self.playerInfo[0]["score"], self.playerInfo[1]["score"])
        gameScore = lowestScore * self.rollCycles
        
        return gameScore
    
    def updateScore(self, playerNumber,score):
        for player in self.playerInfo:
            if player["player"] == playerNumber:
                player["position"] += score
                if player["position"] > 10:
                    modulus = player["position"] % 10
                    if modulus == 0:
                        player["position"] = 10
                    else:
                        player["position"] = modulus
                player["score"] += player["position"]
    
    
    def __throwDiracDice(self, dicePossibilities, maxPoints):
        
        scorePlayer1 = copy.deepcopy(self.playerInfo[0]["score"])
        posPlayer1 = copy.deepcopy(self.playerInfo[0]["position"])
        scorePlayer2 = copy.deepcopy(self.playerInfo[1]["score"])
        posPlayer2 = copy.deepcopy(self.playerInfo[1]["position"])
        
        
        for dice in dicePossibilities:
            self.updateScore(1, dice["throw"])
            if self.playerInfo[0]["score"] >= maxPoints:
                self.universWinsPlayer1 += 1
            else:
                for dice in dicePossibilities:
                    self.updateScore(2, dice["throw"])
                    if self.playerInfo[1]["score"] > maxPoints:
                        self.universWinsPlayer2 += 1
                    else:
                        self.__throwDiracDice(dicePossibilities,maxPoints)
                    self.playerInfo[1]["score"] = scorePlayer2
                    self.playerInfo[1]["position"] = posPlayer2
            
            self.playerInfo[0]["score"] = scorePlayer1
            self.playerInfo[1]["score"] = scorePlayer2
            self.playerInfo[0]["position"] = posPlayer1
            self.playerInfo[1]["position"] = posPlayer2
               
    def mostUniverseWins(self, dicePossibilities, maxPoints):
        self.__throwDiracDice(dicePossibilities, maxPoints) 
        mostWins = max(self.universWinsPlayer1, self.universWinsPlayer2)
        return mostWins
            
def solutionDay21():
    fileReader = FileReader()
    diceRoller = DiceRoller()
    fileString = fileReader.readLinesToStringArray("input/inputday21")
    diceRoller.loadStartPositions(fileString)
    
    answerPart1 = diceRoller.determineGameScore()
    answerPart2 = 0
    printAnswer(20, answerPart1, answerPart2)
    

# %%
