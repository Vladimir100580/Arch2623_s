# Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

lst = [1, 1, 5, 2, 5, 3, 3]
dict_elements = {}
for d in lst:
    dict_elements[d] = dict_elements.get(d, 0) + 1
lst_res = [i for i, j in dict_elements.items() if j > 1]
print(lst_res)
