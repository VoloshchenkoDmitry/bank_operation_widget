import pytest
from datetime import datetime
from src.operations import (
    filter_by_status,
    sort_by_date,
    filter_rub_only
)


@pytest.fixture
def sample_operations():
    return [
        {"date": "12.11.2019", "status": "EXECUTED", "currency": "RUB"},
        {"date": "10.11.2019", "status": "CANCELED", "currency": "USD"},
        {"date": "15.11.2019", "status": "EXECUTED", "currency": "EUR"},
        {"date": "08.11.2019", "status": "EXECUTED", "currency": "RUB"},
        {"date": "20.11.2019", "status": "PENDING", "currency": "RUB"},
    ]


def test_filter_by_status(sample_operations):
    # Тестируем фильтрацию по статусу EXECUTED
    result = filter_by_status(sample_operations, "EXECUTED")
    assert len(result) == 3
    assert all(op["status"] == "EXECUTED" for op in result)

    # Тестируем фильтрацию по статусу CANCELED
    result = filter_by_status(sample_operations, "CANCELED")
    assert len(result) == 1
    assert all(op["status"] == "CANCELED" for op in result)

    # Тестируем фильтрацию по несуществующему статусу
    result = filter_by_status(sample_operations, "UNKNOWN")
    assert len(result) == 0


def test_sort_by_date(sample_operations):
    # Сортировка по возрастанию
    result = sort_by_date(sample_operations)
    assert [op["date"] for op in result] == [
        "08.11.2019",
        "10.11.2019",
        "12.11.2019",
        "15.11.2019",
        "20.11.2019",
    ]

    # Сортировка по убыванию
    result = sort_by_date(sample_operations, reverse=True)
    assert [op["date"] for op in result] == [
        "20.11.2019",
        "15.11.2019",
        "12.11.2019",
        "10.11.2019",
        "08.11.2019",
    ]


def test_filter_rub_only(sample_operations):
    result = filter_rub_only(sample_operations)
    assert len(result) == 3
    assert all(op["currency"] == "RUB" for op in result)


def test_sort_by_date_missing_date():
    # Тест с операциями без даты
    operations = [
        {"status": "EXECUTED"},
        {"date": "12.11.2019", "status": "EXECUTED"},
    ]
    result = sort_by_date(operations)
    assert len(result) == 2
    assert "date" not in result[0]  # Операция без даты должна быть первой


def test_empty_input():
    # Тесты с пустым вводом
    assert filter_by_status([], "EXECUTED") == []
    assert sort_by_date([]) == []
    assert filter_rub_only([]) == []
