class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'

    # def __eq__(self, other):    # Эти объекты
    #     return self is other


one = Triangle(3, 4, 5)    # по id сравнение
two = one
three = Triangle(3, 4, 5)
print(one == two)
print(one == three)
