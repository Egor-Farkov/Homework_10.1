from typing import Union


def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты в виде числа и
    возвращает маску номера по правилу
    :param card_number: номер карты
    :return: маска номера
    """
    list_numbers = []
    star_mask = "*" * (len(card_number) - 10)
    first_part_num = card_number[0:6]
    end_part_num = card_number[-4:]
    card_number_str = f"{first_part_num}{star_mask}{end_part_num}"

    for i in range(0, len(card_number_str), 4):
        list_numbers.append(card_number_str[i : i + 4])

    return " ".join(list_numbers)


def get_mask_account(bill_number: Union[int | str]) -> Union[int | str]:
    """
    Функция принимает на вход номер счета в виде числа и возвращает
    маску номера по правилу **XXXX
    :param bill_number: номер счета
    :return: маска счета
    """
    return f"**{str(bill_number)[-4:]}"
