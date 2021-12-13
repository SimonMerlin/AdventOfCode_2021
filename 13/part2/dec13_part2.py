import sys
import os

f = open(os.path.join(sys.path[0], './data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

def horizontalFold(dots, yaxe):
    dotsCopy = dict()
    for k in dots.keys(): # k = (x, y)
        if k[1] > yaxe:
            newKey = (k[0], yaxe - (k[1] - yaxe))
            dotsCopy[newKey] = True
        else:
            dotsCopy[k] = True
    return dotsCopy

def verticalFold(dots, xaxe):
    dotsCopy = dict()
    for k in dots.keys(): # k = (x, y)
        if k[0] > xaxe:
            newKey = (xaxe - (k[0] - xaxe) , k[1])
            dotsCopy[newKey] = True
        else:
            dotsCopy[k] = True
    return dotsCopy

def printDots(dots):
    dotsList = [['.' for i in range(50)] for i in range(6)]
    for k in dots.keys():
        dotsList[k[1]][k[0]] = '#'
    for y in dotsList:
        print(''.join(y))
    print()

dots = dict()
lineIndex = 0
for lineIndex in range(len(lines)):
    line = lines[lineIndex]
    if line == '':
        lineIndex+=1
        break
    x, y = line.split(',')
    dots[(int(x), int(y))] = True

for lineIndex in range(lineIndex, len(lines)):
    axe, value = lines[lineIndex].split('=')
    if 'x' in axe:
        dots= verticalFold(dots, int(value))
    else:
        dots= horizontalFold(dots, int(value))

printDots(dots)
