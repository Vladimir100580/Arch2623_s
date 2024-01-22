# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

s = 'Строки нумеруются начиная с единицы.'


def string_parse(string: str) -> str:
    """
    Обрабатывает строку.
    :param string:
    :return:
    """
    data = string.split()
    data.sort()

    longest_word = len(max(data, key=len))

    res = ''
    for n, s in enumerate(data, 1):
        res += f'{n} {s:>{longest_word}}\n'

    return res


print(string_parse(s))
help(string_parse)