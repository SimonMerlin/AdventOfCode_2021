import sys
import os
f = open(os.path.join(sys.path[0], './data.txt'), 'r')
lines = [int(l.rstrip()) for l in f.readlines()]

cpt = 0
sums = []
for i in range(len(lines)-2):
    sums.append(lines[i]+lines[i+1]+lines[i+2])

highestValue = sums[0]
for s in sums[1:]:
    if s > highestValue:
        cpt+=1
    highestValue = s
print(cpt)