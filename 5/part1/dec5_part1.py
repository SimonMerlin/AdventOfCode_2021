import sys
import os
f = open(os.path.join(sys.path[0], './data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

data = dict()

for line in lines:
    start, end = line.split('->')
    startx, starty = start.split(',')
    startx, starty = int(startx.strip()), int(starty.strip())

    endx, endy = end.split(',')
    endx, endy = int(endx.strip()), int(endy.strip())

    if startx == endx: # vertical line
        if starty > endy:
            starty, endy = endy, starty
        for i in range(starty, endy+1, 1):
            data[startx] = data.get(startx, dict())
            data[startx][i] = data.get(startx).get(i, 0) +1
    elif starty == endy: # horizontal line
        if startx > endx:
            startx, endx = endx, startx
        for i in range(startx, endx+1, 1):
            data[i] = data.get(i, dict())
            data[i][starty] = data.get(i).get(starty, 0) +1

cpt = 0
for xkey in data.keys():
    for ykey in  data.get(xkey).keys():
        if data[xkey][ykey] >=2:
            cpt+=1
print(cpt)