import os
from typing import Any, Dict, Union, cast

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Args:
        transaction: Словарь с данными о транзакции.

    Returns:
        Сумма транзакции в рублях (float).
    """
    amount: Union[str, int, float] = transaction.get("amount", 0)
    currency: str = transaction.get("currency", "RUB").upper()

    if currency == "RUB":
        return float(amount)

    api_key: Union[str, None] = os.getenv("API_KEY")
    api_url: Union[str, None] = os.getenv("API_URL")

    if not api_key or not api_url:
        raise ValueError("API credentials not configured")

    params: Dict[str, str] = {"base": currency, "symbols": "RUB"}
    headers: Dict[str, str] = {"apikey": api_key}

    response: requests.Response = requests.get(
        cast(str, api_url),  # Явное приведение типа, так как мы проверили что api_url не None
        headers=headers,
        params=params,
        timeout=10,
    )
    response.raise_for_status()

    response_data: Dict[str, Any] = response.json()
    rates: Dict[str, float] = response_data.get("rates", {})
    rate: float = rates.get("RUB", 1.0)

    return float(amount) * rate
