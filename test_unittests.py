import unittest


from src.CaveNavigator import CaveNavigator
from src.LaunterFishCalculator import LaunterFishCalculator
from src.OctopusFlashManager import OctopusFlashManager
from src.PowerManager import PowerManager
from src.SubmarineCalculator import SubmarineCalculator
from src.PositionCalculator import PositionCalculator
from src.BingoManager import BingoManager
from src.VentDetector import VentDetector
from src.CrabPositioner import CrabPositioner
from src.PatternAnalyzer import PatternAnalyzer
from src.PatternReader  import PatternReader
from src.RiskCalculator import RiskCalculator
from src.SyntaxManager import SyntaxManager
from src.SyntaxScoreBoard import SyntaxScoreBoard
from src.OctopusFlashManager import OctopusFlashManager
from src.Folder import Folder
from src.Polymerizator import Polymarizator
from utils.FileReader import FileReader
from src.Dijkstra import Dijkstra
from src.PacketDecoder import PacketDecoder, Packet


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
        self.bingoNumbers = self.bingoFileReader.bingoNumbers
        self.intChartArray = self.bingoFileReader.intChartArray
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

class Test_LaunterFishCalculator(unittest.TestCase):
    
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

class Test_CrabPositioner(unittest.TestCase):
    
    def setUp(self):
        self.crabPositioner = CrabPositioner()
        self.testPositions = [16,1,2,0,4,2,7,1,2,14]

    def test_CalculateLeastFuel(self):
        leastFuel = self.crabPositioner.getLeastAmmountOfFuel(self.testPositions)
        self.assertEqual(leastFuel, 37)

    def test_CalculateLeastFuel_IncreasedRate(self):
        leastFuel = self.crabPositioner.getLeastAmmountOfFuel(self.testPositions, True)
        self.assertEqual(leastFuel, 168)


class Test_PatternAnalyzer(unittest.TestCase):
    
    def setUp(self):
        self.patternReader = PatternReader()
        self.patternAnalyser = PatternAnalyzer()
        self.patternReader.readPattern("testinput/unittestinputday8")

    def test_CalculateNumberOfDigitInstances(self):

        digitCounts = self.patternAnalyser.getNumberOfDigitInstances(self.patternReader.fourDigitArray)
        self.assertEqual(digitCounts, 26)

    def test_CalculateSumAdditionPart2(self):

        fourDigitArray = self.patternReader.fourDigitArray
        uniquePatternArray = self.patternReader.uniquePatternArray
        digitCounts = self.patternAnalyser.calculateSumOfFourDigits(fourDigitArray, uniquePatternArray)
        self.assertEqual(digitCounts, 61229)


class Test_RiskCalculator(unittest.TestCase):
    
    def setUp(self):
        self.fileReader = FileReader()
        self.riskCalculator = RiskCalculator()
        heightMap = self.fileReader.readToIntMap("testinput/unittestinputday9")
        self.riskCalculator.setHeightMap(heightMap)

    def test_calculateSum(self):
        riskSum = self.riskCalculator.calculateSumRiskLevels()
        self.assertEqual(riskSum, 15)

    def test_calculateInitalBassin(self):
        bassin = self.riskCalculator.createInitalBassin(0,0)
        self.assertEqual(len(bassin), 3)
        bassin = self.riskCalculator.createInitalBassin(0,1)
        self.assertEqual(len(bassin), 2)
        bassin = self.riskCalculator.createInitalBassin(1,0)
        self.assertEqual(len(bassin), 2)
        bassin = self.riskCalculator.createInitalBassin(8,4)
        self.assertEqual(len(bassin), 6)

    def test_calculateInitalBassinPerIndex(self):
        self.riskCalculator.createInitialBassinsPerIndex()
        multiplicationLargestThree = self.riskCalculator.getMultiplicationLargest3Bassins()
        self.assertEqual(multiplicationLargestThree, 1134)


