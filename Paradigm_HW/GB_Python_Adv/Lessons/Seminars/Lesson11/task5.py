# Доработайте прошлую задачу.Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения.

class Rectangle:

    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length

    def area(self):
        return self.length * self.width

    def perim(self):
        return 2 * (self.length + self.width)

    def __add__(self, other: 'Rectangle'):
        new_perimetr = self.perim() + other.perim()
        new_length = self.length + other.length
        new_width = new_perimetr / 2 - new_length
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        new_perimetr = abs(self.perim() - other.perim())
        new_length = abs(self.length - other.length)
        new_width = new_perimetr / 2 - new_length
        if new_width < 0:
            raise ValueError('Вычитание данных прямоугольников невозможно!')
        return Rectangle(new_length, new_width)

    def __str__(self):
        return f'Rectangle({self.length=}, {self.width=})'

    def __eq__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()


if __name__ == '__main__':
    P1 = Rectangle(4, 8)
    P2 = Rectangle(1, 11)
    P3 = Rectangle(11, 1)
    # print(P1 + P2)
    # print(P1 - P2)
    print(P1 == P2)
    print(P2 == P3)
    print(P2 < P3)
    print(P2 <= P3)