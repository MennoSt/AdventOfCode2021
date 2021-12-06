import pandas as pd
import re

from PowerManager import PowerManager
from SubmarineCalculator import SubmarineCalculator
from PositionCalculator import PositionCalculator
from BingoChart import BingoChart
from BingoManager import BingoManager
from BingoFileReader import BingoFileReader

class SolutionProvider:

    def SolutionDayOne():
        submarineCalculator = SubmarineCalculator()
        data = pd.read_csv("input/inputday1",names = ["Depth"])
        data['Depth'] = data['Depth'].astype(int)

        answerPart1 = submarineCalculator.GetIncreasedDepthsPart1(data["Depth"].to_numpy())
        answerPart2 = submarineCalculator.GetIncreasedDepthsPart2(data['Depth'].to_numpy())

        print("The answer of Day 1 part 1 is equal to " + str(answerPart1))
        print("The answer of Day 1 part 2 is equal to " + str(answerPart2))

    def SolutionDayTwo():
        positionCalculator = PositionCalculator()
        data = pd.read_csv("input/inputday2",names = ["Direction", "Ammount"], delim_whitespace=True)

        answerPart1 = positionCalculator.getMultiplicationPart1(data["Direction"].astype(str).values.tolist(), data["Ammount"].to_numpy())
        answerPart2 = positionCalculator.getMultiplicationPart2(data["Direction"].astype(str).values.tolist(), data["Ammount"].to_numpy())
        
        print("The answer of Day 2 part 1 is equal to " + str(answerPart1))
        print("The answer of Day 2 part 2 is equal to " + str(answerPart2))
    
    def SolutionDayThree():
        powerManager = PowerManager()
        data = pd.read_csv("input/inputday3", dtype=str, names = ["BinaryValue"])

        answerPart1 = powerManager.CalculateRequiredPower(data["BinaryValue"].astype(str).values.tolist())
        answerPart2 = powerManager.CalculateLifeSupport(data["BinaryValue"].astype(str).values.tolist()) 

        print("The answer of Day 3 part 1 is equal to " + str(answerPart1))
        print("The answer of Day 3 part 2 is equal to " + str(answerPart2))
    
    def SolutionDayFour():
        bingoManager = BingoManager()
        bingoFileReader = BingoFileReader()
        bingoFileReader.readFile("input/inputday4")
        bingoNumbers = bingoFileReader.getBingoNumbers()
        intChartArray = bingoFileReader.getintChartArray()
        
        bingoManager.CreateBingoCharts(intChartArray)
        bingoScorefirst = bingoManager.getFirstBingoScore(bingoNumbers)
        bingoScorelast = bingoManager.getLastBingoScore(bingoNumbers)

        print("The answer of Day 4 part 1 is equal to " + str(bingoScorefirst))
        print("The answer of Day 4 part 2 is equal to " + str(bingoScorelast))