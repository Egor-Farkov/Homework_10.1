from typing import Generator, Iterator


def filter_by_currency(lst: list[dict], currency: str) -> Iterator[dict]:
    """
    Фильтрация по списку transactions.
    :param lst: Принимает список словарей на вход.
    :param currency: Аргумент фильтрации по code.
    :return: Возвращается итератор.
    """
    if len(lst) == 0:
        raise ValueError("Ошибка во входных данных листа словарей")
    return (
        i
        for i in lst
        if i.get("operationAmount", {}).get("currency", {}).get("code", None) == currency or i.get("currency_code")
    )


def transaction_descriptions(lst: list[dict]) -> Generator:
    """
    Функция-генератор, которая возвращает генератор значений по запросу.
    :param lst: Принимает список словарей на вход.
    :return: Возвращается описание транзакции.
    """
    if len(lst) == 0:
        raise ValueError("Ошибка входных данных")
    for i in lst:
        yield i["description"]


def card_number_generator(start: int, stop: int) -> list[str]:
    """
    Функция, которая выдает номера банковских карт в формате XXXX XXXX XXXX XXXX.
    :param start: Принимает начальное значение в качестве аргумента.
    :param stop: Принимает конечное значение в качестве аргумента.
    :return: Возвращает список номеров карт.
    """

    if start > stop:
        raise ValueError("Ошибка start больше чем stop")
    result = []
    for card_number in range(start, stop + 1):
        num = str(card_number).zfill(16)
        temp_result = []
        for i in range(0, len(num), 4):
            temp_result.append(num[i : i + 4])
        result.append(" ".join(temp_result))
    return result
