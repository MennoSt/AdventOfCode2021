class BingoChart:
    
    def __init__(self, bingoChart):
        self.bingoChart = bingoChart
        self.horizontalSums = []
        self.verticalSums = []
    
    def getBingoScore(self, lastNumber):
        array = []
        for number in self.bingoChart:
            if number != -1:
                array.append(number)
        
        sumChart = sum(array)
        score = sumChart*lastNumber

        return score

    def strikeThroughNumber(self, number):
        
        for index in range(0, len(self.bingoChart)):
            if self.bingoChart[index] == number:
                self.bingoChart[index] = -1
        
        self.__updateSums()

    def hasBingo(self):
        
        for index in range (0,len(self.horizontalSums)):
            if(self.horizontalSums[index] == -5):
                return True
        
        for index in range (0,len(self.verticalSums)):
            if(self.verticalSums[index] == -5):
                return True        

        return False
    
    def __updateSums(self):
        self.horizontalSums = []
        self.verticalSums = []     
        bingochart = self.bingoChart

        for index in range(0,5):
            addition = index*5
            sumH = 0
            for i in range(0,5):
                sumH += bingochart[addition+i]
            self.horizontalSums.append(sumH)

        for index in range(0,5):
            sumV = 0
            for i in range(0,25,5):
                sumV += bingochart[index+i]
            self.verticalSums.append(sumV)



            



