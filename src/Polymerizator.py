import numpy as np
import copy
import math
from numpy.lib.polynomial import poly

class Polymers:
    
    def __init__(self):
        self.Polymer = []
        self.Connection = []
        self.nextGen = []
        self.Count = []
    
    def initPolymer(self, polyPairs):
        self.Polymer = []
        self.Connection = []
        self.nextGen = []
        self.Count = []
        
        for pair in polyPairs:
            self.Polymer.append(pair[0])
            self.Connection.append(pair[1])
            self.Count.append([pair[0],0])
            element1 = pair[0][0] + pair[1]
            element2 = pair[1] + pair[0][1]
            self.nextGen.append([element1, element2])
            


class Polymarizator:
    
    def __init__(self):
        self.polyString = ""
        self.polyPairs = []
        self.polymers = Polymers()
        self.length = 0
    
    def updatePolyCyclus(self, initialString, polyPairs, steps):
        
        self.polymers.initPolymer(polyPairs)
        self.__initializeCounterList(initialString)
        
        for _ in range(steps):
            self.updateToNextGeneration()
        
        singleCount = self.getSingleCountArray()
        countArray = []
        for count in singleCount:
            countArray.append(count[1])
            
        maxValue = max(countArray)
        minValue = min(countArray)
        
        difference = maxValue - minValue
        return difference

    def getSingleCountArray(self):
        array = np.array(self.polymers.Connection)
        insertChars = set(array)

        CountArray = []
        for character in insertChars:
            sumChar = 0
            for count in self.polymers.Count:
                number = count[0].count(character)
                if number > 0:
                    sumChar += number*count[1]
            
            sumChar = int((math.ceil(sumChar/2)))
            CountArray.append([character, sumChar])
            sumChar = 0     
        
        return CountArray
        
    def updateToNextGeneration(self):
        polymerCurrent = copy.deepcopy(self.polymers)
        
        for index in range(0,len(polymerCurrent.Count)):
            if polymerCurrent.Count[index][1] > 0:
                nextgen1 = polymerCurrent.nextGen[index][0]
                nextgen2 = polymerCurrent.nextGen[index][1]
                polymer = polymerCurrent.Polymer[index]
                count = polymerCurrent.Count[index][1]
                self.decreaseCounterArray(polymer, count)
                self.increaseCounterArray(nextgen1 , polymerCurrent.Count[index][1])
                self.increaseCounterArray(nextgen2 , polymerCurrent.Count[index][1])
    
    def __initializeCounterList(self, initialString):
        for count in self.polymers.Count:
            counts = initialString.count(count[0])
            if counts > 0:
                count[1] += counts
    
    def increaseCounterArray(self, str, number = 1):
        for index in range(0, len(self.polymers.Count)):
            if self.polymers.Polymer[index] == str:
                self.polymers.Count[index][1] += number
    
    def decreaseCounterArray(self, str, number = 1):
        for index in range(0, len(self.polymers.Count)):
            if self.polymers.Polymer[index] == str:
                self.polymers.Count[index][1] -= number            
                
    
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