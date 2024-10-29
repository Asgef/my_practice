from my_practice.number_of_islands import Solution


def test_number_of_islands():
    solution = Solution()

    assert solution.numIslands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]) == 1

    assert solution.numIslands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]) == 3

    assert solution.numIslands([["0"]]) == 0
    assert solution.numIslands([["1"]]) == 1


def test_number_of_islands_edge_cases():
    solution = Solution()

    assert solution.numIslands([]) == 0
    assert solution.numIslands([["0", "0", "0"], ["0", "0", "0"]]) == 0
    assert solution.numIslands([["1"]]) == 1
    assert solution.numIslands([["0"]]) == 0
    assert solution.numIslands([["1"] * 100 for _ in range(100)]) == 1
    assert solution.numIslands([["1", "0"] * 50 for _ in range(100)]) == 50
