name = 'Vladimir' # пробелы
MAX_CONST = 1000 * 73  # Неизменяемое, в дальнейшем, значение константы

# В python все объекты
a = 42
print(id(a))

a = 'Hello word'
print(id(a))

# txc = int(input("Число: "))
# match txc:
#     case 3 | 5:
#         print("3 или 5")
#     case 10 | 20 | 30:
#         print("10 v 20 v 30")
#     case _:
#         print("Все остальное")

t = True

print(type(t))
print(isinstance(t, bool))
print(isinstance(t, int))
print(isinstance(t, float))
print(isinstance(t, (int, float)))

num1 = 2 + 2 * 2
num2 = 36 / 6
num3 = 37 / 6
print(num1, num2, num3)
print(type(num1), type(num2), type(num3))
print(num1 == num2)
print(num1 is num2)
print(num2 is num3)   # is - сравнивает и тип и численное значение

b = 0

if 5 == 2 + 3 or 7 / b:
    print('ОК!')

if 5 == 10 / 3 and 9 / b:
    print('ОК Again!')
else:
    print('OK! Again now!')

print("1 Варитант" if b == 3 else "2 вариант")

y = 15
print(id(y))
y //= 2
print(id(y))

animals = ["cat", "dor", "wolf", "rabbit", "dragon"]
for i, animal in enumerate(animals, start=2):   # animal
    print(i, animal)
#   Аналог
# for i in enumerate(arr, start=2):
#     print(i[0], i[1])

data = 0
while data < 100:
    data += 3
    if data % 19 == 0:
        continue
    data += 1
    if data % 40 == 0:
        break
else:
    data += 5
print(data)
