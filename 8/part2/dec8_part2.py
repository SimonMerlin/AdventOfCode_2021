import sys
import os
f = open(os.path.join(sys.path[0], './data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

numberValues = {
    "acfgeb" :"0",
    "cf" :"1",
    "acdeg" :"2",
    "acfgd" :"3",
    "bdcf" :"4",
    "abdfg" :"5",
    "abdegf" :"6",
    "acf" :"7",
    "abcdefg" :"8",
    "abcdfg" :"9",
}

def equals(a, b):
    return len(a) == len(b) and all(a[i] in b for i in range(len(a)))

def contains(a, b):
    return len(a) < len(b) and all(a[i] in b for i in range(len(a)))

def containsInList(a, b):
    return any(contains(a, bb) for bb in b)

def countDifferences(base, test):
    return len([v for v in test if v not in base])

cpt = 0

for line in lines:
    inp, oup = line.split('|')
    inp = [v.strip() for v in inp.split(' ')]

    list_235 = [v for v in inp if len(v) == 5]
    list_069 = [v for v in inp if len(v) == 6]

    numbers = dict()
    segments = dict()

    # set know numbers
    for n in inp:
        if len(n) == 2: # 1
            numbers[1] = n
        elif len(n) == 4: # 4
            numbers[4] = n
        elif len(n) == 3: # 7
            numbers[7] = n
        elif len(n) == 7: # 8
            numbers[8] = n
    # find 6 and segment C and F
    for v in list_069:
        if not contains(numbers[1], v):
            numbers[6] = v
            for part in numbers[1]:
                if part in v:
                    segments[part] = 'f'
                else:
                    segments[part] = 'c'
            break
    list_09 = [v for v in inp if len(v) == 6 and v != numbers[6]]
    # compare 1 and 7 to find segment A
    for v7 in numbers[7]:
        if v7 not in numbers[1]:
            segments[v7] = 'a'
            break
    # find 2
    for v in list_235:
         if countDifferences(numbers[4], v) == 3: # v==0
            numbers[2] = v
            break
    list_35 = [v for v in list_235 if v != numbers[2]]
    # find 3
    for v in list_35:
        if contains(numbers[7], v): # v==3
            numbers[3] = v
        else:
            numbers[5] = v
    # find 0 and 9
    for v in list_09:
        cmp_v235 = countDifferences(numbers[3], v)
        if cmp_v235 == 2: # v==0
            numbers[0] = v
        else:
            numbers[9] = v
    
    # find segments left
    # segment in 4 for not in 3 is b
    for v4 in numbers[4]:
        if v4 not in numbers[3]:
            segments[v4] = 'b'
    # unknow segment in 4 is d
    for v4 in numbers[4]:
        if v4 not in segments.keys():
            segments[v4] = 'd'
    # find last sements of 9
    for v9 in numbers[9]:
        if v9 not in segments.keys():
            segments[v9] = 'g'
    for k in numbers[8]:
        if k not in segments.keys():
            segments[k] = 'e'
    
    # map output to real segments
    agr = ''
    for o in [v.strip() for v in oup.split(' ')]:
        realValue = ''.join([segments[x] for x in o])
        for k in numberValues.keys():
            if equals(k, realValue):
                agr += numberValues[k]
    cpt += int(agr)
print(cpt)

