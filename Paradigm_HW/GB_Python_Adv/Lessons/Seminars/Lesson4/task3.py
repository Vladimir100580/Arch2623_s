# Функция получает на вход строку из двух чисел через пробел.
# Сформируйте словарь, где ключом будет символ из Unicode, а значением — целое число.
# Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.

def get_unicode_dict(diapazon: str) -> dict[str, int]:
    start, end = map(int, diapazon.split())
    result = {}
    for i in range(min(start, end), max(start, end)):
        result[chr(i)] = i

    return result


print(get_unicode_dict("98 105"))
