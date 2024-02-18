# Запись в файл
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
# with open('new_data.txt2', 'a', encoding='utf-8') as f:
#     for line in text:
#         res = f.write(line)
#         print(f'{res = }\n{len(line) = }')


# with open('new_data3.txt', 'a', encoding='utf-8') as f:
#     for line in text:
#         res = f.write(f'{line}\n')
#         print(f'{res = }\n{len(line) = }')

with open('new_data4.txt', 'a', encoding='utf-8') as f:
    for line in text:
        print(line, end='***\n##', file=f)
