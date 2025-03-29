import logging
import os
from typing import NoReturn


def setup_masks_logger() -> logging.Logger:
    """
    Настраивает и возвращает логгер для модуля masks.

    Returns:
        logging.Logger: Сконфигурированный логгер для модуля masks
    """
    masks_logger = logging.getLogger("masks")
    masks_logger.setLevel(logging.DEBUG)

    # Создаем директорию logs, если её нет
    os.makedirs("logs", exist_ok=True)

    # Настройка file_handler для masks
    file_handler = logging.FileHandler("logs/masks.log", mode="w")
    file_handler.setLevel(logging.DEBUG)

    # Настройка форматера
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    file_handler.setFormatter(formatter)

    # Очищаем существующие handlers (на случай повторного вызова)
    masks_logger.handlers.clear()

    # Добавляем handler к логгеру
    masks_logger.addHandler(file_handler)

    return masks_logger


# Инициализируем логгер
masks_logger = setup_masks_logger()


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты, оставляя видимыми первые 6 и последние 4 цифры.

    Args:
        card_number: Номер карты (16 цифр)

    Returns:
        str: Маскированный номер карты в формате XXXX XX** **** XXXX

    Raises:
        ValueError: Если номер карты содержит не только цифры или не 16 символов
    """
    try:
        if not card_number.isdigit():
            raise ValueError("Номер карты должен содержать только цифры")
        if len(card_number) != 16:
            raise ValueError("Номер карты должен состоять из 16 цифр")

        masked_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        masks_logger.info(f"Успешно замаскирован номер карты: {masked_card}")
        return masked_card

    except ValueError as e:
        masks_logger.error(f"Ошибка при маскировании номера карты: {str(e)}")
        raise


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета, оставляя видимыми только последние 4 цифры.

    Args:
        account_number: Номер счета (минимум 4 цифры)

    Returns:
        str: Маскированный номер счета в формате **XXXX

    Raises:
        ValueError: Если номер счета содержит не только цифры или менее 4 символов
    """
    try:
        if not account_number.isdigit():
            raise ValueError("Номер счета должен содержать только цифры")
        if len(account_number) < 4:
            raise ValueError("Номер счета должен содержать как минимум 4 цифры")

        masked_account = f"**{account_number[-4:]}"
        masks_logger.info(f"Успешно замаскирован номер счета: {masked_account}")
        return masked_account

    except ValueError as e:
        masks_logger.error(f"Ошибка при маскировании номера счета: {str(e)}")
        raise


def main() -> NoReturn:
    """Примеры использования функций маскирования."""
    print(get_mask_card_number("7000792289606361"))  # 7000 79** **** 6361
    print(get_mask_account("73654108430135874305"))  # **4305


if __name__ == "__main__":
    main()
