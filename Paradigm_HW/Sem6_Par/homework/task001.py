import random
from typing import List


def binary_search(arr: List[int], number: int) -> int:
    """
    Реализует бинарный поиск элемента в целочисленном массиве.

    Agrs:
    - arr (List[int]): Целочисленный массив, в котором осуществляется поиск.
    - number (int): Искомый элемент в массиве.

    Return:
    - int: Индекс элемента в массиве, если элемент найден. Или -1, если элемент не найден.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == number:
            return mid
        elif arr[mid] < number:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main():
    # На вход подаем целочисленный упорядоченный массив
    arr = random.sample([_ for _ in range(100)], k=10)
    arr.sort()

    print(f"Исходный массив: {arr}")
    number = int(input("Введите искомый элемент: "))
    result = binary_search(arr, number)

    if result == -1:
        print("Запрашиваемого элемента нет в массиве")
    else:
        print(f"Запрашиваемый элемент: {number} найден по индексу: {result}")


if __name__ == "__main__":
    main()