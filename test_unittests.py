import unittest
import pandas as pd

from SubmarineCalculator import SubmarineCalculator

class Test_TestCalculatorPart1(unittest.TestCase):

    def setUp(self):
        self.submarineCalculator = SubmarineCalculator()
    
    def test_CalculateDepthIncreases_Part1_Example1(self):
        data = {'Depth':['199','200','208','210','200','207','240','269','260','263']}
        df = pd.DataFrame(data)
        increases = self.submarineCalculator.GetNumberOfIncreasedDepths(df['Depth'])
        self.assertEqual(increases, 7)

if __name__ == '__main__':
    unittest.main()
