from my_practice.find_rotation_point import find_rotation_point


def test_find_rotation_point():
    assert find_rotation_point([4, 5, 6, 7, 0, 1, 2]) == 4
    assert find_rotation_point([3, 4, 5, 1, 2]) == 3
    assert find_rotation_point([]) == -1
    assert find_rotation_point([1, 2, 3, 4, 5, 6, 7]) == 0
