# Создайте функцию генератор чисел Фибоначчи fibonacci.
# https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8

def fibonacci():
    numbers = (0, 1)
    while True:    # !!!!!!!!!!!!!!!
        yield numbers[0]             # сразу возвращает в итератор, запоминая в памяти переменные, и продолжает код
        numbers = (numbers[1], numbers[0] + numbers[1])

f = fibonacci()
for i in range(20):
    print(next(f))
