from config import  VACANCIES_PATH_JSON
from src.json_saver import JSONSaver
from src.utils import user_choice_json

def main():
    """ Запуск программы """
    while True:  # Создаем цикл для повторного запуска программы
        user_input = input("Здравствуйте!\n"
                           "Я курсовая работа №4 и я сегодня буду помогать вам в поиске работы. Пожалуйста, введите ваш запрос:\n"
                           "Если хотите начать новую историю поиска, введите 1\n"
                           "Если хотите удалить данные истории поиска из файла, введите 2\n")

        if user_input == "1":
            user_choice_json()
            break  # Прерываем цикл, если пользователь выбрал "1"
        elif user_input == "2":
            user_input = input("Вы уверены, что хотите очистить историю?\n"
                               "Введите 1 для согласия\n"
                               "Введите 2 для отказа\n")
            if user_input == "1":
                deleter = JSONSaver(VACANCIES_PATH_JSON)
                deleter.del_data()
                print("Данные удалены!")
            elif user_input == "2":
                continue  # Продолжаем цикл, если пользователь выбрал "2"
            else:
                print("Неверный ввод.")
        else:
            print("Неверный ввод.")

if __name__ == "__main__":
    main()

