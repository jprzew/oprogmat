from numbers import Number


class Vect:
    """Represents vectors in n-dimensional Euclidean space

    Attributes:
        items: list of Numbers - coordinates
        n: int - dimension of the vector
    """

    def __init__(self, items):
        self.__items = items
        self.__n = len(items)

    def __repr__(self):
        return f'Vector({self.items})'

    def __add__(self, other):
        """Addition of vectors

        Raises:
            ValueError: if vectors have different dimensions
            TypeError: when trying to add element of type not being Vect
        """

        if not isinstance(other, Vect):
            raise TypeError('Addition implemented for vectors only.')

        if self.n != other.n:
            raise ValueError('Only vectors with the same dimension can be added.')

        coordinates = [element1 + element2 for element1, element2
                       in zip(self.items, other.items)]

        return Vect(coordinates)

    def __mul__(self, other):
        """Multiplication of vectors by scalars

        Raises:
            TypeError: when trying to multiply by element not of type Number
        """

        if not isinstance(other, Number):
            raise TypeError('Scalars should be numbers.')

        coordinates = [element * other for element in self.items]
        return Vect(coordinates)

    __rmul__ = __mul__

    def norm(self):
        """Calculates Euclidean norm"""
        return sum([element**2 for element in self.items]) ** 0.5

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, values):
        self.__items = values
        self.__n = len(values)

    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, value):

        if value > self.n:
            self.items = self.items + (value - self.n) * [0]
        elif value < self.n:
            self.items = self.items[:value]
