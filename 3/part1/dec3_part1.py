f = open('data.txt', 'r')

sums = []
cptLine = 0
for line in f:
    line = line.rstrip()
    if sums == []:
        sums = [0 for _ in range(len(line))]
    cptLine+=1
    for index in range(len(line)):
        sums[index] += int(line[index])

gamma = ''
epsilon = ''
for count in sums:
    if count > cptLine/2: # more 1 than O
        gamma +='1'
        epsilon +='0'
    else: # more 0 than 1
        gamma +='0'
        epsilon +='1'
        
print(gamma*epsilon)