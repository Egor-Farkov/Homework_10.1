from config import ROOT_DIR
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.read_file_transaction import transaction_file_csv, transaction_file_excel
from src.search_by_transaction import filter_transaction
from src.utils import read_json
from src.widget import get_date, mask_account_card


def main() -> None:
    print(
        """
    Привет! Добро пожаловать в программу работы с банковскими транзакциями.""".strip()
    )
    print(
        """
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файл\n""".strip()
    )

    person_choose = int(input("Сделайте выбор от 1 до 3\n"))

    data_list = {1: "JSON-файл", 2: "CSV-файл", 3: "XLSX-файл"}

    print(f"Для обработки выбран {data_list.get(person_choose)}")

    if person_choose == 1:
        data_transaction = read_json(ROOT_DIR + "/data/operations.json")

    elif person_choose == 2:
        data_transaction = transaction_file_csv(ROOT_DIR + "/data/transactions.csv")

    elif person_choose == 3:
        data_transaction = transaction_file_excel(ROOT_DIR + "/data/transactions_excel.xlsx")

    else:
        data_transaction = []

    varios_list = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )
        choose_filter = input().upper()

        if choose_filter in varios_list:
            data_transaction = filter_by_state(data_transaction, choose_filter)
            print(f"Операции отфильтрованы по статусу {choose_filter}")
            break
        else:
            print(f"Статус операции {choose_filter} недоступен.")

    print("Отсортировать операции по дате? Да/Нет")

    answer_user_sort = input().lower() == "да"

    if answer_user_sort:
        print("Отсортировать по возрастанию или по убыванию?")
        answer_user_sum_trans = input().lower() == "по возрастанию"
        data_transaction = sort_by_date(data_transaction, answer_user_sum_trans)

    print("Выводить только рублевые тразакции? Да/Нет")

    answer_user = "RUB" if input().lower() == "да" else False
    if answer_user:
        data_transaction = list(filter_by_currency(data_transaction, str(answer_user)))

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    answer_user = input().lower() == "да"
    if answer_user:
        answer_user = input("Введите слово для фильтрации\n")
        data_transaction = filter_transaction(data_transaction, answer_user)

    print("Распечатываю итоговый список транзакций...")

    print(f"Всего банковских операций в выборке: {len(data_transaction)}")

    for transaction in data_transaction:
        date = get_date(transaction["date"])
        amount = transaction["amount"] if "amount" in transaction else transaction["operationAmount"]["amount"]
        from_transaction = mask_account_card(transaction["from"])
        to_transaction = mask_account_card(transaction["to"])
        description = transaction["description"]
        currency_code = (
            transaction["currency_code"]
            if "currency_code" in transaction
            else transaction["operationAmount"]["currency"]["name"]
        )
        print(f"{date} {description}\n{from_transaction} -> {to_transaction}\nСумма: {amount} {currency_code}\n\n")


if __name__ == "__main__":
    main()
