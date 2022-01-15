#%%

from utils.AocUtils import *
from utils.FileReader import FileReader
from utils.Grid import Grid
import copy


class Trenchmapper:
    
    def __init__(self):
        self.enhancementAlgorithm = []
        self.grid = Grid()
        self.lightPixels = 0
    
    def readData(self, inputFile):
        fileReader = FileReader()
        strMap = fileReader.readToStringMap(inputFile)
        self.enhancementAlgorithm = strMap[0]
        
        for _ in range (2):
            strMap.pop(0)


        self.grid.setGrid(strMap)
    
    def getUpdatedPixel(self,x, y):
        
        binaryNumber = self.calculateBinaryNumber(x, y)
        decimalNumber = int(binaryNumber,2)
        updatedPixel = self.enhancementAlgorithm[decimalNumber]
        
        return updatedPixel

    def calculateBinaryNumber(self, x, y):
        binaryNumber = ""
        upperPart = [self.grid.getValue(x-1,y-1), self.grid.getValue(x,y-1), self.grid.getValue(x+1,y-1)]
        middlePart = [self.grid.getValue(x-1,y), self.grid.getValue(x,y), self.grid.getValue(x+1,y)]
        lowerPart = [self.grid.getValue(x-1,y+1), self.grid.getValue(x,y+1), self.grid.getValue(x+1,y+1)]

        
        upperPart = ["." if v is None else v for v in upperPart]
        middlePart = ["." if v is None else v for v in middlePart]
        lowerPart = ["." if v is None else v for v in lowerPart]

        
        for pixel in upperPart:
            binaryNumber += pixel
        for pixel in middlePart:
            binaryNumber += pixel
        for pixel in lowerPart:
            binaryNumber += pixel

        binaryNumber = binaryNumber.replace("#","1")
        binaryNumber = binaryNumber.replace(".","0")
        return binaryNumber

    def __extendGrid(self, Ndots = 3):
        
        mapCopy = copy.deepcopy(self.grid.gridMap)
        
        for line in mapCopy:
            for _ in range(Ndots):
                line.append(".")
                line.insert(0,".")

        lengthMap = len(mapCopy[0])
        addedLine = []
        
        for _ in range(lengthMap):
            addedLine.append(".")
        
        for _ in range(Ndots):
            mapCopy.append(copy.deepcopy(addedLine))
            mapCopy.insert(0,copy.deepcopy(addedLine))
        
        
        self.grid.gridMap = mapCopy
        self.grid.updateMapSizes()
    
    def __updateGrid(self):
        updatedGrid = copy.deepcopy(self.grid)    

        for x in range(0,self.grid.mapWidth):
            for y in range(0,self.grid.mapHeight):
                updatedPixel = self.getUpdatedPixel(x,y)
                updatedGrid.setValue(x, y, updatedPixel)
        
        width = updatedGrid.mapWidth-2
        height = updatedGrid.mapHeight-2
        for line in updatedGrid.gridMap:
            line.pop(0)
            line.pop(width)
        
        updatedGrid.gridMap.pop(0)
        updatedGrid.gridMap.pop(height)    

        updatedGrid.updateMapSizes()
        self.grid = updatedGrid
    
    
    def enhanceImage(self, NTimes):
        
        self.__extendGrid(5)
        for _ in range(0,NTimes):
            self.__updateGrid()            
        
        self.lightPixels = self.grid.countElementsInGrid("#")
        
def solutionDay20():
    trenchMapper = Trenchmapper()
    trenchMapper.readData("input/inputday20")
    trenchMapper.enhanceImage(2)
    
    answerPart1 = trenchMapper.lightPixels
    
    answerPart2 = 0
    
    printAnswer(20, answerPart1, answerPart2)
    
    
# %%
