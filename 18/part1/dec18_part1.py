import sys
import os
import re
from Node import Node
import math

f = open(os.path.join(sys.path[0], './data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

def getGraphFromLine(line):
    baseCaseRegex = r"^\[\d+,\d+\]$"
    simpleValueRightRegex = r"^\[\[.*\],\d+\]$"
    simpleValueLeftRegex = r"^\[\d+,\[.*\]\]$"
    if re.match(baseCaseRegex, line) != None:
        line = line[1:-1].split(",")
        return Node(None, Node(int(line[0])), Node(int(line[1])))
    elif re.match(simpleValueRightRegex, line) != None:
        index = 1
        file = [line[1]]
        while len(file)>0:
            index +=1
            if line[index] == "[":
                file.append(line[index])
            elif line[index] == "]":
                file.pop()
        return Node(None, getGraphFromLine(line[1:index+1]), Node(int(line[index+2:-1])))
    elif re.match(simpleValueLeftRegex, line) != None:
        line = line[1:-1].split(",", 1)
        return Node(None, Node(int(line[0])),  getGraphFromLine(line[1]))
    else:
        index = 1
        file = [line[1]]
        while len(file)>0:
            index +=1
            if line[index] == "[":
                file.append(line[index])
            elif line[index] == "]":
                file.pop()
        left = getGraphFromLine(line[1:index+1])
        right = getGraphFromLine(line[index+2:-1])
        return Node(None, left, right)

def getValueNodeOrder(node):
    orderered = []
    if node.isNodeValue():
        orderered.append(node)
        return orderered
    else:
        return orderered + getValueNodeOrder(node.getLeft()) + getValueNodeOrder(node.getRight())

def findExplodingPair(node):
    if node == None:
        return None
    if node.depth == 4 and node.left != None and node.left.isNodeValue() and node.right != None and node.right.isNodeValue():
        return node
    elif node.depth > 4:
        return None
    else:
        explodingLeft = findExplodingPair(node.left)
        if explodingLeft != None:
            return explodingLeft
        explodingRight = findExplodingPair(node.right)
        if explodingRight != None:
            return explodingRight
    return None

def findSplitNode(node):
    if node == None:
        return None
    if node.getLeft() is None and node.getRight() is None and node.isNodeValue() and node.getValue() > 9:
        return node
    else:
        splitInLeft = findSplitNode(node.getLeft())
        if splitInLeft != None:
            return splitInLeft
        splitInRight = findSplitNode(node.getRight())
        if splitInRight != None:
            return splitInRight
    return None


def reduceGraph(node):
    explodingNode = findExplodingPair(node)
    splitNode = findSplitNode(node) 
    if explodingNode != None: # exlode this node
        orderedValues = getValueNodeOrder(node)
        #distribute left value
        leftKey = explodingNode.getLeft().key
        index = None
        for i in range(len(orderedValues)):
            if orderedValues[i].key == leftKey:
                index = i
                break
        if index > 0:
            orderedValues[index-1].setValue(orderedValues[index-1].getValue() + explodingNode.getLeft().getValue())
        #distribute right value
        rightKey = explodingNode.getRight().key
        index = None
        for i in range(len(orderedValues)):
            if orderedValues[i].key == rightKey:
                index = i
                break
        if index < len(orderedValues)-1:
            #print(orderedValues[index+1])
            orderedValues[index+1].setValue(orderedValues[index+1].getValue() + explodingNode.getRight().getValue())
        #set explodingNode to 0
        explodingNode.setValue(0)
        node.updateDepth()
        #return node
        reduceGraph(node)
    elif splitNode != None:
        lv = math.floor(splitNode.getValue()/2)
        rv = math.ceil(splitNode.getValue()/2)
        splitNode.setLeft(Node(lv))
        splitNode.setRight(Node(rv))
        node.updateDepth()
        #return node
        reduceGraph(node)
    return node


def addAndReduceLines(lines):
    node = getGraphFromLine(lines[0])
    node.updateDepth(0)
    for line in lines[1:]:
        graphLine = getGraphFromLine(line)
        node = Node(None, node, graphLine)
        node.updateDepth(0)
        node = reduceGraph(node)
    return node

def computeMagnitude(node):
    if node == None:
        return 0
    if node.isNodeValue():
        return node.getValue()
    else:
        return 3*computeMagnitude(node.getLeft()) + 2*computeMagnitude(node.getRight())


node = addAndReduceLines(lines)
print(computeMagnitude(node))

