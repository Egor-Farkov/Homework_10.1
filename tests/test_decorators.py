import pytest
from _pytest.capture import CaptureFixture

from src.decorators import log


def test_decorators() -> None:
    """Тестирование декоратора."""

    @log()
    def one(x: int, y: int) -> float:
        return x / y

    assert one(44, 22) == 2

    with pytest.raises(ZeroDivisionError):
        one(15, 0)


def test_decorators_with_filename() -> None:
    """Тестирование декоратора."""

    @log(filename="list.log")
    def one(x: int, y: int) -> float:
        return x / y

    assert one(44, 22) == 2

    with pytest.raises(ZeroDivisionError):
        one(15, 0)


def test_capsys_decorators(capsys: CaptureFixture[str]) -> None:
    """Тестирование декоратора"""

    @log()
    def two(x: int, y: int) -> float:
        return x / y

    two(10, 5)
    read_out = capsys.readouterr()
    assert read_out.out == "two ok\n"
