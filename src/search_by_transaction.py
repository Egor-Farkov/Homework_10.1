import re
from collections import Counter


def filter_transaction(datas: list[dict], word: str) -> list[dict]:
    """
    Функция принимает список словарей с данными о банковских операциях и строку поиска,
    возвращает список словарей, у которых в описании есть данная строка.
    :param datas: Список словарей с данными.
    :param word: Поисковое слово.
    :return: Список словарей, у которых в описании есть данная строка.
    """
    return [data for data in datas if re.search(word, data["description"], re.I)]


def filter_category(datas: list[dict], word: list) -> dict:
    """
    Функция принимает список словарей с данными о банковских операциях и список категорий операций.
    :param datas: Список словарей.
    :param word: Поисковое слово.
    :return: Словарь, в котором ключи — это названия категорий, а значения — это количество операций
    в каждой категории.
    """
    data_value = [data["description"] for data in datas if data["description"] in word]

    return dict(Counter(data_value))
