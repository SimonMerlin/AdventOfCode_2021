class Octopus:

    def __init__(self, energyLevel, x, y):
        self._energyLevel = energyLevel
        self._x = x 
        self._y = y
        self._hasFlashed = False
    
    def getEnergy(self):
        return self._energyLevel
    
    def getHasFlashed(self):
        return self._hasFlashed
    
    def setHasFlashed(self):
        self._hasFlashed = True
        
    def getX(self):
        return self._x
    
    def getY(self):
        return self._y    
    
    def resetEnergy(self):
        self._energyLevel = 0
    
    def resetHasFlashed(self):
        self._hasFlashed = False
        
    def increaseEnergy(self):
        if self._energyLevel < 10:
            self._energyLevel += 1
    
