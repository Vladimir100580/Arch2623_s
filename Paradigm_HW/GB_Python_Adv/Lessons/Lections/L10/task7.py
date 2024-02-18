class Person:
    max_up = 3         # здесь, как правило константы.

    def __init__(self):
        self.level = 1  # атрибуты уровня экземпляра, сам класс к ним доступа не имеет
        self.health = 100


p1 = Person()
p2 = Person()
print(f'{p1.max_up = }, {p1.level = }, {p1.health = }')
print(f'{p2.max_up = }, {p2.level = }, {p2.health = }')
# print(f'{Person.max_up = }, {Person.level = }, {Person.health =}') # AttributeError: # type object 'Person' has no attribute 'level'
print(f'{Person.max_up = }')
Person.level = 100
print(f'{Person.level = }, {p1.level = }, {p2.level = }')
