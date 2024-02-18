from typing import Union


class Archive:
    _instance = None
    archive_text = []
    archive_number = []

    # def __new__(cls, text: str, number: Union[int, float]):
    #     if cls._instance is None:
    #         cls._instance = super(Archive, cls).__new__(cls)
    #         cls.archive_text = []
    #         cls.archive_number = []
    #         return cls._instance
    #     return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        self.text = text
        self.number = number
        Archive.archive_text.append(self.text)
        Archive.archive_number.append(self.number)

    def __repr__(self):
        return f'Text is {self.text} and number is {self.number}. ' \
               f'Also {Archive.archive_text} and {Archive.archive_number}'


if __name__ == '__main__':
    archive1 = Archive("Запись 1", 42)
    print(archive1.archive_text)
    print(archive1.archive_number)
    archive2 = Archive("Запись 2", 3.14)
    print(archive2.archive_text)
    print(archive2.archive_number)
    archive3 = Archive("Запись 3", 2.72)
    print(archive3.archive_text)
    print(archive3.archive_number)
    print(archive1)

