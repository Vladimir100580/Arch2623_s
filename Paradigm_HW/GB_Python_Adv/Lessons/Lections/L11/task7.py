class Count:
    _count = 0
    _last = None

    def __new__(cls, *args, **kwargs):
        if cls._count < 3:
            cls._last = super().__new__(cls)
            cls._count += 1
        return cls._last

    def __init__(self, name: str):
        self.name = name


p1 = Count('Петя1')
p2 = Count('Петя2')
p3 = Count('Петя3')
p4 = Count('Петя4')
p5 = Count('Петя5')
print(p1.name, p2.name, p3.name, p4.name, p5.name)
