

def test_vacancy_init(vacancy):
    """ Тесты конструктора класса """

    assert vacancy.name == "Менеджер по работе с клиентами"
    assert vacancy.alternate_url == "https://hh.ru/vacancy/101709979"
    assert vacancy.salary_from == 4_000_000
    assert vacancy.salary_to == 7_000_000
    assert vacancy.area_name == "Ташкент"
    assert vacancy.requirement == "Опыт работы в продажах обязателен"
    assert vacancy.responsibility == "Консультирование клиентов"


def test_vacancy_str(vacancy):
    """ Тест строкового представления вакансии """

    assert str(vacancy) == ("Наименование вакансии: Менеджер по работе с клиентами, Ссылка на вакансию: "
                            "https://hh.ru/vacancy/101709979, Зарплата: от 4000000 до 7000000, Место работы: "
                            "Ташкент, Краткое описание: Опыт работы в продажах обязателен, Консультирование клиентов")


def test_vacancy_lt(vacancy, vacancy2):
    """ Тест утверждает, что одно значение меньше другого """

    assert vacancy < vacancy2
    if vacancy > vacancy2:
        assert ValueError
