class Node:

    def __init__(self, label):
        self.label = label
        self.isSmall = label.islower()

    def canBeVisited(self, visitCount, smallCaveVistedTwice):
        if self.label == 'start' or self.label == 'end':
            return visitCount == 0
        if self.isSmall and smallCaveVistedTwice != None and smallCaveVistedTwice == self.label:
            return False
        if self.isSmall and smallCaveVistedTwice != None and smallCaveVistedTwice != self.label:
            return visitCount == 0
        return True
    
    def setVisited(self):
        self.visitCounter += 1
    
    def resetVisited(self):
        self.visited = False
    
    def __str__(self):
        return self.label
