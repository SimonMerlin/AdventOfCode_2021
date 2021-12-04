import copy

f = open('data.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

def findMostCommon(myList, index):
    cpt = 0
    for elem in myList:
        cpt += int(elem[index])
    return '1' if cpt >= len(myList)/2 else '0'

#oxygen
tmp = copy.deepcopy(lines)
for i in range(len(lines[0])):
    mostCommon = findMostCommon(tmp, i)
    tmp = [e for e in tmp if e[i]==mostCommon]
    if len(tmp) == 1:
        break
oxygen = int(tmp[0], 2)

#CO2
tmp = copy.deepcopy(lines)
for i in range(len(lines[0])):
    mostCommon = findMostCommon(tmp, i)
    tmp = [e for e in tmp if e[i]!=mostCommon]
    if len(tmp) == 1:
        break
co2 = int(tmp[0], 2)

print(oxygen*co2)