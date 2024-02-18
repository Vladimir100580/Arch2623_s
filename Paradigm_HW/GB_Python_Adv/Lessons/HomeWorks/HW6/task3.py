# Расстановка ферзей
# Инструкция по использованию платформы
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
# Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка ферзей на шахматной доске,
# в которой ни один ферзь не бьет другого. Другими словами, ферзи размещены таким образом,
# что они не находятся на одной вертикали, горизонтали или диагонали.
# Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо.

import random as rnd
from task2 import check_queens

COORD_X = [i for i in range(8)]
COORD_Y = [j for j in range(8)]

def generate_boards():
    board_list = []
    while len(board_list) < 4:
        x_c = rnd.sample(COORD_X, 8)
        y_c = rnd.sample(COORD_Y, 8)
        lc = [(x_c[i], y_c[i]) for i in range(8)]
        if lc not in board_list and check_queens(lc):
            board_list.append(lc)
    return board_list


if __name__ == '__main__':
    print(generate_boards())



