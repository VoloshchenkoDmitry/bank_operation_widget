import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01T00:00:00.000000"},
        {"id": 2, "state": "CANCELED", "date": "2024-02-01T00:00:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2024-03-01T00:00:00.000000"},
    ]


def test_filter_by_state(operations):
    filtered = filter_by_state(operations, "EXECUTED")
    assert len(filtered) == 2
    assert all(op["state"] == "EXECUTED" for op in filtered)


def test_sort_by_date(operations):
    sorted_ops = sort_by_date(operations, reverse=True)
    assert sorted_ops[0]["id"] == 3
    assert sorted_ops[-1]["id"] == 1
