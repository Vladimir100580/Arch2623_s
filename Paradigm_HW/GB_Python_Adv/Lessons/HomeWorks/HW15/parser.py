import argparse

from task1 import Student


def st_parser():
    parser = argparse.ArgumentParser(description='String to operations on student data')
    parser.add_argument("-s", "--subject", type=str, help='Press subject name')
    parser.add_argument("-gr", "--grade", type=int, help='Add a grade for a subject')
    parser.add_argument("-ts", "--test_sc", type=int, help='Add a test score for a subject')
    parser.add_argument("-ag", "--av_grade", action='store_true', help="Show the average grade")
    parser.add_argument("-at", "--av_test", type=str,
                        help='Show the average score for the tests in the specified subject')
    parser.add_argument("-sv", "--save", action='store_true', help="Save student data")
    parser.add_argument("-l", "--load", type=str, help="Specify the name of the data csv-file", default="subjects.csv")

    args = parser.parse_args()

    student = Student("Name", args.load) # Для примера, используем упрощенный вариант с именем и загрузкой
    if args.subject:
        if args.grade:
            student.add_grade(args.subject, args.grade)
        if args.test_sc:
            student.add_test_score(args.subject, args.test_sc)
    if args.av_grade:
        print(student.get_average_grade()) # print - лишь для проверки результата
    if args.av_test:
        print(student.get_average_test_score(args.av_test)) # print - лишь для проверки результата
    if args.save:
        student.save_subjects()


if __name__ == '__main__':
    st_parser()


# python .\parser.py -at Математика
# >>> 63.4
# python .\parser.py -s Математика -ts 90 -sv
# python .\parser.py -at Математика
# 67.83333333333333

# python .\parser.py -l subjects1.csv -s Информатика -gr 5 -ag -sv  - Загружает данные из файла subjects1.cvs, затем
# добавляет к оценкам по информатике пятерку, выводит среднее всех оценок студента, сохраняет измененные данные.

