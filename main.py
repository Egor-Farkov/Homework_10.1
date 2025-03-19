import os

from src.external_api import get_convert_currency
from src.utils import read_json

if __name__ == "__main__":
    read_j = read_json(os.path.abspath("data/operations.json"))

    for i in read_j:
        get_convert_currency(i)
