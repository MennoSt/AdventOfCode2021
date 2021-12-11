from enum import Enum

class Direction(Enum):
    CURRENT = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class char(str, Enum):
    bracketOpen = "{"
    roundOpen = "("
    arrowOpen = "<"
    squareOpen = "["
    arrowClosed = ">"
    roundClosed = ")"
    bracketClosed = "}"
    squareClosed = "]"