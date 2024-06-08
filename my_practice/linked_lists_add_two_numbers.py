# Task: "Add Two Numbers"
# You are given two non-empty linked lists representing two non-negative 
# integers. The digits are stored in reverse order, and each node contains a 
# single digit. Add the two numbers and return the sum as a linked list.
#

# Задача: "Сложение двух чисел"
# Даны два непустых связанных списка, представляющих два неотрицательных числа. 
# Цифры хранятся в обратном порядке, и каждый узел содержит одну цифру. 
# Сложите два числа и верните сумму как связанный список.
#

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807


from typing import Optional
from hexlet_code.tree_node import LinkedListNode


class Solution:
    def addTwoNumbers(
            self, l1: Optional[LinkedListNode], l2: Optional[LinkedListNode]
    ) -> Optional[LinkedListNode]:
        
        digit = 0
        lst1 = l1
        lst2 = l2

        result = LinkedListNode()
        head = result

        while lst1 or lst2 or digit > 0:

            lst1 = lst1 if lst1 else LinkedListNode()
            lst2 = lst2 if lst2 else LinkedListNode()

            node_sum = lst1.value + lst2.value
            digit, head.value = divmod(node_sum + digit, 10)

            lst1 = lst1.next
            lst2 = lst2.next

            if not lst1 and not lst2 and digit == 0:
                return result
            
            head.next = LinkedListNode()
            head = head.next

        return result

# TODO: Повторить задачу, переписать по памяти решение из leetcode.
