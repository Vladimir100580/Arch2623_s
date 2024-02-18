class Singleton:  # Паттерны одиночки (всегда возвращается первый экземпляр)
    _instance = None   # Если нужно иметь класс в единственном экземпляре (он в замыкании)

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)   # создаем новый класс если он None.
        return cls._instance

    def __init__(self, name: str):
        self.name = name


a = Singleton('Первый')
print(f'{a.name = }')
b = Singleton('Второй')
print(f'{a is b = }')
print(f'{a.name = }\n{b.name = }')