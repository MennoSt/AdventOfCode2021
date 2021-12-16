from numpy.lib.polynomial import poly


class Polymarizator:
    
    def __init__(self):
        self.initialPolyString = ""
        self.foldArray = []

    def getUpdatedString(self, initialString, polyPairs, steps):
        
        polyString = initialString
        self.polyPairs = polyPairs
        
        for _ in range(steps):
            polyString = self.updatePolymerTemplate(polyString)

        return polyString

    def updatePolymerTemplate(self, string):        
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