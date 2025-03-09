import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "currency, result",
    [("USD", [939719570, 142264268, 895315941]), ("RUB", [873106923, 594226727])],
)
def test_filter_by_currency(generators_data: list[dict], currency: str, result: list[int]) -> None:
    """
    Тестирование функции по currency
    """
    list_data = list(filter_by_currency(generators_data, currency))
    ids_data = [id_["id"] for id_ in list_data]
    assert ids_data == result

    with pytest.raises(ValueError):
        filter_by_currency([], currency)


def test_transaction_descriptions(generators_data: list[dict]) -> None:
    """
    Тестирование возврата описания транзакции.
    """
    list_data = transaction_descriptions(generators_data)
    assert next(list_data) == "Перевод организации"
    assert next(list_data) == "Перевод со счета на счет"

    list_data = transaction_descriptions([])
    with pytest.raises(ValueError):
        next(list_data)


@pytest.mark.parametrize(
    "start, stop, result",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (1000, 1002, ["0000 0000 0000 1000", "0000 0000 0000 1001", "0000 0000 0000 1002"]),
    ],
)
def test_card_number_generator(start: int, stop: int, result: list[str]) -> None:
    """
    Тестирование функции генерации номеров карт.
    """
    card_list = card_number_generator(start, stop)
    assert card_list == result
    with pytest.raises(ValueError):
        card_number_generator(3, 1)
