# Создайте модуль с функцией внутри. Функция принимает на вход три целых числа:
# нижнюю и верхнюю границу и количество попыток. Внутри генерируется случайное число
# в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”. Если число угадано, возвращается истина,
# а если попытки исчерпаны - ложь.

import random


def guess(min_numb, max_numb, count):
    numb_1 = random.randint(min_numb, max_numb)
    for i in range(count):
        nubm = int(input('Enter number: '))
        if nubm == numb_1:
            return True
        elif nubm > numb_1:
            print('Число меньше загаданного')
        else:
            print('Число больше загаданного')
    return False


if __name__ == '__main__':
    print(guess(2, 10, 3))
