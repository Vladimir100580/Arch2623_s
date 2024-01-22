def all_(iterable):     # так работает функция all, если все элементы True, то - True
    for element in iterable:
        if not element:
            return False
    return True


numbers = [42, -73, 1024]
if all(map(lambda x: x > 0, numbers)):
    print('Все элементы положительные')
else:
    print('В последовательности есть отрицательные и/или нулевые элементы')


def any(iterable):     # так работает функция any, если хотя бы один элемент True, то - True
    for element in iterable:
        if element:
            return True
        return False


numbers = [42, -73, 1024]
if any(map(lambda x: x > 0, numbers)):
    print('Хотя бы один элемент положительный')
else:
    print('Все элементы не больше нуля')

