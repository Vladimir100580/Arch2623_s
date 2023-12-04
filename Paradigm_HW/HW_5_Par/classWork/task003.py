from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, Z, student, course, number_of_students')

+ student('Алексей', 'Курс1')
+ student('Мария', 'Курс1')
+ student('Иван', 'Курс2')

# Подсчет количества студентов на каждом курсе
number_of_students(X, Y) <= count_(Z, for_each=student(Z, X))

# Запрос: сколько студентов на 'Курс1'?
print(number_of_students('Курс1', Y))