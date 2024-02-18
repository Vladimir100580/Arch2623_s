import base_math


x = base_math.mul # Плохой приём   (x теперь не переменная, а другая функция)
y = base_math._START_MULT # Очень плохой приём  (c подчеркивания нельзя, за пределами модуля)
z = base_math.sub(73, 42)
print(x(2, 3))
print(y)
print(z)

# чтобы не порторять принты из base_math испотзуем там __main__