from numbers import Number


class Vect:
    """Class Vect implements vectors in euclidean spaces

    Attributes:
        items: list of numbers - coordinates of the vector
        n: int - dimension of the vector

    """

    def __init__(self, items):
        self.__items = items
        self.__n = len(self.items)

    def norm(self):
        """Euclidean norm of the vector """
        return sum([element**2 for element in self.items]) ** 0.5

    def __repr__(self):
        return f'Vector: {self.items}'

    def __add__(self, other):

        if self.n != other.n:
            raise ValueError('Vectors should have the same dimension.')

        items = [element1 + element2 for element1, element2 in zip(self.items, other.items)]
        return Vect(items)

    def __mul__(self, other):

        if not isinstance(other, Number):
            raise ValueError('Scalars should be numbers.')

        items = [element * other for element in self.items]
        return Vect(items)

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

        if self.__n < value:
            self.items = self.items + (value-self.__n) * [0]
        elif self.__n > value:
            self.items = self.items[:value]




