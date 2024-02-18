# Наглядный пример локальной, глобальной и nonlocal переменных

candy = 1
candy1 = 3
candy2 = 300

def get_candy():
    candy = 5
    candy1 = 7
    candy2 = 400
    def increment_candy():
        nonlocal candy
        global candy1
        candy += 1
        candy1 += 3
        #candy2 += 100    Вызывает ошибку
        return candy, candy1

    return increment_candy


result = get_candy()()
print(*result)