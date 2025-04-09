# Проект: Виджет банковских операций

## Описание
Проект предназначен для обработки и анализа банковских операций клиента. Включает функции фильтрации и сортировки операций.

## Установка
1. Клонируйте репозиторий:
```bash
   git clone https://github.com/ваш-username/bank-operations-widget.git
   cd bank-operations-widget
```
2. Установите зависимости:
```
pip install -r requirements.txt
```

## Использование
```from src.processing import filter_by_state, sort_by_date

operations = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Фильтрация по статусу
filtered_operations = filter_by_state(operations, state='EXECUTED')

# Сортировка по дате
sorted_operations = sort_by_date(operations, reverse=True)
```
## Модуль `generators`

Модуль `generators` содержит функции для работы с большими объемами данных транзакций.

## Функции

### `filter_by_currency(transactions, currency_code)`
Фильтрует транзакции по заданной валюте.

##Пример использования:##
```python
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))
```

## Новые функции
- Добавлена поддержка файлов CSV
- Добавлена поддержка файлов Excel
- Улучшенная безопасность типов
- Комплексное покрытие тестами

### Использование
```python
from src.file_reader import read_csv_file, read_excel_file

csv_transactions = read_csv_file('transactions.csv')
excel_transactions = read_excel_file('transactions.xlsx')
```

## Новая функциональность

1. Поиск операций по описанию с использованием регулярных выражений
2. Подсчет операций по категориям
3. Фильтрация операций по различным параметрам

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).
