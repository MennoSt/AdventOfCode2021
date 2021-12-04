import pandas as pd

from SubmarineCalculator import SubmarineCalculator

class SolutionProvider:

    def SolutionOne():
        submarineCalculator = SubmarineCalculator()
        data = pd.read_csv("input/inputday1",names = ["Depth"])
        data['Depth'] = data['Depth'].astype(int)

        answerPart1 = str(submarineCalculator.GetIncreasedDepthsPart1(data["Depth"].to_numpy()))
        answerPart2 = str(submarineCalculator.GetIncreasedDepthsPart2(data['Depth'].to_numpy()))

        print("The answer of Day 1 part 1 is equal to " + answerPart1)
        print("The answer of Day 1 part 2 is equal to " + answerPart2)


