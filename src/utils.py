import json


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
                return []
        return list(data)
    except (json.JSONDecodeError, FileNotFoundError):
        return []
