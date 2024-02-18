from random import randint

__all__ = ['func', '_secret', 'SIZE', 'result', 'randint']

SIZE = 100            # глобальная
_secret = 'qwerty'    # защищенная
__top_secret = '1q2w3e4r5t6y'    # приватная


def func(a: int, b: int) -> str:
    z = f'В диапазоне от {a} до {b} получили {randint(a, b)}'
    return z


result = func(1, 6)
