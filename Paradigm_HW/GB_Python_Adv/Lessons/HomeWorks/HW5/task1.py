# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


file_path = "C:/Users/User/Documents/example.txt"
# file_path = '/home/user/docs/my.file.with.dots.txt'
file_path = 'file_in_current_directory.txt'


# Введите ваше решение ниже

def get_file_info(file_path):
    *path, name_extension = file_path.split("/")
    *name, extension = name_extension.split(".")
    dop_sl = ''
    if path != []:
        dop_sl = '/'
    return ('/'.join(path) + dop_sl, '.'.join(name), '.' + extension)


print(get_file_info(file_path))
