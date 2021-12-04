import pandas as pd

class SubmarineCalculator:
    
    # def __init__(self):

    
    def IsDepthIncreased(self, depth, previousDepth):
        if (depth < previousDepth):
            return True
        if (depth > previousDepth):
            return False

    def IsDepthIncreasedArray(self, data):
        array = []
        df_depth = data

        for index in range(0,df_depth.size):
            if index == 0:
                array.append("No previous measurement")
            else:
                array.append(self.IsDepthIncreased(df_depth[index-1], df_depth[index]))
        
        return array
    
    def GetNumberOfIncreasedDepths(self, data):

        increases = 0
        
        measureResult = self.IsDepthIncreasedArray(data)
        for data in measureResult:
            if data == True:
                increases+=1
        
        return increases
    
    def getSummedDepth(self, df_depth):

        array = []
        summedDepth = 0

        for index in range(0,df_depth.size):
            summedDepth += df_depth[index]
            if (index+1) % 3 == 0:
                array.append(summedDepth)
                summedDepth = 0

        array.append(summedDepth)

        return array

        
    def getNumberOfIncreasesSummedDepth(self, df_depth):

        array = self.getSummedDepth(df_depth)
        df = pd.DataFrame(array)
        numberOfIncreasedSummedDepths = self.GetNumberOfIncreasedDepths(df)

        return numberOfIncreasedSummedDepths


            



