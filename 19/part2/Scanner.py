class Scanner:

    def __init__(self, id, x=None, y=None, z=None):
        self.id = id
        self.x = x
        self.y = y
        self.z = z
        self.posx = None
        self.posy = None
        self.posz = None
        self.beacons = []
    
    def addBeacon(self, beacon):
        self.beacons.append(beacon)
    
    def setOriginToZero(self):
        self.x = 0
        self.y = 0
        self.z = 0
    
    def setTranslationVector(self, vector):
        self.translationVector = vector
    
    def setRotationVector(self, vector):
        self.rotationVector = vector
    
    def setPermutationVector(self, vector):
        self.permutationVector = vector
    
    def setPosition(self, vector):
        self.posx = vector[0]
        self.posy = vector[1]
        self.posz = vector[2]
    
    def getPosition(self):
        return (self.posx, self.posy, self.posz)

    

    
