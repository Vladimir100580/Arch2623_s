class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'MyClass(a={self.a}, b={self.b})'

    def __call__(self, *args, **kwargs):
        if args:
            self.a.extend(args)
        self.b.update(kwargs)
        return True


x = MyClass([42], {73: True})
print(x)
y = x(3.14, 100, 500, start=1)     # сам y принимает значение True, т.к. это возвращает call
print(x)
x(15)
print(x)
x(y=y)     # это **kwargs первый y - это ключ, а второй - это True
print(x)
