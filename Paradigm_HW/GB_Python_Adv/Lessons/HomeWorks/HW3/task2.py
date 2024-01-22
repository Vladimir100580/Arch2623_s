# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# Слова разделяются пробелами. Такие слова как
# don t, it s, didn t итд (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.
# Отсортируйте по убыванию значения количества повторяющихся слов.

import re

text = "Python 3.9 is is is the latest version of Python. It's awesome!"

text_1 = re.sub("[^A-Za-z]+", ' ', text.lower())   # ^ - означает, заменяем все на ' '(пробел) кроме того, что указано.
list_txt = text_1.split()
dict_word = {}
for d in text_1.split():
    dict_word[d] = dict_word.get(d, 0) + 1
dict_word = list(sorted(dict_word.items(), key=lambda item: item[1], reverse=True))
print(dict_word)
