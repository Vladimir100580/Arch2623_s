def vnesh(num1):
    t = 7

    def vnutr(num2):
        return t * num1 + num2
    print(vnutr)
    return vnutr  # Возвращаем функцию, как объект, которая, в свою очередь, запрашивает еще один параметр num2.


print(vnesh)
print(vnesh(5)(3))
vn = vnesh(5)
print(vn(3), vn(4))

print(vnesh)
