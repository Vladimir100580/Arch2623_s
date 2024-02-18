# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями. (папки будем называть расширениями)
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

from pathlib import Path
import os


def sort_files_by_ext(path=None):
    if not path:
        path = Path().cwd()
    path = Path(path)
    files = Path(path).iterdir()
    print(*files)
    print(*Path().iterdir())
    os.chdir(path)

    for file in files:
        print(file.is_file(), Path(file.suffix) not in Path().iterdir())
        if (file.is_file()
                and Path(file.suffix) not in Path().iterdir()):
            os.mkdir(file.suffix)

        if file.is_file() and file.suffix != ".py":
            file.replace(rf"{file.suffix}\{file.name}") # либо двойной \\ либо rf


if __name__ == '__main__':
    sort_files_by_ext(r"C:/Users/vovar_h1dqlw1/IdeaProjects/Works/Paradigm_HW/GB_Python_Adv/Lessons/Seminars/Lesson7"
                      r"/DirExp")

