from enum import Enum

class char(str, Enum):
    bracketOpen = "{"
    roundOpen = "("
    arrowOpen = "<"
    squareOpen = "["
    arrowClosed = ">"
    roundClosed = ")"
    bracketClosed = "}"
    squareClosed = "]"

class SyntaxScoreBoard:

    def __init__(self):
        self.roundScore = 3
        self.squareScore = 57
        self.bracketScore = 1197
        self.arrowScore = 25137

    def calculateScore(self, array):
        rounds = array.count(char.roundClosed)
        squares = array.count(char.squareClosed)
        brackets = array.count(char.bracketClosed)
        arrows = array.count(char.arrowClosed)

        score = self.roundScore * rounds + self.squareScore * squares\
            +  self.bracketScore * brackets+ self.arrowScore * arrows
            
        return(score)
    
    def calculateAutoCompletionScore(self, completionString):
        score = 0
        addition = 0

        for part in completionString:
            if part == char.roundClosed:
                addition = 1
            elif part == char.squareClosed:
                addition = 2
            elif part == char.bracketClosed:
                addition = 3
            elif part == char.arrowClosed:
                addition = 4

            score = score*5 + addition
        
        return score




            



