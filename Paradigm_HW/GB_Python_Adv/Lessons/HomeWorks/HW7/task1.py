from pathlib import Path
import os


def rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc", diap_list=None):
    if diap_list is None:
        diap_list = [0, 0]
    os.chdir('./test_folder')
    files = Path(Path().cwd()).iterdir()
    n = 0
    for file in files:

        name_1 = '.'.join(file.name.split('.')[:-1])
        print(file, name_1)
        ext = file.name.split('.')[-1]
        print(file.suffix, ext)
        if ext == source_ext:
            n += 1   # name_1[diap_list[0]: min(diap_list[1] + 1, len(name_1))]}_
            new_name = f'{desired_name}' \
                       f'{(num_digits - len(str(n))) * "0" + str(n)}.{target_ext}'
            print(f'{new_name}')
            Path(f'{name_1}.{ext}').rename(f'{new_name}')



rename_files()

# def sort_files_by_ext(path=None):
#     if not path:
#         path = Path().cwd()
#     path = Path(path)
#     files = Path(path).iterdir()
#     print(*files)
#     print(*Path().iterdir())
#     os.chdir(path)
#
#     for file in files:
#         print(file.is_file(), Path(file.suffix) not in Path().iterdir())
#         if (file.is_file()
#                 and Path(file.suffix) not in Path().iterdir()):
#             os.mkdir(file.suffix)
#
#         if file.is_file() and file.suffix != ".py":
#             file.replace(rf"{file.suffix}\{file.name}") # либо двойной \\ либо rf
#
#
# if __name__ == '__main__':
#     sort_files_by_ext(r"C:/Users/vovar_h1dqlw1/IdeaProjects/Works/Paradigm_HW/GB_Python_Adv/Lessons/Seminars/Lesson7"
#                       r"/DirExp")
#
