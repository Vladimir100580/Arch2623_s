# строки

# конкатенация строк ("+"). не злоупотреблять.

# размер строки
empty_str = ''
en_str = 'Text'
ru_str = 'Текст'
print(empty_str.__sizeof__())     # 48 байт служебная инфорамция + 1 - пустая строка.
print(en_str.__sizeof__())
print(ru_str.__sizeof__())

print('4e6575'.isdecimal())
