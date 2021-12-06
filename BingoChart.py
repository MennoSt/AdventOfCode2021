import re

class BingoChart:
    
    def __init__(self, bingoChart):
        self.bingoChart = bingoChart
        self.horizontalSums = []
        self.verticalSums = []

    def strikeThroughNumber(self, number):
        
        for index in range(0, len(self.bingoChart)):
            if self.bingoChart[index] == number:
                self.bingoChart[index] = -1
        
        self.UpdateSums()

    def hasBingo(self):
        
        for index in range (0,len(self.horizontalSums)):
            if(self.horizontalSums[index] == -5):
                return True
        
        for index in range (0,len(self.verticalSums)):
            if(self.verticalSums[index] == -5):
                return True        

        return False
    
    def UpdateSums(self):
        self.horizontalSums = []
        self.verticalSums = []     

        bingochart = self.bingoChart

        for index in range(0,5):
            addition = index*5
            sumH = bingochart[addition]+bingochart[1+addition]+bingochart[2+addition]+bingochart[3+addition]+bingochart[4+addition]
            self.horizontalSums.append(sumH)

        for index in range(0,5):
            sumV = bingochart[index]+bingochart[index+5]+bingochart[index+10]+bingochart[index+15]+bingochart[index+20]
            self.verticalSums.append(sumV)


    def GetBingoScore(self, lastNumber):
        array = []
        for number in self.bingoChart:
            if number != -1:
                array.append(number)
        
        sumChart = sum(array)
        score = sumChart*lastNumber

        return score



            



