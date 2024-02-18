# Преобразование из JSON строки в JSON файл

import json
my_dict = {
    "first_name": "Джон",
    "last_name": "Смит",
    "hobbies": ["кузнечное дело", "программирование",
    "путешествия"],
    "age": 35,
    "children": [
    {
        "first_name": "Алиса",
        "age": 5
        },
        {
        "first_name": "Маруся",
        "age": 3
    }
    ]
}
print(f'{type(my_dict) = }\n{my_dict = }')
with open('new_user.json', 'w') as f:
    json.dump(my_dict, f)


dic = {}
dic['Вася'] = 183
dic['Петя'] = 181
dic['Костя'] = 189
dic['Рубинчки'] = {3: 134, 4: 145, 5: 147}
# print(dic['Рубинчки'][4])
# print(f'{dic = }, {str(dic) = }')
with open('new_user_vov.json', 'w', encoding='utf-8') as f:
    json.dump(dic, f, ensure_ascii=False)


dict_to_json_text = json.dumps(my_dict)
print(f'{type(dict_to_json_text) = }\n{dict_to_json_text = }')

dict_to_json_text = json.dumps(my_dict, ensure_ascii=False)
print(f'{type(dict_to_json_text) = }\n{dict_to_json_text = }')

dict_to_json_text = json.dumps(my_dict, indent=4, separators=(',', ':'), sort_keys=True, ensure_ascii=False)
print(dict_to_json_text)      #  indent - отступы (без него будет одна строка), separators - разделители, sort_keys - сортировка ключей
