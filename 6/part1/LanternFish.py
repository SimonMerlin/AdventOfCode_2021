class LanternFish:

    def __init__(self, timer):
        self._timer = timer
    
    def decreaseDay(self):
        self._timer = self._timer - 1
        if self._timer < 0:
            self._timer = 6
            return LanternFish(8)
        else:
            return None
