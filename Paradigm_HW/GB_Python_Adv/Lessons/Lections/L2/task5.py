# простые объекты в python
import sys

x = int(42)
y = int(3.1254)
z = int('hello', base=30)
print(x, y, z, sep='\n') # перевод из 30-ричной СС в десятичную СС

# Пример резинового int
STEP = 2 ** 16  # 256**2
num = 1
for _ in range(30):
    print(f'{sys.getsizeof(num)} байт,', num, f', грубо: {_*2} байт')  # + информация об объекте
    num *= STEP

num = 2**16 - 1
print(num, bin(num), oct(num), hex(num))