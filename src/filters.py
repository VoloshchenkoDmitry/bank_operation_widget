import re
from collections import Counter
from typing import Dict, List, Optional, Union


def filter_by_description(operations: List[Dict], search_string: str) -> List[Dict]:
    """
    Фильтрует операции по строке в описании с использованием регулярных выражений.

    Args:
        operations: Список операций (словарей)
        search_string: Строка для поиска в описании операции

    Returns:
        Список отфильтрованных операций
    """
    if not operations or not search_string:
        return []

    pattern = re.compile(search_string, re.IGNORECASE)
    return [op for op in operations if op.get("description") and pattern.search(op["description"])]


def count_categories(operations: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по категориям.

    Args:
        operations: Список операций (словарей)
        categories: Список категорий для подсчета

    Returns:
        Словарь с количеством операций по каждой категории
    """
    if not operations or not categories:
        return {}

    descriptions = [op.get("description", "").lower() for op in operations]
    category_counts = Counter(descriptions)

    return {category: category_counts.get(category.lower(), 0) for category in categories}
