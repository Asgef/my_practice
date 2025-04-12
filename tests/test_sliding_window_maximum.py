from my_practice.sliding_window_maximum import Solution


def test_max_sliding_window():
    s = Solution()
    assert s.maxSlidingWindow(
        [1, 3, -1, -3, 5, 3, 6, 7], 3
    ) == [3, 3, 5, 5, 6, 7]
    assert s.maxSlidingWindow([1], 1) == [1]
    assert s.maxSlidingWindow([9, 11], 2) == [11]
    assert s.maxSlidingWindow([4, -2], 2) == [4]
    assert s.maxSlidingWindow([1, -1], 1) == [1, -1]
