a = 42
print(type(a), id(a))  # Внутрь одной функции передаем две функции. Функции тоже объекты, как и все другое.
print(type(id))

# если функция передается то без "()", если вызывается, то с "()"
very_bad_programming_style = sum  # Передаем переменной функцию VERY BAD.
print(very_bad_programming_style([1, 2, 3]))


def my_func():
    pass  # "pass" лучше избегать


# Не забываем вызывать функцию!

def quadratic_equations(a: int | float, b: int | float, c: int | float) -> tuple[float, float] | float | str:
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    elif d == 0:
        return -b / (2 * a)
    else:
        return 'Нет решений'   # не очень хорошо, т.к. может вернуться строка, в данном случае, лучше "None"


print(quadratic_equations(2, -3, -9))



