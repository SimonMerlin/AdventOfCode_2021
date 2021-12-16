import sys
import os
from functools import cmp_to_key
import timeit
f = open(os.path.join(sys.path[0], './data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cost = 0
        self.h = 0
    
    def __str__(self):
        return '{},{}, {}'.format(self.x, self.y, self.cost)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def compareNode(n1, n2):
    if n1.h < n2.h:
        return 1
    elif n1.h == n2.h:
        return 0
    return -1
cmp_items = cmp_to_key(compareNode)

def getNeighbors(node):
    neighbors = []
    if node.x > 0:
        neighbors.append(Node(node.x-1, node.y))
    if node.x < len(lines[0])-1:
        neighbors.append(Node(node.x+1, node.y))
    if node.y > 0:
        neighbors.append(Node(node.x, node.y-1))
    if node.y < len(lines)-1:
        neighbors.append(Node(node.x, node.y+1))
    return neighbors

def shortestPath(start, end):
    openList = []
    closedList = []
    openList.append(start)
    while len(openList) > 0:
        current = openList[0]
        openList = openList[1:]
        if current.x == end.x and current.y == end.y:
            return current.cost
        for n in getNeighbors(current):
            if not (n in closedList or (n in openList and n.cost < current.cost)):
                n.cost = current.cost + int(lines[n.y][n.x])
                n.h = n.cost + abs(n.x - end.x) + abs(n.y - end.y)
                openList.append(n)
        closedList.append(current)
        openList.sort(key = lambda x: x.h)
        print(current.cost)
    return -1


start = Node(0, 0)
end = Node(len(lines[0])-1, len(lines)-1)

startTimer = timeit.default_timer()
print(shortestPath(start, end))
print(timeit.default_timer() - startTimer)
