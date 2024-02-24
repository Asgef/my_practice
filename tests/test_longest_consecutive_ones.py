from my_practice.longest_consecutive_ones import max_consecutive_ones


def test_max_consecutive_ones():
    assert max_consecutive_ones([1, 1, 0, 1, 1, 1, 1]) == 4
    assert max_consecutive_ones([0, 0, 0]) == 0
    assert max_consecutive_ones([1, 1, 0, 1]) == 2
    assert max_consecutive_ones([1, 1, 0, 1, 1, 1, 0, 0, 1]) == 3
