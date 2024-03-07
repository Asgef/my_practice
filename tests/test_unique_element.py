from my_practice.unique_element import find_unique_element


def test_find_unique_element():
    assert find_unique_element([1, 1, 5, 5, 3, 3, 7, 4, 4]) == 7
    assert find_unique_element([1, 2, 1]) == 2
    assert find_unique_element([4, 3, 5, 6, 5, 4, 3]) == 6
    assert find_unique_element([10, 10, 20, 20, 30]) == 30
