from hexlet_code.tree_node import LinkedListNode
from my_practice.linked_lists_add_two_numbers import Solution


def test_add_two_numbers():
    # Creating nodes for the first number
    l1 = LinkedListNode(2)
    l1.next = LinkedListNode(4)
    l1.next.next = LinkedListNode(3)

    # Creating nodes for the second number
    l2 = LinkedListNode(5)
    l2.next = LinkedListNode(6)
    l2.next.next = LinkedListNode(4)

    # Adding the numbers
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    # Checking the result
    assert result.value == 7
    assert result.next.value == 0
    assert result.next.next.value == 8
