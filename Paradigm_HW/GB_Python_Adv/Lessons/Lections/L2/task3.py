# Аннотация типов
# a: int = 45  # лучше написать a: float = 45.0
# b: float = float(input('Введите число: '))
# a = a / b
# print(a)

def my_func(data: list[int, float]) -> float:  # в списке передаем или int, или float (для коллег)
    res = sum(data) / len(data)
    return res

print(my_func([5, 3, 7.1, 9.8, 12.7]))

# начиная с версии 3.10
a: int | float = 45   # | - или
b: float = float(input('Введите число: '))
a = a / b
print(a)