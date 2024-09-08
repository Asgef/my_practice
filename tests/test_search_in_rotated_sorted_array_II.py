from my_practice.search_in_rotated_sorted_array_II import Solution


def test_search():
    solution = Solution()

    assert solution.search([2, 5, 6, 0, 0, 1, 2], 0) is True
    assert solution.search([2, 5, 6, 0, 0, 1, 2], 3) is False
    assert solution.search([1, 1, 1, 1, 1, 1, 1, 1], 1) is True
    assert solution.search([1, 1, 1, 1, 1, 1, 1, 1], 2) is False
    assert solution.search([0, 0, 0, 1, 0, 0, 0], 1) is True
    assert solution.search([0, 0, 0, 0, 0, 0, 0], 1) is False
    assert solution.search([], 1) is False
    assert solution.search([1], 1) is True
    assert solution.search([1], 2) is False
    assert solution.search(
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], 2
    ) is True
    assert solution.search([1, 3, 5], 1) is True
