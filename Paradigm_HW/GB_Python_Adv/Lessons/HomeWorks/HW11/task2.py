# Разработайте программу для хранения и управления текстовыми и числовыми записями.
# Вам нужно создать класс Archive, который будет представлять архив и реализовывать следующую функциональность:
# Методы и операции:
# При создании экземпляра класса Archive с указанием текстовой и числовой записи (text и number),
# записи добавляются в соответствующие атрибуты archive_text и archive_number.
# Если архив уже существует, текущие записи (text и number) добавляются в архив.
# Метод __str__ возвращает строковое представление объекта, включая текущие записи (text и number)
# и архивированные записи (archive_text и archive_number).
# Метод __repr__возвращает строковое представление объекта, которое можно использовать для создания нового объекта
# того же класса с теми же записями.
# Архивированные записи могут быть получены через атрибуты archive_text и archive_number.
# Метод __new__ - это статический метод, который создает новый экземпляр класса.
# Первым аргументом метод __new__ получает ссылку на класс (cls), а затем может принимать дополнительные аргументы.
# Метод __new__ проверяет, существует ли уже экземпляр класса Archive (с использованием атрибута _instance).
# Если экземпляр существует, то метод вместо создания нового экземпляра добавляет
# текущие значения text и number в архив (списки archive_text и archive_number) для уже существующего экземпляра.
# Если экземпляр еще не существует, метод создает новый экземпляр класса Archive
# с пустыми архивами для текстовых и числовых записей. В любом случае метод возвращает созданный
# или существующий экземпляр класса Archive.
# Метод __init__ - это конструктор экземпляра класса, который вызывается после создания экземпляра
# с использованием метода __new__. Метод __init__ принимает два аргумента: text (строка) и number
# (целое число или число с плавающей точкой). В методе __init__устанавливаются атрибуты text и number текущего
# экземпляра класса для хранения переданных текстовой и числовой записей. Эти записи могут быть затем добавлены в архив
# (списки archive_text и archive_number) с использованием метода __new__.


class Archive:
    _instance = None
    t1 = []
    n1 = []

    # def __new__(cls, text, number):
    #
    #     if cls._instance is None:
    #         cls._instance = super().__new__(cls)
    #         cls._instance.archive_text = []
    #         cls._instance.archive_number = []
    #     else:
    #         cls._instance.archive_text = cls._instance.text
    #         cls._instance.archive_number = cls._instance.number
    #     return cls._instance

    def __init__(self, text: str, number):
        self.text = text
        self.number = number
        self.t1.append(text)
        self.n1.append((number))
        self.archive_number = [number]
        self.archive_text = [text]

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.t1} and {self.n1}'

    def __repr__(self):
        return f'Data_({self.text=}, {self.number=})'


if __name__ == '__main__':
    archive1 = Archive("Запись 1", 42)
    print(archive1.archive_text)
    print(archive1.archive_number)
    archive2 = Archive("Запись 2", 3.14)
    print(archive2.archive_text)
    print(archive2.archive_number)
    archive3 = Archive("Запись 3", 2.72)
    print(archive3.archive_text)
    print(archive3.archive_number)
    # b = Archive_('Good', 7)
    # d = Archive_('sdf', 9)
    # print(Archive_.__dict__)
    #
    # print(f"{c = }\t{c.all_text = }\t{c.all_number = }\t{type(c)}")
    # print(f"{b = }\t{b.all_text = }\t{b.all_number = }\t{type(b)}")
    # print(f"{d = }\t{d.all_text = }\t{d.all_number = }\t{type(d)}")
    print(archive1)
    # print([c])
    # print(repr(c))

