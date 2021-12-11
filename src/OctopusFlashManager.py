from re import X
from utils.Grid import Grid
import copy

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def left(self):
        return [self.x-1,self.y]

class OctopusFlashManager:
    
    def __init__(self):
        self.grid = Grid()
        self.flashCounter = 0

    def setOctopusMap(self, octopusMap):
        self.grid.setGrid(copy.deepcopy(octopusMap))

    def getNumberOfFlashes(self, cycles):
        for _ in range(cycles):
            self.__updateOneCycle()
        
        return self.flashCounter
    
    def getFirstSynchronicCycle(self):
        cycle = 0
        while(True):
            self.__updateOneCycle()
            sumFlashArray = sum(map(sum,self.grid.gridMap))
            cycle += 1
            if sumFlashArray == 0:
                return cycle

    def __updateOneCycle (self):
        
        self.__increaseGridByOne()

        while(self.grid.hasValueGreaterThan(9)):
            self.__updateFlashes()

    def __updateFlashes(self):
        for x in range(0, self.grid.mapWidth):
            for y in range(0,self.grid.mapHeight):
                flashValue = self.grid.getValue(x,y)
                if flashValue > 9:
                    self.grid.gridMap[y][x] = 0
                    self.__increaseSurroundingGridsByOne(x,y)
                    self.flashCounter += 1

    def __increaseSurroundingGridsByOne(self,x,y):
        self.__increaseGridPointByOneAfterFlash(x+1,y-1)
        self.__increaseGridPointByOneAfterFlash(x+1,y+1)
        self.__increaseGridPointByOneAfterFlash(x+1,y)
        self.__increaseGridPointByOneAfterFlash(x-1,y)
        self.__increaseGridPointByOneAfterFlash(x-1,y-1)
        self.__increaseGridPointByOneAfterFlash(x-1,y+1)
        self.__increaseGridPointByOneAfterFlash(x,y+1)
        self.__increaseGridPointByOneAfterFlash(x,y-1)

    def __increaseGridPointByOneAfterFlash(self, x,y):
        flashLevel = self.grid.getValue(x,y)
        if flashLevel != None and flashLevel != 0:
            self.grid.gridMap[y][x] += 1

    def __increaseGridByOne(self):
        for x in range(0, self.grid.mapWidth):
            for y in range(0,self.grid.mapHeight):
                flashLevel = self.grid.getValue(x,y)
                if flashLevel != None:
                    self.grid.gridMap[y][x] += 1

            





            



