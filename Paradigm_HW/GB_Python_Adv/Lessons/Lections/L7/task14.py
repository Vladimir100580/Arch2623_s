import os
from pathlib import Path


print(os.getcwd())
print(Path.cwd())
os.chdir('../..')   # меняем рабочую директрию
print(os.getcwd())
print(Path.cwd())