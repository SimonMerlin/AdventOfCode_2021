from LanternFish import LanternFish

f = open('data.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

timers = [int(t.strip()) for t in lines[0].split(',')]
timerMap = dict()
for initTimer in timers:
    timerMap[initTimer] = timerMap.get(initTimer, 0) + 1

for i in range(256):
    renewFish = timerMap.get(0,0)
    for t in range(8):
        timerMap[t] = timerMap.get(t+1, 0)
    timerMap[8] = renewFish
    timerMap[6] = timerMap.get(6, 0) + renewFish

cpt = 0
for k in timerMap.keys():
    cpt += timerMap[k]
print(cpt)
