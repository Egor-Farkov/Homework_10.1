from src.masks import get_mask_account, get_mask_card_number

if __name__ == "__main__":
    mask_card_number = get_mask_card_number('Maestro 1596837868705199')
    mask_account_number = get_mask_account('Счет 64686473678894779589')
    print(mask_card_number)
    print(mask_account_number)
