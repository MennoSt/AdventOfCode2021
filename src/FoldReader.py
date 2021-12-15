class FoldReader:
    
    def __init__(self):
        self.coordinatesArray = []
        self.foldArray = []

    def readToFoldArray(self, inputFile):
        fileObj = open(inputFile, "r")
        fileString = fileObj.read().splitlines()
        fileObj.close()
        
        for line in fileString:
            if "fold along" in line:
                string = line.replace("fold along ", "")
                string = string.split("=")
                string[1] = int(string[1])
                self.foldArray.append(string)
            elif line != "":
                intValue = list(map(int,line.split(",")))
                self.coordinatesArray.append(intValue)