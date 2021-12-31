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

class Scanner:
    def __init__(self, name:str, position):
        self.name = name
        self.positions = position
         

class ScanManager:
    def __init__(self):
        self.scanners = []
    
    def coordinatesBetweenScanners(self, scanner1:Scanner, scanner2:Scanner):
        xdiff = []
        xMatches = []
        ydiff = []
        zdiff = []
        xdiffTmp = []
        
        for index1 in range (0, len(scanner1.positions)):
            for index2 in range(0,len(scanner2.positions)):
                # diff = scanner1.positions[index1]["x"] + scanner2.positions[index2]["x"]
                # xdiff.append(diff)
                # xMatches.append({'scanner1':scanner1.positions[index1], 'scanner2' :scanner2.positions[index2], 'diff':diff})
                
                xdiff.append(scanner1.positions[index1]["x"] - scanner2.positions[index2]["x"])
                xdiff.append(scanner1.positions[index1]["x"] + scanner2.positions[index2]["x"])
                xdiff.append(scanner1.positions[index1]["x"] - scanner2.positions[index2]["y"])
                xdiff.append(scanner1.positions[index1]["x"] + scanner2.positions[index2]["y"])
                xdiff.append(scanner1.positions[index1]["x"] - scanner2.positions[index2]["z"])               
                xdiff.append(scanner1.positions[index1]["x"] + scanner2.positions[index2]["z"])
                
                ydiff.append(scanner1.positions[index1]["y"] - scanner2.positions[index2]["y"])
                ydiff.append(scanner1.positions[index1]["y"] + scanner2.positions[index2]["y"])
                ydiff.append(scanner1.positions[index1]["y"] - scanner2.positions[index2]["x"])
                ydiff.append(scanner1.positions[index1]["y"] + scanner2.positions[index2]["x"])
                ydiff.append(scanner1.positions[index1]["y"] - scanner2.positions[index2]["z"])                
                ydiff.append(scanner1.positions[index1]["y"] + scanner2.positions[index2]["z"])
                
                zdiff.append(scanner1.positions[index1]["z"] - scanner2.positions[index2]["z"])
                zdiff.append(scanner1.positions[index1]["z"] + scanner2.positions[index2]["z"])
                zdiff.append(scanner1.positions[index1]["z"] - scanner2.positions[index2]["x"])
                zdiff.append(scanner1.positions[index1]["z"] + scanner2.positions[index2]["x"])
                zdiff.append(scanner1.positions[index1]["z"] - scanner2.positions[index2]["y"])
                zdiff.append(scanner1.positions[index1]["z"] + scanner2.positions[index2]["y"])
        
        beacon1 = []
        beacon2 = []
        xcoor = most_frequent(xdiff)
        if xcoor["count"]>=12:
            for match in xMatches:
                if match["diff"] == xcoor["number"]:
                    beacon1.append(match["scanner1"])
                    beacon2.append(match["scanner2"])
        
        print(beacon1)
        print(beacon2)
        
        ycoor = most_frequent(ydiff)
        zcoor = most_frequent(zdiff)
        
        print("xdiff:"+ str(xcoor))
        print("ydiff:"+ str(ycoor))
        print("zdiff:"+ str(zcoor))
        
        return [xcoor["number"], ycoor["number"], zcoor["number"]]
        
        
        
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
    