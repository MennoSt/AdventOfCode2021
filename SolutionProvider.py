import pandas as pd

from SubmarineCalculator import SubmarineCalculator

class SolutionProvider:

    def SolutionOne():
        submarineCalculator = SubmarineCalculator()
        data = pd.read_csv("input/inputday1",names = ["Depth"])
        print(data["Depth"].to_numpy())

        data['Depth'] = data['Depth'].astype(int)
        answerPart1 = str(submarineCalculator.GetNumberOfIncreasedDepths(data["Depth"]))
        # answerPart2 = str(submarineCalculator.getNumberOfIncreasesSummedDepth(data['Depth']))

        print("The answer of Day 1 part 1 is equal to " + answerPart1)
        # print("The answer of Day 2 part 2 is equal to " + answerPart2)


