SIZE = 100
with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.read(SIZE):
        print(res)

print('\n******************\n')

SIZE = 50
with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.readline(SIZE):   # построчный вывод
        print(res)
