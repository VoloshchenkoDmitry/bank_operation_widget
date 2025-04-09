from datetime import datetime
from typing import Dict, List, Optional


def filter_by_status(operations: List[Dict], status: str) -> List[Dict]:
    """
    Фильтрует операции по статусу.

    Args:
        operations: Список операций
        status: Статус для фильтрации

    Returns:
        Список отфильтрованных операций
    """
    if not operations:
        return []

    return [op for op in operations if op.get("status", "").upper() == status.upper()]


def sort_by_date(operations: List[Dict], reverse: bool = False) -> List[Dict]:
    """
    Сортирует операции по дате.

    Args:
        operations: Список операций
        reverse: Если True - сортировка по убыванию

    Returns:
        Отсортированный список операций
    """
    if not operations:
        return []

    return sorted(
        operations,
        key=lambda x: datetime.strptime(x["date"], "%d.%m.%Y") if "date" in x else datetime.min,
        reverse=reverse,
    )


def filter_rub_only(operations: List[Dict]) -> List[Dict]:
    """
    Фильтрует только рублевые операции.

    Args:
        operations: Список операций

    Returns:
        Список рублевых операций
    """
    if not operations:
        return []

    return [op for op in operations if op.get("currency") == "RUB"]
