import pytest
from src.filters import filter_by_description, count_categories


@pytest.fixture
def sample_operations():
    return [
        {'description': 'Перевод организации', 'status': 'EXECUTED'},
        {'description': 'Открытие вклада', 'status': 'EXECUTED'},
        {'description': 'Перевод с карты на карту', 'status': 'CANCELED'},
        {'description': 'Покупка в магазине', 'status': 'EXECUTED'},
    ]


def test_filter_by_description(sample_operations):
    result = filter_by_description(sample_operations, 'перевод')
    assert len(result) == 2
    assert all('Перевод' in op['description'] for op in result)


def test_count_categories(sample_operations):
    categories = ['Перевод организации', 'Открытие вклада', 'Несуществующая категория']
    result = count_categories(sample_operations, categories)
    assert result == {
        'Перевод организации': 1,
        'Открытие вклада': 1,
        'Несуществующая категория': 0
    }
    