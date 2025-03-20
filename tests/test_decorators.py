import os

from src.decorators import log


def test_log_to_file() -> None:
    """
    Тестирование записи логов в файл.
    """
    log_filename = "test_log.txt"

    @log(filename=log_filename)
    def add(a: int, b: int) -> int:
        return a + b

    add(1, 2)

    with open(log_filename, "r") as f:
        log_content = f.read()
        assert "add started" in log_content
        assert "add ok" in log_content

    os.remove(log_filename)


def test_log_to_console(capsys) -> None:
    """
    Тестирование вывода логов в консоль.
    """

    @log()
    def add(a: int, b: int) -> int:
        return a + b

    add(1, 2)

    captured = capsys.readouterr()
    assert "add started" in captured.out
    assert "add ok" in captured.out


def test_log_error(capsys) -> None:
    """
    Тестирование логирования ошибок.
    """

    @log()
    def divide(a: int, b: int) -> float:
        return a / b

    try:
        divide(1, 0)
    except ZeroDivisionError:
        pass

    captured = capsys.readouterr()
    assert "divide error" in captured.out
    assert "ZeroDivisionError" in captured.out
