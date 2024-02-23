# В организации есть два типа людей: сотрудники и обычные люди.
# Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:
# Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая)
# Возраст (целое положительное число) Сотрудники имеют также уникальный идентификационный номер (ID),
# который должен быть шестизначным положительным целым числом.
# Ваша задача:
# Создать класс Person, который будет иметь атрибуты и методы для
# управления данными о людях (Фамилия, Имя, Отчество, Возраст).
# Класс должен проверять валидность входных данных и генерировать исключения InvalidNameError и InvalidAgeError,
# если данные неверные.
# Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID).
# Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.
# Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.
# Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника
# на основе суммы цифр в его ID (по остатку от деления на 7).
# Создать несколько объектов класса Person и Employee с разными данными и проверить,
# что исключения работают корректно при передаче неверных данных.

class InvalidNameError(ValueError):
    def __init__(self, text, fio):
        self.text = text
        self.fio = fio

    def __str__(self):
        return f'Invalid {self.fio}: {self.text}. {self.fio.capitalize()} should be a non-empty string.'


class InvalidAgeError(ValueError):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f'Invalid age: {self.age}. Age should be a positive integer.'


class InvalidIdError(ValueError):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f'Invalid id: {self.id}. Id should be a 6-digit positive integer between 100000 and 999999.'


class Person:
    def __init__(self, first_name, last_name, patronymic, age):
        if not(isinstance(first_name, str) and first_name):
            raise InvalidNameError(first_name, 'name')
        if not(isinstance(last_name, str) and last_name):
            raise InvalidNameError(last_name, 'last_name')
        if not(isinstance(patronymic, str) and patronymic):
            raise InvalidNameError(patronymic, 'patronymic')
        if not (isinstance(age, int) and age >= 0):
            raise InvalidAgeError(age)
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.age = age

    def get_age(self):
        return self.age

    # @property
    # def first_name(self):
    #     return self.first_name
    #
    # @property
    # def last_name(self):
    #     return self.last_name
    #
    # @property
    # def patronymic(self):
    #     return self.patronymic
    #
    # @property
    # def age(self):
    #     return self.age


    def birthday(self):
        self.age += 1

    def __str__(self):
        return f'{self.first_name=}, {self.last_name=}, {self.patronymic=}, {self.age=}'

    # @first_name.setter
    # def first_name(self, value):
    #     self._first_name = value
    #
    # @last_name.setter
    # def last_name(self, value):
    #     self._last_name = value
    #
    # @patronymic.setter
    # def patronymic(self, value):
    #     self._patronymic = value
    #
    # @age.setter
    # def age(self, value):
    #     self._age = value


class Employee(Person):
    def __init__(self, first_name, last_name, patronymic, age, id):
        super().__init__(first_name, last_name, patronymic, age)
        if not (isinstance(id, int) and 999999 < id < 10000000):
            raise InvalidIdError(id)
        self.id = id

    def get_level(self):
        return sum(map(int, list(str(self.id)))) % 7


if __name__ == '__main__':

    # P1 = Person("56", "John", "Doe", 30)
    # print(P1)
    # E1 = Employee("6786", "John", "Doe", 30, 6767786)
    # print(E1.__dict__)
    # print(E1.get_level())
    # pp = Person("Bob", "Johnson", "Brown", 40)
    #
    # employee = Employee("Bob", "Johnson", "Brown", 40, 12345)

    # person = Person("Alice", "Smith", "Johnson", -5)

    # person = Person("Alice", "Smith", "Johnson", 25)
    # print(person.get_age())
    person = Person("", "John", "Doe", 30)