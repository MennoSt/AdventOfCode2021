import pandas as pd

from src.BingoManager import BingoManager
from src.CrabPositioner import CrabPositioner
from utils.FileReader import FileReader
from src.LaunterFishCalculator import LaunterFishCalculator
from src.PatternAnalyzer import PatternAnalyzer
from src.PatternReader import PatternReader
from src.PositionCalculator import PositionCalculator
from src.PowerManager import PowerManager
from src.RiskCalculator import RiskCalculator
from src.SubmarineCalculator import SubmarineCalculator
from src.VentDetector import VentDetector

class SolutionProvider:

    def __init__(self ):
        self.fileReader = FileReader()

    def solutionDayOne(self):
        submarineCalculator = SubmarineCalculator()
        data = pd.read_csv("input/inputday1",names = ["Depth"])
        data['Depth'] = data['Depth'].astype(int)

        answerPart1 = submarineCalculator.GetIncreasedDepthsPart1(data["Depth"].to_numpy())
        answerPart2 = submarineCalculator.GetIncreasedDepthsPart2(data['Depth'].to_numpy())

        print("The answer of Day 1 part 1 is equal to " + str(answerPart1))
        print("The answer of Day 1 part 2 is equal to " + str(answerPart2))

    def solutionDayTwo(self):
        positionCalculator = PositionCalculator()
        data = pd.read_csv("input/inputday2",names = ["Direction", "Ammount"], delim_whitespace=True)

        answerPart1 = positionCalculator.getMultiplicationPart1(data["Direction"].astype(str).values.tolist(), data["Ammount"].to_numpy())
        answerPart2 = positionCalculator.getMultiplicationPart2(data["Direction"].astype(str).values.tolist(), data["Ammount"].to_numpy())
        
        print("The answer of Day 2 part 1 is equal to " + str(answerPart1))
        print("The answer of Day 2 part 2 is equal to " + str(answerPart2))
    
    def solutionDayThree(self):
        powerManager = PowerManager()
        data = pd.read_csv("input/inputday3", dtype=str, names = ["BinaryValue"])

        answerPart1 = powerManager.calculateRequiredPower(data["BinaryValue"].astype(str).values.tolist())
        answerPart2 = powerManager.calculateLifeSupport(data["BinaryValue"].astype(str).values.tolist()) 

        print("The answer of Day 3 part 1 is equal to " + str(answerPart1))
        print("The answer of Day 3 part 2 is equal to " + str(answerPart2))
    
    def solutionDayFour(self):
        bingoManager = BingoManager()
        bingoFileReader = FileReader()
        bingoFileReader.readBingoFile("input/inputday4")
        bingoNumbers = bingoFileReader.getBingoNumbers()
        intChartArray = bingoFileReader.getintChartArray()
        
        bingoManager.createBingoCharts(intChartArray)
        bingoScorefirst = bingoManager.getFirstBingoScore(bingoNumbers)
        bingoScorelast = bingoManager.getLastBingoScore(bingoNumbers)

        print("The answer of Day 4 part 1 is equal to " + str(bingoScorefirst))
        print("The answer of Day 4 part 2 is equal to " + str(bingoScorelast))
    
    def solutionDayFive(self):
        ventDetector = VentDetector()
        ventDetector.readVentFile("input/inputday5")

        answerPart1 = ventDetector.getNumberOfOverlapsPart1()
        answerPart2 = ventDetector.getNumberOfOverlapsPart2()
        
        print("The answer of Day 5 part 1 is equal to " + str(answerPart1))
        print("The answer of Day 5 part 2 is equal to " + str(answerPart2))

    def solutionDaySix(self):
        initalState = self.fileReader.readToIntArray("input/inputday6")
        launterFishCalulator = LaunterFishCalculator()

        answerPart1 = launterFishCalulator.getNumberOfFishes(initalState, 80)
        answerPart2 = launterFishCalulator.getNumberOfFishes(initalState, 256)
        
        print("The answer of Day 6 part 1 is equal to " + str(answerPart1))
        print("The answer of Day 6 part 2 is equal to " + str(answerPart2))
    
    def solutionDaySeven(self):      
        intArray = self.fileReader.readToIntArray("input/inputday7")
        crabPositioner = CrabPositioner()

        answerPart1 = crabPositioner.getLeastAmmountOfFuel(intArray)
        answerPart2 = crabPositioner.getLeastAmmountOfFuel(intArray, True)
        
        print("The answer of Day 7 part 1 is equal to " + str(answerPart1))
        print("The answer of Day 7 part 2 is equal to " + str(answerPart2))
    
    def solutionDayEight(self):      

        patternReader = PatternReader()
        patternAnalyzer = PatternAnalyzer()
        patternReader.readPattern("input/inputday8")
        
        uniquePatternArray = patternReader.uniquePatternArray
        fourDigitArray = patternReader.fourDigitArray

        answerPart1 = patternAnalyzer.getNumberOfDigitInstances(fourDigitArray)
        answerPart2 = patternAnalyzer.calculateSumOfFourDigits(fourDigitArray, uniquePatternArray)
        print("The answer of Day 8 part 1 is equal to " + str(answerPart1))
        print("The answer of Day 8 part 1 is equal to " + str(answerPart2))

    def solutionDayNine(self):      

        riskCalculator = RiskCalculator()
        heightMap = self.fileReader.readHeightMap("input/inputday9")

        riskCalculator.setHeightMap(heightMap)
        answerPart1 =riskCalculator.calculateSumRiskLevels()
        answerPart2 =riskCalculator.getMultiplicationLargest3Bassins()

        print("The answer of Day 9 part 1 is equal to " + str(answerPart1))
        print("The answer of Day 9 part 1 is equal to " + str(answerPart2))
