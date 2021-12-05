from Board import Board

f = open('data.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

numbers = [int(n.strip()) for n in lines[0].split(',')]

boards = []
i = 2
while i<len(lines):
    boards.append(Board([[int(value.strip()) for value in row.split(' ') if value!=''] for row in lines[i:i+5]]))
    i+=6
    
find=False
index = 4
while not find and index < len(numbers):
    for board in boards:
        if board.isWinning(numbers[:index]):
            sumUnmarked = board.sumUnmarkedNumber(numbers[:index])
            print(numbers[index-1] * sumUnmarked)
            find=True
            break
    index +=1
        
