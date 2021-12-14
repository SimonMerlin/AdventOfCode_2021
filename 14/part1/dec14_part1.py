import sys
import os
f = open(os.path.join(sys.path[0], './data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

polymer = lines[0]

pairs = dict()
letterCount = dict()

for line in lines[2:]:
    pair, value = line.split('->')
    pairs[pair.strip()] = value.strip()

for p in polymer:
    letterCount[p] = letterCount.get(p, 0) + 1

for i in range(2):
    polymerCopy = ''
    for pIndex in range(len(polymer)):
        if pIndex == len(polymer) - 1:
            polymerCopy += polymer[pIndex]
        else:
            polymerCopy += polymer[pIndex]
            newLetter = pairs[polymer[pIndex]+polymer[pIndex+1]]
            polymerCopy +=newLetter
            letterCount[newLetter] = letterCount.get(newLetter, 0) + 1
    polymer = polymerCopy

pMin, pMax = min(letterCount.values()), max(letterCount.values())
print(letterCount)
print(pMin, pMax)
print(pMax - pMin)