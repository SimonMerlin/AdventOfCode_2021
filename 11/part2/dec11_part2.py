import sys
import os
from Octopus import Octopus

f = open(os.path.join(sys.path[0], './data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

def getOctopusNeighbors(grid, x, y):
    neighbors = []
    if x>0:
        neighbors.append(grid[y][x-1])
    if x<len(grid[0])-1:
        neighbors.append(grid[y][x+1])
    if y>0:
        neighbors.append(grid[y-1][x])
    if y<len(grid)-1:
        neighbors.append(grid[y+1][x])
    if x>0 and y>0:
        neighbors.append(grid[y-1][x-1])
    if x<len(grid[0])-1 and y>0:
        neighbors.append(grid[y-1][x+1])
    if x>0 and y<len(grid)-1:
        neighbors.append(grid[y+1][x-1])
    if x<len(grid[0])-1 and y<len(grid)-1:
        neighbors.append(grid[y+1][x+1])
    return neighbors

def resetOctopusesState(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x].getEnergy() > 9:
                grid[y][x].resetEnergy()
            grid[y][x].resetHasFlashed()

def isEverybodyFlash(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x].getEnergy() != 0:
                return False
    return True

# map lines to octopus grid
octopusGrid = []
for y in range(len(lines)):
    energies = list(lines[y])
    octoLine = []
    for x in range(len(energies)):
        octoLine.append(Octopus(int(lines[y][x]), x, y))
    octopusGrid.append(octoLine)

stepCount = 0
while not isEverybodyFlash(octopusGrid):
    for y in range(len(octopusGrid)):
        for x in range(len(octopusGrid[0])):
            octopus = octopusGrid[y][x]
            octopus.increaseEnergy()
            if octopus.getEnergy() > 9 and not octopus.getHasFlashed(): # then it flashes
                neighbors = getOctopusNeighbors(octopusGrid, x, y)
                while neighbors:
                    octo = neighbors.pop()
                    if octo.getEnergy() <= 9:
                        octo.increaseEnergy()
                        if octo.getEnergy() > 9:
                            octopusGrid[octo.getY()][octo.getX()].setHasFlashed()
                            neighbors += getOctopusNeighbors(octopusGrid, octo.getX(), octo.getY())
    resetOctopusesState(octopusGrid)
    stepCount +=1

print(stepCount)

