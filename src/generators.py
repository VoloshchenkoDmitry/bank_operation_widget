def filter_by_currency(transactions, currency_code):
    """
    Фильтрует транзакции по заданной валюте.

    :param transactions: Список словарей, представляющих транзакции.
    :param currency_code: Код валюты для фильтрации.
    :return: Итератор, который возвращает транзакции с заданной валютой.
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions):
    """
    Генератор, который возвращает описание каждой транзакции.

    :param transactions: Список словарей, представляющих транзакции.
    :return: Итератор, который возвращает описание каждой транзакции.
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start, end):
    """
    Генератор, который выдает номера банковских карт в заданном диапазоне.

    :param start: Начальное значение диапазона.
    :param end: Конечное значение диапазона.
    :return: Итератор, который возвращает номера карт в формате XXXX XXXX XXXX XXXX.
    """
    for number in range(start, end + 1):
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + f"{number:016d}"[8:12] + " " + f"{number:016d}"[12:16]


# Пример использования transaction_descriptions:
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

# Пример использования card_number_generator:
for card_number in card_number_generator(1, 5):
    print(card_number)
