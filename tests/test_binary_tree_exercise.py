from my_practice.binary_tree_exercise import solution


def test_solution():
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected = [
        [5, 3, 2, 1],
        [5, 3, 4],
        [5, 8, 7, 6],
        [5, 8, 9],
    ]

    assert solution(items) == expected