class Test_SyntaxErrorDetector(unittest.TestCase):
    
    def setUp(self):
        self.syntaxErrorDetector = SyntaxManager()
        self.filereader = FileReader()
        self.navigationLines = self.filereader.readLinesToStringArray("testinput/unittestinputday10")

    def test_checkSyntaxErrorExampleOne(self):
        charSyntaxError = self.syntaxErrorDetector.checkOnSyntaxError("<}")
        self.assertEqual(charSyntaxError,"}")
    
    def test_checkSyntaxErrorExampleTwo(self):
        charSyntaxError = self.syntaxErrorDetector.checkOnSyntaxError("{()()()>")
        self.assertEqual(charSyntaxError,">")
    
    def test_checkSyntaxErrorExampleThree(self):
        charSyntaxError = self.syntaxErrorDetector.checkOnSyntaxError("(((()))}")
        self.assertEqual(charSyntaxError,"}")
    
    def test_checkSyntaxErrorExampleFour(self):
        charSyntaxError = self.syntaxErrorDetector.checkOnSyntaxError("<([]){()}[{}])")
        self.assertEqual(charSyntaxError,")")

    def test_foundErrorClosingBracket(self):
        secondCharSyntaxError = self.syntaxErrorDetector.checkOnSyntaxError("{([(<{}[<>[]}>{[]{[(<()>")
        self.assertEqual(secondCharSyntaxError, "}")
    
    def test_foundErrorRoundBracket(self):
        charSytaxError = self.syntaxErrorDetector.checkOnSyntaxError("[[<[([]))<([[{}[[()]]]")
        self.assertEqual(charSytaxError, ")")

    def test_foundErrorSquareBracket(self):
        charSytaxError = self.syntaxErrorDetector.checkOnSyntaxError("[{[{({}]{}}([{[{{{}}([]")
        self.assertEqual(charSytaxError, "]")
    
    def test_foundErrorRoundBracket_Two(self):
        charSytaxError = self.syntaxErrorDetector.checkOnSyntaxError("[<(<(<(<{}))><([]([]()")
        self.assertEqual(charSytaxError, ")")
    
    def test_foundErrorArrow(self):
        charSytaxError = self.syntaxErrorDetector.checkOnSyntaxError("<{([([[(<>()){}]>(<<{{")
        self.assertEqual(charSytaxError, ">")
    
    def test_foundErrorArrow(self):
        charSytaxError = self.syntaxErrorDetector.checkOnSyntaxError("<{([([[(<>()){}]>(<<{{")
        self.assertEqual(charSytaxError, ">")
    
    def test_autocompleteStringExampleOne(self):
        addedString = self.syntaxErrorDetector.autoCompleteLine("[({(<(())[]>[[{[]{<()<>>")
        self.assertEqual(addedString, "}}]])})]")
    
    def test_autocompleteStringExampleTwo(self):
        addedString = self.syntaxErrorDetector.autoCompleteLine("[(()[<>])]({[<{<<[]>>(")
        self.assertEqual(addedString, ")}>]})")
    
    def test_autocompleteStringExampleThree(self):
        addedString = self.syntaxErrorDetector.autoCompleteLine("(((({<>}<{<{<>}{[]{[]{}")
        self.assertEqual(addedString, "}}>}>))))")
    
    def test_autocompleteStringExampleFour(self):
        addedString = self.syntaxErrorDetector.autoCompleteLine("{<[[]]>}<{[{[{[]{()[[[]")
        self.assertEqual(addedString, "]]}}]}]}>")
    
    def test_autocompleteStringExampleFive(self):
        addedString = self.syntaxErrorDetector.autoCompleteLine("<{([{{}}[<[[[<>{}]]]>[]]")
        self.assertEqual(addedString, "])}>")

    def test_calculateSyntaxErrorScore(self):
        syntaxErrorScore = self.syntaxErrorDetector.calculateSyntaxErrorScore(self.navigationLines)
        self.assertEqual(syntaxErrorScore, 26397)

    def test_calculateMiddleScore(self):
        middleScore = self.syntaxErrorDetector.calculateMiddleScore(self.navigationLines)
        self.assertEqual(middleScore, 288957)

