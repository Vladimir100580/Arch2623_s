# Однострочники
a = 73
b = 42
a, b = b, a  # Как и множество современных языков, python читает строку справа налево поэтому, так - работает.
print(f'{a=}  {b=}')

data = {10, 9, 8, 1, 6, 3}
a, b, c, *d, e = data
print(a, b, c, d, e)       # Т.к. множество, то хеширование создает упорядочивание (с какой-то версии)


# Смысл * распаковки, запаковки
data = ["один", "два", "три", "четыре", "пять", "шесть", "семь",]
a, b, c, *d = data
print(f'{a=} {b=} {c=} {d=}')
a, b, *c, d = data
print(f'{a=} {b=} {c=} {d=}')
a, *b, c, d = data
print(f'{a=} {b=} {c=} {d=}')
*a, b, c, d = data
print(f'{a=} {b=} {c=} {d=}')

link ='https://docs.python.org/3/faq/programming.html#how-can-i-pass-optional-or-keyword-parameters-from-one-function-to-another'
prefix, *_, suffix = link.split('/')    # _ - означает, что в дальнейшем эта "переменная" использоваться не будет.
print(suffix)

