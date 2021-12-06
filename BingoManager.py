from BingoChart import BingoChart

class BingoManager:
    
    def __init__(self):
        self.bingoChartArray = [BingoChart]
        self.sumChart = 0
        self.lastNumber = 0
    
    def CreateBingoCharts(self, chartData):
        self.bingoChartArray = []
        for chart in chartData:
            bingochart = BingoChart(chart)
            self.bingoChartArray.append(bingochart)
    
    
    def getFirstBingoScore(self, numbers):
        bingo = False
        for number in numbers:
            for index in range (0,len(self.bingoChartArray)):
                if bingo == False:
                    self.bingoChartArray[index].strikeThroughNumber(number)
                if self.bingoChartArray[index].hasBingo() == True and bingo == False:
                    bingoScore = self.bingoChartArray[index].GetBingoScore(number)
                    self.lastNumber = number
                    bingo = True

        return bingoScore

    def getLastBingoScore(self, numbers):
        lastBingoScore = 0
        indexesToPop = []

        for number in numbers:
            leftBingoCharts = self.bingoChartArray
            for index in range (0, len(leftBingoCharts)):
                length = len(leftBingoCharts)
                if length == 1:
                    index = 0
                leftBingoCharts[index].strikeThroughNumber(number)
                if leftBingoCharts[index].hasBingo() == True:
                    lastBingoScore = leftBingoCharts[index].GetBingoScore(number)
                    indexesToPop.append(index)
            
            for index in sorted(indexesToPop, reverse = True):
                del self.bingoChartArray[index]
                indexesToPop =[]

        return lastBingoScore
  

            





            



