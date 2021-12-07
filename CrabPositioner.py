class CrabPositioner:
    
    def __init__(self):
        self.sumChart = 0
        self.lastNumber = 0
    

    def calculateFuel(self, horPos, suggestedPos):
        return abs(horPos-suggestedPos)
    
    # def calculateFuelIncreasedRate(self, horPos, sugestedPos):
    #     hor
    
    def calculateFuelSum(self, positionArray, suggestedPos):
        fuelSum = 0
        for horPostion in positionArray:
            fuelSum += self.calculateFuel(horPostion, suggestedPos)
        
        return fuelSum
    
    def getLeastAmmountOfFuel(self, positionArray, increasedRate = False):

        fuelSumArray = []
        lowerLimit = min(positionArray)
        highLimit = max(positionArray)
        
        for sugestedPos in range(lowerLimit, highLimit):
            fuelSum = self.calculateFuelSum(positionArray, sugestedPos)
            fuelSumArray.append(fuelSum)
        
        minimumFuel = min(fuelSumArray)

        return minimumFuel

            





            



