f = open('data.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

depth = 0
forward = 0
for line in lines:
    key, value = line.split(' ')
    if key == 'forward':
        forward += int(value)
    elif key == 'down':
        depth += int(value)
    elif key == 'up':
        depth -= int(value)
print(depth*forward)