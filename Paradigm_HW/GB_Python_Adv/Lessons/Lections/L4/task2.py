def mutable(data: list[int]) -> list[int]:
    for i, item in enumerate(data):
        data[i] = item + 1
    print(f'In func {data = }')  # Для демонстрации работы, но не для привычки принтить из функции
    return data


my_list = [2, 4, 6, 8]
print(f'In main {my_list = }')
new_list = mutable(my_list)  # ссылка
print(f'{my_list = }\t{new_list = }')  # т.к. передали изменяемый объект (список, словарь, множество)


def no_return(data: list[int]):
    for i, item in enumerate(data):
        data[i] = item + 1
    print(f'In func {data = }')  # Для демонстрации работы, но не для привычки принтить из функции


my_list = [2, 4, 6, 8]
print(f'In main {my_list = }')
new_list = no_return(my_list)
print(f'{my_list = }\t{new_list = }')
