import sys
import os
from functools import reduce
f = open(os.path.join(sys.path[0], './data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

rowSize = len(lines[0])
colSize = len(lines)

lowestPoint = []
basinsSize = []

visited = []

cpt = 0
for r in range(rowSize):
    for c in range(colSize):
        up, down, right, left = 9, 9, 9, 9
        if c > 0:
            left = int(lines[r][c-1])
        if c < colSize-1:
            right = int(lines[r][c+1])
        if r > 0:
            up = int(lines[r-1][c])
        if r < rowSize-1:
            down = int(lines[r+1][c])
        v = int(lines[r][c])
        if v < left and v < right and v < up and v < down:
            lowestPoint.append((r, c))

def basinSizeFromPoint(r, c):
    up, down, right, left = 0, 0, 0, 0
    visited.append((r, c))
    v = int(lines[r][c])
    if c > 0 and ((r,c-1) not in visited) and int(lines[r][c-1]) != 9:
        left = basinSizeFromPoint(r, c-1)
    if c < colSize-1 and ((r,c+1) not in visited) and int(lines[r][c+1]) != 9:
        right = basinSizeFromPoint(r, c+1)
    if r > 0 and ((r-1,c) not in visited) and int(lines[r-1][c]) != 9:
        up = basinSizeFromPoint(r-1, c)
    if r < rowSize-1 and ((r+1,c) not in visited) and int(lines[r+1][c]) != 9:
        down = basinSizeFromPoint(r+1, c)
    return 1 + up + down + right + left

for p in lowestPoint:
    basinsSize.append(basinSizeFromPoint(p[0], p[1]))

basinsSize.sort(reverse=True)
print(reduce(lambda a, b: a * b, basinsSize[:3]))
