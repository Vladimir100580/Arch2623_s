# Создайте функцию generate_csv_file(file_name, rows),которая будет генерировать по три случайных числа в каждой строке,
# от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:
# file_name (строка) - имя файла, в который будут записаны данные.
# rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.
# Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения вида ax^2 + bx + c = 0.
# Функция принимает три аргумента:
# a, b, c (целые числа) - коэффициенты квадратного уравнения.
# Функция возвращает:
# None, если уравнение не имеет корней (дискриминант отрицателен).
# Одно число, если уравнение имеет один корень (дискриминант равен нулю).
# Два числа (корни), если уравнение имеет два корня (дискриминант положителен).
# Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots.
# Декоратор выполняет следующие действия:
# Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
# Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
# Сохраняет результаты в формате JSON в файл results.json.
# Каждая запись JSON содержит параметры a, b, c и результаты вычислений.
# Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json будет сохранена
# информация о параметрах и результатах вычислений для каждой строки данных из CSV-файла.

import os
import json
import csv
from random import randint


def generate_csv_file(file_name, rows):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        # writer.writerow(['a', 'b', 'c'])
        for _ in range(rows):
            writer.writerow([randint(100, 1000), randint(100, 1000), randint(100, 1000)])
    return True


def save_to_json(func):
    def wrapper(*args, **kwargs):
        with open('abc.csv', 'r', newline='') as f, \
                open('results.json', 'w', encoding='utf-8') as f_in:
            file_csv_read = csv.reader(f, delimiter=",")
            ll = []
            for i in file_csv_read:
                res = func(*map(int, i))
                ll.append({"parameters": [i[0], i[1], i[2]], "result": res})

            json.dump(ll, f_in)

        return True

    return wrapper


@save_to_json
def find_roots(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    elif d == 0:
        return -b / (2 * a)
    else:
        return (-b - d ** .5) / (2 * a), (-b + d ** .5) / (2 * a)



if __name__ == '__main__':
    generate_csv_file('abc.csv', 15)
    find_roots()
