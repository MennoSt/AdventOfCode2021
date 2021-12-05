import pandas as pd
from PowerManager import PowerManager
# from BitCalculator import BitCalculator

from SubmarineCalculator import SubmarineCalculator
from PositionCalculator import PositionCalculator

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

        answerPart1 = positionCalculator.getMultiplication(data["Direction"].astype(str).values.tolist(), data["Ammount"].to_numpy())
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
