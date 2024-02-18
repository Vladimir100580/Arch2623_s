import time

def dec_1(func):
    def wrapper(*args, **kwargs):
        print(f'Запуск функции {func.__name__} в {time.time()}')
        result = func(*args, **kwargs)
        print(f'Результат функции {func.__name__}: {result}')
        print(f'Завершение функции {func.__name__} в {time.time()}')
        return result

    return wrapper


# def fun_1(list_1, num_2):
#     s = 0
#     for i in list_1:
#         s += i * num_2
#
#     return s
#

# ls = [2, 3, 7, 4, 5]
# mult = 6
# f_mult = dec_1(fun_1)
# print(f'{f_mult(ls, mult) = }')

@dec_1
def fun_1(list_1, num_2):
    s = 0
    for i in list_1:
        s += i * num_2

    return s

ls = [2, 3, 7, 4, 5]
mult = 6
print(f'{fun_1(ls, mult) = }')           # сразу срабатывает обертка
