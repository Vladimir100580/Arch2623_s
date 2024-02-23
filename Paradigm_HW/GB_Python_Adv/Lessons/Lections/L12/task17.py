class Text:
    def __init__(self, param):
        self.param = param
        print(f'{self.param = }')

    def __set_name__(self, owner, name):  # owner класс владельца дескриптора, имя атрибута из класса
        print(f'{self = }, {owner = }, {name = }, {self.param = }')
        self.param_name = '_' + name

    def __set__(self, instance, value):   # Позволяет определить поведение при присвоении значения дескриптору.
        print(f'!!{self = }, {instance = }, {value = }, {self.param_name = }')
        if self.param(value):
            setattr(instance, self.param_name, value) # instance : Экземпляр класса владельца дескриптора.
                            # setattr -
        else:
            raise ValueError(f'Bad {value}')


class User:
    first_name = Text(str.istitle)
    last_name = Text(str.isupper)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f'Student(first_name={self.first_name}, last_name = {self.last_name})'


if __name__ == '__main__':
    std_one = User('Гвидо Ван', 'РОССУМ')
    print(std_one.__dict__)
    # std_one = User('Гвидо ван', 'Россум')
