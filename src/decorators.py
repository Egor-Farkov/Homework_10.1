from functools import wraps
from typing import Any


def log(filename: Any = None) -> Any:
    """Декоратор, который логирует ход выполнения функции, ее результаты и возникшие ошибки"""

    def my_decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args, **kwargs):  # type: ignore
            try:
                func(*args, **kwargs)
                message_in_log = f"{func.__name__} ok"
            except Exception as e:
                message_in_log = f"{func.__name__} Ошибка {type(e).__name__} {args} {kwargs}"
            finally:
                if filename:
                    with open(filename, "a") as file:
                        file.write(message_in_log + "\n")
                else:
                    print(message_in_log)

            return func(*args, **kwargs)

        return wrapper

    return my_decorator
