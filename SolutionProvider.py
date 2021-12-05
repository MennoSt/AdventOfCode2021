import pandas as pd

from PowerManager import PowerManager
from SubmarineCalculator import SubmarineCalculator
from PositionCalculator import PositionCalculator
from BingoChart import BingoChart

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
        data = pd.read_csv("input/inputday4", dtype=str, names = ["BingoChart"], delim_whitespace=True)
        bingoNumbers = list(map(int, data["BingoChart"][0].split(",")))

        with open ("input/inputday4", "r") as myfile:
            dataread = myfile.read().rstrip()

        
        chartData = dataread.split('\n\n')
        chartData.pop(0)
        bingochart = BingoChart(chartData[0])

        bingochart.hasBingo(bingoNumbers)
        
        print(chartData[0])



        # for index in range(0,len(bingoNumbers)):
        #     # bingoNumbers[index] = bingoNumbers[index].replace('\n', '')
        #     bingoNumbers[index] = int(bingoNumbers[index])
        
        # print(bingoNumbers)
        
        # with open("input/inputday4") as f:
        #     first_line = f.readline()
        #     print(first_line)

        # bingoNumbers = first_line.split(",")

        # for index in range(0,len(bingoNumbers)):
        #     bingoNumbers[index] = bingoNumbers[index].replace('\n', '')
        #     bingoNumbers[index] = int(bingoNumbers[index])

        # print(bingoNumbers)

        # print(data)
        # answerPart1 = powerManager.CalculateRequiredPower(data["BinaryValue"].astype(str).values.tolist())
        # answerPart2 = powerManager.CalculateLifeSupport(data["BinaryValue"].astype(str).values.tolist()) 

        # print("The answer of Day 3 part 1 is equal to " + str(answerPart1))
        # print("The answer of Day 3 part 2 is equal to " + str(answerPart2))
