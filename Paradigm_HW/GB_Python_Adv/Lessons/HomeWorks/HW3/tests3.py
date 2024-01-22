import re

text = "Python 3.9 is is is the latest version of Python. It's awesome!"

text_1 = re.sub("[^A-Za-z]+", ' ', text.lower())   # ^ - означает заменяем все на ' '(пробел) кроме того, что указано.
list_txt = text_1.split()
dict_word = {}
for d in text_1.split():
    dict_word[d] = dict_word.get(d, 0) + 1
dict_word = dict(sorted(dict_word.items(), key=lambda item: item[1], reverse=True))
print(dict_word)
