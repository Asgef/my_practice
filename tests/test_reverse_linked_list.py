from hexlet_code.tree_node import LinkedListNode
from my_practice.reverse_linked_list import Solution


def test_reverse_linked_list():
    l1 = LinkedListNode(1)
    l1.next = LinkedListNode(2)
    l1.next.next = LinkedListNode(3)
    l1.next.next.next = LinkedListNode(4)
    l1.next.next.next.next = LinkedListNode(5)

    solution = Solution()
    result = solution.reverseList(l1)
    assert result.value == 5
    assert result.next.value == 4
    assert result.next.next.value == 3
    assert result.next.next.next.value == 2
    assert result.next.next.next.next.value == 1

    l2 = LinkedListNode(1)
    l2.next = LinkedListNode(2)

    result = solution.reverseList(l2)
    assert result.value == 2
    assert result.next.value == 1

    l3 = None
    result = solution.reverseList(l3)
    assert result is None
