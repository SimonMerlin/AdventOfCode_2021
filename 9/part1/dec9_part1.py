import sys
import os
f = open(os.path.join(sys.path[0], './data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

rowSize = len(lines[0])
colSize = len(lines)

cpt = 0
for r in range(rowSize):
    for c in range(colSize):
        up, down, right, left = 9, 9, 9, 9
        if c > 0: # get left
            left = int(lines[r][c-1])
        if c < colSize-1:
            right = int(lines[r][c+1])
        if r > 0:
            up = int(lines[r-1][c])
        if r < rowSize-1:
            down = int(lines[r+1][c])
        v = int(lines[r][c])
        if v < left and v < right and v < up and v < down:
            cpt += int(v)+1
print(cpt)
