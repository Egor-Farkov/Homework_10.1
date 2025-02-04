from src.widget import get_date, mask_account_card

if __name__ == "__main__":
    mask_card_number = mask_account_card("Maestro 1596837868705199")
    mask_account_number = get_date("2024-03-11T02:26:18.671407")
    print(mask_card_number)
    print(mask_account_number)
