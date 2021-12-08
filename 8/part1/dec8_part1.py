import sys
import os
f = open(os.path.join(sys.path[0], './data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

uniqueLen = [2, 4, 3, 7]

cpt = 0
for line in lines:
    out = line.split('|')[1]
    cpt += len([v for v in out.split(' ') if len(v.strip()) in uniqueLen])
print(cpt)
