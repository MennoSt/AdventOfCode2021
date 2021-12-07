class LaunterFishCalculator:
    
    def __init__(self):
        self.fishArray = []
    
    def GetNumberOfFishes(self, initialstate, days):
        
        self.fishArray = initialstate
        self.UpdateToNextGeneration()

        for _ in range(days-1):
            self.UpdateToNextGeneration()
    
        sumFishes = len(self.fishArray)

        return sumFishes

    def UpdateToNextGeneration(self):
        eightsToAppend = 0
        for index in range(0,len(self.fishArray)):
            if(self.fishArray[index] == 0):
                self.fishArray[index] = 6
                eightsToAppend += 1
            else:
                self.fishArray[index] -= 1

        for _ in range(eightsToAppend):
            self.fishArray.append(8)

  

            





            



