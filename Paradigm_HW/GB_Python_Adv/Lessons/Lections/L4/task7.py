print(*[1, 2, 3])

# Локальные переменные

def func(y: int) -> int:
    x = 100
    print(f'In func {x = }') # Для демонстрации работы, но не для привычки принтить из функции
    return y + 1


x = 42
print(f'In main {x = }')
z = func(x)
print(f'{x = }\t{z = }')


print('**********')

def func1(y: int) -> int:
    global x
    x += 100
    print(f'In func {x = }') # Для демонстрации работы, но не для привычки принтить из функции
    return y + 1


x = 42
print(f'In main {x = }')
z = func1(x)
print(f'{x = }\t{z = }')

print('**********')

def main(a):
    x = 1
    def func2(y):
        nonlocal x     # "Заглядывает" только на один уровень вверх
        x += 100
        print(f'In func {x = }') # Для демонстрации работы, но не для привычки принтить из функции
        return y + 1
    return x + func2(a)

x = 42
print(f'In main {x = }')
z = main(x)
print(f'{x = }\t{z = }')