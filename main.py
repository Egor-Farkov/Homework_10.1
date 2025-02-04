from src.masks import get_mask_account, get_mask_card_number

if __name__ == "__main__":
    mask_card_number = get_mask_card_number(7000792289606361)
    mask_account_number = get_mask_account(73654108430135874305)
    print(mask_card_number)
    print(mask_account_number)
