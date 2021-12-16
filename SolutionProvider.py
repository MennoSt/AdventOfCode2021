from numpy.lib.polynomial import poly
import pandas as pd


from src.BingoManager import BingoManager
from src.CaveNavigator import CaveNavigator
from src.CrabPositioner import CrabPositioner
from src.OctopusFlashManager import OctopusFlashManager
from src.SyntaxManager import SyntaxManager
from utils.FileReader import FileReader
from src.LaunterFishCalculator import LaunterFishCalculator
from src.PatternAnalyzer import PatternAnalyzer
from src.PatternReader import PatternReader
from src.PositionCalculator import PositionCalculator
from src.PowerManager import PowerManager
from src.RiskCalculator import RiskCalculator
from src.SubmarineCalculator import SubmarineCalculator
from src.VentDetector import VentDetector
from src.Folder import Folder
from src.Polymerizator import Polymarizator

def printAnswer(day, answer1, answer2):
    print("The answer of Day " + str(day) + " part 1 is equal to " + str(answer1))
    print("The answer of Day " + str(day) + " part 2 is equal to " + str(answer2))

class SolutionProvider:

    def __init__(self ):
        self.fileReader = FileReader()

    def solutionDayOne(self):
        submarineCalculator = SubmarineCalculator()
        data = pd.read_csv("input/inputday1",names = ["Depth"])
        data['Depth'] = data['Depth'].astype(int)

        answerPart1 = submarineCalculator.GetIncreasedDepthsPart1(data["Depth"].to_numpy())
        answerPart2 = submarineCalculator.GetIncreasedDepthsPart2(data['Depth'].to_numpy())

        printAnswer(1, answerPart1, answerPart2)

    def solutionDayTwo(self):
        positionCalculator = PositionCalculator()
        data = pd.read_csv("input/inputday2",names = ["Direction", "Ammount"], delim_whitespace=True)

        answerPart1 = positionCalculator.getMultiplicationPart1(data["Direction"].astype(str).values.tolist(), data["Ammount"].to_numpy())
        answerPart2 = positionCalculator.getMultiplicationPart2(data["Direction"].astype(str).values.tolist(), data["Ammount"].to_numpy())
        
        printAnswer(2, answerPart1, answerPart2)
    
    def solutionDayThree(self):
        powerManager = PowerManager()
        data = pd.read_csv("input/inputday3", dtype=str, names = ["BinaryValue"])

        answerPart1 = powerManager.calculateRequiredPower(data["BinaryValue"].astype(str).values.tolist())
        answerPart2 = powerManager.calculateLifeSupport(data["BinaryValue"].astype(str).values.tolist()) 

        printAnswer(3, answerPart1, answerPart2)
    
    def solutionDayFour(self):
        bingoManager = BingoManager()
        bingoFileReader = FileReader()
        bingoFileReader.readBingoFile("input/inputday4")
        bingoNumbers = bingoFileReader.bingoNumbers
        intChartArray = bingoFileReader.intChartArray
        
        bingoManager.createBingoCharts(intChartArray)
        answerPart1 = bingoManager.getFirstBingoScore(bingoNumbers)
        answerPart2 = bingoManager.getLastBingoScore(bingoNumbers)

        printAnswer(4, answerPart1, answerPart2)
    
    def solutionDayFive(self):
        ventDetector = VentDetector()
        ventDetector.readVentFile("input/inputday5")

        answerPart1 = ventDetector.getNumberOfOverlapsPart1()
        answerPart2 = ventDetector.getNumberOfOverlapsPart2()
        
        printAnswer(5, answerPart1, answerPart2)

    def solutionDaySix(self):
        initalState = self.fileReader.readToIntArray("input/inputday6")
        launterFishCalulator = LaunterFishCalculator()

        answerPart1 = launterFishCalulator.getNumberOfFishes(initalState, 80)
        answerPart2 = launterFishCalulator.getNumberOfFishes(initalState, 256)
        
        printAnswer(6, answerPart1, answerPart2)
    
    def solutionDaySeven(self):      
        intArray = self.fileReader.readToIntArray("input/inputday7")
        crabPositioner = CrabPositioner()

        answerPart1 = crabPositioner.getLeastAmmountOfFuel(intArray)
        answerPart2 = crabPositioner.getLeastAmmountOfFuel(intArray, True)
        
        printAnswer(7, answerPart1, answerPart2)
    
    def solutionDayEight(self):      

        patternReader = PatternReader()
        patternAnalyzer = PatternAnalyzer()
        patternReader.readPattern("input/inputday8")
        
        uniquePatternArray = patternReader.uniquePatternArray
        fourDigitArray = patternReader.fourDigitArray

        answerPart1 = patternAnalyzer.getNumberOfDigitInstances(fourDigitArray)
        answerPart2 = patternAnalyzer.calculateSumOfFourDigits(fourDigitArray, uniquePatternArray)
        printAnswer(8, answerPart1, answerPart2)

    def solutionDayNine(self):      

        riskCalculator = RiskCalculator()
        heightMap = self.fileReader.readHeightMap("input/inputday9")

        riskCalculator.setHeightMap(heightMap)
        answerPart1 =riskCalculator.calculateSumRiskLevels()
        answerPart2 =riskCalculator.getMultiplicationLargest3Bassins()

        printAnswer(9, answerPart1, answerPart2)

    def solutionDayTen(self):      
        filestring = self.fileReader.readLinesToStringArray("input/inputday10")
        syntaxErrorDetector = SyntaxManager()

        answerPart1 = syntaxErrorDetector.calculateSyntaxErrorScore(filestring)
        answerPart2 = syntaxErrorDetector.calculateMiddleScore(filestring)
        printAnswer(10, answerPart1, answerPart2)

    def solutionDayEleven(self):      
        initialMap = self.fileReader.readOctopusMap("input/inputday11")
        octopusFlashManager = OctopusFlashManager()

        octopusFlashManager.setOctopusMap(initialMap)
        answerPart1 = octopusFlashManager.getNumberOfFlashes(100)

        octopusFlashManager.setOctopusMap(initialMap)
        answerPart2 = octopusFlashManager.getFirstSynchronicCycle()

        printAnswer(11, answerPart1, answerPart2)

    def solutionDayTwelve(self):      
        initialMap = self.fileReader.readLinesToStringArray("input/inputday12")
        caveNavigator = CaveNavigator()

        answerPart1 = caveNavigator.findNumberOfRoutes(initialMap)
        answerPart2 = caveNavigator.findNumberOfRoutes(initialMap, True)
        printAnswer(12, answerPart1, answerPart2)
        
    def solutionDayThirteen(self):
        
        folder = Folder()
        
        folder.importInputFiles("input/inputday13")
        answerPart1 = folder.CalculateNumberOfDots(True)
        printAnswer(13, answerPart1, "PFKLKCFP")
        folder.CalculateNumberOfDots()

       
    def solutionDayFourteen(self):
        
        fileReader = FileReader()
        polymarizator = Polymarizator()
        
        data = fileReader.readPolymerTemplate("input/inputday14")
        initialString = data[0]
        polyPairs = data[1]
        stepsPart1 = 10
        stepsPart2 = 40
        
        answerPart1 = polymarizator.getMostCommonMinusLeastCommon(initialString, polyPairs, stepsPart1)
        answerPart2 = polymarizator.getMostCommonMinusLeastCommon(initialString, polyPairs, stepsPart2)
        printAnswer(14, answerPart1, answerPart2)