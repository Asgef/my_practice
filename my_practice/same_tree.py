# Задача: "Одинаковые деревья"
# Даны корни двух бинарных деревьев p и q. Нужно определить, являются ли
# эти деревья одинаковыми. Деревья считаются одинаковыми, если они
# структурно идентичны и значения всех соответствующих узлов равны.
#
# Task: "Same Tree"
# Given the roots of two binary trees p and q, write a function to check
# if they are the same. Two binary trees are considered the same if they
# are structurally identical and the nodes have the same value.
#
# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
#
# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false
#
# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false


from typing import Optional
from hexlet_code.tree_node import BinaryTreeNode

class Solution:
    def isSameTree(
            self, p: Optional[BinaryTreeNode], q: Optional[BinaryTreeNode]
    ) -> bool:
        if not p and not q:
            return True
        elif p and q:
            if p.value != q.value:
                return False
            return self.isSameTree(p.right, q.right) \
                and self.isSameTree(p.left, q.left)
        return False
