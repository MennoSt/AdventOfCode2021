from utils.AocUtils import *
from utils.AocEnums import *
import copy



class SnailFishUpdater:

    def updateList(self, initialList):
        i_initialList = copy.deepcopy(initialList)
        
        for index1 in range(0, len(i_initialList)):
            if isinstance(i_initialList[index1], list):
                for index2 in range(0, len(i_initialList[index1])):
                    if isinstance(i_initialList[index1][index2], list):
                        for index3 in range(0, len(i_initialList[index1][index2])):
                            if isinstance(i_initialList[index1][index2][index3], list):
                                for index4 in range(0, len(i_initialList[index1][index2][index3])):
                                    if isinstance(i_initialList[index1][index2][index3][index4], list):
                                        i_depth0 = i_initialList
                                        i_depth1 = i_initialList[index1]
                                        i_depth2 = i_initialList[index1][index2]
                                        i_depth3 = i_initialList[index1][index2][index3]
                                        self.i_depth4 = i_initialList[index1][index2][index3][index4]
                                        
                                        depth0 = initialList
                                        depth1 = initialList[index1]
                                        depth2 = initialList[index1][index2]
                                        depth3 = initialList[index1][index2][index3]
                                        depth4 = initialList[index1][index2][index3][index4]
                                        self.depth4 = initialList[index1][index2][index3][index4]
                                                          
                                        if index4-1 >= 0:
                                            self.updateFourthNestedList(index4, i_depth3, Direction.LEFT)
                                        elif index3-1 >= 0:
                                            self.addExplodedValue(index3, i_depth2, depth2, Direction.LEFT)
                                        elif index2-1 >= 0:
                                            self.addExplodedValue(index2, i_depth1, depth1, Direction.LEFT)
                                        elif index1-1 >= 0:
                                            self.addExplodedValue(index1, i_depth0, depth0, Direction.LEFT)
                                        else:
                                            initialList[index1][index2][index3][index4][0] = 0
                                            
                                        if index4+1 < len(i_depth3):
                                            self.updateFourthNestedList(index4, i_depth3, Direction.RIGHT)
                                        elif index3+1 < len(i_depth2):
                                            self.addExplodedValue(index3, i_depth2, depth2, Direction.RIGHT)
                                        elif index2+1 < len(i_depth1):
                                            self.addExplodedValue(index2, i_depth1, depth1, Direction.RIGHT)
                                        elif index1+1 < len(i_depth0):
                                            self.addExplodedValue(index1, i_depth0, depth0, Direction.RIGHT)
                                        else:
                                            initialList[index1][index2][index3][index4][1] = 0
                                        
                                        initialList[index1][index2][index3] = initialList[index1][index2][index3][index4]
    
        return initialList

    def updateFourthNestedList(self, index4, i_depth3, direction=Direction.RIGHT):
        
        if direction == Direction.RIGHT:
            i = 1
            dir = 1
        else:
            i = -1
            dir = 0
        
        if type(i_depth3[index4+i]) == list:
            self.depth4[dir] += i_depth3[index4+i][0]
        else:
            self.depth4[dir] += i_depth3[index4+i]

    def addExplodedValue(self, index, i_depth, depth, direction=Direction.RIGHT):
        if direction == Direction.RIGHT:
            i = 1
            dir = 1
        else:
            i = -1
            dir = 0
            
        if type(i_depth[index+i ]) == list:
            depth[index+i] += self.i_depth4[dir]
            self.depth4[dir] = 0
        else:
            depth[index+i] += self.i_depth4[dir]
            self.depth4[dir] = 0
            

def hasNestedDepth(depth, nestedList):
    nestCounter = 0
    for _ in range(depth):
        if any(isinstance(i,list) for i in nestedList):
            nestedList = nestedList[0]
            nestCounter +=1

    if nestCounter == depth:
        return True
    else:
        return False
    
    

def solutionDay18():
    return