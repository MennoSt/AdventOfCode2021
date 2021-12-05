class PositionCalculator:
    
    def __init__(self):
        self.horizontalP = 0
        self.depthP = 0
        self.aim = 0

    def UpdatePosition(self, directionArray, positionArray):
        self.horizontalP = 0
        self.depthP = 0
        length_dir = len(directionArray)
        length_pos = len(positionArray)   

        if (length_dir != length_pos):
            raise Exception("Length of arrays is not equal")
        
        for index in range(0,length_dir):
            if (directionArray[index] == "up"):
                self.depthP -= positionArray[index]
            elif (directionArray[index] == "down"):
                self.depthP += positionArray[index]
            elif (directionArray[index] == "forward"):
                self.horizontalP += positionArray[index]
            else:
                raise Exception("Invalid Direction")
    
    def getMultiplication(self, directionArray, positionArray):

        self.UpdatePosition(directionArray, positionArray)
        multiplication = self.horizontalP * self.depthP

        return multiplication
    
    def UpdatePositionPart2(self, directionArray, positionArray):
        length_dir = len(directionArray)
        length_pos = len(positionArray) 
        self.horizontalP = 0
        self.depthP = 0
        self.aim = 0

        if (length_dir != length_pos):
            raise Exception("Length of arrays is not equal")
        
        for index in range(0,length_dir):
            if (directionArray[index] == "up"):
                self.aim -= positionArray[index]
            elif (directionArray[index] == "down"):
                self.aim += positionArray[index]
            elif (directionArray[index] == "forward"):
                self.horizontalP += positionArray[index]
                self.depthP += self.aim * positionArray[index]
            else:
                raise Exception("Invalid Direction")
    
    def getMultiplicationPart2(self, directionArray, positionArray):

        self.UpdatePositionPart2(directionArray, positionArray)

        multiplication = self.horizontalP * self.depthP

        return multiplication
    
            

            





            



