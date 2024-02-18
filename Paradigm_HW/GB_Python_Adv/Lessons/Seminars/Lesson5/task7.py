# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел, начиная с числа 2.
# ✔ Для проверки числа на простоту используйте правило: «число является простым, если делится
# нацело только на единицу и на себя».

def is_simple(n:int) -> bool:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def simple_generate(number: int):
    i = 2
    yield i
    i += 1
    while i <= number:
        if is_simple(i):
            yield i
        i += 2

a = simple_generate(27)
for _ in range(27):
    print(next(a, 'перебор'), end=' ')