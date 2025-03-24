def filter_by_state(data_state: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    :param data_state: Функция принимает список словарей.
    :param state: Опциональное значение для ключа state
    (по умолчанию 'EXECUTED').
    :return: Функция возвращает новый список словарей, содержащий
    только те словари, у которых ключ
    state соответствует указанному значению.
    """
    if len(data_state) == 0:
        raise ValueError("Входящий лист пуст")

    return [i for i in data_state if i.get("state", "") == state]


def sort_by_date(data_list: list[dict], reverse: bool = True) -> list[dict]:
    """Возвращает новый список отсортированный по дате"""

    return sorted(data_list, key=lambda x: x["date"], reverse=reverse)
