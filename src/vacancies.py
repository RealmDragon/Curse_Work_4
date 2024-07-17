
class Vacancies:

    """ Класс для обработки вакансии """

    def __init__(self):
        self.__all_vacancies = []

    def add_vacancies(self, new_vacancies):
        self.__all_vacancies += new_vacancies

    @property
    def all_vacancies(self):
        return self.__all_vacancies

    def to_list_dict(self):
        list_dict = []
        for i in self.__all_vacancies:
            list_dict.append(i.vacancies_dict())
        return list_dict

    def sorted_vacancy_by_salary(self):
        self.__all_vacancies.sort(reverse=True)
