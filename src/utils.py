import json
import logging

from config import ROOT_DIR

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(ROOT_DIR + "/logs/utils.log", "w", encoding="utf-8")
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
