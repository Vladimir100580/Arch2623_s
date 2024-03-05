from collections import namedtuple

Data = namedtuple('Data', ['mathematics', 'chemistry', 'physics', 'genetics'],
                  defaults=[5, 5, 5, 5])
d = {
    'Ivanov': Data(4, 5, 3, 5),
    'Petrov': Data(physics=4, genetics=3),
    'Sidorov': Data(),
}

print(d)
# {'Ivanov': Data(mathematics=4, chemistry=5, physics=3, genetics=5),
#  'Petrov': Data(mathematics=5, chemistry=5, physics=4, genetics=3),
#  'Sidorov': Data(mathematics=5, chemistry=5, physics=5, genetics=5)}


# arr1 = array('B', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# arr2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# import sys
#
# print(sys.getsizeof(arr1))  # 90 байтов
# print(sys.getsizeof(arr2))  # 136 байтов