# срезы
import copy
my_list = [2, 4, 8, 'а', 9, 2, 6, 2]
print(my_list[6:2:-1])    # -1 - шаг
my_list_1 = my_list
my_list[2] = 777   # если my_list_1 - будет тоже самое.
print(my_list, my_list_1, sep='\n')  # необходимо использовать copy - создает поверхностную копию,
                                     # работает только с одномерным списком

my_list = [2, 4, 8, 'а', 9, 2, 6, 2]
my_list_2 = my_list.copy()
my_list[2] = 777
print(my_list, my_list_2, sep='\n')

matrix = [[1, 2, 3, 11], [4, 5, 6], [7, 8, 9]]
new_matrix = matrix.copy()      # пробегается поверхностно
new_matrix_2 = copy.deepcopy(matrix)    # Используется для вложенных списков. (тратит много памяти)
matrix[1][0] = 777
print(matrix, new_matrix, new_matrix_2,  sep='\n')

print(len(matrix), len(matrix[0]))