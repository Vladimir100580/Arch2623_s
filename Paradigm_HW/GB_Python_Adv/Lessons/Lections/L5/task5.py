# Создание функции генератора

def factorial(n):
    number = 1
    result = []
    for i in range(1, n + 1):
        number *= i
        result.append(number)
    return result

for i, num in enumerate(factorial(10), start=1):
    print(f'{i}! = {num}')


def factorial1(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number

for i, num in enumerate(factorial1(10), start=1):
    print(f'{i}! = {num}')


def fibonacci():
    numbers = (0, 1)
    for i in range(1, 12):
        yield numbers[0]             # сразу возвращает в итератор, запоминая в памяти переменные, и продолжает код
        numbers = (numbers[1], numbers[0] + numbers[1])

f = fibonacci()
for i in range(10):
    print(next(f))