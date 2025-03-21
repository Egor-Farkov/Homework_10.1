from typing import Any
from unittest.mock import patch

import pandas as pd

from config import ROOT_DIR
from src.read_file_transaction import transaction_file_csv, transaction_file_excel


@patch("src.read_file_transaction.csv.DictReader")
def test_transaction_file_csv(data_file: Any) -> None:
    """Тест для функции считывания финансовых операций из CSV"""
    data_file.return_value = "test"
    result = transaction_file_csv(ROOT_DIR + "/data/transactions.csv")
    assert result == ["t", "e", "s", "t"]


@patch("src.read_file_transaction.pd.read_excel")
def test_transaction_file_excel(mock_read_exel: Any) -> None:
    """Тест для функции считывания финансовых операций из Excel"""
    mock_df = pd.DataFrame([{"id": 1, "amount": 100}, {"id": 2, "amount": 200}])
    mock_read_exel.return_value = mock_df

    result = transaction_file_excel(ROOT_DIR + "/data/transactions_excel.xlsx")
    assert result == [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
