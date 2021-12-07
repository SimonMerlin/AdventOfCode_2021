import math
import sys
import os
f = open(os.path.join(sys.path[0], './data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

positions = [int(p) for p in lines[0].split(',')]

average = int(sum(positions) / len(positions))

fuel = 0
for p in positions:
    fuel += sum(range(1, int(math.fabs(p-average))+1)) # 
print(fuel)

