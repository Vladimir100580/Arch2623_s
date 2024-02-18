code_to_write = '''
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
                open('results.json', 'w', newline='', encoding='utf-8') as f_in:
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
'''

with open("__init__.py", "w") as init_file:
    init_file.write(code_to_write)
