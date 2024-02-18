from functools import wraps


def par_decor(num):
    def decor1(fun1):
        dic1 = {}

        @wraps(fun1)
        def whr(*args, **kwargs):
            vypoln = fun1(*args, **kwargs)
            print('Декоратор вовсю!')
            n = len(dic1)
            dic1[n] = vypoln * num
            return dic1

        return whr

    return decor1


@par_decor(2)
def fun1(n_pow):
    """ Крутое возведение в квадрат """
    return n_pow ** 2


print(fun1.__name__)
print(fun1(5))
print(fun1(7))
print(fun1(17))
print(f'{fun1.__name__ = }')

help(fun1)

# print(fun1(5))
