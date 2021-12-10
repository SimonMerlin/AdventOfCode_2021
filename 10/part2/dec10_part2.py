import sys
import os
f = open(os.path.join(sys.path[0], './data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

openChunks = ['(', '[', '{', '<']
closeChunks = [')', ']', '}', '>']
matchClose = {'(': ')', '[': ']', '{': '}', '<': '>'}

chunkPoint = {')': 1, ']': 2, '}': 3, '>': 4}

def computeCompletionScore(missingsChunks):
    score = 0
    for c in missingsChunks:
        score *=5
        score += chunkPoint[c]
    return score

# find all corrupted lines
corruptedLines = []
for index in range(len(lines)):
    line = lines[index]
    stack = []
    for c in line:
        if c in openChunks:
            stack.append(c)
        elif c in closeChunks:
            lastOpenChunk = stack.pop()
            if matchClose[lastOpenChunk] != c:
                corruptedLines.append(index)
                break

scores = []
for index in range(len(lines)):
    if index not in corruptedLines:
        stack = []
        for c in lines[index]:
            if c in openChunks:
                stack.append(c)
            elif c in closeChunks:
                lastOpenChunk = stack.pop()
                if matchClose[lastOpenChunk] != c: # should not happen
                    raise Exception("Error in line {}, expected {} but got {}".format(index, matchClose[lastOpenChunk], c))
        missingChunks = ''.join([matchClose.get(c) for c in reversed(stack)])
        scores.append(computeCompletionScore(missingChunks))

scores = sorted(scores)
print(scores[int(len(scores)/2)])

                


