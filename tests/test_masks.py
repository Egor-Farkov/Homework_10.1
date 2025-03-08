import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    """
    Функция тестирования масок карт
    """
    assert get_mask_card_number("21541221421212525845") == "2154 12** **** **** 5845"
    with pytest.raises(ValueError):
        get_mask_card_number("215412214212125")

    with pytest.raises(ValueError):
        get_mask_card_number("")


def test_get_mask_account() -> None:
    """
    Функция тестирования номеров счета
    """
    assert get_mask_account("9866548755412145") == "**2145"
    with pytest.raises(ValueError):
        get_mask_account("1154122")

    with pytest.raises(ValueError):
        get_mask_account("")
