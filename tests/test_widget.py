import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "data_number, result",
    [
        ("Visa Platinum 7000792254878960", "Visa Platinum **8960"),
        ("Счет 73654108430143057592", "Счет 7365 41** **** **** 7592"),
        ("MasterCard 7158300754873472", "MasterCard **3472"),
    ],
)
def test_mask_account_card(data_number: str, result: str) -> None:
    """
    Функция проверки номеров карт
    :param data_number: Входные данные карт с параметризации
    :param result: Выходные данные карт с параметризации
    """
    assert mask_account_card(data_number) == result
    with pytest.raises(ValueError):
        mask_account_card("12125512")
    with pytest.raises(ValueError):
        mask_account_card("")


@pytest.mark.parametrize(
    "date, result",
    [
        ("2025-02-10T00:25:00.000000", "10.02.2025"),
        ("2024-02-09", "09.02.2024"),
    ],
)
def test_get_data(date: str, result: str) -> None:
    """
    Функция тестирования дат
    :param date: Входные данные дат с параметризации
    :param result: Выходные данные дат с параметризации
    """
    assert get_date(date) == result
    with pytest.raises(ValueError):
        get_date("2024-02-")
    with pytest.raises(ValueError):
        get_date("")
