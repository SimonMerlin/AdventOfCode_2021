import sys
import os
import re

f = open(os.path.join(sys.path[0], './data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

def parseAreaSize():
    xRegex = r"x=(-?\d+)\.\.(-?\d+)"
    yRegex = r"y=(-?\d+)\.\.(-?\d+)"
    l = lines[0]
    xValues = re.findall(xRegex, l)
    yValues = re.findall(yRegex, l)
    return (int(xValues[0][0]), int(xValues[0][1]), int(yValues[0][0]), int(yValues[0][1]))

succPositions = [] # list of successsives positions
xMin, xMax, yMin, yMax = parseAreaSize()

def getNextPosition(x, y, xVelocity, yVelocity):
    x += xVelocity
    y += yVelocity
    if xVelocity>0:
        xVelocity -=1
    elif xVelocity<0:
        xVelocity +=1
    yVelocity -=1
    return x, y, xVelocity, yVelocity

def isInArea(x, y):
    if xMin <= x <= xMax and yMin <= y <= yMax:
        return True
    return False

def findBestYInPositions(positions):
    return max([p[1] for p in positions])

def getSuccessivesPositions(xVelocity, yVelocity):
    positions = [(0, 0)]
    lastPosition = (0, 0)
    nextX, nextY, nextXVelocity, nextYVelovity = getNextPosition(lastPosition[0], lastPosition[1], xVelocity, yVelocity)
    while True:
        lastPosition = (nextX, nextY)
        positions.append(lastPosition)
        xVelocity, yVelocity = nextXVelocity, nextYVelovity
        if isInArea(lastPosition[0], lastPosition[1]):
            return positions
        elif lastPosition[1] < yMin: # probe is already under the area and will never go up
            return None
        nextX, nextY, nextXVelocity, nextYVelovity = getNextPosition(lastPosition[0], lastPosition[1], xVelocity, yVelocity)

#test a bunch of values
for xVelocity in range(0, 100):
    for yVelocity in range(0, 100):
        positions = getSuccessivesPositions(xVelocity, yVelocity)
        if positions is not None:
            succPositions.append(positions)

print(max([findBestYInPositions(position) for position in succPositions]))
