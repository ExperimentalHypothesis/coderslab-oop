from math import sqrt

class Square:
    def __init__(self, side):
        self._side = side
        self._perimeter = self._side * 4
        self._area = self._side * self._side
        self._diagonal = sqrt(self._area * 2)

    def get_side(self):
        return self._side

    def get_perimeter(self):
        return self._perimeter

    def get_area(self):
        return self._area

    def get_diagonal(self):
        return self._diagonal

    def set_side(self, new_length):
        self._side = new_length
        self._perimeter = self._side * 4
        self._area = self._side * self._side
        self._diagonal = sqrt(self._area * 2)

    def set_perimeter(self, new_perimeter):
        self._perimeter = new_perimeter
        self._side = self._perimeter / 4
        self._area = self._side * 2
        self._diagonal = sqrt(self._area * 2)

    def set_area(self, new_area):
        self._area = new_area
        self._side = sqrt(self._area)
        self._perimeter = self._side * 4
        self._diagonal = sqrt(self._area * 2)

    def set_diagonal(self, new_diagonal):
        self._diagonal = new_diagonal
        self._area = self._diagonal * self._diagonal / 2
        self._side = sqrt(self._area)
        self._perimeter = self._side * 4
