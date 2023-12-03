# Решим задачу для двух вариантов:
# - формула из презентации с ДЗ
# - реальная формула мат.статистики

def average(arr) -> float:
    """
        Расчет среднего значения элементов массива.

    Args:
        - arr: массив целых значений

    Return:
        - Среднее значение элементов массива
    """
    return sum(arr) / len(arr)


def _covariance_pow(arr1, arr2, pow) -> float:      # '_' т.к. данная функция характерна лишь для данного использования
    """
            Расчет ковариации в заданной степени.  (Для нахождения корреляции по истинной формуле pow = 1, и только)

        Args:
            - arr1: первый массив значений
            - arr2: второй массив значений
            - pow: заданная степень входящих в ковариацию множителей

        Return:
            - Значение ковариации в заданной степени
    """
    n = len(arr1)
    n1 = average(arr1)
    n2 = average(arr2)
    return sum([((arr1[i] - n1) ** pow) * ((arr2[i] - n2) ** pow) for i in range(n)])


def mean_square_deviation(arr) -> float:      # Для вычисления знаменателя по верной формуле
    """
            Расчет среднего квадратического отклонения значений массива.

        Args:
            - arr: массив целых значений

        Return:
            - Среднее квадратического отклонения значений массива.
    """
    aver = average(arr)
    return (sum([(xi - aver) ** 2 for xi in arr])) ** 0.5


def pearson_correlation_sem(arr1, arr2) -> float:
    """
    Расчет "корреляции Пирсона" между двумя массивами. (по формуле ДЗ из презентации семинара)

    Args:
     - arr1: первый массив значений
     - arr2: второй массив значений

    Return:
     - "Корреляция Пирсона" между массивами arr1 и arr2
    """

    # Проверка на то, что массивы одинаковой длины
    if len(arr1) != len(arr2):
        raise ValueError("Массивы должны быть одинаковой длины")

    correlation_sem = _covariance_pow(arr1, arr2, 1) / (_covariance_pow(arr1, arr2, 2) ** 0.5)

    return correlation_sem


def pearson_correlation(arr1, arr2) -> float:
    """
    Расчет корреляции Пирсона между двумя массивами. (по истинной формуле)

    Args:
     - arr1: первый массив значений
     - arr2: второй массив значений

    Return:
     - Корреляция Пирсона между массивами arr1 и arr2
    """

    # Проверка на то, что массивы одинаковой длины
    if len(arr1) != len(arr2):
        raise ValueError("Массивы должны быть одинаковой длины")

    msd_x = mean_square_deviation(arr1)
    msd_y = mean_square_deviation(arr2)
    correlation = _covariance_pow(arr1, arr2, 1) / (msd_x * msd_y)

    return correlation


array1 = [3, 2, 1]         # Этот пример должен дать коэффициент корреляции равный 1.
array2 = [5, 3, 1]


correlation_sem = round(pearson_correlation_sem(array1, array2), 3)
correlation = round(pearson_correlation(array1, array2), 3)

print(f"Коэффициент по формуле из презентации семинара: {correlation_sem}")
print(f"Коэффициент корреляции Пирсона по стандартной формуле: {correlation}")
