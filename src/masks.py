def get_mask_card_number(card_number: str) -> str:
    # Убедимся, что номер карты состоит только из цифр
    if not card_number.isdigit():
        raise ValueError("Номер карты должен содержать только цифры")

    # Проверяем, что длина номера карты корректна
    if len(card_number) != 16:
        raise ValueError("Номер карты должен состоять из 16 цифр")

    # Форматируем номер карты в нужный вид
    masked_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return masked_card


def get_mask_account(account_number: str) -> str:
    # Убедимся, что номер счета состоит только из цифр
    if not account_number.isdigit():
        raise ValueError("Номер счета должен содержать только цифры")

    # Проверяем, что длина номера счета корректна
    if len(account_number) < 4:
        raise ValueError("Номер счета должен содержать как минимум 4 цифры")

    # Форматируем номер счета в нужный вид
    masked_account = f"**{account_number[-4:]}"
    return masked_account


# Примеры использования:
print(get_mask_card_number("7000792289606361"))  # 7000 79** **** 6361
print(get_mask_account("73654108430135874305"))  # **4305
