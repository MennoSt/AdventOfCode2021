from utils.AocUtils import *
from utils.AocEnums import *
from utils.FileReader import FileReader

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
            
            beacon1 = []
            beacon2 = []    
            coordinate = most_frequent(diffList)
            if coordinate["count"] >= 12:
                coordinateOutput = coordinate
                lastOperator = operator
                print(lastOperator)
                Matches = xMatches
                for match in Matches:
                    if match["diff"] == coordinate["number"]:
                        beacon1.append(match["scanner1"])
                        beacon2.append(match["scanner2"])
                Beacons =[beacon1,beacon2]
                
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
                 
            diffList = []
            xMatches = []
            
        return [coordinateOutput, Beacons]
    
    def coordinatesBetweenScanners(self, scanner1:Scanner, scanner2:Scanner):
    
        xcoor = self.findCommonCoordinate(scanner1, scanner2, "x")
        ycoor = self.findCommonCoordinate(scanner1, scanner2, "y")
        zcoor = self.findCommonCoordinate(scanner1, scanner2, "z")
                
        return [xcoor[0]["number"], ycoor[0]["number"], zcoor[0]["number"]]
        
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
    