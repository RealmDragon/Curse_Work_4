from pathlib import Path

ROOT_PATH = Path(__file__).parent
VACANCIES_PATH = ROOT_PATH.joinpath("data", "vacancies.json")
TEST_VACANCIES_PATH = ROOT_PATH.joinpath("tests", "tests_vacancies.json")
