from utils.AocUtils import *
from utils.AocEnums import *
from utils.FileReader import FileReader
import copy

def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
    
    numberCount = {"number": num, "count":counter}
    
    return numberCount

class Operator(Enum):
    MINUSX = 0
    PLUSX = 1
    MINUSY = 2
    PLUSY = 3
    MINUSZ = 4
    PLUSZ = 5
    
class Scanner:
    def __init__(self, name:str, position):
        self.name = name
        self.positions = position
         

class ScanManager:
    def __init__(self):
        self.scanners = []
        self.beacons = []
    
    def getLengthBeacons(self):
        #from Scanner0:
        for index in range(1,5):
            beacons = self.updateCommonBeacons(self.scanners[0], self.scanners[index])
            if beacons != None:
                tmpBeacons = copy.deepcopy(beacons)
                for beacon in tmpBeacons:
                    self.beacons.append(beacon)
        
        #Scanner1:
        for index in range(2,5):
            beacons = self.updateCommonBeacons(self.scanners[1], self.scanners[index])
            if beacons != None:
                coordinates = self.coordinatesBetweenScanners(self.scanners[0], self.scanners[1])
                
                tmpBeacons = copy.deepcopy(beacons)
                for lap in tmpBeacons:
                    lap['x'] = -1*(lap['x']-coordinates[0])
                    lap['y'] = lap['y']+coordinates[1]
                    lap['z'] = -1*(lap['z']-coordinates[2])
                
                for beacon in tmpBeacons:
                    self.beacons.append(beacon)
        
        # remove duplicates:
        self.beacons = [dict(t) for t in {tuple(d.items()) for d in self.beacons}]
        
        lengthBeacons = len(self.beacons[0])
        
        return lengthBeacons
    
    def updateCommonBeacons(self, scanner1:Scanner, scanner2:Scanner):
        forString = "x"
        beacon1 = None
        xMatches =[]
        diffList = []
        operators = [Operator.MINUSX, Operator.PLUSX, Operator.MINUSY, Operator.PLUSY, Operator.MINUSZ, Operator.PLUSZ]

        for operator in operators:
            for index1 in range (0, len(scanner1.positions)):
                for index2 in range(0,len(scanner2.positions)):
                    if operator == Operator.MINUSX:
                        diff = scanner1.positions[index1][forString] - scanner2.positions[index2]["x"]
                    elif operator == Operator.PLUSX:
                        diff = scanner1.positions[index1][forString] + scanner2.positions[index2]["x"]
                    elif operator == Operator.MINUSY:
                        diff = scanner1.positions[index1][forString] - scanner2.positions[index2]["y"]
                    elif operator == Operator.PLUSY:
                        diff = scanner1.positions[index1][forString] + scanner2.positions[index2]["y"]
                    elif operator == Operator.MINUSZ:
                        diff = scanner1.positions[index1][forString] - scanner2.positions[index2]["z"]
                    elif operator == Operator.PLUSZ:
                        diff = scanner1.positions[index1][forString] + scanner2.positions[index2]["z"]
                        
                    diffList.append(diff)
                    xMatches.append({'scanner1':scanner1.positions[index1], 'diff':diff})
                
            coordinate = most_frequent(diffList)
            if coordinate["count"] >= 12:
                Matches = xMatches    
                beacon1 = []
                for match in Matches:
                    if match["diff"] == coordinate["number"]:
                        beacon1.append(match["scanner1"])
                
            diffList = []
            xMatches = []
        
        return beacon1
        
     
    def findCommonCoordinate(self, scanner1:Scanner, scanner2:Scanner, forString:str):
        diffList = []
        xMatches =[]
        coordinateOutput = None
        operators = [Operator.MINUSX, Operator.PLUSX, Operator.MINUSY, Operator.PLUSY, Operator.MINUSZ, Operator.PLUSZ]

        for operator in operators:
            for index1 in range (0, len(scanner1.positions)):
                for index2 in range(0,len(scanner2.positions)):
                    if operator == Operator.MINUSX:
                        diff = scanner1.positions[index1][forString] - scanner2.positions[index2]["x"]
                    elif operator == Operator.PLUSX:
                        diff = scanner1.positions[index1][forString] + scanner2.positions[index2]["x"]
                    elif operator == Operator.MINUSY:
                        diff = scanner1.positions[index1][forString] - scanner2.positions[index2]["y"]
                    elif operator == Operator.PLUSY:
                        diff = scanner1.positions[index1][forString] + scanner2.positions[index2]["y"]
                    elif operator == Operator.MINUSZ:
                        diff = scanner1.positions[index1][forString] - scanner2.positions[index2]["z"]
                    elif operator == Operator.PLUSZ:
                        diff = scanner1.positions[index1][forString] + scanner2.positions[index2]["z"]
                        
                    diffList.append(diff)
                    xMatches.append({'scanner1':scanner1.positions[index1], 'scanner2' :scanner2.positions[index2], 'diff':diff})
                
            coordinate = most_frequent(diffList)
            if coordinate["count"] >= 12:
                coordinateOutput = coordinate
                lastOperator = operator
                print(lastOperator)
                Matches = xMatches
                self.handleMinusSign(coordinate, lastOperator, Matches)
                 
            diffList = []
            xMatches = []
            
        return coordinateOutput

    def handleMinusSign(self, coordinate, lastOperator, Matches):
        for match in Matches:
            if match["diff"]== coordinate["number"]:
                if lastOperator == Operator.MINUSX:
                    if match["scanner1"]["x"] > match["scanner2"]["x"]:
                        coordinate["number"] *= -1
                elif lastOperator == Operator.MINUSY:
                    if match["scanner1"]["y"] > match["scanner2"]["y"]:
                        coordinate["number"] *= -1
                elif lastOperator == Operator.MINUSZ:
                    if match["scanner1"]["z"] > match["scanner2"]["z"]:
                        coordinate["number"] *= -1
    
    def coordinatesBetweenScanners(self, scanner1:Scanner, scanner2:Scanner):
    
        xcoor = self.findCommonCoordinate(scanner1, scanner2, "x")
        ycoor = self.findCommonCoordinate(scanner1, scanner2, "y")
        zcoor = self.findCommonCoordinate(scanner1, scanner2, "z")
        
        coordinate = [xcoor["number"], ycoor["number"], zcoor["number"]]
            
        return coordinate
    
    def readInputDataIntoScanners(self, input):
        with open (input, "r") as myfile:
            dataread = myfile.read().rstrip()
            chartData = dataread.split('\n\n')
    
        for data in chartData:
            scanData = data.split("\n")
            self.__readDataIntoScanners(scanData)    

    def __readDataIntoScanners(self,scanData):
        name = scanData[0]
        scanData.pop(0)
        
        positions = []
        for line in scanData:
            line = list(map(int,line.split(",")))
            position = {"x" : line[0], "y" :line[1], "z": line[2]}
            positions.append(position)
        
        scanner = Scanner(name,positions)
        self.scanners.append(scanner) 
        
        
    def addScanner(self, scanner:Scanner):
        self.scanners.append(scanner)
        
def solutionDay19():
    scanManager = ScanManager()
    fileReader = FileReader()
    # fileString = fileReader.readLinesToStringArray("input/inputday19")
    
    scanManager.readInputDataIntoScanners("input/inputday19")
    
    print(scanManager.scanners)
    