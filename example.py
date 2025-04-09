from src.decorators import log


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y


@log()
def my_function_with_error(x: int, y: int) -> int:
    return x / y


if __name__ == "__main__":
    my_function(1, 2)
    my_function_with_error(1, 0)  # Вызовет ошибку деления на ноль
