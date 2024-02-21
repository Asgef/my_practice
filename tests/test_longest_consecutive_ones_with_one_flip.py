from my_practice.longest_consecutive_ones_with_one_flip import (
    max_consecutive_onesII
)


def test_max_consecutive_onesII():
    # assert max_consecutive_onesII([1, 0, 1]) == 3
    assert max_consecutive_onesII([1, 0, 1, 0, 1, 1]) == 4
    assert max_consecutive_onesII([1, 1, 1, 0, 1, 1]) == 3
    assert max_consecutive_onesII([1, 0, 1, 1, 1, 1]) == 4
    assert max_consecutive_onesII([1, 0, 1, 0, 0, 0, 1, 1]) == 3
    assert max_consecutive_onesII([0, 0, 0, 1, 1, 1, 1, 0, 0, 1]) == 5  # !!!
    assert max_consecutive_onesII([1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1]) == 5
    assert max_consecutive_onesII([1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1]) == 6
    assert max_consecutive_onesII([1, 1, 0, 0, 0, 1, 1, 1, 0, 1]) == 5
    assert max_consecutive_onesII([1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1]) == 5
