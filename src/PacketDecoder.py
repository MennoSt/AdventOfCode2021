
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
    
class PacketDecoder:
    
    def __init__(self):
        self.packages = [Packet]

    def convertToBinaryString(self, hexstring):
        binaryString = ""
        for char in hexstring:
            for conversion in binaryConversionList:
                if char == conversion[0]:
                    binaryString += conversion[1]
        
        return binaryString
        
        
    def decodeStringToPackage(self, hexstring):
        binString = self.convertToBinaryString(hexstring)
        
        
        packet =  Packet()
        packet.version = int(binString[0:3],2)
        packet.typeID = int(binString[3:6],2)
        
        #literal package
        if packet.typeID == 4:
            packet.literal = True
            self.__addLiteralValue(binString, packet)
        
        #operater package
        else:
            packet.lengthTypeId = binString[6]
            if packet.lengthTypeId == "0":
                # 15 bit length number
                packet.length = int(binString[7:22],2)
                lengthSubpackages = 0
                while(lengthSubpackages < packet.length):
                    subpacket = Packet()
                    startIndex = 22 + lengthSubpackages
                    subpacket.version = int(binString[startIndex:(startIndex+3)],2)
                    subpacket.typeID = int(binString[(startIndex+3):(startIndex+6)],2)
                    if subpacket.typeID == 4:
                        subpacket.literal = True
                        self.__addLiteralValue(binString, subpacket, startIndex + 6)
                    else:
                        Exception("would expect type ID 4, no subpackages of subpackages")
                        #add functionality for subpackages in subpackages
                    
                    lengthSubpackages += subpacket.getLengthlitValuePackages()
                    packet.subPackages.append(subpacket)
                
            elif packet.lengthTypeId == "1":         
                # 11 bit length number
                packet.length = int(binString[7:18], 2)
                for it in range(0, packet.length):
                    subpacket = Packet()
                    startIndex = 18 + it *11
                    subpacket.version = int(binString[startIndex:(startIndex+3)],2)
                    subpacket.typeID = int(binString[(startIndex+3):(startIndex+6)],2)
                    if subpacket.typeID == 4:
                        subpacket.literal = True
                        self.__addLiteralValue(binString, subpacket, startIndex + 6)
                    else:
                        Exception("would expect type ID 4, no subpackages of subpackages")
                        #add functionality for subpackages in subpackages
                        
                    packet.subPackages.append(subpacket)
                

        
        return packet

    def __addLiteralValue(self, binString, packet, startIndex = 6):

        endReached = False
        
        while(not endReached):
            firstIndex = startIndex
            firstValue = binString[firstIndex]
            if firstValue == '1' and not endReached:
                index1 = startIndex
                index2 = 5 + startIndex
                packet.literalValuePackages.append(binString[index1:index2])
                startIndex += 5
            else:
                index1 = startIndex
                index2 = 5 + startIndex
                packet.literalValuePackages.append(binString[index1:index2])
                startIndex += 5
                endReached = True
    
        packet.updateLiteralValue()
            
            