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
        self.scanners = [Scanner]
        self.scanners.pop(0)
        self.beaconsRelativeToScanner = []
        self.visitedScanners = [0]
        self.lastOperation = {'x':Operator.PLUSX, 'y':Operator.PLUSY, 'z':Operator.PLUSZ,}
    
    def getLengthBeacons(self):
        lengthBeacons = len(self.beaconsRelativeToScanner)
        return lengthBeacons
    
    def AddBeaconsRelativeToScanner(self):
        
        self.addAllCoordinatesRelativeToScanner(self.scanners[0])
        
        beacons = []
        for scanner in self.scanners:
            for beacon in scanner.positions:
                beacons.append(beacon)
        
        beacons = self.__removeDuplicatesInDictionairy(beacons)
        self.beaconsRelativeToScanner = sorted(beacons, key=lambda x: x['x'])
        
        print("sorted removed")
    
    def __removeDuplicatesInDictionairy(self, listInput):
        return [dict(t) for t in {tuple(d.items()) for d in listInput}]
        
    def addAllCoordinatesRelativeToScanner(self, scannerInput:Scanner):
        numberOfScanners = len(self.scanners)
        for index in range(0,numberOfScanners):
            if index not in self.visitedScanners:
                print(index)
                coordinates = self.coordinatesBetweenScanners(scannerInput, self.scanners[index])
                print(coordinates)
            
                if coordinates != None:
                    if index not in self.visitedScanners:
                        self.visitedScanners.append(index)
                        scannerTmp = []
                        for beacon in self.scanners[index].positions:
                            beaconInit = copy.deepcopy(beacon)
                            self.updateBeacon(coordinates, beacon, beaconInit, "x")
                            self.updateBeacon(coordinates, beacon, beaconInit, "y")
                            self.updateBeacon(coordinates, beacon, beaconInit, "z")
                            # scannerInput.positions.append(beacon)
                            scannerTmp.append(beacon)
                        self.scanners[index].positions = scannerTmp
                        self.addAllCoordinatesRelativeToScanner(self.scanners[index])
        
                
    def updateBeacon(self, coordinates, beacon, beaconInit, coor:str):
        
        coordinate = 0
        if coor == "x":
            coordinate = coordinates[0]
        elif coor == "y":
            coordinate = coordinates[1]
        elif coor == "z":
            coordinate = coordinates[2]
            
        operator = self.lastOperation[coor]
        if operator == Operator.PLUSX:
            beacon[coor] = -1*(beaconInit['x'] - coordinate)
        elif operator == Operator.MINUSX:
            beacon[coor] = beaconInit['x'] + coordinate
        elif operator == Operator.PLUSY:
            beacon[coor] = -1*(beaconInit['y'] - coordinate)
        elif operator == Operator.MINUSY:
            beacon[coor] = beaconInit['y'] + coordinate  
        elif operator== Operator.PLUSZ:
            beacon[coor] = -1*(beaconInit['z'] - coordinate)
        elif operator == Operator.MINUSZ:
            beacon[coor] = beaconInit['z'] + coordinate
     
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
                self.lastOperation[forString] = lastOperator
                print(lastOperator)
                return coordinateOutput
            
            diffList = []
            xMatches = []
            
        return coordinateOutput
    
    def coordinatesBetweenScanners(self, scanner1:Scanner, scanner2:Scanner):
    
        xcoor = self.findCommonCoordinate(scanner1, scanner2, "x")
        ycoor = self.findCommonCoordinate(scanner1, scanner2, "y")
        zcoor = self.findCommonCoordinate(scanner1, scanner2, "z")
        
        if xcoor != None and ycoor != None and zcoor != None:
            coordinate = [xcoor["number"], ycoor["number"], zcoor["number"]]
        else:
            coordinate = None
            
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

    scanManager.readInputDataIntoScanners("input/inputday19")
    scanManager.AddBeaconsRelativeToScanner()
    answerPart1 = scanManager.getLengthBeacons()
    answerPart2 = 0
    
    printAnswer(18, answerPart1, answerPart2)

    