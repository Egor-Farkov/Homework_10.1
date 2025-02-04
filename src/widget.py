import masks
from typing import Union

from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(all_name_card: str | int) -> str | int:
    new_list = all_name_card.split(' ')
    card_num = []
    card_alph = []

    for i in new_list:
        if i.isalpha():
            card_alph.append(i)
        else:
            card_num.append(i)

    name_letter_card = ''.join(card_alph)

    if name_letter_card == 'Счет':
        name_number_card = get_mask_account(''.join(card_num))
    else:
        name_number_card = get_mask_card_number(''.join(card_num))

    return f'{name_letter_card} {name_number_card}'

print(mask_account_card('Счет 64686473678894779589'))
