from typing import Callable


def add_one_str(a: str) -> Callable[[str], str]:
    def add_two_str(b: str) -> str:
        return a + ' ' + b

    return add_two_str     # функцию ПЕРЕДАЕМ, а не вызываем


print(add_one_str('Hello')('world!'))
