class SubmarineCalculator:
    
    def GetIncreasedDepthsPart1(self, data):
        increases = 0
        measureResult = self.__IsDepthIncreasedArray(data)
        
        for data in measureResult:
            if data == True:
                increases+=1
        
        return increases

    def GetIncreasedDepthsPart2(self, data):

        array = self.__getSummedDepth(data)
        numberOfIncreasedSummedDepths = self.GetIncreasedDepthsPart1(array)

        return numberOfIncreasedSummedDepths

    def __IsDepthIncreased(self, depth, previousDepth):
        if (depth < previousDepth):
            return True
        if (depth > previousDepth):
            return False

    def __IsDepthIncreasedArray(self, data):
        array = []

        for index in range(0,len(data)):
            if index == 0:
                array.append("No previous measurement")
            else:
                array.append(self.__IsDepthIncreased(data[index-1], data[index]))
        
        return array
    
    def __getSummedDepth(self, data):
        array = []
        summedDepth = 0

        for index in range(0,len(data)-2):
            summedDepth = data[index] + data[index+1] + data[index+2]
            array.append(summedDepth)

        return array

            



