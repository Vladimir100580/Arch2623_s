with open('text_data.txt', 'r+', encoding='utf-8') as f:       # with гарантирует закрытие файла
    print(list(f))
print(f.write('Пока')) # ValueError: I/O operation on closed file. Даже, если произойдет ошибка