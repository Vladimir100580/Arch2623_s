# Примет из Ютуба
# class O
# class A extends O
# class B extends O
# class C extends O
# class D extends O
# class E extends O
# class K1 extends A, B, C
# class K2 extends D, B, E
# class K3 extends D, A
# class Z extends K1, K2, K3

class A:
    def __init__(self):
        print('Init class A')
        self.data_a = 'A'


class B:
    def __init__(self):
        print('Init class B')
        self.data_b = 'B'


class C:
    def __init__(self):
        print('Init class C')
        self.data_c = 'C'


class D:
    def __init__(self):
        print('Init class D')
        self.data_d = 'D'


class E:
    def __init__(self):
        print('Init class E')
        self.data_e = 'E'


class K1(A, B, C):
    def __init__(self):
        print('Init class K1')
        super().__init__()


class K2(D, B, E):
    def __init__(self):
        print('Init class K2')
        super().__init__()


class K3(A, D):
    def __init__(self):
        print('Init class K3')
        super().__init__()


class Z(K1, K2, K3):
    def __init__(self):
        print('Init class Z')
        super().__init__()


print(*Z.mro(), sep='\n')
z = Z()
# print(f'{z.data_b = }')
# print(f'{z.data_a = }') # AttributeError: 'Z' object has no attribute 'data_a' (такая, вот, хитрая штука)

