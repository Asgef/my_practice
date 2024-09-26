# Problem: "Reverse Linked List"
# Given the head of a singly linked list, reverse the list, and return the
# reversed list.

# Задача: "Reverse Linked List"
# Дано: Голова односвязного списка. Необходимо развернуть список и вернуть его.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#
# Example 2:
# Input: head = [1,2]
# Output: [2,1]
#
# Example 3:
# Input: head = []
# Output: []


from typing import Optional
from hexlet_code.tree_node import LinkedListNode


# class Solution:
#     def reverseList(
#     self, head: Optional[LinkedListNode]
#     ) ->Optional[LinkedListNode]:
#         prev = None
#         current = head
#
#         while current:
#             next_ = current.next
#             current.next = prev
#             prev = current
#             current = next_
#
#         return prev


class Solution:
    def reverseList(
            self, head: Optional[LinkedListNode]
    ) -> Optional[LinkedListNode]:

        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

# Односвязный список, рекурсия, разворот односвязного списка.
