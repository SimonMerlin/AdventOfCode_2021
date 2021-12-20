class Beacon:

    def __init__(self, x, y, z=None):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return "[" + str(self.x) +", " + str(self.y) +", " + str(self.z) +"]"
    
    def __eq__(self, o: object):
        return self.x == o.x and self.y == o.y and self.z == o.z
    
    def __hash__(self):
        return hash((self.x, self.y, self.z))
