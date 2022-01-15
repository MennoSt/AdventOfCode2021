from utils.AocUtils import *
from utils.FileReader import FileReader

# %%

class DiceRoller:
    
    def __init__(self):
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
    
    def throwDices(self):
        self.diceOne += 3
        self.diceTwo += 3
        self.diceThree += 3
        self.totalScore = self.diceOne + self.diceTwo + self.diceThree
    
    def performNextRound(self):
        self.playerThrowsDice(1)
        self.playerThrowsDice(2)

    def playerThrowsDice(self, playerNumber):
        self.throwDices()
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
        
def solutionDay21():
    fileReader = FileReader()
    diceRoller = DiceRoller()
    fileString = fileReader.readLinesToStringArray("testinput/unittestinputday21")
    diceRoller.loadStartPositions(fileString)
    diceRoller.performNextRound()
    
solutionDay21()

# %%
