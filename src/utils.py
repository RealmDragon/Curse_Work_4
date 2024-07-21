from config import VACANCIES_PATH_JSON
from src.hh_api import HeadHunterAPI
from src.json_saver import JSONSaver
from src.vacancy import Vacancy

def user_choice_json():
    """ Функция для работы с пользователем, записи в json-файл """

    keyword = input("Давайте Приступим Ведите ваш запрос Например Python-Разрабочик:\n").lower()
    per_page = int(input("Сколько профессии вывести?\n"))

    hh_api = HeadHunterAPI()
    vacancies = hh_api.get_vacancies(keyword, per_page)
    vacancies = [Vacancy.from_hh_dict(vacancy) for vacancy in vacancies]
    vacancies = sorted(vacancies, reverse=True)

    print("Топ выбранных вакансии с 'HeadHunter' по зарплате: \n")
    for i in sorted(vacancies, reverse=True):
        print(i)

    vacancies = [vacancy.to_dict() for vacancy in vacancies]
    saver = JSONSaver(VACANCIES_PATH_JSON)

    saver.write_data(vacancies)
    saver.get_data()
    print("Данные записаны в json-файл")



