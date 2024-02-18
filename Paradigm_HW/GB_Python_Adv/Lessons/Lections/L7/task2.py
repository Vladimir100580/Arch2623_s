f = open('text_data.txt', 'r', encoding='utf-8')
print(f)
print(list(f))

f = open('text_data1.txt', 'a', encoding='utf-8')
f.write('\nОкончание файла')
f.close()     # сохраняем
