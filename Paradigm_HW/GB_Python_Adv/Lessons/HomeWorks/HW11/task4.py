# Разработать класс Matrix, представляющий матрицу и обеспечивающий базовые операции с матрицами.
# Атрибуты класса:
# rows (int): Количество строк в матрице.
# cols (int): Количество столбцов в матрице.
# data (list): Двумерный список, содержащий элементы матрицы.
# Методы класса:
# __init__(self, rows, cols): Конструктор класса, который инициализирует атрибуты rows и cols, а также создает
# двумерный список data размером rows x cols и заполняет его нулями.
# __str__(self): Метод, возвращающий строковое представление матрицы. Возвращаемая строка представляет матрицу, где элементы разделены пробелами,
# а строки разделены символами новой строки.
# Например:
# 1 2 3
# 4 5 6
# __repr__(self): Метод, возвращающий строковое представление объекта, которое может быть использовано
# для создания нового объекта того же класса с такими же размерами и данными.
# __eq__(self, other): Метод, определяющий операцию "равно" для двух матриц. Сравнивает две матрицы и возвращает True,
# если они имеют одинаковое количество строк и столбцов, а также все элементы равны. Иначе возвращает False.
# __add__(self, other): Метод, определяющий операцию сложения двух матриц. Проверяет, что обе матрицы
# имеют одинаковые размеры (количество строк и столбцов). Если размеры совпадают, создает новую матрицу,
# где каждый элемент равен сумме соответствующих элементов входных матриц.
# __mul__(self, other): Метод, определяющий операцию умножения двух матриц.
# Проверяет, что количество столбцов в первой матрице равно количеству строк во второй матрице.
# Если условие выполняется, создает новую матрицу, где элемент на позиции [i][j] равен сумме произведений
# элементов соответствующей строки из первой матрицы и столбца из второй матрицы.


class Matrix:

    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        return ''.join([' '.join(map(str, i)) + '\n' for i in self.data])[:-1]

    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'

    def __eq__(self, other) -> bool:
        if other.rows != self.rows or other.cols != self.cols:
            return False
        for i in range(other.rows):
            for j in range(other.cols):
                if other.data[i][j] != self.data[i][j]:
                    return False
        return True

    def __add__(self, other):
        if other.rows != self.rows or other.cols != self.cols:
            return None
        list_m = []
        Ma = Matrix(other.rows, self.cols)
        for i in range(other.rows):
            r = []
            for j in range(other.cols):
                r.append(other.data[i][j] + self.data[i][j])
            list_m.append(r)
        Ma.data = list_m
        return Ma

    def __mul__(self, other):
        if self.cols != other.rows:
            return None
        list_m = []
        Ma = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            r = []
            for j in range(other.cols):
                r.append(sum([self.data[i][k] * other.data[k][j] for k in range(self.cols)]))
            list_m.append(r)
        Ma.data = list_m
        return Ma


if __name__ == '__main__':
    M1 = Matrix(2, 3)
    M1.data[1][1] = 78
    print(M1)

    M1.data = [[3, 4, 5], [9, 7, 5]]
    M2 = Matrix(2, 3)
    M2.data = [[1, 4, 5], [4, 7, 5]]
    M3 = Matrix(3, 2)
    M3.data = [[1, 4], [4, 5], [1, 2]]
    print(M1)
    print(M3)
    # print(repr(M1))

    print(M1 == M2)
    print(M1 + M2)
    print(M1*M3)

