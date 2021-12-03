f = open('data.txt', 'r')

cpt = 0
lastValue =  int(f.readline())
for line in f:
    value = int(line)
    if value > lastValue:
        cpt+=1
    lastValue = value
print(cpt)