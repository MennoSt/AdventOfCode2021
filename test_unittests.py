import unittest

from PowerManager import PowerManager
from SubmarineCalculator import SubmarineCalculator
from PositionCalculator import PositionCalculator
from BingoFileReader import BingoFileReader
from BingoManager import BingoManager

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

class Test_TestDirectionCalculator(unittest.TestCase):

    def setUp(self):
        self.directionCalculator = PositionCalculator()
        self.testdataAmmount = [5,5,8,3,8,2]
        self.testdataDirection = ["forward", "down", "forward", "up", "down", "forward"]
    
    def test_CalculateMultiplication(self):
        multiplication = self.directionCalculator.getMultiplicationPart1(self.testdataDirection, self.testdataAmmount)
        self.assertEqual(multiplication, 150)

    def test_CalculateMultiplication(self):
        multiplicationPart2 = self.directionCalculator.getMultiplicationPart2(self.testdataDirection, self.testdataAmmount)
        self.assertEqual(multiplicationPart2, 900)

class Test_TestBitCalculator(unittest.TestCase):

    def setUp(self):
        self.powerManager = PowerManager()
        self.testdataPower = ["00100", 
                              "11110", 
                              "10110", 
                              "10111",
                              "10101",
                              "01111",
                              "00111",
                              "11100",
                              "10000",
                              "11001",
                              "00010",
                              "01010"]

    def test_CalculatePowerConsumption(self):
        consumedPower = self.powerManager.CalculateRequiredPower(self.testdataPower)
        self.assertEqual(consumedPower, 198)
    
    def test_CalculateLifeSupport(self):
        lifeSupport = self.powerManager.CalculateLifeSupport(self.testdataPower)
        self.assertEqual(lifeSupport, 230)


class Test_TestBingoManager(unittest.TestCase):
    
    def setUp(self):
        self.bingoFileReader = BingoFileReader()
        self.bingoFileReader.readFile("unittestinputday4")
        self.bingoManager = BingoManager()
        self.bingoNumbers = self.bingoFileReader.getBingoNumbers()
        self.intChartArray = self.bingoFileReader.getintChartArray()
        self.bingoManager.CreateBingoCharts(self.intChartArray)

    def test_CalculateBingoManagerPart1(self):

        bingoScore = self.bingoManager.getFirstBingoScore(self.bingoNumbers)
        self.assertEqual(bingoScore, 4512)
    
    def test_CalculateBingoManagerPart2(self):
        bingoScore = self.bingoManager.getLastBingoScore(self.bingoNumbers)
        self.assertEqual(bingoScore, 1924)


if __name__ == '__main__':
    unittest.main()
