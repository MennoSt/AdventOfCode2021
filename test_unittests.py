import unittest

from LaunterFishCalculator import LaunterFishCalculator
from PowerManager import PowerManager
from SubmarineCalculator import SubmarineCalculator
from PositionCalculator import PositionCalculator
from FileReader import FileReader
from BingoManager import BingoManager
from VentDetector import VentDetector

class Test_SumbarineCalculator(unittest.TestCase):

    def setUp(self):
        self.submarineCalculator = SubmarineCalculator()
        self.testdata = [199,200,208,210,200,207,240,269,260,263]
    
    def test_CalculateDepthIncreases_Part1_Example1(self):
        increases = self.submarineCalculator.GetIncreasedDepthsPart1(self.testdata)
        self.assertEqual(increases, 7)
    
    def test_CalculateDepthIncreases_Part1_Example1(self):
        increases = self.submarineCalculator.GetIncreasedDepthsPart2(self.testdata)
        self.assertEqual(increases, 5)

class Test_PositionCalculator(unittest.TestCase):

    def setUp(self):
        self.positionCalculator = PositionCalculator()
        self.testdataAmmount = [5,5,8,3,8,2]
        self.testdataDirection = ["forward", "down", "forward", "up", "down", "forward"]
    
    def test_CalculateMultiplication(self):
        multiplication = self.positionCalculator.getMultiplicationPart1(self.testdataDirection, self.testdataAmmount)
        self.assertEqual(multiplication, 150)

    def test_CalculateMultiplication(self):
        multiplicationPart2 = self.positionCalculator.getMultiplicationPart2(self.testdataDirection, self.testdataAmmount)
        self.assertEqual(multiplicationPart2, 900)

class Test_PowerManager(unittest.TestCase):

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
        consumedPower = self.powerManager.calculateRequiredPower(self.testdataPower)
        self.assertEqual(consumedPower, 198)
    
    def test_CalculateLifeSupport(self):
        lifeSupport = self.powerManager.calculateLifeSupport(self.testdataPower)
        self.assertEqual(lifeSupport, 230)


class Test_BingoManager(unittest.TestCase):
    
    def setUp(self):
        self.bingoFileReader = FileReader()
        self.bingoFileReader.readBingoFile("testinput/unittestinputday4")
        self.bingoManager = BingoManager()
        self.bingoNumbers = self.bingoFileReader.getBingoNumbers()
        self.intChartArray = self.bingoFileReader.getintChartArray()
        self.bingoManager.createBingoCharts(self.intChartArray)

    def test_CalculateBingoManagerPart1(self):

        bingoScore = self.bingoManager.getFirstBingoScore(self.bingoNumbers)
        self.assertEqual(bingoScore, 4512)
    
    def test_CalculateBingoManagerPart2(self):
        bingoScore = self.bingoManager.getLastBingoScore(self.bingoNumbers)
        self.assertEqual(bingoScore, 1924)

class Test_TestVentDetector(unittest.TestCase):
    
    def setUp(self):
        self.ventDetector = VentDetector()
        self.ventDetector.readVentFile("testinput/unittestinputday5")

    def test_CalculateOverlapsPart1(self):
        numberOfOverlaps = self.ventDetector.getNumberOfOverlapsPart1()
        self.assertEqual(numberOfOverlaps, 5)

    def test_CalculateOverlapsPart2(self):
        numberOfOverlaps = self.ventDetector.getNumberOfOverlapsPart2()
        self.assertEqual(numberOfOverlaps, 12)

class Test_TestLaunterFishCalculator(unittest.TestCase):
    
    def setUp(self):
        self.launterFishCalculator = LaunterFishCalculator()
        self.initialState = [3,4,3,1,2]

    def test_calculateFishesAfter18Days(self):
        days = 18
        totalFishes = self.launterFishCalculator.getNumberOfFishes(self.initialState, days)
        self.assertEqual(totalFishes, 26)

    def test_calculateFishesAfter80Days(self):
        days = 80
        totalFishes = self.launterFishCalculator.getNumberOfFishes(self.initialState, days)
        self.assertEqual(totalFishes, 5934)

    def test_calculateFishesAfter256Days(self):
        days = 256
        totalFishes = self.launterFishCalculator.getNumberOfFishes(self.initialState, days)
        self.assertEqual(totalFishes, 26984457539)


if __name__ == '__main__':
    unittest.main()
