import os
import json
import csv
import pickle

directory = r'C:/Users/vovar_h1dqlw1/IdeaProjects/Works/Paradigm_HW/GB_Python_Adv/Lessons/Lections/'


def traverse_directory(directory):
    list0 = []
    for parent, dirs, files in os.walk(directory):
        for dir in dirs:
            list0.append({'Path': f'{parent}{dir}', 'Type': 'Directory', 'Size': get_dir_size(f'{parent}{dir}')})
        for file in files:
            fullname = os.path.join(parent, file)
            list0.append({'Path': fullname, 'Type': 'File', 'Size': os.path.getsize(fullname)})
    return list0


def get_dir_size(dir_path: str):
    size = 0
    for cdir, dirs, files in os.walk(dir_path):
        for file in files:
            full_path = os.path.join(cdir, file)
            if not os.path.islink(full_path):
                size += os.path.getsize(full_path)
    return size


def size_dir(folder_path):
    full_size = 0
    for parent, dirs, files in os.walk(folder_path):
        full_size = sum(os.path.getsize(os.path.join(parent, file)) for file in files)
    return full_size


print(traverse_directory(directory))


def save_results_to_json(name_file):
    with open(name_file, 'w') as file:
        json.dump(traverse_directory(directory), file)


def save_results_to_csv(name_file):
    to_csv = traverse_directory(directory)
    keys = to_csv[0].keys()
    with open(name_file, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(to_csv)


def save_results_to_pickle(name_file):
    a = traverse_directory(directory)
    with open(name_file, 'wb') as handle:
        pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)



save_results_to_json('results.json')
save_results_to_csv('results.csv')
save_results_to_pickle('results.pkl')

