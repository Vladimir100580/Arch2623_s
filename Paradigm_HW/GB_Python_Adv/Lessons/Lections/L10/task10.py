class Person:
    max_up = 3

    def __init__(self, name, race='unknown'):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100

    def level_up(self):  # Работаю с вызываемым экземпляром
        self.level += 1

    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity

    def change_health_1(self, other1, other2, quantity):
        self.health += quantity
        other1.health -= quantity
        other2.health -= 2*quantity


p1 = Person('Сильвана', 'Эльф')
p2 = Person('Иван', 'Человек')
p3 = Person('Грогу')
print(f'{p1.health = }, {p2.health = }, {p3.health = }')
p1.change_health(p2, 30)
print(f'{p1.health = }, {p2.health = }, {p3.health = }')
p2.change_health_1(p1, p3, 20)
print(f'{p1.health = }, {p2.health = }, {p3.health = }')