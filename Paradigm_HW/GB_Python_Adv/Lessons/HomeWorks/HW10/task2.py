class LotteryGame:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def compare_lists(self):
        list = [i for i in self.list1 if i in self.list2]
        if list:
            print(f'Совпадающие числа: {list}')
            print(f'Количество совпадающих чисел: {len(list)}')
        else:
            print('Совпадающих чисел нет.')


list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()
game.compare_lists()

