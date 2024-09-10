from my_practice.binary_search import binary_search, Solution


def test_binary_search():
    assert binary_search([-5, 2, 4, 6, 9], 4) == 2
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
    assert binary_search([], 1) == -1
    assert binary_search([3], 3) == 0
    assert binary_search([3], 4) == -1
    assert binary_search([1, 2, 3, 4, 5], -1) == -1


def test_solution():
    solution = Solution()
    assert solution.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert solution.search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert solution.search([1, 2, 3, 4, 5, 6, 7, 8, 9], 7) == 6
    assert solution.search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10) == -1
    assert solution.search([], 2) == -1
    assert solution.search([3], 3) == 0
