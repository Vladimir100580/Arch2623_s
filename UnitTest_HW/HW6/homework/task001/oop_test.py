class Person:
    name = "Ivan"
    age = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set(self, name, age):
        self.name = name
        self.age = age

class Student (Person):
    course = 2

    def set(self, name, age, course):
        self.name = name
        self.age = age

# vlad = Person()
# vlad.age = 10
# vlad.name = "Владик"
# print(f'{vlad.name=} {vlad.age=}')
#
# vova = Person()
# vova.set("Владимир", 43)
# print(f'{vova.name=} {vova.age=}')
#
# nata = Student()
# nata.set("Наталья", 54, 3)
# print(f'{nata.name=} {nata.age=} {nata.course=}')


peter = Person("Петр", 56)
print(f'{peter.name=} {peter.age=}')
