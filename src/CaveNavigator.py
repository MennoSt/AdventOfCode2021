class Node():
    def __init__(self, character):
        self.character = character
        self.neighbours =[]
        
    def addNeighour(self, neighbour):
        self.neighbours.append(neighbour)
    
    def getCharacter(self):
        return self.character


class CaveNavigator:
    def __init__(self):
        self.Nodes = [Node("")]
        self.numberOfPaths = 0
        self.nextnode = Node("")
        self.pathString = []
        
    def findNumberOfRoutes(self, fileinput):
        
        self.__updateNodeInfo(fileinput)
        routes = self.iterateThroughPath()
        return routes


    def iterateThroughPath(self):
        
        startNode = self.__getStartNode()
        visitedNodes = ["start"]
        self.pathCount = 0

        self.__compareNode(startNode, visitedNodes)

        return self.pathCount
    
    def __compareNode(self, nextnode, visitedNodes):
        for str in nextnode.neighbours:
            if str == "end":
                self.pathCount += 1
            elif str not in visitedNodes:
                if not str.isupper():
                    visitedNodes.append(str)
                nextnode = self.__getNode(str)
                self.__compareNode(nextnode, visitedNodes)
                if str in visitedNodes: visitedNodes.remove(str)
            
    def __getNode(self, char):
        for node in self.Nodes:
            if node.getCharacter() == char:
                return node       
        
    def __getStartNode(self):
        for node in self.Nodes:
            if node.getCharacter() == "start":
                return node
            
    def __getUniqeNodeArray(self, fileinput):
        array = []
        for file in fileinput:
            connection = file.split("-")
            array.append(connection[0])
            array.append(connection[1])
        
        uniqueNodeList = list(set(array))
        return uniqueNodeList
    
    def __updateNodeInfo(self, fileinput):
        
        NodeList = self.__getUniqeNodeArray(fileinput)
        
        self.Nodes.pop()
        
        for char in NodeList:
            newnode = Node(char)
            self.Nodes.append(newnode)
        
        for file in fileinput:
            nodePair = file.split("-")

            for node in self.Nodes:
                if node.getCharacter() == nodePair[0]:
                    node.addNeighour(nodePair[1])
                if node.getCharacter() == nodePair[1]:
                    node.addNeighour(nodePair[0])
        

                    



            





            



