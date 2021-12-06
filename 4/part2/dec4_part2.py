from Board import Board

import sys
import os
f = open(os.path.join(sys.path[0], './data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

numbers = [int(n.strip()) for n in lines[0].split(',')]

boards = []
i = 2
while i<len(lines):
    boards.append(Board([[int(value.strip()) for value in row.split(' ') if value!=''] for row in lines[i:i+5]]))
    i+=6
    
index = 4
while len(boards)>1:
    boards = [board for board in boards if not board.isWinning(numbers[:index])]
    index +=1

losingBoard = boards[0]
while not losingBoard.isWinning(numbers[:index]):
    index+=1

sumUnmarked = losingBoard.sumUnmarkedNumber(numbers[:index])
print(numbers[index-1] * sumUnmarked)
        
