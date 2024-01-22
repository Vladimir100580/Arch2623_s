# кортежи tuple (неизменяемы)   работаю методы, такие как count, index, ...
a = ()
b = 1,
b1 = (1,)    # здесь запятая обязательна
c = 1, 2, 3,
c1 = (1, 2, 3,)  # можно без последней запятой (это знак для читателя кода)
d = tuple(range(3))
print(a, b, b1, type(b1), c, type(c), c1, type(c1), d, sep='\n')

# f((a, b, c)) функции передается один аргумент в виде кортежа
# f(a, b, c) функции передаются 3 элемента

print(type('text',))    # класс str т.к. нужны еще скобки

# Словари.   пары: ключ (неизменяемый), значение (может быть изменяемое, или нет)
a = {'one': 1, 'two': 2, 'three': 3}
b = dict(one=1, two=2, three=3)
c = dict([('one', 1), ('two', 2), ('three', 3)])
print(a == b == c)
a['four'] = 4
print(a)
print(a['two'])
print(a.get('two'))
print(a.get('five'))
print(a.get('five', 777))

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}

# my_dict['two'] = 7   заменяется в отличии от setdefault
# print(my_dict)

spam = my_dict. setdefault('five')   # добавит ключ в словарь c None
print(f'{spam = }\t{my_dict=}')

eggs = my_dict.setdefault('six', 6)
print(f'{eggs = }\t{my_dict=}')
new_spam = my_dict.setdefault('two')
print(f'{new_spam=}\t{my_dict=}')
new_eggs = my_dict.setdefault('one', 1_000)
print(f'{new_eggs=}\t{my_dict=}')

# методы keys(), values() и items()
for key, value in my_dict.items():  # так правильно
    print(key, value)
print('*******************')
# popitem() удаляет последнюю пару, присваивая значение (или pop удаляет по ключу)
k, v = my_dict.popitem()
print(k, v, my_dict)
k = my_dict.pop('two')
print(k, my_dict)

# update - обновление одного словарю еще одним
# С версии python 3.10 работает операция | - объединение словарей