# Создайте класс прямоугольник. Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона,
# считаем что у нас квадрат.



class Rectangle:

    def __init__(self, *args):
        self.length = args[0]
        self.width = args[1] if len(args) > 1 else self.length

    def len(self):
        return (self.width + self.length) * 2

    def area(self):
        return self.width * self.length


d = Rectangle(4, 5)

print(d.len())
print(d.area())
