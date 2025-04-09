from typing import List, Dict, Optional
from . import operations
from . import filters


def main():
    """
    Основная функция программы для работы с банковскими транзакциями.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # Здесь должна быть логика загрузки данных из файлов
    # Для примера используем пустой список
    all_operations: List[Dict] = []

    # Выбор файла
    file_type = input(
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла\n"
        "Ваш выбор: "
    )

    print(f"\nДля обработки выбран {'JSON' if file_type == '1' else 'CSV' if file_type == '2' else 'XLSX'}-файл.")

    # Фильтрация по статусу
    while True:
        status = input(
            "\nВведите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            "Ваш выбор: "
        ).upper()

        if status in {'EXECUTED', 'CANCELED', 'PENDING'}:
            break
        print(f'Статус операции "{status}" недоступен.')

    filtered_ops = operations.filter_by_status(all_operations, status)
    print(f'\nОперации отфильтрованы по статусу "{status}"')

    # Дополнительные фильтры
    sort_answer = input('\nОтсортировать операции по дате? Да/Нет: ').lower()
    if sort_answer == 'да':
        sort_order = input('Отсортировать по возрастанию или по убыванию? ').lower()
        filtered_ops = operations.sort_by_date(filtered_ops, sort_order == 'по убыванию')

    rub_answer = input('\nВыводить только рублевые тразакции? Да/Нет: ').lower()
    if rub_answer == 'да':
        filtered_ops = operations.filter_rub_only(filtered_ops)

    word_answer = input('\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет: ').lower()
    if word_answer == 'да':
        search_word = input('Введите слово для поиска в описании: ')
        filtered_ops = filters.filter_by_description(filtered_ops, search_word)

    # Вывод результатов
    print('\nРаспечатываю итоговый список транзакций...')
    if not filtered_ops:
        print('\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации')
    else:
        print(f'\nВсего банковских операций в выборке: {len(filtered_ops)}')
        for op in filtered_ops:
            print(f"\n{op.get('date', 'Нет даты')} {op.get('description', 'Нет описания')}")
            print(f"Сумма: {op.get('amount', 'Нет суммы')} {op.get('currency', '')}")


if __name__ == '__main__':
    main()
    