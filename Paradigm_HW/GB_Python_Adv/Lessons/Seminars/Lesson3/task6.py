# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

user_string = 'трам паujjnрам пам ням'
list_str = user_string.split()
list_str.sort()
max_len = max(list_str, key=len)    # key - это правило по которому ищем max
print(max_len)
print(list_str)
for i, word in enumerate(list_str, 1):
    print(f"{i} {word:>{len(max_len)}}")