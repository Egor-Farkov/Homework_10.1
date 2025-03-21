import csv

import pandas as pd


def transaction_file_csv(path: str) -> list[dict]:
    """Функция для считывания финансовых операций из CSV"""
    with open(path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        return list(reader)


def transaction_file_excel(path: str) -> list[dict]:
    """Функция для считывания финансовых операций из Excel"""
    return pd.read_excel(path).to_dict("records")
