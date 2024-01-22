# Функции locals(), globals(), vars()

SIZE = 10
def func(a, b, c):
    x = a + b
    print(locals())     # Возвращает только то, что внутри функции
    z = x + c
    return z

func(1, 2, 3)



def func1(a, b, c):
    x = a + b
    print(globals())    # Выводит переменные из глобальной области видимости (можно работать как со словарем)
    z = x + c
    return z


print(globals())
print(func1(1, 2, 3))


# print(vars(int))

data = [25, -42, 146, 73, -100, 12]
print(list(map(str, data)))
print(max(data, key=lambda x: -x))
print(*filter(lambda x: not x[0].startswith('__'), globals().items()))