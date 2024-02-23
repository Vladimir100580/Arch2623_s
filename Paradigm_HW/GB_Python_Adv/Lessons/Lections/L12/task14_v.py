# Мои эксперименты

class User:
    def __init__(self, pere):
        self.pere = pere
        self._vovar = 5

    @property
    def vovar(self):
        return self._vovar

    # @property
    # def age(self):
    #     return self._age

    def mult(self, mn):
        return self._vovar * mn + self.pere

    @vovar.setter
    def vovar(self, value):
        self._vovar = value

    @vovar.deleter
    def vovar(self):
        self._vovar = 0


US = User(7)
print(US.vovar)
print(US.mult(6))

US.vovar = 10 # Без сеттера не работает
print(US.vovar)
print(US.mult(6))

del US.vovar
print(US.vovar)
print(US.mult(6))

    # @age.setter
    # def age(self, value):
    #     if value > self._age:
    #         self._age = value
    #     else:
    #         raise ValueError(f'Новый возраст должен быть больше текущего: {self._age}')
    #
    # @age.deleter     # Без этого была бы ошибка
    # def age(self):
    #     self._age = 0


# user = User('Стивен', 'Спилберг')
# user.age = 75
# print(f'Меня зовут {user.full_name} и мне {user.age} лет.')
# print('Прошло много лет. Изобретена технология перерождения.')
# del user.age
# print(f'Меня зовут {user.full_name} и мне {user.age} лет.')

