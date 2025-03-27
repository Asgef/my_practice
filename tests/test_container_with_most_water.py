from my_practice.container_with_most_water import Solution


def test_container_with_most_water():
    solution = Solution()
    assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert solution.maxArea([1, 1]) == 1
    assert solution.maxArea([4, 3, 2, 1, 4]) == 16
    assert solution.maxArea([1, 2, 1]) == 2
