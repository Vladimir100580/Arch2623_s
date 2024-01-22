# Напишите функцию для транспонирования матрицы transposed_matrix,
# принимает в аргументы matrix, и возвращает транспонированную матрицу.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]


def transpose(matrix):
    tr_matr = []
    for j in range(len(matrix[0])):
        row = []
        for i in matrix:
            row.append(i[j])
        tr_matr.append(row)
    return tr_matr


def transpose_1(matrix):
    return list([list(i) for i in zip(*matrix)])



transposed_matrix = transpose(matrix)
print(transposed_matrix)
print(transpose_1(matrix))
# Введите ваше решение ниже
