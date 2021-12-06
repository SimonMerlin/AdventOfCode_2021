import sys
import os
f = open(os.path.join(sys.path[0], './data.txt'), 'r')
lines = [int(l.rstrip()) for l in f.readlines()]

cpt = 0
lastValue =  lines[0]
for line in lines:
    value = line
    if value > lastValue:
        cpt+=1
    lastValue = value
print(cpt)