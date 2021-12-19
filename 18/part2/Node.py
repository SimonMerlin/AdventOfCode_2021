import uuid

class Node():

    def __init__(self, value=None, left=None, right=None):
        self.key = uuid.uuid4()
        self.value = value
        self.right = right
        self.left = left
        self.depth = 0
    
    def getRight(self):
        return self.right
    
    def getLeft(self):
        return self.left
    
    def setRight(self, node):
        self.value = None
        self.right = node
    
    def setLeft(self, node):
        self.value = None
        self.left = node
    
    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.left = None
        self.right = None
        self.value = value
    
    def isNodeValue(self):
        return self.value != None
    
    def updateDepth(self, depth=None):
        if depth == None:
            depth = self.depth
        self.depth = depth
        if self.left != None:
            self.left.updateDepth(depth+1)
        if self.right != None:
              self.right.updateDepth(depth+1)

    def __str__(self):
        if self.value != None:
            return str(self.value) + "(" + str(self.depth) + ")"
        else:
            return "[" + str(self.left) + "," + str(self.right) + "]"+ "(" + str(self.key) + ")"