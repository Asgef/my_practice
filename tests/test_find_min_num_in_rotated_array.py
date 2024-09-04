from my_practice.find_min_num_in_rotated_array import Solution


def test_find_min():
    solution = Solution()
    assert solution.findMin([3, 4, 5, 1, 2]) == 1
    assert solution.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert solution.findMin([11, 13, 15, 17]) == 11
    assert solution.findMin([2, 1]) == 1
    assert solution.findMin([1]) == 1
