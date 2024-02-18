def outers():
    n = 2

    def closure():
        return n ** 2
    return closure


closure_foo = outers()      # Вызываем внешнюю функцию, возвращаемая функция (замыкание) присваивается переменной
print(closure_foo)          # <function outers.<locals>.closure at 0x7f254d6fe170>
num = closure_foo()         # Вызываем замыкание, результат присваивается переменной
print(num)                  # 4

# Второй вариант вызова замыкания
print(outers)
print(outers())
print(outers()())           # 4


def add_one_str(a: str):
    print(1, a)

    def add_two_str(b: str):
        return a + ' ' + b

    print(2, add_two_str)
    return add_two_str


print(add_one_str('Hello')('world!'))