from datetime import datetime
from functools import wraps
from typing import Any, Callable, Dict, Optional, Tuple


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования вызовов функций.

    Args:
        filename (Optional[str]): Имя файла для записи логов. Если не указано, логи выводятся в консоль.

    Returns:
        Callable: Декорированная функция.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Tuple[Any, ...], **kwargs: Dict[str, Any]) -> Any:
            # Логирование начала выполнения функции
            start_time = datetime.now()
            func_name = func.__name__
            log_message = f"{func_name} started at {start_time} with args: {args}, kwargs: {kwargs}\n"

            try:
                # Выполнение функции
                result = func(*args, **kwargs)
                # Логирование успешного выполнения
                log_message += f"{func_name} ok. Result: {result}\n"
                return result
            except Exception as e:
                # Логирование ошибки
                log_message += f"{func_name} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
                raise
            finally:
                # Запись логов в файл или вывод в консоль
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message)
                else:
                    print(log_message)

        return wrapper

    return decorator
