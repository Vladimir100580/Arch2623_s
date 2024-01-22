a = 5
print(id(a))
a += 1
print(id(a))   # создается новый объект, т.к. число неизменяемый тип

# аналогично со строкой
st = "Hello Vasya"
print(id(st))
st = st.replace(" ", "_")
print(st, id(st))      # изменяет объект, т.к. это не изменяемый объект

print()
a = b = 7      # аналогично двум равенствам a = 7, b = 7. Что понятно.
c = 9
print(id(a), id(b), id(c))
b = c
print(id(a), id(b), id(c))
print(a, b, c)

# как проверить изменяемый или нет объект?
# У изменяемых объектов невозможно вычислить хеш (-это криптографическая функция хеширования)
x = 71
y = 'hello'
z = 3.1415
list_1 = [x, y, z]
print(hash(x), hash(y), hash(z))
# print(hash(list_1))  ошибка, значит объект изменяемый

inp = input('>>> ')
print(id(inp))
print(type(inp))
print(hash(inp))