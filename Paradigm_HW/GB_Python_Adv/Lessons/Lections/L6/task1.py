import sys
print(sys)

print(sys.builtin_module_names)
print(*sys.path, sep='\n')



from sys import builtin_module_names, path
print(builtin_module_names)
print(*path, sep='\n')

