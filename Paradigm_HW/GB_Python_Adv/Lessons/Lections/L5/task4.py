# Генерация списков

my_listcomp = [chr(i) for i in range(97, 123)]
print(my_listcomp) # ['a', 'b', 'c', 'd', ..., z]
for char in my_listcomp:
    print(char)

# Длинный код:
data = [2, 5, 1, 42, 65, 76, 24, 77]
res = []
for item in data:
    if item % 2 == 0:
        res.append(item)
print(f'{res = }')


# Аналогичное решение, но с использованием синтаксического сахара listcomp:
data = [2, 5, 1, 42, 65, 76, 24, 77]
res = [item for item in data if item % 2 == 0]
print(f'{res = }')

# () - генераторное выражение, когда не нужны все элементы.  [] генератор списка, когда нужны все элементы.

# Генерация словарей
data = {2, 4, 4, 6, 8, 10, 12}
res1 = {None: item for item in data if item > 4}
res2 = (item for item in data if item > 4)
res3 = [[item] for item in data if item > 4]
print(res1, res2, res3)

