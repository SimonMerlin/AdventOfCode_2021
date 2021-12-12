import sys
import os
from Graph import Graph
from Node import Node

f = open(os.path.join(sys.path[0], './data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

graph = Graph()
nodes = dict()
for line in lines:
    line = line.strip().split('-')
    nodes[line[0]] = nodes.get(line[0], Node(line[0]))
    nodes[line[1]] = nodes.get(line[1], Node(line[1]))
    graph.addEdge(nodes[line[0]], nodes[line[1]])

#graph.printGraph()

graph.computeAllPaths(nodes['start'], nodes['end'])
print(graph.pathCounter)
    