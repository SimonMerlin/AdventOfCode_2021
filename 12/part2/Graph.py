from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.pathCounter = 0
    
    def addEdge(self, n1, n2):
        if n2 not in self.graph[n1]:
            self.graph[n1].append(n2)
        if n1 not in self.graph[n2]:
            self.graph[n2].append(n1)
    
    def printGraph(self):
        for i in self.graph.keys():
            print(i.label + " : ", end="")
            for n in self.graph[i]:
                print(n.label + " ", end="")
            print()
    
    def printPath(self, path):
        for node in path:
            print(node.label, end=",")
        print()
    
    def computeAllPaths(self, start, end):
        visiteCount = {node.label: 0 for node in self.graph.keys()}
        path = []
        self._computeAllPathsUtil(start, end, visiteCount, path, None)
    
    def _computeAllPathsUtil(self, start, end, visiteCount, path, smallCaveVistedTwice):
        if start.isSmall:
            visiteCount[start.label] +=1
            if smallCaveVistedTwice == None and visiteCount[start.label] == 2:
                smallCaveVistedTwice = start.label

        path.append(start)
 
        if start == end:
            self.pathCounter +=1
        else:
            for node in self.graph[start]:
                if node.canBeVisited(visiteCount[node.label], smallCaveVistedTwice):
                    self._computeAllPathsUtil(node, end, visiteCount, path, smallCaveVistedTwice)
                     
        path.pop()
        if start.isSmall:
            visiteCount[start.label] -=1