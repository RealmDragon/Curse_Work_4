import requests

from src import vacancies
from src.get_vacancies import GetVacanciesAPI
from src.vacancy import Vacancy


class HeadHunterAPI(GetVacanciesAPI):
    """ Класс для подключения к hh.ru """

    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.vacancies = []

    def get_response(self, keyword, per_page):
        assert isinstance(keyword, str), "Запрос должен быть строкой"
        assert isinstance(per_page, int), "Страницы должен быть целым числом"
        assert per_page > 0, "Страниц должно быть больше 0"

        params = {"Запрос": keyword, "Страница": per_page}
        status_check = requests.get(self.url)
        if status_check.status_code == 200:
            response = requests.get(self.url, params=params)
            return response
        else:
            print("API вернуло не верный ответ")
            exit()

    def get_vacancies(self, keyword, per_page):
        response = self.get_response(keyword, per_page)
        try:
            data = response.json()
            if "Запрос" in data:
                return data["Запрос"]
            else:
                print("Ответ API не содержит ключа 'items'")
                return []
        except vacancies.json.JSONDecodeError:
            print("Ошибка декодирования JSON")
            return []

    def get_filter_vacancies(self, keyword, per_page):
        filter_vacancies = []
        vacancies = self.get_vacancies(keyword, per_page)
        for vacancy in vacancies:
            filter_vacancies.append(Vacancy.vacancies_lst(vacancy))
        return filter_vacancies

