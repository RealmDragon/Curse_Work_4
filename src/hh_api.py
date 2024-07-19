import requests

from src.get_vacancies import GetVacanciesAPI
from src.vacancy import Vacancy


class HeadHunterAPI(GetVacanciesAPI):
    """ Класс для подключения к hh.ru """

    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.vacancies = []

    def get_response(self, keyword, per_page):
        params = {"text": keyword, "per_page": per_page}
        status_check = requests.get(self.url)
        if status_check.status_code == 200:
            return requests.get(self.url, params=params)
        else:
            print("API вернуло не верный ответ")
            exit()


    def get_vacancies(self, keyword, per_page):
        return self.get_response(keyword, per_page).json()["items"]

    def get_filter_vacancies(self, keyword, per_page):
        filter_vacancies = []
        vacancies = self.get_vacancies(keyword, per_page)
        for vacancy in vacancies:
            filter_vacancies.append(Vacancy.vacancies_lst(vacancy))
        return filter_vacancies

