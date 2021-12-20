
binaryConversionList = [["0","0000"],
                        ["1","0001"],
                        ["2","0010"],
                        ["3","0011"],
                        ["4","0100"],
                        ["5","0101"],
                        ["6","0110"],
                        ["7","0111"],
                        ["8","1000"],
                        ["9","1001"],
                        ["A","1010"],
                        ["B","1011"],
                        ["C","1100"],
                        ["D","1101"],
                        ["E","1110"],
                        ["F","1111"]]

class Packet:
    
    def __init__(self):
        self.version = -1
        self.typeID = -1
        self.literal = False
        self.literalValue = -1
        self.literalValuePackages = []
        
        self.operator = False
        self.lengthTypeId = -1
        self.numberOfSubPackages = -1
        self.subPackages = []
        self.length = -1
        
    def updateLiteralValue(self):
        litValue=""
        for value in self.literalValuePackages:
            litValue+=value[1:5]
        
        self.literalValue  = int(litValue,2)
    
    def getLengthlitValuePackages(self):
        sumLiteralValue = 6  # includes header
        for literalValue in self.literalValuePackages:
            sumLiteralValue += (len(literalValue))
            
        return sumLiteralValue
    
    def getVersionSum(self):
        sumVersion = self.version
        
        for subpackage in self.subPackages:
            sumVersion += subpackage.version
        
        return sumVersion    
    
class PacketDecoder:
    
    def __init__(self):
        self.packets = [Packet]
        self.packets.pop()
        self.binItIndex = 0
    
    def getVersionSum(self):
        totalSum =0
        for packet in self.packets:
            versionSum = packet.getVersionSum()
            totalSum+=versionSum
        
        return totalSum
        
    def convertToBinaryString(self, hexstring):
        binaryString = ""
        for char in hexstring:
            for conversion in binaryConversionList:
                if char == conversion[0]:
                    binaryString += conversion[1]
        
        return binaryString
        
        
    def decodeStringToPackage(self, hexstring):
        
        binString = self.convertToBinaryString(hexstring)
        self.binItIndex = 0
        lengthBinString = len(binString)
        
        while (self.binItIndex+3 < lengthBinString):   
            self.addPackets(binString)

    def addPackets(self, binString):
        packet =  Packet()
        
        packet.version = int(binString[self.binItIndex:self.binItIndex+3],2)
        packet.typeID = int(binString[self.binItIndex+3:self.binItIndex+6],2)
            
            #literal package
        if packet.typeID == 4:
            packet.literal = True
            self.binItIndex += 6
            self.__readLiteralData(binString, packet)

            #operater package
        else:
            self.readOperatorData(binString, packet)
                
        self.packets.append(packet)

    def readOperatorData(self, binString, packet):
        
        packet.lengthTypeId = binString[self.binItIndex+6]
        if packet.lengthTypeId == "0":
                    # 15 bit length number
            packet.length = int(binString[self.binItIndex+7:self.binItIndex+22],2)
            lengthSubpackages = 0
            self.binItIndex+=22
            while(lengthSubpackages < packet.length):
                subpacket = Packet()
                subpacket.version = int(binString[self.binItIndex:self.binItIndex+3],2)
                subpacket.typeID = int(binString[self.binItIndex+3:self.binItIndex+6],2)
                if subpacket.typeID == 4:
                    self.binItIndex += 6
                    subpacket.literal = True
                    self.__readLiteralData(binString, subpacket)
                    lengthSubpackages += subpacket.getLengthlitValuePackages()
                    packet.subPackages.append(subpacket)
                else:
                    subpacket.operator = True
                    break
            self.binItIndex += lengthSubpackages
                    
        elif packet.lengthTypeId == "1":         
                    # 11 bit length number
            packet.length = int(binString[self.binItIndex+7:self.binItIndex+18], 2)
            self.binItIndex += 18
            for it in range(0, packet.length):
                subpacket = Packet()
                subpacket.version = int(binString[self.binItIndex:(self.binItIndex+3)],2)
                subpacket.typeID = int(binString[(self.binItIndex+3):(self.binItIndex+6)],2)
                if subpacket.typeID == 4:
                    self.binItIndex += 6
                    subpacket.literal = True
                    self.__readLiteralData(binString, subpacket)
                    packet.subPackages.append(subpacket)
                else:
                    subpacket.operator = True
                    break
            self.binItIndex += it *11
        
        
    def __readLiteralData(self, binString, packet):

        endReached = False
        
        while(not endReached):
            firstIndex = self.binItIndex
            firstValue = binString[firstIndex]
            if firstValue == '1' and not endReached:
                index1 = self.binItIndex
                index2 = 5 + self.binItIndex
                packet.literalValuePackages.append(binString[index1:index2])
                self.binItIndex += 5
            else:
                index1 = self.binItIndex
                index2 = 5 + self.binItIndex
                packet.literalValuePackages.append(binString[index1:index2])
                self.binItIndex += 5
                endReached = True
    
        packet.updateLiteralValue()
            
            