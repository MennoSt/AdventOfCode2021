import re

class FileReader:
    
    def __init__(self):
        self.bingoNumbers = ""
        self.intChartArray = []
    
    def readToIntArray(self, inputFile):
        fileObj = open(inputFile, "r")
        fileString = fileObj.read().splitlines()
        fileObj.close()
        intArray = list(map(int,fileString[0].split(",")))
        return intArray

    def readBingoFile(self, inputFile):
        self.intChartArray = []

        with open (inputFile, "r") as myfile:
            dataread = myfile.read().rstrip()
        
        chartData = dataread.split('\n\n')
        chartbingoNumbers = chartData[0]
        self.bingoNumbers = list(map(int, chartbingoNumbers.split(",")))
        chartData.pop(0)

        for data in chartData:
            data = data.replace("\n"," ")
            data = data.replace("  "," ")
            array = re.split(' ',data)
            array = filter(None, array)
            self.intChartArray.append(list(map(int, array)))
    
    def getBingoNumbers(self):
        return self.bingoNumbers
    
    def getintChartArray(self):
        return self.intChartArray

        





            



