# Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

import typing


def key_params(**kwargs):
    dic = {}
    for key, value in kwargs.items():
        if isinstance(value, typing.Hashable) and value is not None:
            dic[value] = key
        else:
            dic[str(value)] = key
    return dic


params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)
