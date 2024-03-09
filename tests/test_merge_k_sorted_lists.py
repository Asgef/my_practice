from my_practice.merge_k_sorted_lists import merge_lists


def test_merge_sorted_lists():
    assert merge_lists([[1,4,5],[1,3,4],[2,6]]) == [1,1,2,3,4,4,5,6]
    assert merge_lists([]) == []
    assert merge_lists([[]]) == []