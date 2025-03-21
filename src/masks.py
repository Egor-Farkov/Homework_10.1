import logging

from config import ROOT_DIR

print(ROOT_DIR)

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(ROOT_DIR + "/logs/masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(module)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты в виде числа и
    возвращает маску номера по правилу
    :param card_number: номер карты
    :return: маска номера
    """

    len_number = len(card_number)

    if len_number != 20:
        logger.error("Исключение на ошибку по кол-ву символов")
        raise ValueError(f"Wrong length of the card number: len = {len_number} right 20")

    list_numbers = []
    star_mask = "*" * (len(card_number) - 10)
    first_part_num = card_number[0:6]
    end_part_num = card_number[-4:]
    card_number_str = f"{first_part_num}{star_mask}{end_part_num}"

    for i in range(0, len(card_number_str), 4):
        list_numbers.append(card_number_str[i : i + 4])

    logger.info("Успешное выполнение функции")
    return " ".join(list_numbers)


def get_mask_account(bill_number: str) -> str:
    """
    Функция принимает на вход номер счета в виде числа и возвращает
    маску номера по правилу **XXXX
    :param bill_number: номер счета
    :return: маска счета
    """

    len_number = len(bill_number)

    if len_number != 16:
        logger.error("Ошибка, число должно состоять из 16 цифр")
        raise ValueError(f"Wrong length of the card number: len = {len_number} right 16")
    logger.info("Успешное выполнение функции")
    return f"**{str(bill_number)[-4:]}"
