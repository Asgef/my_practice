from my_practice.quick_sort import quick_sort #, quick_sort_2


def test_quick_sort():
    assert quick_sort([10, 20, 0, -1]) == [-1, 0, 10, 20]
    assert quick_sort([]) == []
    assert quick_sort([10, 20, 0, -1], 'desc') == [20, 10, 0, -1]


# def test_quick_sort_2():
#     assert quick_sort_2([1]) == [1]
#     assert quick_sort_2([]) == []
#     assert quick_sort_2([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
#     assert quick_sort_2([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
#     assert quick_sort_2([1, 2, 3, 4, 5], reverse=True) == [5, 4, 3, 2, 1]
#     assert quick_sort_2(
#         [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
#     ) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
#     assert quick_sort_2(
#         [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], reverse=True
#     ) == [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]
