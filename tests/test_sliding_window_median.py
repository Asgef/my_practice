from my_practice.sliding_window_median import Solution


def test_median_sliding_window():
    solution = Solution()
    assert solution.medianSlidingWindow(
        [1, 3, -1, -3, 5, 3, 6, 7], 3
    ) == [1.00000, -1.00000, -1.00000, 3.00000, 5.00000, 6.00000]
    assert solution.medianSlidingWindow(
        [1, 2, 3, 4, 2, 3, 1, 4, 2], 3
    ) == [2.00000, 3.00000, 3.00000, 3.00000, 2.00000, 3.00000, 2.00000]
    assert solution.medianSlidingWindow([1], 1) == [1.00000]
    assert solution.medianSlidingWindow([1, 2], 2) == [1.50000]
    assert solution.medianSlidingWindow(
        [5, 5, 5, 5], 2
    ) == [5.00000, 5.00000, 5.00000]
    assert solution.medianSlidingWindow([1, 2], 3) == []
