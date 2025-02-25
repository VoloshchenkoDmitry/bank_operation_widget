from typing import List, Dict, Optional

def filter_by_state(operations: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :parameter operations: Список словарей с данными о банковских операциях.
    :parameter state: Значение для фильтрации (по умолчанию 'EXECUTED').
    :return: Отфильтрованный список словарей.
    """
    return [op for op in operations if op.get('state') == state]

def sort_by_date(operations: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по дате.

    :parameter operations: Список словарей с данными о банковских операциях.
    :parameter reverse: Порядок сортировки (по умолчанию True — по убыванию).
    :return: Отсортированный список словарей.
    """
    return sorted(operations, key=lambda x: x['date'], reverse=reverse)

