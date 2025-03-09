from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от типа.
    Принимает строку с типом и номером, возвращает замаскированную строку.
    """
    parts = info.rsplit(" ", 1)
    if len(parts) != 2:
        return info  # Если строка не соответствует ожидаемому формату, возвращаем её как есть

    type_, number = parts

    if type_.lower() == "счет":
        return f"{type_} {get_mask_account(number)}"
    else:
        return f"{type_} {get_mask_card_number(number)}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата "2024-03-11T02:26:18.671407" в формат "ДД.ММ.ГГГГ".
    """
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")


if __name__ == "__main__":
    # Примеры для mask_account_card
    print(mask_account_card("Visa Platinum 7000792289606361"))  # Visa Platinum 7000 79** **** 6361
    print(mask_account_card("Счет 73654108430135874305"))  # Счет **4305
    print(mask_account_card("Maestro 1596837868705199"))  # Maestro 1596 83** **** 5199

    # Примеры для get_date
    print(get_date("2024-03-11T02:26:18.671407"))  # 11.03.2024