class Test_SyntaxScoreBoard(unittest.TestCase):
    
    def setUp(self):
        self.syntaxScoreBoard = SyntaxScoreBoard()

    def test_calculateScore(self):
        testarray = ["}",">","]",")","}"]
        score = self.syntaxScoreBoard.calculateScore(testarray)
        expectedScore = 1197 + 25137 + 57 + 3 + 1197
        self.assertEqual(score, expectedScore)
    
    def test_calculateScoreOne(self):
        teststring = "])}>"
        score = self.syntaxScoreBoard.calculateAutoCompletionScore(teststring)
        expectedScore = 294
        self.assertEqual(score, expectedScore)

    def test_calculateScoreTwo(self):
        teststring = "}}]])})]"
        score = self.syntaxScoreBoard.calculateAutoCompletionScore(teststring)
        expectedScore = 288957
        self.assertEqual(score, expectedScore)

class Test_OctopusFlashManager(unittest.TestCase):
    
    def setUp(self):
        self.octopusFlashManager = OctopusFlashManager()
        self.filereader = FileReader()
        self.input1 = self.filereader.readToIntMap("testinput/unittestinputday11_1")
        self.input2 = self.filereader.readToIntMap("testinput/unittestinputday11_2")

    def test_calculateFlashesAfter1Day(self):
        self.octopusFlashManager.setOctopusMap(self.input1)
        score = self.octopusFlashManager.getNumberOfFlashes(4)
        self.assertEqual(score, 9)

    def test_calculateFlashesAfter100Days(self):
        self.octopusFlashManager.setOctopusMap(self.input2)
        score = self.octopusFlashManager.getNumberOfFlashes(100)
        self.assertEqual(score, 1656)

    def test_calculateFirstSynchroinicCycle(self):
        self.octopusFlashManager.setOctopusMap(self.input2)
        cycle = self.octopusFlashManager.getFirstSynchronicCycle()
        self.assertEqual(cycle, 195)

class Test_CaveNavigator(unittest.TestCase):
    
    def setUp(self):
        self.caveNavigator = CaveNavigator()
        self.filereader = FileReader()
        self.input1 = self.filereader.readLinesToStringArray("testinput/unittestinputday12_1")
        self.input2 = self.filereader.readLinesToStringArray("testinput/unittestinputday12_2")
        self.input3 = self.filereader.readLinesToStringArray("testinput/unittestinputday12_3")
    
    def test_findNumberOfRoutesInput1(self):
        routes = self.caveNavigator.findNumberOfRoutes(self.input1)
        self.assertEqual(routes, 10)
        
    def test_findNumberOfRoutesInput2(self):
        routes = self.caveNavigator.findNumberOfRoutes(self.input2)
        self.assertEqual(routes, 19)
        
    def test_findNumberOfRoutesInput3(self):
        routes = self.caveNavigator.findNumberOfRoutes(self.input3)
        self.assertEqual(routes, 226)

    def test_findNumberOfRoutesInput1Part2(self):
        routes = self.caveNavigator.findNumberOfRoutes(self.input1, True)
        self.assertEqual(routes, 36)
        
    def test_findNumberOfRoutesInput2Part2(self):
        routes = self.caveNavigator.findNumberOfRoutes(self.input2, True)
        self.assertEqual(routes, 103)
        
    def test_findNumberOfRoutesInput3Part2(self):
        routes = self.caveNavigator.findNumberOfRoutes(self.input3, True)
        self.assertEqual(routes, 3509)
        

class Test_FolderReader(unittest.TestCase):
    
    def setUp(self):
        self.folder = Folder()
        self.folder.importInputFiles("testinput/unittestinputday13_1")

    def test_findNumberOfDots(self):
        dots = self.folder.CalculateNumberOfDots(True)
        self.assertEqual(dots, 17)
    
    def test_findNumberOfDots2(self):
        dots = self.folder.CalculateNumberOfDots()
        self.assertEqual(dots, 16)
    
    def test_findNumberOfDots3(self):
        self.folder.importInputFiles("testinput/unittestinputday13_2")
        dots = self.folder.CalculateNumberOfDots()
        self.assertEqual(dots, 5)

