from my_practice.two_sum import Solution


def test_two_sum():
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    # assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    assert solution.twoSum([3, 3], 6) == [0, 1]
    assert solution.twoSum([1, 4, 5, 6], 10) == [1, 3]
    assert solution.twoSum([5, 7, 1, 8], 12) == [0, 1]
    assert solution.twoSum([-3, 4, 3, 90], 0) == [0, 2]
    assert solution.twoSum([1, 2, 3, 4, 5, 6], 11) == [4, 5]
    assert solution.twoSum([5, 7, 1, 8], 11) == []
