class LaunterFishCalculator:
    
    def __init__(self):
        self.fishArray = []
        self.fishArrayFast = []
        self.initialState = []

    def ConvertArrayToCounterArray(self, initialState):
        countArray = []
        for i in range(0,8):
            countArray.append(initialState.count(i))
        
        for _ in range(2):
            countArray.append(0)

        return countArray

    def GetNumberOfFishes(self, initialstate, days):
        self.fishArrayFast = self.ConvertArrayToCounterArray(initialstate)
        self.UpdateToNextGeneration()

        for _ in range(days-1):
            self.UpdateToNextGeneration()
    
        sumFishes = sum(self.fishArrayFast)

        return sumFishes

    def UpdateToNextGeneration(self):
        
        newArray = []
        additionalEights = self.fishArrayFast[0]
        additionalSixes = self.fishArrayFast[0] + self.fishArrayFast[7]
        
        newArray.append(self.fishArrayFast[1])
        newArray.append(self.fishArrayFast[2])
        newArray.append(self.fishArrayFast[3])
        newArray.append(self.fishArrayFast[4])
        newArray.append(self.fishArrayFast[5])
        newArray.append(self.fishArrayFast[6])
        newArray.append(additionalSixes)
        newArray.append(self.fishArrayFast[8])
        newArray.append(additionalEights)

        self.fishArrayFast = newArray

  

            





            



