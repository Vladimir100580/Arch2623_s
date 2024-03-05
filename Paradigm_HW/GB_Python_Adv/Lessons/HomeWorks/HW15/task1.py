import csv
import pytest


# Решил расширить функционал и добавить загрузку не только названий учебных дисциплин (из файла),
# но и оценок с тестовыми баллами + добавлен метод save_subjects для сохранения изменений
def str_to_list(st: str):
    """
     Перевод строки (переданной из csv-файла), содержащей список, в list-список
    """
    return list(map(int, st[1:-1].split(',')))


class Student:
    """
    Класс, представляющий студента.
    """

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = {}
        self.load_subjects(subjects_file)
        self.subjects_file = subjects_file

    def __setattr__(self, name, value):
        if name == 'Name':
            if not value.replace(' ', '').isalpha() or not value.istitle():
                raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        # self.__dict__[name] = value
        super().__setattr__(name, value)  # обращаемся к базовому классу
        # print(super().__dict__)

    def __getattr__(self, name):
        if name in self.subjects:
            return self.subjects[name]
        else:
            raise AttributeError(f"Предмет {name} не найден")

    def __str__(self):
        return f"Студент: {self.name}\nПредметы: {', '.join(self.subjects.keys())}"

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                subject = row[0]
                if subject not in self.subjects:
                    # print(subject, self.subjects)
                    # self.subjects[subject] = {'grades': [], 'test_scores': []}
                    self.subjects[subject] = {'grades': str_to_list(row[2]), 'test_scores': str_to_list(row[1])}

    def save_subjects(self):
        with open(self.subjects_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for k, v in self.subjects.items():
                writer.writerow([k, v['test_scores'], v['grades']])
        return True


    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            self.subjects[subject] = {'grades': [], 'test_scores': []}
        if not isinstance(grade, int) or grade < 2 or grade > 5:
            raise ValueError("Оценка должна быть целым числом от 2 до 5")
        # print(1, self.subjects[subject]['grades'], type(self.subjects[subject]['grades']))
        self.subjects[subject]['grades'].append(grade)

    def add_test_score(self, subject, test_score):
        if subject not in self.subjects:
            self.subjects[subject] = {'grades': [], 'test_scores': []}
        if not isinstance(test_score, int) or test_score < 0 or test_score > 100:
            raise ValueError("Результат теста должен быть целым числом от 0 до 100")
        self.subjects[subject]['test_scores'].append(test_score)

    def get_average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")

        test_scores = self.subjects[subject]['test_scores']
        if len(test_scores) == 0:
            return 0
        return sum(test_scores) / len(test_scores)

    def get_average_grade(self):
        total_grades = []
        for subject in self.subjects:
            grades = self.subjects[subject]['grades']
            if len(grades) > 0:
                total_grades.extend(grades)
        if len(total_grades) == 0:
            return 0
        # print(f'{total_grades=}')
        return sum(total_grades) / len(total_grades)


# Тестирование добавления оценки
def test_add_grade():
    s1 = Student("Name", 'for_tests.csv')
    s1.add_grade('Математика', 5)
    assert s1.subjects['Математика']['grades'] == [3, 4, 5]


# Тестирование на добавление оценки, не входящей в диапазон [2, 5]
def test_add_negative_grade():
    s1 = Student("Name", 'for_tests.csv')
    with pytest.raises(ValueError):
        s1.add_grade('Математика', 7)
    with pytest.raises(ValueError):
        s1.add_grade('Математика', 3.6)


# Тестирование добавления тестового балла
def test_add_test_score():
    s1 = Student("Name", 'for_tests.csv')
    s1.add_test_score('Информатика', 70)
    assert s1.subjects['Информатика']['test_scores'] == [80, 90, 70]


# Тестирование на добавление тестового балла, не входящего в диапазон целых чисел [0, 100]
def test_add_negative_test_score():
    s1 = Student("Name", 'for_tests.csv')
    with pytest.raises(ValueError):
        s1.add_test_score('Информатика', 170)
    with pytest.raises(ValueError):
        s1.add_test_score('Информатика', 70.5)


# Тестирование нахождения средней оценки
def test_get_average_grade():
    s1 = Student("Name", 'for_tests.csv')
    assert s1.get_average_grade() == 3.375


# Тестирование нахождения среднего тестового балла по предмету
def test_get_average_test_score():
    s1 = Student("Name", 'for_tests.csv')
    assert s1.get_average_test_score("Химия") == 65
    assert s1.get_average_test_score("Физика") == 40


if __name__ == '__main__':
    student = Student("Name", "subjects.csv")  # Для тестирования, используется файл 'for_tests.csv'

    student.add_grade("Математика", 4)
    student.add_grade("Математика", 3)
    student.add_test_score("Математика", 85)
    student.add_test_score("Математика", 93)

    student.add_grade("История", 5)
    student.add_test_score("История", 92)

    student.add_grade("Кибернетика", 4)
    student.add_test_score("ТФКП", 91)

    student.save_subjects()

    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")

    average_test_score = student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")


