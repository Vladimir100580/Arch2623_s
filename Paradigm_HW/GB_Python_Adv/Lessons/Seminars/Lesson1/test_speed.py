import time
import random

start = time.time()
for i in range(100000):
    number = '472'
    # number = int(number)
    # res = (number % 10 * 100) + (number // 10 % 10 * 10) + number // 100
    res = number[::-1]
print(time.time() - start)