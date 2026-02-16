from utils import calculate_total


def test_calculate_total():
    assert calculate_total([10, 15, 25]) == 50


def test_empty_list():
    assert calculate_total([]) == 0
