
from typing import Callable
def deco_a(func: Callable):
    def wrapper_a(*args, **kwargs):
        print('Старт декоратора A')
        print(f'Запускаю {func.__name__}')
        res = func(*args, **kwargs)
        print(f'Завершение декоратора A')
        return res
    print('Возвращаем декоратор A')
    return wrapper_a


def deco_c(func: Callable):
    def wrapper_c(*args, **kwargs):
        print('Старт декоратора C')
        print(f'Запускаю {func.__name__}')
        res = func(*args, **kwargs)
        print(f'Завершение декоратора C')
        return res
    print('Возвращаем декоратор C')
    return wrapper_c


def deco_b(func: Callable):
    def wrapper_b(*args, **kwargs):
        print('Старт декоратора B')
        print(f'Запускаю {func.__name__}')
        res = func(*args, **kwargs)
        print(f'Завершение декоратора B')
        return res
    print('Возвращаем декоратор B')
    return wrapper_b


@deco_c            # ... = deco_c(deco_b)
@deco_b            # ... = deco_b(deco_a)
@deco_a            # ... = deco_a(main)
def main(num):
    i = num ** 2
    print('Работает основная функция')
    return i


if __name__ == '__main__':
    print('Запуск функции main')
    print(main(6))
    print('Завершение функции main')
