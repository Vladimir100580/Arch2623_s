class Number:
    def __init__(self, num):
        self.num = num


n = Number(42)
print(f'{callable(Number) = }')    # проверяет является ли Number функцией или нет (т.е. можно передать параметры ()
print(f'{callable(n) = }')

