from src.get_vacancies import GetVacanciesAPI
import requests
from typing import List, Dict

class HeadHunterAPI(GetVacanciesAPI):
    """Класс для подключения к hh.ru"""

    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "per_page": "", "only_with_salary": True}

    def get_response(self, keyword, per_page) -> requests.Response:
        self.params["text"] = keyword
        self.params["per_page"] = per_page
        return requests.get(self.url, params=self.params)

    def get_vacancies(self, keyword: str, per_page: int):
        return self.get_response(keyword, per_page).json()["items"]

    def get_filter_vacancies(self, keyword: str, per_page: int) -> List[Dict]:
        """
        Получает отфильтрованные вакансии по ключевому слову и количеству на странице.

        Args:
            keyword (str): Ключевое слово для поиска.
            per_page (int): Количество вакансий на странице.

        Returns:
            List[Dict]: Список отфильтрованных вакансий.
        """
        vacancies = self.get_vacancies(keyword, per_page)
        return vacancies