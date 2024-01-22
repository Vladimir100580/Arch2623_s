import random
from random import randint

a = [chr(i) for i in range(50, 58)]
a.extend(chr(i) for i in range(97, 123) if i not in [108, 111])
d = 3
arr_c = a.copy()
brackets = (d // 2) % 2  # скобки, если 0 - вначале, 1 - вконце
oper = [[0, 1], [1, 0]][d % 2]  # последовательность операций
i = randint(1, 2)  # Элементов в общем пересечении
i1 = randint(i+1, i+2)    # c и d
i2 = randint(i+1, i+2)    # d и e
i3 = randint(i+1, i+2)    # e и c
k1, k2, k3 = random.sample([7, 8, 9], 3)
c1 = []
d1 = []
e1 = []
for k in range(i):
    ii = randint(0, len(arr_c) - 1)
    el = arr_c.pop(ii)
    c1.append(el)
    d1.append(el)
    e1.append(el)
for k in range(i1 - i):
    ii = randint(0, len(arr_c) - 1)
    el = arr_c.pop(ii)
    c1.append(el)
    d1.append(el)
for k in range(i2 - i):
    ii = randint(0, len(arr_c) - 1)
    el = arr_c.pop(ii)
    d1.append(el)
    e1.append(el)
for k in range(i3 - i):
    ii = randint(0, len(arr_c) - 1)
    el = arr_c.pop(ii)
    c1.append(el)
    e1.append(el)
for k in range(k1 - len(c1)):
    ii = randint(0, len(arr_c) - 1)
    el = arr_c.pop(ii)
    c1.append(el)
for k in range(k2 - len(d1)):
    ii = randint(0, len(arr_c) - 1)
    el = arr_c.pop(ii)
    d1.append(el)
for k in range(k3 - len(e1)):
    ii = randint(0, len(arr_c) - 1)
    el = arr_c.pop(ii)
    e1.append(el)
while True:
    random.shuffle(c1)
    random.shuffle(d1)
    random.shuffle(e1)
    if c1[0] != d1[0] != e1[0] and c1[-1] != d1[-1] != e1[-1]:
        break

print( f' {i=} {i1=} {i2=} {i3=} {c1=} {d1=} {e1=}')


# print(a, len(a))
# b = a.copy()
# i = randint(2, 5)   # Элементов в пересечении
# kk, j = random.sample([7, 8, 9, 10], 2)
#
# while True:
#     kk = randint(7, 10)
#     j = randint(7, 10)
#     if kk != j:
#         break
# c = []
# d = []
# for k in range(i):
#     ii = randint(0, len(b) - 1)
#     el = b.pop(ii)
#     c.append(el)
#     d.append(el)
# for k in range(kk - i):
#     ii = randint(0, len(b) - 1)
#     el = b.pop(ii)
#     c.append(el)
# for k in range(j - i):
#     ii = randint(0, len(b) - 1)
#     el = b.pop(ii)
#     d.append(el)
# while True:
#     print(c)
#     random.shuffle(c)
#     print(c)
#     random.shuffle(d)
#     print(c[0], d[0], c[-1], d[-1])
#     if c[0] != d[0] != c[-1] != d[-1] != c[0]:
#         break
#
# un = set(c).union(set(d))  # oбъединение множеств ⋃
# inters = set(c).intersection(set(d))         # пересечение множеств  ⋂
# diff = set(c).difference(set(d))            # разность множеств \
# c1 = str(c).replace("'", "").replace("[", "{").replace("]", "}")
# d1 = str(d).replace("'", "").replace("[", "{").replace("]", "}")
# print( f' {c1} {d1} {i} ⋂ = {inters} ⋃ = {un} \ = {diff}')
# # \, ⋃, ⋂
#
#
#
#
# class CrLetter1:
#     def __init__(self, n, iskl = []):
#         masb = []
#         for z in range(n):
#             while True:
#                 a = randint(65, 90)
#                 if a != 79 and chr(a) not in masb and chr(a) not in iskl:
#                     masb.append(chr(a))
#                     break
#         masb.sort()
#         self.bs = masb
#
#
#
# print(CrLetter1(24).bs)
#
#
# k1, k2, k3 = random.sample([7, 8, 9], 3)
# print(f'{k1 =} {k2 = } {k3 = }')






# a.extend([i for i in range(9)])
#
# p = [i for i in range(9)]
# print(p)
#
# print(a)

