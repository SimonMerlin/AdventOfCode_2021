f = open('data.txt', 'r')

depth = 0
forward = 0
for line in f:
    key, value = line.split(' ')
    if key == 'forward':
        forward += int(value)
    elif key == 'down':
        depth += int(value)
    elif key == 'up':
        depth -= int(value)
print(depth*forward)