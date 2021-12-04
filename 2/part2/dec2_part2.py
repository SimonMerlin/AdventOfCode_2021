f = open('data.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

depth = 0
forward = 0
aim = 0
for line in lines:
    key, value = line.split(' ')
    if key == 'forward':
        forward += int(value)
        depth += aim * int(value)
    elif key == 'down':
        aim += int(value)
    elif key == 'up':
        aim -= int(value)
print(depth*forward)