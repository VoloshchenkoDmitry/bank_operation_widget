import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "info, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(info: str, expected: str):
    assert mask_account_card(info) == expected


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-31T23:59:59.999999", "31.12.2023"),
    ],
)
def test_get_date(date_str: str, expected: str):
    assert get_date(date_str) == expected
