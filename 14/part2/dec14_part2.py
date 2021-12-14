import sys
import os
f = open(os.path.join(sys.path[0], './data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

polymer = dict()
pairs = dict()
letterCount = dict()

for line in lines[2:]:
    pair, value = line.split('->')
    pairs[pair.strip()] = value.strip()

startPolymer = lines[0]
for p in startPolymer:
    letterCount[p] = letterCount.get(p, 0) + 1

for i in range(len(startPolymer)-1):
    polymer[startPolymer[i]+startPolymer[i+1]] = polymer.get(startPolymer[i]+startPolymer[i+1], 0) + 1

for i in range(40):
    polymerCopy = dict()
    for k in polymer.keys():
        newLetter = pairs[k]
        newK1 = k[0]+newLetter
        newK2 = newLetter+k[1]
        cpt = polymer[k]

        polymerCopy[newK1] = polymerCopy.get(newK1, 0) + cpt
        polymerCopy[newK2] = polymerCopy.get(newK2, 0) + cpt
        letterCount[newLetter] = letterCount.get(newLetter, 0) + cpt
    polymer = polymerCopy

pMin, pMax = min(letterCount.values()), max(letterCount.values())
print(pMax - pMin)