import json

from config import VACANCIES_PATH
from src.saver import Saver
from src.vacancy import Vacancy
from src.vacancies import Vacancies


class JSONSaver(Vacancies, Saver):

    def write_data(self):

        try:
            data = json.load(open(VACANCIES_PATH, encoding='utf-8'))
        except FileNotFoundError:
            data = []

        data.append(self.to_list_dict())

        with open(VACANCIES_PATH,"w",encoding='utf-8') as file:
            json.dump(self.to_list_dict(), file, indent=7, ensure_ascii=False)

    def get_data(self):
        with open(VACANCIES_PATH, encoding="utf-8") as file:
            data = json.load(file)
            self.__all_vacancies = []
            for vacancy in data:
                self.all_vacancies.append(Vacancy.vacancies_lst(vacancy))

    def del_data(self, data_json):
        del data_json



