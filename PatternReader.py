import re

class PatternReader:
    
    def __init__(self):
        self.uniquePatternArray = []
        self.fourDigitArray = []
    
    def readPattern(self, inputFile):

        fileObj = open(inputFile, "r")
        fileString = fileObj.read().splitlines()
        fileObj.close()

        uniquePatternArray = []
        fourDigitArray = []
        for file in fileString:
            splittedString = file.split("|")
            uniquePattern = splittedString[0].split(" ")
            uniquePattern = list(filter(None, uniquePattern))
            uniquePatternArray.append(uniquePattern)

            fourDigitString = splittedString[1].split(" ")
            fourDigitString = list(filter(None, fourDigitString))
            fourDigitArray.append(fourDigitString)

        self.uniquePatternArray = uniquePatternArray
        self.fourDigitArray = fourDigitArray

        