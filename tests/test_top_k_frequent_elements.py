from my_practice.top_k_frequent_elements import Solution


def test_top_k_frequent():
    solution = Solution()
    assert solution.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert solution.topKFrequent([1], 1) == [1]
    assert solution.topKFrequent([1, 2], 1) in [[1], [2]]
    assert solution.topKFrequent([1, 2, 3, 1, 2, 1], 2) == [1, 2]
