from src.search_by_transaction import filter_category, filter_transaction


def test_filter_transaction(generators_data: list[dict]) -> None:
    """
    Функция проверяет список словарей с данными о банковских операциях и возвращает список по строке поиска.
    """
    assert filter_transaction(generators_data, word="Перевод организации") == [
        {
            "date": "2018-06-30T02:08:58.425572",
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "id": 939719570,
            "operationAmount": {"amount": "9824.07", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 11776614605963066702",
        },
        {
            "date": "2018-09-12T21:27:25.241689",
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "id": 594226727,
            "operationAmount": {"amount": "67314.70", "currency": {"code": "RUB", "name": "руб."}},
            "state": "CANCELED",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_filter_category(generators_data: list[dict]) -> None:
    """
    Функция тестирует список словарей с данными о банковских операциях и список категорий операций
    и возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций
    в каждой категории
    """
    assert filter_category(generators_data, ["Перевод организации"]) == {"Перевод организации": 2}
