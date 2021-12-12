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
        visited = {node.label: False for node in self.graph.keys()}
        path = []
        self._computeAllPathsUtil(start, end, visited, path)
    
    def _computeAllPathsUtil(self, start, end, visited, path):
        if start.isSmall:
            visited[start.label]= True

        path.append(start)
 
        if start == end:
            self.pathCounter +=1
        else:
            for node in self.graph[start]:
                if not visited[node.label]:
                    self._computeAllPathsUtil(node, end, visited, path)
                     
        path.pop()
        visited[start.label]= False