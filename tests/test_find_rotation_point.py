from my_practice.find_rotation_point import find_rotation_point


def test_find_rotation_point():
    assert find_rotation_point([4, 5, 6, 7, 0, 1, 2]) == 4
    assert find_rotation_point([3, 4, 5, 1, 2]) == 3
    assert find_rotation_point([]) == -1
    assert find_rotation_point([1, 2, 3, 4, 5, 6, 7]) == 0
    assert find_rotation_point([1]) == 0
    assert find_rotation_point([2, 1]) == 1
    assert find_rotation_point([1, 2]) == 0
    assert find_rotation_point([6, 7, 8, 9, 1, 2, 3, 4, 5]) == 4
    assert find_rotation_point([5, 6, 7, 8, 9, 10, 1, 2, 3, 4]) == 6
    assert find_rotation_point([2, 3, 4, 5, 6, 7, 1]) == 6
    assert find_rotation_point([4, 5, 6, 7, 8, 1, 2, 3]) == 5
    assert find_rotation_point([2, 3, 4, 5, 6, 7, 8, 1]) == 7
    assert find_rotation_point(list(range(1000))) == 0
    assert find_rotation_point(list(range(500, 1000)) + list(range(500))) == 500
