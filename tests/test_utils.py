import pathlib
from unittest.mock import patch

from src.utils import read_json

path = pathlib.Path(__file__).parent.resolve()


@patch("json.load")
def test_read_json(mock_open):  # type:ignore
    """Пустой файл"""
    data = [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        }
    ]
    mock_open.return_value = data

    first_result_func = read_json("/Users/egorfedorovic/Documents/Skypro/Home_works/H_w_skypro/data/operations.json")
    assert first_result_func == data

    mock_open.return_value = []
    second_result_func = read_json("/Users/egorfedorovic/Documents/Skypro/Home_works/H_w_skypro/data/operations.json")
    assert second_result_func == []
    assert read_json("") == []
    assert read_json("/Users/egorfedorovic/Documents/Skypro/Home_works/H_w_skypro/tests/test_file.json") == []
