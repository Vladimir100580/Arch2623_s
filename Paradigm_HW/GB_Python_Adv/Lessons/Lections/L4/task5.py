# Позиционные и ключевые параметры

def func(positional_only_parameters, /, positional_or_keyword_parameters, *, keyword_only_parameters):
    pass

def standard_arg(arg): # здесь подразумевается positional_or_keyword_parameters, т.е. любой тип
    print(arg) # Принтим для примера, а не для привычки


standard_arg(42)    # Позиционный стиль
standard_arg(arg=42)  # Ключевой стиль


def pos_only_arg(arg, /):   # запрет ключевого стиля
    print(arg) # Принтим для примера, а не для привычки


pos_only_arg(42)
# pos_only_arg(arg=42) # TypeError: pos_only_arg() got somepositional-only arguments passed as keyword arguments: 'arg'

def kwd_only_arg(*, arg): # Теперь только позиционный стиль.
    print(arg) # Принтим для примера, а не для привычки


# kwd_only_arg(42)  # Ошибка теперь здесь
kwd_only_arg(arg=42)


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only) # Принтим для примера, а не для привычки

# combined_example(1, 2, 3) # TypeError: combined_example() takes 2 positional arguments but 3 were given
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
# combined_example(pos_only=1, standard=2, kwd_only=3) # TypeError: combined_example() got some positional-only
# arguments passed as keyword arguments: 'pos_only'

def men_mest(*, a, b):
    print(a, b)

men_mest(b=5, a=6)   # Если ключевой стиль, можно менять последовательность.