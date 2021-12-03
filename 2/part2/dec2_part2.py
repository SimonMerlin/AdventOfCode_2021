f = open('data.txt', 'r')

depth = 0
forward = 0
aim = 0
for line in f:
    key, value = line.split(' ')
    if key == 'forward':
        forward += int(value)
        depth += aim * int(value)
    elif key == 'down':
        aim += int(value)
    elif key == 'up':
        aim -= int(value)
print(depth*forward)