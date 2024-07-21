import json

from src.saver import Saver


class JSONSaver(Saver):
    """ Класс для записи в json-файл """

    def __init__(self, filename):
        """ Конструктор класса """

        super().__init__(filename)

    def write_data(self, data):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def get_data(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"Файл {self.filename} не найден")
            return []

    def del_data(self):
        try:
            with open(self.filename, 'w'):
                pass
        except FileNotFoundError:
            print(f"Файл {self.filename} не найден")