import sys
import os

f = open(os.path.join(sys.path[0], './data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

def horizontalFold(dots, yaxe):
    dotsCopy = dict(dots)
    for k in dots.keys(): # k = (x, y)
        if k[1] < yaxe:
            newKey = (k[0], yaxe + (yaxe - k[1]))
            dotsCopy[newKey] = True
            del dotsCopy[k]
    return dotsCopy

def verticalFold(dots, xaxe):
    dotsCopy = dict(dots)
    for k in dots.keys(): # k = (x, y)
        if k[0] < xaxe:
            newKey = (xaxe + (xaxe - k[0]) , k[1])
            dotsCopy[newKey] = True
            del dotsCopy[k]
    return dotsCopy

dots = dict()
lineIndex = 0
for lineIndex in range(len(lines)):
    line = lines[lineIndex]
    if line == '':
        lineIndex+=1
        break
    x, y = line.split(',')
    dots[(int(x), int(y))] = True

for lineIndex in range(lineIndex, lineIndex+1):
    axe, value = lines[lineIndex].split('=')
    if 'x' in axe:
        dots= verticalFold(dots, int(value))
    else:
        dots= horizontalFold(dots, int(value))
print(len(dots.keys()))