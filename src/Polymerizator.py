import numpy as np


class Polymarizator:
    
    def __init__(self):
        self.polyString = ""
        self.polyPairs = []
    
    def getMostCommonMinusLeastCommon(self, initialString, polyPairs,steps):
        string = self.getUpdatedString(initialString, polyPairs, steps)

        substraction = self.calculateDiffMostCommonAndLeastCommon(string)
        
        return substraction

    def calculateDiffMostCommonAndLeastCommon(self, string):
        array = np.array(self.polyPairs)
        insertChars = set(array[:,1])
        
        countArray = []
        counts = []
        for character in insertChars:
            countValue = string.count(character)
            counts.append(countValue)
            countArray.append([character, countValue])
        
        maxValue = max(counts)
        minValue = min(counts)
        substraction = maxValue - minValue
        return substraction

    def getUpdatedString(self, initialString, polyPairs, steps):
        
        polyString = initialString
        self.polyPairs = polyPairs
        step = 0
        
        for _ in range(steps):
            polyString = self.__updatePolymerTemplate(polyString)
            step+=1

        return polyString

    def __updatePolymerTemplate(self, string):        
        polyInsertions = self.__determinePolyInsertions(string)
        string = self.__updateStringWithInsertions(polyInsertions,string)
            
        return string
    
    def __updateStringWithInsertions(self, polyInsertions, string):
        shift=0
        for index in range(0,len(polyInsertions)):
            k = polyInsertions[index][0]+shift
            string = string[:k] + polyInsertions[index][1] + string[k:]
            shift+=1
            
        return string
        
    def __determinePolyInsertions(self, string):
        polyInsertions =[]
        
        for i in range(0,len(string)-1):
            for pair in self.polyPairs:
                if string[i:i+2] in pair[0]:
                    index = [i+1,pair[1]]
                    polyInsertions.append(index)
        
        return polyInsertions