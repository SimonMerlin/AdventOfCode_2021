f = open('data.txt', 'r')

cpt = 0
values = [int(v) for v in f]
sums = []
for i in range(len(values)-2):
    sums.append(values[i]+values[i+1]+values[i+2])

highestValue = sums[0]
for s in sums[1:]:
    if s > highestValue:
        cpt+=1
    highestValue = s
print(cpt)