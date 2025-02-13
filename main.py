from datetime import datetime
from src.widget import get_date, mask_account_card
from src.processing import filter_by_state
from src.processing import sort_by_date

input_data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
              {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
              {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
              {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

if __name__ == "__main__":
    mask_card_number = mask_account_card("Visa Classic 6831982476737658")
    mask_account_number = get_date("2024-03-11T02:26:18.671407")
    print(mask_card_number)
    print(mask_account_number)

    sorted_data = sort_by_date(input_data, False)
    sorted_d = sort_by_date(input_data)

    print(sorted_data)
    print(sorted_d)

    filter_data = filter_by_state(input_data, 'CANCELED')
    filter_d = filter_by_state(input_data)

    print(filter_data)
    print(filter_d)
