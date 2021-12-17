import copy
from utils.AocEnums import Direction
from utils.Grid import Grid

class Dijkstra:
    def __init__(self):
        self.initialGrid = Grid()
        self.dijkstraGrid = Grid()
    
    def setGrid(self, gridMap, extendMap = False):
        copyGridMap = copy.deepcopy(gridMap)
        
        if extendMap == True:
            self.extendGridMap(copyGridMap)
            self.initialGrid.setGrid(copyGridMap)
        else:
            self.initialGrid.setGrid(copyGridMap)
        
        array = [[999999 for col in range(self.initialGrid.mapHeight)] for row in range(self.initialGrid.mapWidth)]
        array[0][0] = 0
        self.dijkstraGrid.setGrid(array)
    
    def extendGridMap(self,gridmap):
        for line in gridmap:
            lineCopy = copy.deepcopy(line)
            for i in range(1,5):
                line+=self.__increaseLineByValue(lineCopy,i)
        
        copyGridmap = copy.deepcopy(gridmap)
        for i in range(1,5):
            for line in copyGridmap:
                lineCopy = copy.deepcopy(line)
                gridmap.append(self.__increaseLineByValue(lineCopy,i))

        for line in gridmap:
            for index in range(0,len(line)):
                if line[index] > 9:
                    line[index] -= 9
                    
    def __increaseLineByValue(self, line, value):
            
        incrementedList = [x+value for x in line]
                   
        return incrementedList
        
    def findShortestPath(self):
        
        self.iterateThroughGrid()
        shortestPath = self.dijkstraGrid.getValue(self.dijkstraGrid.mapWidth-1, self.dijkstraGrid.mapHeight-1)
        return shortestPath
    
    def iterateThroughGrid(self):
        # directions = [Direction.RIGHT, Direction.UP, Direction.DOWN, Direction.LEFT]
        directions = [Direction.LEFT, Direction.UP, Direction.DOWN, Direction.RIGHT]
        for y in range(0,self.dijkstraGrid.mapHeight):
            for x in range(0,self.dijkstraGrid.mapWidth):
                for direction in directions:
                    self.updateDijkstra(y, x, direction)

        # self.initialGrid.printGrid("Initial")
        self.dijkstraGrid.printGrid("Dijkstra")

    def updateDijkstra(self, y, x, direction):

        value = self.initialGrid.getValue(x,y,direction)
        if value != None:
            valueCurrent = self.dijkstraGrid.getValue(x,y)
            updatedValueDijkstra = value + valueCurrent
            currentValueDijkstra = self.dijkstraGrid.getValue(x,y,direction)
                
            if updatedValueDijkstra < currentValueDijkstra:
                self.dijkstraGrid.setValue(x,y,updatedValueDijkstra, direction)
        else:
            return