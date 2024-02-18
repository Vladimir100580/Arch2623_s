class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __getattribute__(self, item):  # обрабатываем только имя z
        if item == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')

        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')

        return object.__setattr__(self, key, value)

    def __getattr__(self, item):   # при обращении к несуществующему атрибуту вызывает None
        return None


a = Vector(2, 4)
print(a.z)  # None
print(f'{a = }')
