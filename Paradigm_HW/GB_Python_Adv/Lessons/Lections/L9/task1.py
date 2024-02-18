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
print(outers)               # <function outers at 0x000002C096B29D00>
print(outers())             # <function outers.<locals>.closure at 0x000002C096B2ACA0>
print(outers()())           # 4

