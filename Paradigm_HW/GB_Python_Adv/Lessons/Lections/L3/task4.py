# методы строк
# a, b, c = input('Введите 3 символа через пробелы ').split()    # нельзя вводить больше или меньше.
# a, b, c, *_ = input('Введите 3 символа через пробелы ').split()    # здесь можно .
a, b, c = input('Введите 3 символа через пробелы ').split()[:3]  # можно и без выпендрежа
print(a, b, c)
# upper - все заглывные
# lower
# title - каждое слово с большой, остальное с малой
# capitalize - Вся строка с одной большой буквы, остальное все с малой.

text = "Однажды с студеную зимнюю пору"
print(text.startswith('Однажды'))
print(text.endswith('зимнюю', 0, -5))