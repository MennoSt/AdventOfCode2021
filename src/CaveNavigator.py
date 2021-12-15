class Node():
    def __init__(self, character):
        self.character = character
        self.neighbours = []
        self.numberOfVisits = 0
        self.array = []
        
    def addNeighour(self, neighbour):
        self.neighbours.append(neighbour)
    
    def getCharacter(self):
        return self.character

    def increaseNumberOfVisits(self, string):
        self.numberOfVisits += 1
    
    def decreaseNumberOfVisits(self):
        self.numberOfVisits -= 1
        


class CaveNavigator:
    def __init__(self):
        self.Nodes = [Node("")]
        self.numberOfPaths = 0
        self.nextnode = Node("")
        # self.visitArray = []
        # self.visitArrays = []
        
    def findNumberOfRoutes(self, fileinput, smallCavesTwice = False):
        
        self.__updateNodeInfo(fileinput)
        routes = self.iterateThroughPath(smallCavesTwice)
        return routes


    def iterateThroughPath(self, smallCavesTwice):
        
        startNode = self.__getStartNode()
        visitedNodes = ["start", "start"]
        self.pathCount = 0
        
        if not smallCavesTwice:
            self.__compareNodePart1(startNode, visitedNodes)
        else:
            self.__compareNodePart2(startNode, visitedNodes)

        return self.pathCount
    
    def __compareNodePart1(self, currentNode, visitedNodes):
        for str in currentNode.neighbours:
            nextnode = self.__getNode(str)
            if str == "end":
                self.pathCount += 1
            elif str not in visitedNodes:
                if not str.isupper():
                    visitedNodes.append(str)
                self.__compareNodePart1(nextnode, visitedNodes)
                if str in visitedNodes: 
                    visitedNodes.remove(str)
    
    def __compareNodePart2(self, currentNode, visitedNodes):
        for str in currentNode.neighbours:
            nextnode = self.__getNode(str)
            if str == "end":
                # print(self.visitArray)
                # self.visitArrays.append(self.visitArray)
                self.pathCount += 1
            elif self.isNextVisitAllowed(str,visitedNodes) == True:
                nextnode.increaseNumberOfVisits(str)
                # self.visitArray.append(str) 
                if not str.isupper():
                    visitedNodes.append(str)
                self.__compareNodePart2(nextnode, visitedNodes)
                if str in visitedNodes: 
                    visitedNodes.remove(str)
                nextnode.decreaseNumberOfVisits()
                # self.visitArray.pop()
    
    def isNextVisitAllowed(self, str, visitedNodes):
        allowed = False
        if str not in visitedNodes:
            allowed = True
        elif str in visitedNodes and not self.isSmallNodeVisitedMoreThanTwice() and str!="start" and not str.isupper():
            allowed = True
        else:
            allowed = False
            
        return allowed
                        
    def isSmallNodeVisitedMoreThanTwice(self):
        for node in self.Nodes:
            if not node.character.isupper() and node.character != "start":
                if node.numberOfVisits > 1:
                    return True

        return False
                         
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
        

                    



            





            



