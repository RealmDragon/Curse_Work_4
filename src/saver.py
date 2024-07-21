from abc import ABC, abstractmethod


class Saver(ABC):

    def __init__(self, filename):
        """
        Инициализирует экземпляр Saver.

        Args:
            filename (str): Имя файла для записи/чтения данных.
        """
        self.filename = filename

    @abstractmethod
    def write_data(self, data):
        """
        Записывает данные в файл.

        Args:
            data: Данные для записи.
        """
        pass

    @abstractmethod
    def get_data(self):
        """
        Считывает данные из файла.

        Returns:
            Данные из файла.
        """
        pass

    @abstractmethod
    def del_data(self):
        """
        Удаляет данные из файла.
        """
        pass
