
import csv
from random import randint

subjects = ['Математика', 'Физика', 'Химия', 'Информатика']


def generate_csv_file(file_name, rows=1):
    """
    Искусственно созданный генератор для формирования файла subjects.csv (c предметами, оценками и баллами)
    """
    with open(file_name + '.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # writer.writerow(['subject', 'tests', 'grades'])
        for _ in range(rows):
            for j in subjects:
                writer.writerow([j, [randint(10, 100) for i in range(randint(1, 7))],
                                 [randint(2, 5) for k in range(randint(1, 7))]])
    return True


if __name__ == '__main__':
    generate_csv_file('for_tests')
