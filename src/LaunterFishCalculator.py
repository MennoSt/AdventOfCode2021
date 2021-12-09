class LaunterFishCalculator:
    
    def __init__(self):
        self.fishArray = []
        self.initialState = []

    def convertArrayToCounterArray(self, initialState):
        countArray = []
        for i in range(0,8):
            countArray.append(initialState.count(i))
        
        for _ in range(2):
            countArray.append(0)

        return countArray

    def getNumberOfFishes(self, initialstate, days):
        self.fishArray = self.convertArrayToCounterArray(initialstate)
        self.updateToNextGeneration()

        for _ in range(days-1):
            self.updateToNextGeneration()
    
        sumFishes = sum(self.fishArray)

        return sumFishes

    def updateToNextGeneration(self):
        
        updatedArray = []
        additionalEights = self.fishArray[0]
        additionalSixes = self.fishArray[0] + self.fishArray[7]

        for i in range(1,7):
            updatedArray.append(self.fishArray[i])
            
        updatedArray.append(additionalSixes)
        updatedArray.append(self.fishArray[8])
        updatedArray.append(additionalEights)

        self.fishArray = updatedArray

  

            





            



