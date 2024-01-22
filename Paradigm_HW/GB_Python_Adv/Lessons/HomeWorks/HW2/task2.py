# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
# Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

frac1 = "2/7"
frac2 = "4/5"

fr1 = Fraction(frac1)
fr2 = Fraction(frac2)

numerator1, denominator1 = map(int, frac1.split("/"))
numerator2, denominator2 = map(int, frac2.split("/"))

sum_fr = f'{numerator1*denominator2 + numerator2*denominator1}/{denominator2*denominator1}'
mult_fr = f'{numerator1*numerator2}/{denominator1*denominator2}'

print(f"Сумма дробей: {sum_fr}")
print(f"Произведение дробей: {mult_fr}")
print(f"Сумма дробей: {fr1 + fr2}")
print(f"Произведение дробей: {fr1 * fr2}")

