class Board:

    def __init__(self, rows):
        self._rows = rows
        self._columns = []
        for i in range(len(rows)):
            self._columns.append([row[i] for row in rows])
    
    def isWinning(self, numbers):
        return any(match for match in [all(elem in numbers for elem in row) for row in self._rows]) or any(match for match in [all(elem in numbers for elem in column) for column in self._columns])

    def _containsNumber(self, number):
        return any(inRow for inRow in [number in row for row in self._rows])

    def sumUnmarkedNumber(self, numbers):
        sumMarkedNumber = sum([n for n in numbers if self._containsNumber(n)])
        boardSum = sum([sum(row) for row in self._rows])
        return boardSum - sumMarkedNumber