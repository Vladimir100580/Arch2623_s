t = True

print(type(t))
print(isinstance(t, bool))
print(isinstance(t, int))     # bool подкласс int
print(isinstance(t, float))
print(isinstance(t, (int, float)))    # принадлежность какому-либо классу

num1 = 2 + 2 * 2
num2 = 36 / 6
num3 = 37 / 6
print(num1, num2, num3)
print(type(num1), type(num2), type(num3))
print(num1 == num2)
print(num1 is num2)
print(num2 is num3)   # is - сравнивает и тип и численное значение

y = 15
print(id(y))
y //= 2
print(id(y))

i = (-1)**.5
i1 = 7 + (-1)**.5
i2 = 7 - (-1)**.5
print(i, i1)
print(type((-1)**.5), type(i1))  #комплексный тип
print(i1 * i2)

a = complex(2, 3)
b = complex('2+3j') # j в пайтоне вместо i (особенность языка)
print(a == b, a, type(a))

print(divmod(13, 5))  # сразу 13//5 и 13%5 Результат неизменная коллекция (кортеж)