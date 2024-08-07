import pytest

from config import TEST_VACANCIES_PATH_JSON
from src.json_saver import JSONSaver
from src.vacancy import Vacancy


@pytest.fixture
def vacancy():
    return Vacancy("Менеджер по работе с клиентами", "https://hh.ru/vacancy/101709979",
                   4_000_000, 7_000_000, "Ташкент",
                   "Опыт работы в продажах обязателен", "Консультирование клиентов")


@pytest.fixture()
def vacancy2():
    return Vacancy("Менеджер по работе с клиентами", "https://hh.ru/vacancy/101709979",
                   40_000, 70_000, "Ташкент",
                   "Опыт работы в продажах обязателен", "Консультирование клиентов")


@pytest.fixture()
def json_saver():
    return JSONSaver(filename=TEST_VACANCIES_PATH_JSON)

