list = [['Петя', 15, 24], ['Вова', 17, 13], ['Женя', 15, 10], ['Коля', 17, 20]]

sorted_list = sorted(list, key=lambda x: (-x[1], x[2]))

print(sorted_list)