class Game():
    def __init__(self, weight, hight):
        self._weight = weight
        self._hight = hight
    def posiz(self):
        position = []
        for i in range(6):
            for j in range(2):
                center_x = ((self._weight / 6) * (i + 2.5)) - (self._weight / 12)
                center_y = ((self._hight / 3) * (j + 1)) - (self._hight / 6)
                position.append(([center_x, center_y]))
        return position
    def posiz1(self):
        position = []
        for i in range(6):
            for j in range(2):
                center_x = ((self._weight / 6) * (i + 1)) - (self._weight / 12)
                center_y = ((self._hight / 3) * (j + 1)) - (self._hight / 6)
                position.append(([center_x, center_y]))
        return position
    def pozis2(self):
        position = []
        for i in range(6):
            for j in range(2):
                center_x = ((self._weight / 6) * (i + 2)) - (self._weight / 12)
                center_y = ((self._hight / 3) * (j + 1)) - (self._weight / 12)
                position.append(([center_x, center_y]))
        return position
