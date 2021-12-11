class CrabPositioner:

    def getLeastAmmountOfFuel(self, positionArray, increasedRate = False):

        fuelSumArray = []
        lowerLimit = min(positionArray)
        highLimit = max(positionArray)
        
        for sugestedPos in range(lowerLimit, highLimit):
            if increasedRate == True:
                fuelSum = self.__calculateFuelSum(positionArray, sugestedPos, True)
            else:
                fuelSum = self.__calculateFuelSum(positionArray, sugestedPos)
            fuelSumArray.append(fuelSum)
        
        minimumFuel = min(fuelSumArray)

        return minimumFuel
    
    def __recursiveFunction(self,x):
        value = int(x*(x+1)/2)
        return value

    def __calculateFuel(self, horPos, suggestedPos):
        return abs(horPos-suggestedPos)
    
    def __calculateIncreasedFuel(self, horPos, sugestedPos):
        difference = abs(horPos - sugestedPos)
        fuel = self.__recursiveFunction(difference)
        return fuel
    
    def __calculateFuelSum(self, positionArray, suggestedPos, increasedRate = False):
        fuelSum = 0
        for horPostion in positionArray:
            if increasedRate == False:
                fuelSum += self.__calculateFuel(horPostion, suggestedPos)
            else:
                fuelSum += self.__calculateIncreasedFuel(horPostion, suggestedPos)
        
        return fuelSum
    


            





            



