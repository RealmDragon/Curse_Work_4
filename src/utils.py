from src.hh_api import HeadHunterAPI
from src.json_saver import JSONSaver
from src.vacancy import Vacancy


def user_choice():
    keyword = input("Я курсовая работа №4 и я сегодня буду помогать вам в поиске работы пожалуста ввидете ваш запрос:\n").lower()
    per_page = int(input("Сколько профессии вы хотите видет?\n"))

    hh_api = HeadHunterAPI()
    from_hh = hh_api.get_filter_vacancies(keyword, per_page=per_page)

    print("Топ выбранных вакансии с 'HeadHunter' по зарплате: \n")
    for i in sorted(from_hh, reverse=True):
        print(i)

    json_write = JSONSaver()
    json_write.add_vacancies(from_hh)
    json_write.sorted_vacancy_by_salary()
    json_write.write_data()
    print("Данные записаны в json файл")