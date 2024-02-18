# Разработайте программное обеспечение для ведения журнала событий. Вам необходимо создать класс,
# который будет представлять строки журнала и включать в себя информацию об авторе и времени создания каждой записи.
# Условие задачи:
# Создайте класс MyStr, который наследуется от встроенного класса str и добавлять дополнительную информацию
# о создателе строки и времени ее создания. Этот класс будет представлять строки с информацией о событиях.
# Класс MyStr должен иметь следующие атрибуты и методы:
# value (str): Строковое значение с описанием события.
# author (str): Имя автора, создавшего запись.
# time: Время создания записи в формате '%Y-%m-%d %H:%M'.
# Магические методы (Dunder-методы):
# Реализуйте метод __new__(cls, value, author), который создает новый объект класса MyStr с заданным value и author.
# Метод также автоматически фиксирует время создания записи. В этом методе создается новый объект MyStr
# с указанными атрибутами и текущим временем в атрибуте time.
# Реализуйте метод __str__(self), который возвращает строковое представление объекта класса MyStr
# с информацией о событии, авторе и времени создания.
# Реализуйте метод __repr__(self), который возвращает строковое представление объекта класса MyStr.
# Метод __repr__ возвращает строку, которая может быть использована для создания точно такого же объектаMyStrс
# теми же значениямиvalueиauthor`.

import time
import datetime


class MyStr(str):
    """ Класс MyString где на вход поступают:
             value - со всеми возможностями str;
             author = имя автора строки.

        Дополнительно:
             time = время создания (time.time) """
    def __init__(self, *args):
        value, autor, *_ = args
        self.value = value

    def __new__(cls, value: str, author: str = None):
        instance = super().__new__(cls, value)
        instance.author = author
        tz_obj = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        instance.time = tz_obj
        return instance

    def __str__(self):
        return f'{self.value} (Автор: {self.author}, Время создания: {self.time})'

    def __repr__(self):
        return f"MyStr('{self.value}', '{self.author}')"


if __name__ == '__main__':
    t = MyStr("HELLO? i'm one string", 'Alex')
    # t2 = MyStr("HELLO? i'm two string", 'Jo')
    # t3 = MyStr("HELLO? i'm three string")
    # st = t + t2 + t3 + 'Hero'
    # print(f'{st = }')
    # print(f'{t = }\t{t.author = }\t{t.time}')
    # print(f'{t2 = }\t{t2.author = }\t{t2.time}')
    # print(f'{t3 = }\t{t3.author = }\t{t3.time}')
    # res = t.__doc__
    # for line in res.split('\n'):
    #     print(line)
    # print(str(t))
    print(repr(t))

