from utils.AocEnums import *

class Grid:

    def __init__(self):
        self.heightMap = []
        self.mapWidth = []
        self.mapHeight = []
    
    def setGrid(self, heightMap):
        self.heightMap = heightMap
        self.mapWidth = len(heightMap[0])
        self.mapHeight = len(heightMap)

    def getValue(self, x, y):
        return self.heightMap[y][x]

    def getValue(self, x, y, direction = Direction.CURRENT):
        
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
            heightValue = self.heightMap[mapy][mapx]

        return heightValue
            