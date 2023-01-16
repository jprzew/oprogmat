from numbers import Number


class Vect:
    """Class implements vectors in n-dimensional spaces

    Attributes:
        items: list of Numbers - coordinates of the vector
        n: int - dimension of the vector

    """

    def __init__(self, items):
        self.items = items

    def __repr__(self):
        return f'Vector({self.items})'

    def __add__(self, other):

        if not isinstance(other, Vect):
            raise TypeError('Only vectors can be added.')

        if self.n != other.n:
            raise ValueError('Vectors with different dimensions cannot be added.')

        coordinates = [element1 + element2 for element1, element2
                       in zip(self.items, other.items)]

        return Vect(coordinates)

    def __mul__(self, other):

        if not isinstance(other, Number):
            raise TypeError('Scalars need to be numbers.')

        coordinates = [element * other for element in self.items]
        return Vect(coordinates)

    __rmul__ = __mul__

    def norm(self):
        """Euclidean norm of the vector"""
        return sum([element**2 for element in self.items]) ** 0.5

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        self.__items = value
        self.__n = len(value)

    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, value):

        if self.n < value:
            self.items = self.items + [0] * (value - self.n)
        elif self.n > value:
            self.items = self.items[:value]


