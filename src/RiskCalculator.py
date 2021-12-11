from utils.AocEnums import *
from utils.Operations import *

class RiskCalculator():
    
    def __init__(self):
        self.heightMap = []
        self.mapWidth = 0

    def setHeightMap(self, heightMap):
        self.heightMap = heightMap
        self.mapWidth = len(heightMap[0])
        self.mapHeight = len(heightMap)

    def __getHeightFromMap(self, x,y):
        return self.heightMap[y][x]
    
    def __calcualteRiskLevel(self, height):
        return height+1

    def calculateSumRiskLevels(self):

        riskSum = 0
        for x in range (0, self.mapWidth):
            for y in range(0, self.mapHeight):
                if self.__isRiskSpot(x,y):
                    height = self.__getHeightFromMap(x,y)
                    riskLevel = self.__calcualteRiskLevel(height)
                    riskSum += riskLevel
        
        return riskSum

    def __getHeight(self, x, y, direction = Direction.CURRENT):
        
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
            heightValue = 9
        elif mapy < 0 or mapy > mapHeight: 
            mapy=0
            heightValue = 9
        else:
            heightValue = self.__getHeightFromMap(mapx, mapy)

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
        isUpGreater = self.__isHeightGreater(x, y, Direction.UP)
        isDownGreater = self.__isHeightGreater(x, y, Direction.DOWN)
        isLeftGreater = self.__isHeightGreater(x, y, Direction.LEFT)
        isRightGreater = self.__isHeightGreater(x, y, Direction.RIGHT)

        if isUpGreater and isDownGreater and isLeftGreater and isRightGreater:
            riskSpot = True

        return riskSpot

    def __toListIndex(self,x,y):
        listIndex = x+y*self.mapWidth
        return listIndex

    def createInitalBassin(self,x,y):
        bassin = []
        x_init = x
        y_init = y
        
        if self.__getHeight(x,y) == 9:
            return bassin
        else:
            bassin.append(self.__toListIndex(x,y))

        x = x_init
        for _ in range(self.mapWidth):
            x+=1
            height = self.__getHeight(x,y)
            if height != 9:
                bassin.append(self.__toListIndex(x,y))
            else:
                break
        
        x = x_init
        for _ in range(self.mapWidth):
            x-=1
            height = self.__getHeight(x,y)
            if height != 9:
                bassin.append(self.__toListIndex(x,y))
            else:
                break
        
        x = x_init
        y = y_init
        for _ in range(self.mapHeight):
            y+=1
            height = self.__getHeight(x,y)
            if height != 9:
                bassin.append(self.__toListIndex(x,y))
            else:
                break
        
        y = y_init
        for _ in range(self.mapHeight):
            y-=1
            height = self.__getHeight(x,y)
            if height != 9:
                bassin.append(self.__toListIndex(x,y))
            else:
                break
        
        return bassin

    def createInitialBassinsPerIndex(self):
        bassinsPerIndex = []
        for y in range(0, self.mapHeight):
            for x in range (0, self.mapWidth):
                bassinsPerIndex.append(self.createInitalBassin(x,y))
        
        bassinsPerIndex = [x for x in bassinsPerIndex if x != []]
        
        return bassinsPerIndex

    def __getLengthArray(self, bassinArray):
        bassinSizeArray =[]
        for array in bassinArray:
            bassinSizeArray.append(len(array))
        
        return bassinSizeArray

    def getMultiplicationLargest3Bassins(self):
        bassins = self.createInitialBassinsPerIndex()
        
        mergedbassins = list(merge_common(bassins))
        sizeArray = self.__getLengthArray(mergedbassins)
        threeLargest = Nmaxelements(sizeArray,3)

        multiplication = threeLargest[0] * threeLargest[1] *threeLargest[2]

        return multiplication

        
