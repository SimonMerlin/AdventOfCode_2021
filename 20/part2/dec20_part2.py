import sys
import os
f = open(os.path.join(sys.path[0], './data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

enhancerAlgo = lines[0]
image = lines[2:]

def increaseImageBy(image, inc, left, right, top, bottom, step):
    width = len(image[0])
    pixel = "#" if step%2 == 1 else "."
    top = [''.join([pixel for _ in range(width+(inc-left)+(inc-(width-right-1)))]) for _ in range(inc-top)]
    bottom = [''.join([pixel for _ in range(width+(inc-left)+(inc-(width-right-1)))]) for _ in range(inc-(len(image) - bottom - 1))]
    for i in range(len(image)):
        image[i] = pixel*(inc-left) + image[i] + pixel*(inc-(width-right-1))
    return top + image + bottom

def getStringForPixel(image, x, y, step):
    pixel = "#" if step%2 == 1 else "."
    a = image[y-1][x-1] if y > 0 and x > 0 else pixel
    b = image[y-1][x] if y > 0 else pixel
    c = image[y-1][x+1] if y > 0 and x < len(image[y-1]) - 1 else pixel
    d = image[y][x-1] if x > 0 else pixel
    e = image[y][x]
    f = image[y][x+1] if x < len(image[y]) - 1 else pixel
    g = image[y+1][x-1] if y < len(image) - 1 and x > 0 else pixel
    h = image[y+1][x] if y < len(image) - 1 else pixel
    i = image[y+1][x+1] if y < len(image) - 1 and x < len(image[y+1]) - 1 else pixel
    return a + b + c + d + e + f + g + h + i

def convertStringImageToInteger(input):
    binary = ''
    for x in input:
        binary += '1' if x == '#' else '0'
    return int(binary, 2)

def enhanceImage(image, step):
    width = len(image[0])
    height = len(image)
    newImage = []
    for y in range(2, height-2):
        row = ''
        for x in range(2, width-2):
            string = getStringForPixel(image, x, y, step)
            index = convertStringImageToInteger(string)
            row += enhancerAlgo[index]
        newImage.append(row)
    return newImage

def countLitPixels(image):
    count = 0
    for row in image:
        for pixel in row:
            if pixel == '#':
                count += 1
    return count

def printImage(image):
    for row in image:
        print(row)
    print()

def getImageSize(image):
    left, right, top, bottom = 0, len(image[0])-1, 0, len(image)-1
    # top
    while "#" not in image[top]:
        top += 1
    # bottom
    while "#" not in image[bottom]:
        bottom -=1
    # left
    while "#" not in ''.join([r[left] for r in image]):
        left += 1
    # right
    while "#" not in ''.join([r[right] for r in image]):
        right -= 1
    return left, right, top, bottom
    

left, right, top, bottom = getImageSize(image)
for i in range(50):
    image = increaseImageBy(image, 3, left, right, top, bottom, i)
    image = enhanceImage(image, i)
    left, right, top, bottom = getImageSize(image)
print(countLitPixels(image))