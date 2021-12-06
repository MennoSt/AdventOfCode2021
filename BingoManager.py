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
        for number in numbers:
            leftBingoCharts = self.bingoChartArray
            # length = len(leftBingoCharts)
            for index in range (0, len(leftBingoCharts)):
                if len(leftBingoCharts) == 1:
                    index = 0
                self.bingoChartArray[index].strikeThroughNumber(number)
                if self.bingoChartArray[index].hasBingo() == True:
                    lastBingoScore = self.bingoChartArray[index].GetBingoScore(number)
                    self.bingoChartArray.pop(index)

        return lastBingoScore
  

            





            



