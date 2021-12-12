class Node():
    def __init__(self, character):
        self.character = character
        self.neighbours =[]
        
    def addNeighour(self, neighbour):
        self.neighbours.append(neighbour)
    
    def getCharacter(self):
        return self.character


class CaveNavigator:
    def findNumberOfRoutes(self, connectionMap):
        return 0

    def getUniqeNodeArray(self, fileinput):
        array = []
        for file in fileinput:
            connection = file.split("-")
            array.append(connection[0])
            array.append(connection[1])
        
        uniqueNodeList = list(set(array))
        return uniqueNodeList
    
    def determineNeighboursPerNode(self, fileinput):
        
        NodeList = self.getUniqeNodeArray(fileinput)
        Nodes =[]
        
        test = Node("3")
        print(test.character)

        for char in NodeList:
            newnode = Node(char)
            Nodes.append(newnode)
        
        for file in fileinput:
            connection = file.split("-")
            connector0 = connection[0]
            connector1 = connection[1]

            for node in Nodes:
                if node.getCharacter() == connector0:
                    node.addNeighour(connector1)
                if node.getCharacter() == connector1:
                    node.addNeighour(connector0)
        
        for node in Nodes:
            print(node.neighbours)
                    



            





            



