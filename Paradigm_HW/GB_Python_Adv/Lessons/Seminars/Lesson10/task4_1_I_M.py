
from task4 import DataPerson


class Employee(DataPerson):
    def __init__(self, name: str, sername: str, age: int, emp_id: int = 1):
        if len(str(emp_id)) != 6:
            raise ValueError('Некорректный идентификационный номер')
        self.emp_id = emp_id
        self.level = sum(map(int, str(emp_id))) % 7

        super().__init__(name, sername, age)


if __name__ == '__main__':
    e = Employee('Александр', 'Пушкин', 19, 123321)
    print(f'{e.emp_id=}, {e.level=}')