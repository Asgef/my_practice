from my_practice.search_2d_matrix import Solution


def test_search_matrix():
    solution = Solution()
    assert solution.searchMatrix(
        [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3
    ) is True
    assert solution.searchMatrix(
        [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13
    ) is False
