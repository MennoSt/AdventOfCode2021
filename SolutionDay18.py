from utils.AocUtils import *
from utils.FileReader import FileReader

class SnailFishUpdater:

    def updateList(self, initialList):
        for index1 in range(0, len(initialList)):
            if isinstance(initialList[index1], list):
                for index2 in range(0, len(initialList[index1])):
                    if isinstance(initialList[index1][index2], list):
                        for index3 in range(0, len(initialList[index1][index2])):
                            if isinstance(initialList[index1][index2][index3], list):
                                for index4 in range(0, len(initialList[index1][index2][index3])):
                                    if isinstance(initialList[index1][index2][index3][index4], list):
                                        left = index3-1
                                        right = index3+1
                                        
                                        if left >= 0:
                                            initialList[index1][index2][index3][index4][0] += initialList[index1][index2][index3][index3-1]
                                        else:
                                            initialList[index1][index2][index3][index4][0] = 0
                                            
                                        if right < len(initialList[index1][index2][index3]):
                                            initialList[index1][index2][index3][index4][1] += initialList[index1][index2][index3][index3+1]
                                        else:
                                            initialList[index1][index2][index3][index4][1] = 0
                                        initialList[index1][index2][index3] = initialList[index1][index2][index3][index4]
                                        break
    
        return initialList

initialList = [[[[[9,8],1],2],3],4]
initialList = [7,[6,[5,[7,0]]]]
snailFishUpdater = SnailFishUpdater()
list2 = snailFishUpdater.updateList(initialList)
print(list2)

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