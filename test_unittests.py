import unittest
import pandas as pd

from SubmarineCalculator import SubmarineCalculator

class Test_TestSumbarineCalculator(unittest.TestCase):

    def setUp(self):
        self.submarineCalculator = SubmarineCalculator()
        self.testdata = [199,200,208,210,200,207,240,269,260,263]
    
    def test_CalculateDepthIncreases_Part1_Example1(self):
        increases = self.submarineCalculator.GetIncreasedDepthsPart1(self.testdata)
        self.assertEqual(increases, 7)
    
    def test_CalculateDepthIncreases_Part1_Example1(self):
        increases = self.submarineCalculator.GetIncreasedDepthsPart2(self.testdata)
        self.assertEqual(increases, 5) 

if __name__ == '__main__':
    unittest.main()
