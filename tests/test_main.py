import pytest
from unittest.mock import patch, MagicMock
from src.main import main
from src.operations import filter_by_status


@pytest.fixture
def mock_operations():
    return [
        {"date": "12.11.2019", "status": "EXECUTED", "currency": "RUB", "description": "Payment"},
        {"date": "10.11.2019", "status": "CANCELED", "currency": "USD", "description": "Transfer"},
    ]


@patch("builtins.input")
@patch("src.main.operations.filter_by_status")
@patch("src.main.operations.sort_by_date")
@patch("src.main.operations.filter_rub_only")
@patch("src.main.filters.filter_by_description")
def test_main_flow(
    mock_filter_desc, mock_filter_rub, mock_sort, mock_filter_status, mock_input, mock_operations
):
    # Настраиваем моки
    mock_filter_status.return_value = mock_operations
    mock_sort.return_value = mock_operations
    mock_filter_rub.return_value = mock_operations
    mock_filter_desc.return_value = mock_operations

    # Эмулируем пользовательский ввод
    input_values = [
        "1",  # Выбор JSON
        "EXECUTED",  # Статус
        "да",  # Сортировать по дате?
        "по возрастанию",  # Порядок сортировки
        "нет",  # Только рублевые?
        "нет",  # Фильтр по описанию?
    ]
    mock_input.side_effect = input_values

    # Запускаем main
    with patch("builtins.print") as mock_print:
        main()

    # Проверяем вызовы
    mock_filter_status.assert_called_once()
    mock_sort.assert_called_once()
    mock_filter_rub.assert_not_called()  # Не должен вызываться, так как ответ "нет"
    mock_filter_desc.assert_not_called()  # Не должен вызываться, так как ответ "нет"

    # Проверяем вывод
    assert any("Распечатываю итоговый список транзакций" in str(call) for call in mock_print.call_args_list)


@patch("builtins.input")
def test_main_invalid_status(mock_input):
    # Эмулируем сначала неверный статус, затем верный
    input_values = [
        "1",  # Выбор JSON
        "invalid_status",  # Неверный статус
        "EXECUTED",  # Верный статус
        "нет", "нет", "нет"  # Остальные ответы
    ]
    mock_input.side_effect = input_values

    with patch("builtins.print") as mock_print:
        main()

    # Проверяем, что было сообщение о неверном статусе
    assert any("недоступен" in str(call).lower() for call in mock_print.call_args_list)


@patch("builtins.input")
def test_main_empty_result(mock_input):
    # Эмулируем ввод, который приведет к пустому результату
    input_values = ["1", "PENDING", "нет", "нет", "нет"]
    mock_input.side_effect = input_values

    # Фильтр по статусу вернет пустой список
    with patch("src.main.operations.filter_by_status", return_value=[]):
        with patch("builtins.print") as mock_print:
            main()

    # Проверяем сообщение о пустом результате
    assert any("не найдено ни одной транзакции" in str(call).lower() for call in mock_print.call_args_list)


@patch("builtins.input")
def test_main_full_filtering(mock_input):
    # Проверяем полный путь с фильтрацией
    input_values = [
        "2",  # CSV
        "EXECUTED",
        "да",  # Сортировать
        "по убыванию",
        "да",  # Только рубли
        "да",  # Фильтр по описанию
        "Payment"  # Слово для поиска
    ]
    mock_input.side_effect = input_values

    with patch("src.main.operations.filter_by_status") as mock_filter_status:
        with patch("src.main.operations.sort_by_date") as mock_sort:
            with patch("src.main.operations.filter_rub_only") as mock_rub:
                with patch("src.main.filters.filter_by_description") as mock_desc:
                    mock_desc.return_value = [{"date": "12.11.2019", "description": "Payment"}]
                    main()

    # Проверяем, что все фильтры были вызваны
    mock_filter_status.assert_called_once()
    mock_sort.assert_called_once()
    mock_rub.assert_called_once()
    mock_desc.assert_called_once()
