from my_practice.quick_sort import solution


def test_quick_sort():
    assert solution([10, 20, 0, -1]) == [-1, 0, 10, 20]
    assert solution([]) == []
    assert solution([10, 20, 0, -1], 'desc') == [20, 10, 0, -1]
