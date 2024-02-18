import shutil


shutil.copytree('dir', 'one_more_dir') # копирование всего дерева каталогов


# Удаления файлов
import shutil

shutil.rmtree('dir')


import os
from pathlib import Path
os.remove('one_more_dir/one.txt')
Path('one_more_dir/one_more.txt').unlink()
