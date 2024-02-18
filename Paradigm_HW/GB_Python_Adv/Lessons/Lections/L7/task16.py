import os
from pathlib import Path

print(Path.cwd())
os.makedirs('dir/other_dir/new_os_dir')
# Path('some_dir/dir/new_path_dir').mkdir() # FileNotFoundError
Path('some_dir/dir/new_path_dir').mkdir(parents=True)    # Если каталог уже создан, получаем ошибку

os.rmdir('dir/other_dir/new_os_dir')              # удаляем каталоги Не удаляет каталоги, если они не пусты
Path('some_dir/dir/new_path_dir').rmdir()

Path('some_dir/dir/new_path_dir').mkdir(parents=True)