# Множества
my_set = {1, 6, 8, 5, 9}
my_f_set = frozenset((1, 3, 7, 9, 12, 15))
my_set.add(7)
print(my_set)
# my_set.add((7, 9))  # добавляется только один элемент, в данном случае кортеж
print(my_set)
my_set.remove(8)   # удаляет существующий элемент (если отсутствует - вызывает ошибку)
my_set.discard(12)  #  удаляет существующий элемент (если отсутствует - НЕ вызывает ошибку)

my_set_1 = {1, 2, 4, 6, 9}
print(my_set_1)
intersec = my_set.intersection(my_set_1)   # в новых версиях &
un = my_set.union(my_set_1)            #  | - объединение
differ = my_set.difference(my_set_1)    # -
print(intersec, un, differ)

# метод in # списки, кортежи и строки время нахождения - линейное. Словари и set-множества - константное время!!!

my_set = frozenset({3, 4, 1, 2, 5, 6, 1, 7, 2, 7})
print(len(my_set))
print(my_set - {1, 2, 3})
print(my_set.union({2, 4, 6, 8}))
print(my_set & {2, 4, 6, 8})
# print(my_set.discard(10))


