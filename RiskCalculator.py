from enum import Enum
from re import I

class Direction(Enum):
        CURRENT = 0
        UP = 1
        DOWN = 2
        LEFT = 3
        RIGHT = 4

class RiskCalculator():
    
    def __init__(self):
        self.heightMap = []
        self.mapWidth = 0

    def setHeightMap(self, heightMap):
        self.heightMap = heightMap
        self.mapWidth = len(heightMap[0])
        self.mapHeight = len(heightMap)
    
    def __calcualteRiskLevel(self, height):
        return height+1

    def __getHeightFromMap(self, x,y):
        return self.heightMap[y][x]

    def calculateSumRiskLevels(self):

        riskSum = 0
        mapWidth = self.mapWidth
        mapHeight = self.mapHeight
        for x in range (0, mapWidth):
            for y in range(0, mapHeight):
                if self.__isRiskSpot(x,y):
                    height = self.__getHeightFromMap(x,y)
                    riskLevel = self.__calcualteRiskLevel(height)
                    riskSum += riskLevel
        
        return riskSum

    def __getHeight(self, x, y, direction):
        
        mapx = x
        mapy = y

        if direction == Direction.CURRENT:
            mapx = x
            mapy = y
        if direction == Direction.UP:
            mapx = x
            mapy = y + 1
        if direction == Direction.DOWN:
            mapx = x
            mapy = y -1
        if direction == Direction.LEFT:
            mapx = x-1
            mapy = y
        if direction == Direction.RIGHT:
            mapx = x + 1
            mapy = y
        
        # Return the lowest index 0 if the mapIndex is out of the map range
        mapWidth = int(self.mapWidth) -1
        mapHeight = int(self.mapHeight) -1

        if mapx < 0 or mapx > mapWidth: 
            mapx=0
            heightValue = 99
        elif mapy < 0 or mapy > mapHeight: 
            mapy=0
            heightValue = 99
        else:
            heightValue = self.__getHeightFromMap(mapx,mapy)

        return heightValue

    def __isHeightGreater(self, x,y, direction):
        heightDirection = self.__getHeight(x,y, direction)
        heightCurrent = self.__getHeight(x,y, Direction.CURRENT)
        
        if heightDirection > heightCurrent:
            return True
        else:
            return False

    def __isRiskSpot(self, x, y):
        riskSpot = False
        isUpGreater = self.__isHeightGreater(x,y, Direction.UP)
        isDownGreater = self.__isHeightGreater(x,y, Direction.DOWN)
        isLeftGreater = self.__isHeightGreater(x,y, Direction.LEFT)
        isRightGreater = self.__isHeightGreater(x,y, Direction.RIGHT)

        if isUpGreater and isDownGreater and isLeftGreater and isRightGreater:
            riskSpot = True

        return riskSpot

            




