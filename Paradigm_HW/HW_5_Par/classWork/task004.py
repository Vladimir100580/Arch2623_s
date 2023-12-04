from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, Z, expense, total_expense')

+ expense('Еда', 100)
+ expense('Транспорт', 50)
+ expense('Еда', 200)

# Расчет общих затрат по категориям
total_expense(X, Y) <= sum_(Z, for_each=expense(X, Z))

# Запрос и вывод общих затрат на еду
print(total_expense('Еда', Y))