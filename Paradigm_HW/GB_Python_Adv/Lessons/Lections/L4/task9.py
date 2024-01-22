

texts = ["Привет", "ЗДОРОВА", "привеТствую"]
res = map(lambda x: x.lower(), texts)
print(*res)    # * - преобразует итерируемый объект в последовательность

numbers = [42, -73, 1024]
res = tuple(filter(lambda x: x > 0, numbers))
print(res)


names = ["Иван", "Николай", "Пётр"]
salaries = [125_000, 96_000, 109_000]
awards = [0.1, 0.25, 0.13, 0.99]
for name, salary, award in zip(names, salaries, awards):     # можно легко транспонировать.
    print(f'{name} заработал {salary:.2f} денег и премию {salary * award:.2f}')