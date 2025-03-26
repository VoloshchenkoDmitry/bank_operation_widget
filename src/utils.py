import json
from typing import Any, Dict, List


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
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
