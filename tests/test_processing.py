import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, result",
    [("EXECUTED", [41428829, 939719570]), ("CANCELED", [594226727, 615064591])],
)
def test_filter_by_state(data_state: list[dict], state: str, result: list[dict]) -> None:
    """
    Функция фильтра значений по ключу state
    :param data_state: Тестовые данные
    :param state: Аргумент фильтра значения
    :param result: Результативные данные с параметризации
    :return: None
    """

    get_func_data = filter_by_state(data_state, state=state)
    list_1 = [filtered_list["id"] for filtered_list in get_func_data]
    assert list_1 == result

    with pytest.raises(ValueError):
        filter_by_state([], state=state)


def test_sort_by_date(data_state: list[dict]) -> None:
    """
    Функция сортировки данных по дате
    :param data_state: Тестовые данные
    :return: None
    """
    sort_data = sort_by_date(data_state)
    false_reverse_data = sort_by_date(data_state, reverse=False)

    list_1 = [id_sort_data["id"] for id_sort_data in sort_data]
    list_false_reverse_ids = [id_sort_data["id"] for id_sort_data in false_reverse_data]

    assert list_1 == [41428829, 615064591, 594226727, 939719570]
    assert list_false_reverse_ids == [939719570, 594226727, 615064591, 41428829]
