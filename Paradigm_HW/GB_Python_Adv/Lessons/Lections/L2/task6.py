# Логические типы

DEFAULT = 42
num = int(input("Введите уровень: "))
level = num or DEFAULT    # если num = 0, то 42. 0 - это FALSE, "" - FALSE, остальное True
print(level)

t = input('>>>') or 'Ananim'   #!!!!!!!!!!!
