import json
import logging
import os
from typing import Any, Dict, List


def setup_logger(name: str, log_file: str) -> logging.Logger:
    """
    Настраивает и возвращает сконфигурированный логгер.

    Args:
        name: Имя логгера
        log_file: Имя файла для логов

    Returns:
        Сконфигурированный логгер
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Создаем директорию logs, если её нет
    os.makedirs("logs", exist_ok=True)

    # Настройка file_handler
    file_handler = logging.FileHandler(f"logs/{log_file}", mode="w")
    file_handler.setLevel(logging.DEBUG)

    # Настройка форматера
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    file_handler.setFormatter(formatter)

    # Очищаем существующие handlers
    logger.handlers.clear()

    # Добавляем handler к логгеру
    logger.addHandler(file_handler)

    return logger


# Инициализация логгера
utils_logger = setup_logger("utils", "utils.log")


def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список словарей с данными о транзакциях.

    Args:
        file_path: Путь к JSON-файлу с транзакциями.

    Returns:
        Список словарей с данными о транзакциях. Если файл не найден,
        пустой или содержит не список, возвращает пустой список.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if not isinstance(data, list):
                utils_logger.warning(f"Файл {file_path} не содержит список, возвращен пустой список")
                return []

            utils_logger.info(f"Успешно прочитан файл {file_path}, получено {len(data)} записей")
            return data

    except FileNotFoundError:
        utils_logger.error(f"Файл {file_path} не найден")
        return []
    except json.JSONDecodeError as e:
        utils_logger.error(f"Ошибка декодирования JSON в файле {file_path}: {str(e)}")
        return []
