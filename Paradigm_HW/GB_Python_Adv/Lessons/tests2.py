# for i in range(360, 370):
#     print(i / 100 + 0.005, round(i / 100 + 0.005, 2))

# n = 30.5
# while n <= 41:
#     print(n, round(n))
#     n += 1
#     n = float(str(int(n * 10 + 0.5)/10))
#
# print('**************')
# print(round(2.675, 2))
# print('**************')
#
#
# n = 36.05
# while n <= 37:
#     print(n, round(n,1))
#     n += 0.1
#     n = float(str(int(n * 100 + 0.5)/100))
#
# print('**************')
#
# n = 36.705
# while n <= 36.81:
#     print(n, round(n,2))
#     n += 0.01
#     n = float(str(int(n * 1000 + 0.5)/1000))

def vnesh_kv(num):
    return num**2

def add_3(num):
    return vnesh_kv(num+3)

print(add_3(5))