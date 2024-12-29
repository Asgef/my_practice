from my_practice.merge_intervals import Solution


def test_merge_intervals():
    assert Solution().merge(
        [[1, 3], [2, 6], [8, 10], [15, 18]]
    ) == [[1, 6], [8, 10], [15, 18]]
    assert Solution().merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert Solution().merge([[1, 4], [2, 3]]) == [[1, 4]]
    assert Solution().merge([[1, 4], [5, 6]]) == [[1, 4], [5, 6]]
    assert Solution().merge([[1, 10], [2, 6], [8, 9]]) == [[1, 10]]
    assert Solution().merge([[1, 4], [0, 4]]) == [[0, 4]]
