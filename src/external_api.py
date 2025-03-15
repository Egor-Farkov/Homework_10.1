import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv(".env")
API_KEY = os.getenv("API_KEY")


def get_convert_currency(data: dict) -> Any:
    """
    Функция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях.
    :param data: Принимает на вход транзакцию.
    :return: Сумму транзакции (amount) в рублях, тип данных — float.
    """
    code = data.get("operationAmount", {}).get("currency", {}).get("code", None)
    if code:
        amount = data.get("operationAmount", {}).get("amount", 0)
        if code != "RUB":
            headers = {"apikey": API_KEY}

            response = requests.get(
                f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}",
                headers=headers,
            )
            return response.json()["result"]
        else:
            return float(amount)
