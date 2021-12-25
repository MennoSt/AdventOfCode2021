from utils.AocUtils import *
from utils.AocEnums import *
from utils.FileReader import FileReader
import copy
import math
import ast


class SnailFishUpdater:
    def __init__(self):
         self.fishLists = []
         
    def readDataIntoLists(self, input):
        fileReader = FileReader()
        self.fishLists = fileReader.readLinesToListArray(input)

    def calculateFinalSum(self):
        
        updatedList = self.fishLists[0]
        
        for index in range(0, len(self.fishLists)-1):
            updatedList = self.addTwoLists(updatedList, self.fishLists[index+1])
            print(updatedList)
            updatedList = self.updateSnailFishNumbers(updatedList)
        
        return updatedList
            
    def addTwoLists(self, list1, list2):
        listSum = [list1,list2]
        return listSum
    
    def updateSnailFishNumbers(self, initialList):
        
        listChanged = True
        updatedList = initialList
        
        print("New Update:")
        
        while(listChanged):
            startList = copy.deepcopy(updatedList)
            updatedList = self.updateListWithExplosions(updatedList)
            print("after explosions" + str(updatedList))
            updatedList = self.updateListWithSplits(updatedList)
            print("after splits" + str(updatedList))
            if startList == updatedList:
                listChanged = False
            else:
                listChanged = True
        
        return updatedList
        
    def updateListWithSplits(self,initialList):
        
        for index1 in range(0, len(initialList)):
            self.__splitListIfHigherThanTen(initialList, index1)
            
            if isinstance(initialList[index1], list):
                for index2 in range(0, len(initialList[index1])):
                    self.__splitListIfHigherThanTen(initialList[index1], index2)
                    
                    if isinstance(initialList[index1][index2], list):
                        for index3 in range(0, len(initialList[index1][index2])):
                            self.__splitListIfHigherThanTen(initialList[index1][index2], index3)
                            
                            if isinstance(initialList[index1][index2][index3], list):
                                for index4 in range(0, len(initialList[index1][index2][index3])):
                                    self.__splitListIfHigherThanTen(initialList[index1][index2][index3], index4)
        
        return initialList

    def __splitListIfHigherThanTen(self, initialList, index1):
        tmpList = initialList[index1]
        if type(initialList[index1]) != list:
            if initialList[index1] > 9:
                initialList[index1] =[math.floor(initialList[index1]/2), math.ceil(initialList[index1]/2)]
        
        
    def updateListWithExplosions(self, initialList):
        
        for index1 in range(0, len(initialList)):
            if isinstance(initialList[index1], list):
                for index2 in range(0, len(initialList[index1])):
                    if isinstance(initialList[index1][index2], list):
                        for index3 in range(0, len(initialList[index1][index2])):
                            if isinstance(initialList[index1][index2][index3], list):
                                for index4 in range(0, len(initialList[index1][index2][index3])):
                                    if isinstance(initialList[index1][index2][index3][index4], list):
                                        
                                        self.depth0 = initialList
                                        self.depth1 = initialList[index1]
                                        self.depth2 = initialList[index1][index2]
                                        self.depth3 = initialList[index1][index2][index3]
                                        self.depth4 = initialList[index1][index2][index3][index4]
                                                          
                                        if index4-1 >= 0:
                                            self.__updateFourthNestedList(index4, Direction.LEFT)
                                        elif index3-1 >= 0:
                                            self.__addExplodedValue(index3, self.depth2, Direction.LEFT)
                                        elif index2-1 >= 0:
                                            self.__addExplodedValue(index2, self.depth1, Direction.LEFT)
                                        elif index1-1 >= 0:
                                            self.__addExplodedValue(index1, self.depth0, Direction.LEFT)
                                            
                                        if index4+1 < len(self.depth3):
                                            self.__updateFourthNestedList(index4, Direction.RIGHT)
                                        elif index3+1 < len(self.depth2):
                                            self.__addExplodedValue(index3, self.depth2, Direction.RIGHT)
                                        elif index2+1 < len(self.depth1):
                                            self.__addExplodedValue(index2, self.depth1, Direction.RIGHT)
                                        elif index1+1 < len(self.depth0):
                                            self.__addExplodedValue(index1, self.depth0, Direction.RIGHT)

                                        initialList[index1][index2][index3][index4] = 0
    
        return initialList

    def __updateFourthNestedList(self, index4, direction=Direction.RIGHT):
        
        if direction == Direction.RIGHT:
            i = 1
            dir = 1
        else:
            i = -1
            dir = 0
            
        if type(self.depth3[index4+i]) == list:
            self.depth3[index4+i][0] += self.depth4[dir]
        else:
            self.depth3[index4+i] += self.depth4[dir]

    def __addExplodedValue(self, index, depth, direction=Direction.RIGHT):
        if direction == Direction.RIGHT:
            i = 1
            dir = 1
        else:
            i = -1
            dir = 0
            
        if type(depth[index+i]) == list:
            depth[index+i][0] += self.depth4[dir]
            self.depth4[dir] = 0
        else:
            depth[index+i] += self.depth4[dir]
            self.depth4[dir] = 0
    

def solutionDay18():
    fileReader = FileReader()
    listArray = fileReader.readLinesToListArray("input/inputday18")
    
    