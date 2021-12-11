from utils.AocEnums import *

class Grid:

    def __init__(self):
        self.gridMap = 0
        self.mapWidth = 0
        self.mapHeight = 0
    
    def setGrid(self, heightMap):
        self.gridMap = heightMap
        self.mapWidth = len(heightMap[0])
        self.mapHeight = len(heightMap)


    def getValue(self, x, y):
        mapWidth = self.mapWidth-1
        mapHeight = self.mapHeight -1
        if x < 0 or x > mapWidth or y < 0 or y > mapHeight:
            value = None
        else:
            value = self.gridMap[y][x]

        return value
    
    def hasValueGreaterThan(self, value):
        boolGreaterThan = False
        for x in range (0, self.mapWidth):
            for y in range(0, self.mapHeight):
                if self.gridMap[x][y] > 9:
                    boolGreaterThan = True
        
        return boolGreaterThan

    def getValueDirection(self, x, y, direction = Direction.CURRENT):

        value = 0
        if direction == Direction.CURRENT:
            value = self.getValue(x, y)
        if direction == Direction.UP:
            value = self.getValue(x, y+1)
        if direction == Direction.DOWN:
            value = self.getValue(x, y-1)
        if direction == Direction.LEFT:
            value = self.getValue(x-1, y)
        if direction == Direction.RIGHT:
            value = self.getValue(x+1, y)

        return value


    def getHeightValue(self, x, y, direction = Direction.CURRENT):
        
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
            mapx = 0
            heightValue = 9
        elif mapy < 0 or mapy > mapHeight: 
            mapy = 0
            heightValue = 9
        else:
            heightValue = self.gridMap[mapy][mapx]

        return heightValue
            