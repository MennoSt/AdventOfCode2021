from utils.AocEnums import *
from utils.Operations import *

from src.SyntaxScoreBoard import SyntaxScoreBoard

class SyntaxManager:

    def __init__(self):
        self.SyntaxScoreBoard = SyntaxScoreBoard()
        self.openingCharacters = ["(", "[", "{", "<"]
        self.closingCharacters = [")", "]", "}", ">"]
    
    def __convertOpenToClosedCharacterString(self, charactersToAdd):
        string = ""
        for character in charactersToAdd:
            if character == char.bracketOpen:
                string += char.bracketClosed
            elif character == char.roundOpen:
                string += char.roundClosed
            elif character == char.arrowOpen:
                string += char.arrowClosed
            elif character == char.squareOpen:
                string+= char.squareClosed
        
        return string

    def autoCompleteLine(self, string):
        charactersToAdd =[]

        if self.checkOnSyntaxError(string) == None:
            for char in string:
                if self.__isClosingCharacter(char):
                    charactersToAdd.pop()
                if self.__isOpeningCharacter(char):
                    charactersToAdd.append(char)
        else:
            charactersToAdd = None

        if(charactersToAdd != None):
            charactersToAdd.reverse() #since the to be added characters are appended at the end of the array
            charactersToAdd = self.__convertOpenToClosedCharacterString(charactersToAdd)

        return charactersToAdd

    def calculateMiddleScore(self, navigationLines):
       
        autoCompletionLines = []
        for line in navigationLines:
            autoCompletionLines.append(self.autoCompleteLine(line))

        autoCompletionLines = list(filter(None, autoCompletionLines))

        autoCompletionScores = []
        for line in autoCompletionLines:
            autoCompletionScore = self.SyntaxScoreBoard.calculateAutoCompletionScore(line)
            autoCompletionScores.append(autoCompletionScore)

        autoCompletionScores.sort()
        middle = findMiddle(autoCompletionScores)

        return middle

    def calculateSyntaxErrorScore(self, navigationLines):

        errorChars = []
        for line in navigationLines:
            errorChars.append(self.checkOnSyntaxError(line))
        
        errorScore = self.SyntaxScoreBoard.calculateScore(errorChars)

        return errorScore

    def checkOnSyntaxError(self, string):
        errorChar = None
        openChars = []

        for char in string:
            if self.__isClosingCharacter(char):
                lastOpenChar = openChars.pop()
                if not self.__areCharactersPaired(lastOpenChar, char):
                    errorChar = char
                    break
            
            if self.__isOpeningCharacter(char):
                openChars.append(char)

        return errorChar

    def __areCharactersPaired(self, openChar, closedChar):
    
        roundPair = (openChar == char.roundOpen and closedChar == char.roundClosed)
        bracketPair = (openChar == char.bracketOpen and closedChar == char.bracketClosed)
        arrowPair = (openChar == char.arrowOpen and closedChar == char.arrowClosed)
        squarePair = (openChar == char.squareOpen and closedChar == char.squareClosed)

        return (roundPair or bracketPair or arrowPair or squarePair)

    def __isOpeningCharacter(self, char):
        if char in self.openingCharacters:
            return True
        else:
            return False
    
    def __isClosingCharacter(self, char):
        if char in self.closingCharacters:
            return True
        else:
            return False


            



