# Итераторы

a = 42
# iter(a) # TypeError: 'int' object is not iterable

data = [2, 4, 6, 8]
list_iter = iter(data)
print(list_iter)

data = [2, 4, 6, 8]
list_iter = iter(data)
print(*list_iter)
print(*list_iter)   # получаемый объект удалятся при одном переходе

import functools
f = open('mydata.bin', 'rb')
for block in iter(functools.partial(f.read, 16), b''):  # Ровно по 16 байт
    print(block)
f.close()

# data = [2, 4, 6, 8, 10, 12, 14, 16, 18, 19, 21, 22, 23, 25]
# for el in iter(data):
#     print(el)


data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter)) # StopIteration


data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))


data = {"один": 1, "два": 2, "три": 3}
x = iter(data.items())
print(x)
y = next(x)
print(y)
z = next(iter(y))
print(z)