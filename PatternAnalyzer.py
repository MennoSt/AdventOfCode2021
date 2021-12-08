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
        lengthData = len(digitArrayAll)
        totalDigitSum = 0

        for index in range(0,lengthData):
            self.UpdateInitalStrings(uniquePatternArrayAll[index])
            totalDigitSum += self.determineIntNumberTotal(digitArrayAll[index])
            
        return totalDigitSum
    
    def determineIntNumberTotal(self, digitArray):
        result = ""

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
        number = None

        
        if length in digitsArray:
            if length == 7:
                number = 8
            elif length == 3 :
                number = 7
            elif length == 4:
                number = 4
            elif length == 2:
                number = 1
            else:
                Exception("length is not valid")
        
        # return 0,6 or 9 when the length is equal to six
        if length == 6:
            if all(char in string for char in self.stringFour):
                number = 9
            elif all(char in string for char in self.stringSeven):
                number = 0
            else:
                number = 6

        #return 2,3 or 5 when the length is equal to five
        if length == 5:
            if all(char in string for char in self.stringOne):
                number = 3
            elif len(list(set(string).intersection(self.stringFour))) == 3:
                number = 5
            else:
                number = 2
        
        return number