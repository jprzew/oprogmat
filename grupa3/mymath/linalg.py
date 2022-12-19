class Vect:

    def __init__(self, items):
        self.items = items
        self.n = len(items)

    def __repr__(self):
        return f'Vector({self.items})'

    def __add__(self, other):
        coordinates = [element1 + element2 for element1, element2
                       in zip(self.items, other.items)]

        return Vect(coordinates)
