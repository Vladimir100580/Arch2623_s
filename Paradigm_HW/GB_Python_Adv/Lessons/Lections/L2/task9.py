# Математика в Пайтон

import math
import decimal    # 28 знаков для числа по умолчанию
import fractions   # обыкновенные дроби

print(dir(math))
print(help(math.gcd))   # поясняет функцию

decimal.getcontext().prec = 120
s = decimal.Decimal(0.1 + 0.2)
print(s)
s = decimal.Decimal(1/3)
print(s)
s = decimal.Decimal(1) / decimal.Decimal(3)   # Была установлена точность 120 знаков
print(s)

f1 = fractions.Fraction(1, 3)
print(f1)
f2 = fractions.Fraction(2, 5)
print(f2)
f3 = f1 + f2
print(f3, type(f3))