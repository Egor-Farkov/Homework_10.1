import json
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("/Users/egorfedorovic/Documents/Skypro/Home_works/H_w_skypro/logs/utils.log", "w")
file_formatter = logging.Formatter("%(asctime)s %(module)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_json(path: str) -> list:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
     :param path: Путь к файлу json.
     :return: Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        with open(path) as file:
            data = json.load(file)
            if len(data) == 0:
                logger.warning("Внимание файл пустой")
                return []
        logger.info("Операция выполнена успешно")
        return list(data)
    except (json.JSONDecodeError, FileNotFoundError):
        logger.error("Ошибка функции")
        return []
