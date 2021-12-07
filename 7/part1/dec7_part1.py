import math
import sys
import os
f = open(os.path.join(sys.path[0], './data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

positions = [int(p) for p in lines[0].split(',')]

positions = sorted(positions)

if len(positions) % 2 == 0:
    median = positions[int((len(positions) +1) / 2)]
else:
    median  = (positions[int(len(positions) / 2)] + positions[int((len(positions)/2)+1)]) / 2

fuel = 0
for p in positions:
    fuel += int(math.fabs((p - median)))
print(fuel)


