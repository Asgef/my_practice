from my_practice.merge_k_sorted_lists import merge_lists, Solution
from hexlet_code.helpers import list_to_linkedlist, linkedlist_to_list
from hexlet_code.tree_node import LinkedListNode


def test_solution():
    solution = Solution()

    list_1 = [
        list_to_linkedlist([1, 4, 5]),
        list_to_linkedlist([1, 3, 4]),
        list_to_linkedlist([2, 6])
    ]
    list_2 = []
    list_3 = [list_to_linkedlist([])]

    lnkd_lst_1 = solution.mergeKLists(list_1)
    lnkd_lst_2 = solution.mergeKLists(list_2)
    lnkd_lst_3 = solution.mergeKLists(list_3)

    assert linkedlist_to_list(lnkd_lst_1) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert linkedlist_to_list(lnkd_lst_2) == []
    assert linkedlist_to_list(lnkd_lst_3) == []


def test_merge_sorted_lists():
    assert merge_lists(
        [[1, 4, 5], [1, 3, 4], [2, 6]]
    ) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert merge_lists([]) == []
    assert merge_lists([[]]) == []
