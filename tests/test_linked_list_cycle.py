from hexlet_code.tree_node import LinkedListNode
from my_practice.linked_list_cycle import Solution


def test_has_cycle():
    # Create nodes
    node1 = LinkedListNode(3)
    node2 = LinkedListNode(2)
    node3 = LinkedListNode(0)
    node4 = LinkedListNode(-4)

    # Link nodes
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Create cycle

    solution = Solution()

    assert solution.hasCycle(node4) is True

    # New list with cycle
    node1 = LinkedListNode(1)
    node2 = LinkedListNode(2)
    node1.next = node2
    node2.next = node1  # Create cycle

    assert solution.hasCycle(node1) is True

    # New list with one element
    node1 = LinkedListNode(1)

    assert solution.hasCycle(node1) is False
