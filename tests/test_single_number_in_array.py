from my_practice.single_number_in_array import Solution


def test_single_number():
    assert Solution().singleNumber([2, 2, 1]) == 1
    assert Solution().singleNumber([4, 1, 2, 1, 2]) == 4
    assert Solution().singleNumber([1]) == 1
    assert Solution().singleNumber([0, 1, 0]) == 1
    assert Solution().singleNumber([3, 3, 7, 7, 10]) == 10
    assert Solution().singleNumber([-1, -1, -2]) == -2
