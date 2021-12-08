class PatternAnalyzer:
    def __init__(self):
        self.stringSeven = []
        self.stringFour = []
        self.stringOne = []

    def getNumberOfDigitInstances(self, digitArray):

        totalDigitSum = 0
        for pattern in digitArray:
            totalDigitSum += self.calculateDigitSum(pattern)
            
        return totalDigitSum

    def calculateDigitSum(self, pattern):

        digitSum = 0
        intArray = [1,4,7,8]
        digitsArray = self.convertIntToDigitLengthArray(intArray)
        
        for value in pattern:
            length = len(value)
            if length in digitsArray:
                digitSum += 1

        return digitSum 

    def convertIntToDigitLengthArray(self, IntArray):
        
        digitsArray = []
        for value in IntArray:
            if value == 1 :
                digitsArray.append(2)
            if value == 4:
                digitsArray.append(4)
            if value == 7:
                digitsArray.append(3)
            if value == 8:
                digitsArray.append(7)
        
        return digitsArray
    

    def calculateSumAdditionPart2(self, digitArrayAll, uniquePatternArrayAll):

        totalDigitSum = 0
        for pattern in digitArrayAll:
            totalDigitSum += self.determineIntNumberTotal(pattern, uniquePatternArrayAll)
            
        return totalDigitSum
    
    def determineIntNumberTotal(self, digitArray, uniquePatternArray):
        result = ""

        self.UpdateInitalStrings(uniquePatternArray)

        for pattern in digitArray:
            result += str(self.determineIntNumber(pattern))
        
        return int(result)
    
    def UpdateInitalStrings(self,array):
        returnArray = [1,4,7,8]
        digitsArray = self.convertIntToDigitLengthArray(returnArray)

        for element in array:
            length = len(element)
            if length in digitsArray:
                if length == 3 :
                    self.stringSeven = list(element)
                elif length == 4:
                    self.stringFour = list(element)
                elif length == 2:
                    self.stringOne = list(element)
                else:
                    Exception("length is not valid")
        




    def determineIntNumber(self, string):
        
        returnArray = [1,4,7,8]
        digitsArray = self.convertIntToDigitLengthArray(returnArray)
        length = len(string)
        
        if length in digitsArray:
            if length == 7:
                return 8
            elif length == 3 :
                return 7
            elif length == 4:
                return 4
            elif length == 2:
                return 1
            else:
                Exception("length is not valid")

        
        # return 6 or 9 when the length is equal to six
        if length == 6:
            if all(char in string for char in self.stringFour):
                return 9
            elif all(char in string for char in self.stringSeven):
                return 0
            else:
                return 6

        #return 2,3 or 5 when the length is equal to five
        if length == 5:
            if all(char in string for char in self.stringOne):
                return 3
            elif all(char in string for char in self.stringFour):
                return 5
            else:
                return 2
            