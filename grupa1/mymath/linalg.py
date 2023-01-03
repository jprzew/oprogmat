from numbers import Number


class Vect:

    def __init__(self, items):
        self.items = items
        self.n = len(items)

    def __repr__(self):
        return f'Vector({self.items})'

    def __add__(self, other):

        if not isinstance(other, Vect):
            raise TypeError('Addition implemented for vectors only.')

        if self.n != other.n:
            raise ValueError('Only vectors with the same dimension can be added.')

        coordinates = [element1 + element2 for element1, element2
                       in zip(self.items, other.items)]

        return Vect(coordinates)

    def __mul__(self, other):

        if not isinstance(other, Number):
            raise TypeError('Scalars should be numbers.')

        coordinates = [element * other for element in self.items]
        return Vect(coordinates)



