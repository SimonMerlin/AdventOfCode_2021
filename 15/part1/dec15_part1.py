import sys
import os
f = open(os.path.join(sys.path[0], './data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]


start = (0, 0)
end = (len(lines[0])-1, len(lines)-1)

paths = dict()

def shortestPath(start, end, visited):
    value = int(lines[start[1]][start[0]])
    if start == end:
        return value
    if (start, end) in paths.keys():
        return paths[(start, end)]
    visited.add(start)
    min_path = float('inf')
    for x, y in [(start[0], start[1] - 1), (start[0] + 1, start[1]), (start[0], start[1] + 1), (start[0] - 1, start[1])]:
        if (x, y) not in visited and x >= 0 and y >= 0 and x < len(lines[0]) and y < len(lines):
            min_path = min(min_path, shortestPath((x, y), end, visited.copy()))
    paths[(start, end)] = min_path
    return value + min_path

dataW = len(lines[0])
dataHeigth = len(lines)
xm, ym = int(dataW*0.75), int(dataHeigth*0.75)

for x in range(xm, len(lines[0])-1):
    shortestPath((x, ym), end, set())
for y in range(ym, len(lines)-1):
    shortestPath((xm, y), end, set())

startValue = int(lines[start[1]][start[0]])
#shortestValue = shortestPath(start, end, set())
print(shortestValue - startValue)