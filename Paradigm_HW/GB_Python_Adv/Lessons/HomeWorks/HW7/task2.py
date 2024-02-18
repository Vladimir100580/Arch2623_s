with open("__init__.py", "w") as init_file:
    init_file.write("import os\n\n\n")
    init_file.write("def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=None):")
    init_file.write("\n    new_names = []")
    init_file.write("\n    files = os.listdir('test_folder')")
    init_file.write("\n    filtered_files = [file for file in files if file.endswith(source_ext)]")
    init_file.write("\n    filtered_files.sort()")
    init_file.write("\n    num = 1")
    init_file.write("\n    for file in filtered_files:")
    init_file.write("\n        name = os.path.splitext(file)[0]")
    init_file.write("\n        if name_range:")
    init_file.write("\n            name = name[name_range[0]-1:name_range[1]]")
    init_file.write("\n        new_name = desired_name + str(num).zfill(num_digits) + '.' + target_ext")
    init_file.write("\n        path_old = os.path.join(os.getcwd(), folder_name, file)")
    init_file.write("\n        path_new = os.path.join(os.getcwd(), folder_name, new_name)")
    init_file.write("\n        os.rename(path_old, path_new)")
    init_file.write("\n        num += 1")
# def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=None):
#     new_names = []
#     files = os.listdir('test_folder')
#     filtered_files = [file for file in files if file.endswith(source_ext)]
#     filtered_files.sort()
#     num = 1
#     for file in filtered_files:
#         name = os.path.splitext(file)[0]
#         if name_range:
#             name = name[name_range[0]-1:name_range[1]]
#         new_name = desired_name + str(num).zfill(num_digits) + '.' + target_ext
#         path_old = os.path.join(os.getcwd(), folder_name, file)
#         path_new = os.path.join(os.getcwd(), folder_name, new_name)
#         os.rename(path_old, path_new)
#         num += 1")
