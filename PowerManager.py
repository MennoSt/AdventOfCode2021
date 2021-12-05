class PowerManager:
    
    def __init__(self):
        self.binList = []
        self.oxygenRating = []
        self.co2ScrubberRating = []

    def getMostCommenBit(self, binList, Nth):
        zeroCounter = 0
        oneCounter = 0
        totalNumbers = len(binList)

        for number in range(0, totalNumbers):
            value = binList[number][Nth]
            if value == "0":
                zeroCounter += 1
            elif value == "1":
                oneCounter += 1
        
        if (zeroCounter > oneCounter):
            return "0"
        elif (oneCounter > zeroCounter):
            return "1"
        elif (oneCounter == zeroCounter):
            return "1"
        else:
            raise Exception("No Zero and No one is bigger")
    
    def getLeastCommenBit(self, binList, Nth):
        commonBit = self.getMostCommenBit(binList,Nth)
        if commonBit == "1":
            return "0"
        if commonBit == "0":
            return "1"


    def InvertBitString(self, b_string):
        ib_string = ""

        for bit in b_string:
            if bit == "1":
                ib_string += "0"
            else:
                ib_string += "1"

        return ib_string

    def CalculateRequiredPower(self, binList):
        
        numberOfCharacters = len(binList[0])
        string = ""

        for index in range (0, numberOfCharacters):
            mostCommonBitValue = self.getMostCommenBit(binList, index)
            string += mostCommonBitValue
            
        inverted_str = self.InvertBitString(string)

        gammaRate = int(string,2)
        epsilonRate = int(inverted_str,2)

        return gammaRate*epsilonRate
    
    def UpdateOxygenArray(self, mostCommonBith, index):
        
        listLength = len(self.oxygenRating)
        arrayTmpOxy = []

        for number in range (0, listLength):
            bitValue = self.oxygenRating[number][index]
            if bitValue == mostCommonBith:
                arrayTmpOxy.append(self.oxygenRating[number])

        self.oxygenRating = arrayTmpOxy
    
    def UpdateScrubArray(self, leastCommonBith, index):
        
        listLength = len(self.co2ScrubberRating)
        arrayTmpScrub = []

        for number in range (0, listLength):
            bitValue = self.co2ScrubberRating[number][index]
            if bitValue == leastCommonBith:
                arrayTmpScrub.append(self.co2ScrubberRating[number])

        self.co2ScrubberRating = arrayTmpScrub

    def CalculateLifeSupport(self, binList):
        
        self.binList = binList
        self.oxygenRating = binList
        self.co2ScrubberRating = binList
        numberOfCharacters = len(self.binList[0])


        for index in range (0, numberOfCharacters):
            mostCommonBitValue = self.getMostCommenBit(self.oxygenRating, index)
            leastCommonBitValue = self.getLeastCommenBit(self.co2ScrubberRating, index)

            if len(self.oxygenRating) > 1:
                self.UpdateOxygenArray(mostCommonBitValue, index)
            if len(self.co2ScrubberRating) > 1:    
                self.UpdateScrubArray(leastCommonBitValue, index)
        
        oxygenRating = int(self.oxygenRating[0],2)
        scrubRating = int(self.co2ScrubberRating[0],2)

        return oxygenRating * scrubRating
            

            





            



