
class Vacancies:

    """ Класс для обработки вакансии """

    def __init__(self):
        self.all_vacancies = []

    def add_vacancies(self, new_vacancies):
        assert isinstance(new_vacancies, list), "Новые Вакансии должен быть списком"
        for vacancy in new_vacancies:
            assert isinstance(vacancy, Vacancy), "Элементы новые вакансии должны быть объектами Vacancy"
            if vacancy not in self.all_vacancies:  # Проверка дубликатов
                self.all_vacancies.append(vacancy)

    @property
    def all_vacancies(self):
        return self.all_vacancies

    def to_list_dict(self):
        if self.all_vacancies:  # Проверка наличия элементов
            list_dict = []
            for i in self.all_vacancies:
                list_dict.append(i.vacancies_dict())
            return list_dict
        else:
            return []

    def sorted_vacancy_by_salary(self):
        for vacancy in self.all_vacancies:
            assert vacancy.salary_from is not None and vacancy.salary_from > 0, "Зарплата от должена быть не нулевым"
        self.all_vacancies.sort(reverse=True)  # Сортировка по salary_from в порядке убывания
