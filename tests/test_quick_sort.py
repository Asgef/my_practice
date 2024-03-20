from my_practice.quick_sort import quick_sort


def test_quick_sort():
    assert quick_sort([10, 20, 0, -1]) == [-1, 0, 10, 20]
    assert quick_sort([]) == []
    assert quick_sort([10, 20, 0, -1], 'desc') == [20, 10, 0, -1]
