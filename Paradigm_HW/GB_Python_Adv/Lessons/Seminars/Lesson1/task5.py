# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

FORMAT = 15
def print_mult(n, m):
    for i in range(2, 11):
        st = ''
        for j in range(n, m + 1):
            mult = j * i
            # if i < 10:
            #     s1 = ' '
            # else:
            #     s1 = ''
            # if mult < 10:
            #     s2 = ' '
            # else:
            #     s2= ''
            st0 = f'{j} X {s1}{i} = {s2}{mult}'
            st += st0 + ' ' * (FORMAT - len(st0))
        print(st)

print_mult(2, 5)
print()
print_mult(6, 9)