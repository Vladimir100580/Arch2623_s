#
# from typing import List
#
#
# def merge_sorting(lst: List[int]):
#     if len(lst) <= 1:
#         return lst
#     mid = len(lst) // 2
#     left = merge_sorting(lst[:mid])
#     right = merge_sorting(lst[mid:])
#     return merge(left, right)
#
#
# def merge(left: List[int], right: List[int]) -> List[int]:
#     result = []
#     i, j = 0, 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#     else:
#         result.append(right[j])
#         j += 1
#         return result + left[i:] + right[j:]
#
# print(merge_sorting([6,4,8,5,3,4,8,3,5]))

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Пример использования метода сортировки слиянием
arr = [14, 7, 3, 12, 9, 11, 6, 2]
print("Исходный массив:", arr)
merge_sort(arr)
print("Отсортированный массив:", arr)