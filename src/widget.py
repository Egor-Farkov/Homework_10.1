from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(all_name_card: str) -> str:
    """Функция обработки данных о карте"""

    try:
        new_list = all_name_card.split()
        card_num = []
        card_alph = []

        for i in new_list:
            if i.isalpha():
                card_alph.append(i)
            else:
                card_num.append(i)

        name_letter_card = " ".join(card_alph)

        if name_letter_card == "Счет":
            name_number_card = get_mask_card_number("".join(card_num))
        else:
            name_number_card = get_mask_account("".join(card_num))

        return f"{name_letter_card} {name_number_card}"
    except Exception as err:
        raise ValueError(f"Error: {str(err)}")


def get_date(my_date: str) -> str:
    """Функция обработки данных о счете"""

    try:
        date_object = datetime.fromisoformat(my_date)
        return date_object.strftime("%d.%m.%Y")
    except Exception:
        raise ValueError("Invalid input ISO format datetime")
