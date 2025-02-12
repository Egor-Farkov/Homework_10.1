from datetime import datetime

def filter_by_state(data_state: list[dict], state = 'EXECUTED') -> tuple[list[dict], list[dict]]:
    """
    :param data_state: Функция принимает список словарей.
    :param state: Опциональное значение для ключа state (по умолчанию 'EXECUTED').
    :return: Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
state соответствует указанному значению.
    """

    list_1 = []
    list_2 = []

    for i in data_state:
        if i['state'] == state:
            list_1.append(i)

        else:
            list_2.append(i)

    return f'{list_1} \n {list_2}'

def sort_by_date(data_list: list[dict], reverse=True) -> list[dict]:
    """Возвращает новый список отстортированный по дате"""

    return sorted(data_list, key=lambda x: x["date"], reverse=True)
