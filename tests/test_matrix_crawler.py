from my_practice.matrix_crawler import matrix_crawler


def test_spiral_matrix_traversal():
    data_case_1 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    expected_case_1 = [1, 5, 9, 13, 14, 15, 16, 12, 8, 4, 3, 2, 6, 10, 11, 7]
    assert matrix_crawler(data_case_1) == expected_case_1

    data_case_2 = [
        [1, 2],
        [3, 4]
    ]
    expected_case_2 = [1, 3, 4, 2]
    assert matrix_crawler(data_case_2) == expected_case_2

    data_case_3 = [[1]]
    expected_case_3 = [1]
    assert matrix_crawler(data_case_3) == expected_case_3

    data_case_4 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected_case_4 = [1, 4, 7, 8, 9, 6, 3, 2, 5]
    assert matrix_crawler(data_case_4) == expected_case_4

    data_case_5 = []
    expected_case_5 = []
    assert matrix_crawler(data_case_5) == expected_case_5

    data_case_6 = [
        [1, 2, 3],
        [4, 5, 6]

    ]
    expected_case_6 = []
    assert matrix_crawler(data_case_6) == expected_case_6

    data_case_7 = [
        [1, 2],
        [4, 5],
        [6, 7]

    ]
    expected_case_7 = []
    assert matrix_crawler(data_case_7) == expected_case_7
