import sys
import os
f = open(os.path.join(sys.path[0], './data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

openChunks = ['(', '[', '{', '<']
closeChunks = [')', ']', '}', '>']
matchClose = {'(': ')', '[': ']', '{': '}', '<': '>'}

chunkCpt = {')': 0, ']': 0, '}': 0, '>': 0}
chunkPoint = {')': 3, ']': 57, '}': 1197, '>': 25137}

for line in lines:
    stack = []
    for c in line:
        if c in openChunks:
            stack.append(c)
        elif c in closeChunks:
            lastOpenChunk = stack.pop()
            if matchClose[lastOpenChunk] != c:
                chunkCpt[c] += 1
                break
chunkScore = sum([chunkCpt.get(k) * chunkPoint.get(k) for k in chunkCpt.keys()])
print(chunkScore)
