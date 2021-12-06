from LanternFish import LanternFish

f = open('data.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

timers = [int(t.strip()) for t in lines[0].split(',')]

fishs = [LanternFish(timer) for timer in timers]
added = []

for i in range(80):
    for f in fishs:
        newFish = f.decreaseDay()
        if newFish != None:
            added.append(newFish)
    fishs = fishs + added
    added=[]
    print(len(fishs))
print(len(fishs))