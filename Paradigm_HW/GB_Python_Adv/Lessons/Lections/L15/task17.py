import argparse

parser = argparse.ArgumentParser(description='My first argument parser')
parser.add_argument('numbers', metavar='N', type=str, nargs='*',
                    help='press some numbers')
args = parser.parse_args()

print(f'В скрипт передано: {args.numbers}')


# 💡 Внимание! Тут и далее до конца главы запускать файл будет из терминала ОС.
#       Примерно так:
#       $ python main.py ... , где многоточие - передаваемые скрипту аргументы

# Запустим скрипт с несколькими значениями:
# $ python .\task17.py 42 123 4.5

# На выходе получаем объект Namespace(numbers=[42.0, 3.14, 73.0]).