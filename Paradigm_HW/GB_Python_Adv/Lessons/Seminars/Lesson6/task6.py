# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY и возвращает истину,
# если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# И весь период действует григорианский календарь. Проверку года на високосность вынести в отдельную защищённую функцию.

# from data_parser import parse_data as pd

MONTHS = {
    1: range(1, 32),
    2: range(1, 29),
    3: range(1, 32),
    4: range(1, 31),
    5: range(1, 32),
    6: range(1, 31),
    7: range(1, 32),
    8: range(1, 32),
    9: range(1, 31),
    10: range(1, 32),
    11: range(1, 31),
    12: range(1, 32),
}


# from datetime import datetime
# d = datetime()

def parse_data(date: str) -> bool:
    d, m, y = map(int, date.split('.'))
    return _y_is_valid(y) and _m_is_valid(m) and _d_is_valid(d, m, y)


def _d_is_valid(d: int, m: int, y: int) -> bool:
    if _is_leap_year(y) and m == 2:
        return d in range(1, 30)
    return d in MONTHS[m]


def _m_is_valid(m: int) -> bool:
    return m in range(1, 13)


def _y_is_valid(y: int) -> bool:
    return y in range(1, 10_000)


def _is_leap_year(y: int) -> bool:
    return y % 4 == 0 and y % 100 != 0 or y % 400 == 0


print(parse_data('28.02.2000'))
print(parse_data('29.02.2024'))
print(parse_data('28.02.1900'))
print(parse_data('28.02.0001'))
print(parse_data('30.02.2010'))
