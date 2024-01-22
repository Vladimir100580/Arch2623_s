# Списки

my_list = [2, 4, 6, 7, 8, 9, 12]
print(my_list)
print(my_list[2], my_list[-3])
print(my_list.pop())
print(my_list)
print(my_list.pop(3))    # удаляет элемент по индексу
print(my_list)
my_list.extend([2, 6, 2])
print(my_list)
print(f"{my_list.count(2)=}")
print(f'{my_list.index(4)=}')
my_list.insert(4, "а")
print(my_list)
my_list.remove(6)  # удаляет элемент по значению (первое вхождение слева, по умолчанию)
print(my_list)
# rev = reversed(my_list)  # объект развернутого списка
# print(list(rev))
my_list = my_list[::-1]    # !! Синтаксический сахар для разворота
print(my_list)
print('******************')
my_list = [2, 4, 7, 'a', 'n', [9, 'y', 12]]
my_list.append(my_list)
print(my_list)

a = 42
b = 'Hello, world'
c = [1, 3, 5, 7]
my_list = [None]
my_list.append(a)
print(my_list)
my_list.extend(c)   #  Сами эти методы (как и sort) возвращают None
print(my_list)
my_list.extend(b)   # рассматривает отдельнгые элементы списка или строки
print(my_list)


