lst_1 = []
lst_2 = [42, 256, 73]
lst_3 = [("Иван", 125_000), ("Николай", 96_000), ("Пётр", 109_000)]
print(max(lst_1, default='empty'))  # чтобы не вызывать ошибок
print(max(*lst_2))       # можно без *
print(max(lst_3, key=lambda x: x[1]))


lst_1 = []
lst_2 = [42, 256, 73]
lst_3 = [("Иван", 125_000), ("Николай", 96_000), ("Пётр", 109_000)]
print(min(lst_1, default='empty'))
print(min(*lst_2))             # зачем распаковывать!??
print(min(lst_3, key=lambda x: x[1]))


my_list = [42, 256, 73]
print(sum(my_list))
print(sum(my_list, start=1024))