class Test_Polymarizator(unittest.TestCase):
    
    def setUp(self):
        self.fileReader = FileReader()
        self.polymarizator = Polymarizator()
        data = self.fileReader.readPolymerTemplate("testinput/unittestinputday14")
        self.initialString = data[0]
        self.polyPairs = data[1]

    def test_calculateMostCommonMinusLeastCommon10Steps(self):
        steps = 10
        difference = self.polymarizator.calculateDifference(self.initialString, self.polyPairs, steps)
        self.assertEqual(difference, 1588)
        
    def test_calculateMostCommonMinusLeastCommon40Steps(self):
        steps = 40
        string = self.polymarizator.calculateDifference(self.initialString, self.polyPairs, steps)
        self.assertEqual(string, 2188189693529)

# class Test_DijkstraTests(unittest.TestCase):
    
#     def setUp(self):
#         self.fileReader = FileReader()
#         self.dijkstra = Dijkstra()
#         self.inputMap1 = self.fileReader.readToIntMap("testinput/unittestinputday15_1")
#         self.inputMap2 = self.fileReader.readToIntMap("testinput/unittestinputday15_2")
#         self.inputMap3 = self.fileReader.readToIntMap("testinput/unittestinputday15_3")
        
#     def test_findShortestPathMap1(self):
#         self.dijkstra.setGrid(self.inputMap1)
#         shortestPath1 = self.dijkstra.findShortestPath()
#         self.assertEqual(shortestPath1, 14)
        
#     def test_findShortestPathMap2(self):
#         self.dijkstra.setGrid(self.inputMap2)
#         shortestPath2 = self.dijkstra.findShortestPath()
#         self.assertEqual(shortestPath2, 40)
    
#     def test_findShortestPathExtendedMap2(self):
#         self.dijkstra.setGrid(self.inputMap2, True)
#         shortestPath3 = self.dijkstra.findShortestPath()
#         self.assertEqual(shortestPath3, 315)
    
#     def test_findShortestPathExtendedMap3(self):
#         self.dijkstra.setGrid(self.inputMap3)
#         shortestPath3 = self.dijkstra.findShortestPath()
#         self.assertEqual(shortestPath3, 12)

class Test_PackerDecoder(unittest.TestCase):
    
    def setUp(self):
        self.packetDecoder = PacketDecoder()
        self.examplePackage1 = "D2FE28"
        self.examplePackage2 = "38006F45291200"
        self.examplePackage3 = "EE00D40C823060"
        
    def test_hexToBinaryCoversionTest1(self):
        binString = self.packetDecoder.convertToBinaryString(self.examplePackage1)
        self.assertEqual(binString, "110100101111111000101000")

    def test_hexToBinaryCoversionTest2(self):
        binString = self.packetDecoder.convertToBinaryString(self.examplePackage2)
        self.assertEqual(binString, "00111000000000000110111101000101001010010001001000000000")
 
    def test_hexToBinaryCoversionTest3(self):
        binString = self.packetDecoder.convertToBinaryString(self.examplePackage3)
        self.assertEqual(binString, "11101110000000001101010000001100100000100011000001100000")               
                
    def test_createLiteralPackage(self):
        packet = self.packetDecoder.decodeStringToPackage(self.examplePackage1)
        
        self.assertEqual(packet.version, 6)
        self.assertEqual(packet.typeID, 4)
        self.assertEqual(packet.literalValue, 2021)
        
    def test_createOperatorPackageExampleTwo(self):
        packet = Packet()
        packet = self.packetDecoder.decodeStringToPackage(self.examplePackage2)
        
        self.assertEqual(packet.version, 1)
        self.assertEqual(packet.typeID, 6)
        self.assertEqual(packet.length, 27)        
        self.assertEqual(packet.lengthTypeId, '0')
        self.assertEqual(packet.subPackages[0].literalValue, 10)
        self.assertEqual(packet.subPackages[1].literalValue, 20)
        
        
    def test_createOperatorPackageExampleThree(self):
        packet = Packet()
        packet = self.packetDecoder.decodeStringToPackage(self.examplePackage3)
        
        self.assertEqual(packet.version, 7)
        self.assertEqual(packet.typeID, 3)     
        self.assertEqual(packet.lengthTypeId, '1')
        self.assertEqual(packet.subPackages[0].literalValue, 1)
        self.assertEqual(packet.subPackages[1].literalValue, 2)
        self.assertEqual(packet.subPackages[2].literalValue, 3)        
        
        
if __name__ == '__main__':
    unittest.main()
