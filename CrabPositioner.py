class CrabPositioner:
    
    def __init__(self):
        self.sumChart = 0
        self.lastNumber = 0
    
    def recursiveFunction(self,x):
        value = int(x*(x+1)/2)
        return value

    def calculateFuel(self, horPos, suggestedPos):
        return abs(horPos-suggestedPos)
    
    def calculateIncreasedFuel(self, horPos, sugestedPos):
        difference = abs(horPos - sugestedPos)
        fuel = self.recursiveFunction(difference)
        return fuel
    
    def calculateFuelSum(self, positionArray, suggestedPos, increasedRate = False):
        fuelSum = 0
        for horPostion in positionArray:
            if increasedRate == False:
                fuelSum += self.calculateFuel(horPostion, suggestedPos)
            else:
                fuelSum += self.calculateIncreasedFuel(horPostion, suggestedPos)
        
        return fuelSum
    
    def getLeastAmmountOfFuel(self, positionArray, increasedRate = False):

        fuelSumArray = []
        lowerLimit = min(positionArray)
        highLimit = max(positionArray)
        
        for sugestedPos in range(lowerLimit, highLimit):
            if increasedRate == True:
                fuelSum = self.calculateFuelSum(positionArray, sugestedPos, True)
            else:
                fuelSum = self.calculateFuelSum(positionArray, sugestedPos)
            fuelSumArray.append(fuelSum)
        
        minimumFuel = min(fuelSumArray)

        return minimumFuel

            





            



